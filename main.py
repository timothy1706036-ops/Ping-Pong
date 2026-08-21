from pygame import *

back = (200, 255, 255)
win_height = 500
win_width = 700

window = display.set_mode((win_width, win_height))
window.fill(back)
clock = time.Clock()

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
ball = Ball('Ball.png', 200, 200, 50, 50, 5, 5)

while True:
    window.fill(back)
    for e in event.get():
        if e.type == QUIT:
            exit()
    player_left.reset()
    player_right.reset()
    ball.reset()
    player_left.update_l()
    player_right.update_r()
    ball.update()
    display.update()
    clock.tick(60)