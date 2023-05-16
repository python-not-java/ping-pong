import pygame

pygame.init()

window_width = 700
window_height = 500
platform_x = 5
platform_y = 100

back = pygame.transform.scale(pygame.image.load('background.jpg'), (window_width, window_height))
platform = "platform.png"
ball = "ball.png"

class GameSprite():
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def update_l(self):
        keys = key.get_pressed()
        if e.type == pygame.KEYDOWN:
            if keys[K_W] and self.rect.y > 5:
                move_up1 = True
            if keys[K_S] and self.rect.y < 5:
                move_dowm1 = False
    def update_l(self):
        keys = key.get_pressed()
        if e.type == pygame.KEYDOWN:
            if keys[K_UP] and self.rect.y > 5:
                move_up1 = True
            if keys[K_DOWN] and self.rect.y < 5:
                move_dowm1 = False
    def reset (self):
        window.blit(self.image, (self.rect.x, self.rect.y))

main_win = pygame.display.set_mode((window_width, window_height))
platform = GameSprite('platform.png', platform_x, platform_y, 3, 30, 2)

clock = pygame.time.Clock()

game_finished = False
while not game_finished:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game_finished = True
    main_win.blit(back, (0, 0))

    pygame.display.update()
    clock.tick(60)