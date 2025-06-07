import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))

class rect():
    def __init__(self, color, dimensions):
        self.color = color
        self.dimensions = dimensions
        self.screen = screen
    def display(self):
        self.draw = pygame.draw.rect(self.screen, self.color, self.dimensions)    

whiteRect = rect("white", (50, 75, 300, 120))
redRect = rect("red", (150, 200, 100, 40))
purpleRect = rect("purple", (310, 100, 105, 64))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.fill("pink")
    whiteRect.display()
    redRect.display()
    purpleRect.display()
    pygame.display.update()
