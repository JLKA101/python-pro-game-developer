import pygame
from time import time
from random import randint
pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("pollinate! :D")
font = pygame.font.SysFont("Serif", 30)

clock = pygame.time.Clock()
score = 0
gameOver = False
fleur = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("hib.png"), (50, 50)), 0)
flower = pygame.Rect(500, 300, 50, 50)
bumblebee = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("bee.png"), (75, 75)), 0)
bee = pygame.Rect(750, 300, 50, 50)
grass = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("grass.jpg"), (800, 800)), 0)
winner = ""
startTime = time()
gameDuration = 30
print(startTime)
victory_chime = pygame.mixer.Sound("chime.mp3")
point = pygame.mixer.Sound("point.mp3")

def draw():
    screen.blit(grass, (0, 0))
    screen.blit(fleur, (flower.x, flower.y))
    screen.blit(bumblebee, (bee.x, bee.y))
    redtext = font.render(f"score: {score}", True, "white")
    screen.blit(redtext, (605, 50))

    victory = font.render(f"Time's up! You scored {score}", True, "white")
    if gameOver:
        screen.blit(grass, (0, 0))
        screen.blit(victory, (400, 100))
        victory_chime.play()

def collide():
    global score
    if bee.colliderect(flower):
        score += 10
        point.play()
        flower.center = randint(25, 775), randint(25, 775)

"""
HOMEWORK hint :)
yellow and red ships are each separate moving functions
move the rect, not the image
"""

def move(keys):
        if keys[pygame.K_w]:
            bee.y -= 10
        if keys[pygame.K_s]:
            bee.y += 10
        if keys[pygame.K_a]:
            bee.x -= 10
        if keys[pygame.K_d]:
            bee.x += 10
        if bee.left < 0:
            bee.left = 0
        if bee.top < 0:
            bee.top = 0
        if bee.right > 800:
            bee.right = 800
        if bee.bottom > 800:
            bee.bottom = 800

while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    draw()
    keys = pygame.key.get_pressed()
    move(keys)
    collide()
    timePassed = time() - startTime
    if timePassed >= gameDuration:
        gameOver = True
    pygame.display.update()
"""    if gameOver == False:
        shoot(yellowbullet, redbullet)"""