import pygame
pygame.init()
screen = pygame.display.set_mode((850, 600))
pygame.display.set_caption("spaceship battle :D")
font = pygame.font.SysFont("Serif", 30)

border = pygame.Rect(390, 0, 20, 600)
redhealth = 10
yellowhealth = 10
gameOver = False
yellowship = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("yellowship.png"), (50, 50)), 90)
redship = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("redship.png"), (50, 50)), 270)
yellowrect = pygame.Rect(50, 300, 50, 50)
redrect = pygame.Rect(750, 300, 50, 50)

def draw():
    screen.blit(pygame.image.load("nebula.png"), (0, 0))
    pygame.draw.rect(screen, "blue", border)
    screen.blit(yellowship, (yellowrect.x, yellowrect.y))
    screen.blit(redship, (redrect.x, redrect.y))
    yellowtext = font.render(f"Health: {yellowhealth}", True, "white")
    redtext = font.render(f"Health: {redhealth}", True, "white")
    screen.blit(yellowtext, (50, 50))
    screen.blit(redtext, (675, 50))

"""
HOMEWORK hint :)
yellow and red ships are each seperate moving functions
move the rect, not the image
"""

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    draw()
    pygame.display.update()