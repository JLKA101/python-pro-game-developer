import pygame
pygame.init()
screen = pygame.display.set_mode((850, 600))
pygame.display.set_caption("spaceship battle :D")
font = pygame.font.SysFont("Serif", 30)

clock = pygame.time.Clock()
border = pygame.Rect(390, 0, 20, 600)
redhealth = 10
yellowhealth = 10
gameOver = False
yellowship = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("yellowship.png"), (50, 50)), 90)
redship = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("redship.png"), (50, 50)), 270)
yellowrect = pygame.Rect(50, 300, 50, 50)
redrect = pygame.Rect(750, 300, 50, 50)
yellowbullet = []
redbullet = []
winner = ""

def draw():
    screen.blit(pygame.image.load("nebula.png"), (0, 0))
    pygame.draw.rect(screen, "blue", border)
    screen.blit(yellowship, (yellowrect.x, yellowrect.y))
    screen.blit(redship, (redrect.x, redrect.y))
    yellowtext = font.render(f"Health: {yellowhealth}", True, "white")
    redtext = font.render(f"Health: {redhealth}", True, "white")
    screen.blit(yellowtext, (50, 50))
    screen.blit(redtext, (675, 50))
    for i in yellowbullet:
        pygame.draw.rect(screen, "yellow", i)
    for i in redbullet:
        pygame.draw.rect(screen, "red", i)
    victory = font.render(winner, True, "white")
    if gameOver:
        screen.blit(pygame.image.load("nebula.png"), (0, 0))
        screen.blit(victory, (425, 300))


def shoot(yellowbullet, redbullet):
    global redhealth, yellowhealth
    for i in yellowbullet:
        i.x += 10
        if redrect.colliderect(i):
            redhealth -= 1
            yellowbullet.remove(i)
        elif i.x > 850:
            yellowbullet.remove(i)
    for i in redbullet:
        i.x -= 10
        if yellowrect.colliderect(i):
            yellowhealth -= 1
            redbullet.remove(i)
        elif i.x < 0:
            redbullet.remove(i)

"""
HOMEWORK hint :)
yellow and red ships are each separate moving functions
move the rect, not the image
"""

def yellow(keys):
        if keys[pygame.K_w]:
            yellowrect.y -= 10
        if keys[pygame.K_s]:
            yellowrect.y += 10
        if keys[pygame.K_a]:
            yellowrect.x -= 10
        if keys[pygame.K_d]:
            yellowrect.x += 10
        if yellowrect.left < 0:
            yellowrect.left = 0
        if yellowrect.top < 0:
            yellowrect.top = 0
        if yellowrect.right > 390:
            yellowrect.right = 390
        if yellowrect.bottom > 600:
            yellowrect.bottom = 600

def red(keys):
        if keys[pygame.K_UP]:
            redrect.y -= 10
        if keys[pygame.K_DOWN]:
            redrect.y += 10
        if keys[pygame.K_LEFT]:
            redrect.x -= 10
        if keys[pygame.K_RIGHT]:
            redrect.x += 10
        if redrect.left < 410:
            redrect.left = 410
        if redrect.top < 0:
            redrect.top = 0
        if redrect.right > 850:
            redrect.right = 850
        if redrect.bottom > 600:
            redrect.bottom = 600

def finished():
    global gameOver, winner
    if yellowhealth == 0:
        winner = "Yellow lost. Red victory!"
        gameOver = True

    if redhealth == 0:
        winner = "Red lost. Yellow victory!"
        gameOver = True
        
    if redhealth == 0 and yellowhealth == 0:
        winner = "Tie."
        gameOver = True
        
while True:
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                bullet = pygame.Rect(yellowrect.x + 25, yellowrect.y + 25, 10, 10)
                yellowbullet.append(bullet)
            if event.key == pygame.K_l:
                bullet = pygame.Rect(redrect.x + 25, redrect.y + 25, 10, 10)
                redbullet.append(bullet)
    draw()
    keys = pygame.key.get_pressed()
    yellow(keys)
    red(keys)
    if gameOver == False:
        shoot(yellowbullet, redbullet)
    finished()
    pygame.display.update()