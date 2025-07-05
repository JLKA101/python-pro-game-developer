import pygame, time
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("rocket in space!")

class rocket(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("rocket.png"),(100, 100))
        self.rect = self.image.get_rect()
    def update(self, keys):
        if keys[pygame.K_w]:
            self.rect.move_ip(0, -10)
        if keys[pygame.K_s]:
            self.rect.move_ip(0, 10)
        if keys[pygame.K_a]:
            self.rect.move_ip(-10, 0)
        if keys[pygame.K_d]:
            self.rect.move_ip(10, 0)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.right > 600:
            self.rect.right = 600
        if self.rect.bottom > 600:
            self.rect.bottom = 600

player = rocket()
sprites = pygame.sprite.Group()
sprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.blit(pygame.image.load("galaxy.png"), (0, 0))
    sprites.draw(screen)
    keys = pygame.key.get_pressed()
    player.update(keys)

    pygame.display.update()