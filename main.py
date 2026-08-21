from pygame import *

back = (200, 255, 255)
win_height = 500
win_width = 700

window = display.set_mode((win_width, win_height))
window.fill(back)
clock = time.Clock()

font.init()
font1 = font.SysFont(None, 36)
score_text_l = font1.render('SCORE: 0', True, (180, 0, 0))
score_text_r = font1.render('SCORE: 0', True, (180, 0, 0))
text_player_l = font1.render('PLAYER 1 WINS', True, (180, 0, 0))
text_player_r = font1.render('PLAYER 2 WINS', True, (180, 0, 0))
score_l = 0
score_r = 0

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= 5
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += 5

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= 5
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += 5

class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, speed_x, speed_y):
        super().__init__(player_image, player_x, player_y, size_x, size_y)
        self.speed_x = speed_x
        self.speed_y = speed_y

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y > win_height - 50 or self.rect.y < 0:
            self.speed_y *= -1
        if sprite.collide_rect(self, player_left) or sprite.collide_rect(self, player_right):
            self.speed_x *= -1

player_left = Player('Platform.png', 5, 300, 30, 100)
player_right = Player('Platform.png', 660, 300, 30, 100)
ball = Ball('Ball.png', 350, 250, 50, 50, 5, 5)

game_over = False

while True:
    for e in event.get():
        if e.type == QUIT:
            exit()
    if not game_over:   

        window.fill(back)
        player_left.reset()
        player_right.reset()
        ball.reset()
        player_left.update_l()
        player_right.update_r()
        ball.update()
        window.blit(score_text_l, (10, 10))
        window.blit(score_text_r, (560, 10))

        if ball.rect.x < 0:
            score_r += 1
            score_text_r = font1.render(f'SCORE: {score_r}', True, (180, 0, 0))
            ball.rect.x = 350
            ball.rect.y = 250
        if ball.rect.x > win_width:
            score_l += 1
            score_text_l = font1.render(f'SCORE: {score_l}', True, (180, 0, 0))
            ball.rect.x = 350
            ball.rect.y = 250

        if score_l > 20:
            window.blit(text_player_l, (200, 200))
            game_over = True
        if score_r > 20:
            window.blit(text_player_r, (200, 200))
            game_over = True

    display.update()
    clock.tick(60)