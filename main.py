from pygame import *

back = (200, 255, 255)
win_height = 500
win_width = 700

window = display.set_mode((win_width, win_height))
window.fill(back)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

player_left = GameSprite('Platform.png', 5, 300, 30, 100)
player_right = GameSprite('Platform.png', 670, 300, 30, 100)
ball = GameSprite('Ball.png', 200, 200, 50, 50)

while True:
    for e in event.get():
        if e.type == QUIT:
            exit()
    player_left.reset()
    player_right.reset()
    ball.reset()
    display.update()