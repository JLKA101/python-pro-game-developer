import pygame, time
pygame.init()
screen = pygame.display.set_mode((216, 233))
pygame.display.set_caption("bulb")
font = pygame.font.SysFont("Calibri", 50)

pos = None
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            img2 = pygame.image.load("bulb_on.jpg")
            screen.blit(img2, (0, 0))
            pygame.display.update()
        if event.type == pygame.MOUSEBUTTONUP:
            img1 = pygame.image.load("bulb_off.jpg")
            screen.blit(img1, (0, 0))
            pygame.display.update()
