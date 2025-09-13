import pygame
import random
pygame.init()
screen = pygame.display.set_mode((864, 800))
pygame.display.set_caption("flabby bird!")

bg = pygame.image.load("buildings.png")
floor = pygame.image.load("ground.png")
ground_scroll = 0
flying = False
gameOver = False
clock = pygame.time.Clock()
pipe_frequency = 1500
last_pipe = pygame.time.get_ticks() - pipe_frequency
past_pipe = False

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

class pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, face):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("pipe.png")
        self.rect = self.image.get_rect()
        if face == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - 75]
        elif face == -1:
            self.rect.topleft = [x, y + 75]
    def update(self):
        self.rect.x -= 5
        if self.rect.right < 0:
            self.kill()

flappy = bird(90, 300)
birdGroup = pygame.sprite.Group()
birdGroup.add(flappy)
pipeGroup = pygame.sprite.Group()

while True:
    clock.tick(60)
    screen.blit(bg, (0, 0))
    pipeGroup.draw(screen)
    screen.blit(floor, (ground_scroll, 670))
    birdGroup.draw(screen)
    birdGroup.update()
    if flappy.rect.bottom > 670 or flappy.rect.top < 0:
        gameOver = True
        flying = False
    if flying == True and gameOver == False:
        time = pygame.time.get_ticks()
        pipe_height = random.randint(-125, 125)
        if time - last_pipe > pipe_frequency:
            top = pipe(864, 400 + pipe_height, 1)
            bottom = pipe(864, 400 + pipe_height, -1)
            pipeGroup.add(top)
            pipeGroup.add(bottom)
            last_pipe = time
        pipeGroup.update()
        ground_scroll -= 5
        if ground_scroll < -35:
            ground_scroll = 0
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
move ground to left
make ground.blit a variable to change and set back to 0 when ground runs out
"""