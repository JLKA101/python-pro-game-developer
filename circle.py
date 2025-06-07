import pygame
pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("bouncy circle")

ball = pygame.draw.circle(surface=screen, color="purple", center=[500, 300], radius=40)
speed = [1, 1]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.fill("orange")
    ball = ball.move(speed)
    if ball.left <= 0 or ball.right >=1000:
        speed[0]=-speed[0]
    if ball.top <= 0 or ball.bottom >=600:
        speed[1]=-speed[1]
    pygame.draw.circle(surface=screen, color="purple", center=ball.center, radius=40)
    pygame.display.update()

