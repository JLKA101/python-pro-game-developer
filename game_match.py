import pygame, time
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("card")
font = pygame.font.SysFont("Calibri", 50)

pos = None
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            pygame.draw.circle(screen, "white", pos, 15)
            pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP:
            pos2 = pygame.mouse.get_pos()
            pygame.draw.line(screen, "white", pos, pos2)
            pygame.draw.circle(screen, "white", pos2, 15)
            pygame.display.update()
    img1 = pygame.image.load("candy.jpg")
    screen.blit(img1, (50, 50))
    img2 = pygame.image.load("surfers.png")
    screen.blit(img2, (50, 150))
    img3 = pygame.image.load("temple.png")
    screen.blit(img3, (50, 250))
    img4 = pygame.image.load("ludo.png")
    screen.blit(img4, (50, 350))

    text = font.render("Ludo", True, "green")
    screen.blit(text, (300, 50))
    text = font.render("Subway Surfers", True, "red")
    screen.blit(text, (300, 150))
    text = font.render("Candy Crush", True, "pink")
    screen.blit(text, (300, 250))
    text = font.render("Temple Run", True, "orange")
    screen.blit(text, (300, 350))

    pygame.display.update()