import pygame
from random import randint

pygame.init()

pygame.font.init()
font1 = pygame.font.Font(None, 80)
win = font1.render("YOU WIN!", True, (255, 255, 255))
lose = font1.render("YOU LOSE!", True, (180, 0, 0))
font2 = pygame.font.Font(None, 36)

window_width = 700
window_height = 500
ball_x = 350
ball_y = 250

main_win = pygame.display.set_mode((window_width, window_height))

class GameSprite():
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        self.image = pygame.transform.scale(pygame.image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def update_l(self):
        keys = pygame.key.get_pressed()
        if e.type == pygame.KEYDOWN:
            if keys[pygame.K_a] and self.rect.y > 5:
                self.rect.y += 5
            if keys[pygame.K_d] and self.rect.y < 5:
                self.rect.y -= 5
    def update_r(self):
        keys = pygame.key.get_pressed()
        if e.type == pygame.KEYDOWN:
            if keys[pygame.K_LEFT] and self.rect.y > 5:
                self.rect.y += 5
            if keys[pygame.K_RIGHT] and self.rect.y < 5:
                self.rect.y -= 5
    def colliderect(self, rect):
        return self.rect.colliderect(rect)

class Player(GameSprite):
    def draw(self):
        main_win.blit(self.image, (self.rect.x, self.rect.y))

class Enemy(GameSprite):
    def update(self):
        self.rect.x += self.speed
        global lost
        if self.rect.x > window_height:
            self.rect.y = randint(80, window_width - 80)
            self.rect.x = 0
    def draw(self):
        main_win.blit(self.image, (self.rect.x, self.rect.y))

pygame.display.set_caption('Ping-Pong')
back = pygame.transform.scale(pygame.image.load('bg.jpg'), (window_width, window_height))
player1 = Player('platform2.png', 10, 220, 50, 120, 2)
player2 = Player('platform.png', 640, 220, 50, 120, 2)
ball = Enemy('ball.png', ball_x, ball_y, 25, 25, 10)

clock = pygame.time.Clock()

game_finished = False
while not game_finished:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game_finished = True
        elif e.type == pygame.KEYDOWN:
            player1.update_l()
            player2.update_r()

    main_win.blit(back, (0, 0))
    ball.draw()
    ball.update()
    player1.draw()
    player2.draw()
    player1.update_l()
    player2.update_r()

    pygame.display.update()
    clock.tick(60)