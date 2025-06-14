import pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("drawing pad with circle class")

class circles:
    def __init__(self, color, position, radius):
        self.color = color
        self.position = position
        self.radius = radius
        self.screen = screen

    def display(self):
        pygame.draw.circle(self.screen, self.color, self.position, self.radius)

    def grow(self):
        self.radius += 5
        pygame.draw.circle(self.screen, self.color, self.position, self.radius)

c1 = circles("purple", (300, 250), 50)
c2 = circles("orange", (400, 300), 20)
c3 = circles("green", (300, 500), 55)
c4 = circles("blue", (100, 350), 40)
c5 = circles("yellow", (300, 320), 20)

screen.fill("white")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            c1.display()
            c2.display()
            c3.display()
            c4.display()
            c5.display()
            pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP:
            c1.grow()
            c2.grow()
            c3.grow()
            c4.grow()
            c5.grow()
            pygame.display.update()
        elif event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            c6 = circles("red", pos, 10)
            c6.display()
    pygame.display.update()