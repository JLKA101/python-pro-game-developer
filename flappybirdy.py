import pygame
pygame.init()
screen = pygame.display.set_mode((864, 800))
pygame.display.set_caption("flabby bird!")

bg = pygame.image.load("buildings.png")
floor = pygame.image.load("ground.png")
flying = False
gameOver = False
clock = pygame.time.Clock()

class bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        for i in range(1, 4):
            img = pygame.image.load(f"bird{i}.png")
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.velocity = 0
        self.clicked = False
        self.counter = 0
    
    def update(self):
        if flying == True:
            self.velocity += 0.5
            if self.rect.bottom < 670:
                self.rect.y += self.velocity
        if gameOver == False:
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.velocity = -8
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
            self.counter += 1
            if self.counter > 5:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
                self.image = self.images[self.index]

flappy = bird(90, 300)
birdGroup = pygame.sprite.Group()
birdGroup.add(flappy)

while True:
    clock.tick(60)
    screen.blit(bg, (0, 0))
    screen.blit(floor, (0, 670))
    birdGroup.draw(screen)
    birdGroup.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and flying == False and gameOver == False:
            flying = True


    pygame.display.update()

"""HOMEWORK HINT!
creating bird class
self.image, self.rect are the arguments
list for animation

HOMEWORK HINT!
move grund to left
make blit a varoable to change and set back to 0 when ground runs out
"""