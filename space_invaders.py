import pygame, time, random
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("space invaders")

clock = pygame.time.Clock()
score = 0

class invaders(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.reset_pos()
    def reset_pos(self):
        self.rect.x = random.randint(20, 580)
        self.rect.y = random.randint(-500, -20)
    def update(self):
        self.rect.y += 1
        if self.rect.y > 600:
            self.reset_pos()
        
class player(invaders):
    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

sprites = pygame.sprite.Group()
allsprites = pygame.sprite.Group()

for i in range(50):
    aliens = invaders("red")
    sprites.add(aliens)
    allsprites.add(aliens)
user = player("white")
allsprites.add(user)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.fill("black")
    allsprites.update()
    hitlist = pygame.sprite.spritecollide(user, sprites, False)
    for i in hitlist:
        i.reset_pos()
        score += 1
        print(score)
    allsprites.draw(screen)
    clock.tick(80)
    pygame.display.update()