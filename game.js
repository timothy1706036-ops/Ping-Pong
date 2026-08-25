// Ping Pong - versi JavaScript dari main.py (pygame)
// Ukuran, kecepatan, dan aturan skor dibuat sama dengan versi Python.

const BACK = 'rgb(200, 255, 255)';
const TEXT_COLOR = 'rgb(180, 0, 0)';
const WIN_WIDTH = 700;
const WIN_HEIGHT = 500;

const canvas = document.getElementById('game');
const ctx = canvas.getContext('2d');

let scoreL = 0;
let scoreR = 0;
let gameOver = false;

// Pengganti key.get_pressed(): catat tombol yang sedang ditekan.
const keys = Object.create(null);

window.addEventListener('keydown', (e) => {
  keys[e.code] = true;
  // Cegah halaman ikut scroll saat panah atas/bawah dipakai.
  if (e.code === 'ArrowUp' || e.code === 'ArrowDown') e.preventDefault();
});

window.addEventListener('keyup', (e) => {
  keys[e.code] = false;
});

/** Pengganti GameSprite di pygame. */
class GameSprite {
  constructor(imageSrc, x, y, sizeX, sizeY) {
    this.image = new Image();
    this.image.src = imageSrc;
    this.x = x;
    this.y = y;
    this.width = sizeX;
    this.height = sizeY;
  }

  // Sama seperti reset() di Python: gambar sprite ke layar.
  reset() {
    ctx.drawImage(this.image, this.x, this.y, this.width, this.height);
  }
}

class Player extends GameSprite {
  updateL() {
    if (keys['KeyW'] && this.y > 5) {
      this.y -= 5;
    }
    if (keys['KeyS'] && this.y < WIN_HEIGHT - 80) {
      this.y += 5;
    }
  }

  updateR() {
    if (keys['ArrowUp'] && this.y > 5) {
      this.y -= 5;
    }
    if (keys['ArrowDown'] && this.y < WIN_HEIGHT - 80) {
      this.y += 5;
    }
  }
}

class Ball extends GameSprite {
  constructor(imageSrc, x, y, sizeX, sizeY, speedX, speedY) {
    super(imageSrc, x, y, sizeX, sizeY);
    this.speedX = speedX;
    this.speedY = speedY;
  }

  update() {
    this.x += this.speedX;
    this.y += this.speedY;

    if (this.y > WIN_HEIGHT - 50 || this.y < 0) {
      this.speedY *= -1;
    }

    if (collideRect(this, playerLeft) || collideRect(this, playerRight)) {
      this.speedX *= -1;
    }
  }
}

// Pengganti sprite.collide_rect(): cek dua kotak saling tumpang tindih.
function collideRect(a, b) {
  return a.x < b.x + b.width &&
         a.x + a.width > b.x &&
         a.y < b.y + b.height &&
         a.y + a.height > b.y;
}

const playerLeft = new Player('Platform.png', 5, 300, 30, 100);
const playerRight = new Player('Platform.png', 660, 300, 30, 100);
const ball = new Ball('Ball.png', 350, 250, 50, 50, 5, 5);

function drawText(text, x, y) {
  ctx.fillStyle = TEXT_COLOR;
  ctx.font = '36px Arial, sans-serif';
  ctx.textBaseline = 'top';
  ctx.fillText(text, x, y);
}

function loop() {
  if (!gameOver) {
    ctx.fillStyle = BACK;
    ctx.fillRect(0, 0, WIN_WIDTH, WIN_HEIGHT);

    playerLeft.reset();
    playerRight.reset();
    ball.reset();

    playerLeft.updateL();
    playerRight.updateR();
    ball.update();

    drawText('SCORE: ' + scoreL, 10, 10);
    drawText('SCORE: ' + scoreR, 560, 10);

    if (ball.x < 0) {
      scoreR += 1;
      ball.x = 350;
      ball.y = 250;
    }
    if (ball.x > WIN_WIDTH) {
      scoreL += 1;
      ball.x = 350;
      ball.y = 250;
    }

    if (scoreL > 20) {
      drawText('PLAYER 1 WINS', 200, 200);
      gameOver = true;
    }
    if (scoreR > 20) {
      drawText('PLAYER 2 WINS', 200, 200);
      gameOver = true;
    }
  }

  requestAnimationFrame(loop);
}

requestAnimationFrame(loop);
