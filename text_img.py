import pygame, time
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("card")
font = pygame.font.SysFont("Calibri", 50)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    img1 = pygame.image.load("cover.jpg")
    screen.blit(img1, (0, 0))
    text = font.render("Happy Birthday", True, "pink")
    screen.blit(text, (165, 200))
    time.sleep(2)
    pygame.display.update()

    img2 = pygame.image.load("present.jpg")
    screen.blit(img2, (0, 0))
    text = font.render("Have a great day!", True, "red")
    screen.blit(text, (135, 200))
    time.sleep(2)
    pygame.display.update()

    img3 = pygame.image.load("cake.jpg")
    screen.blit(img3, (0, 0))
    text = font.render("Enjoy your cake :)", True, "orange")
    screen.blit(text, (135, 50))
    time.sleep(2)
    pygame.display.update()

