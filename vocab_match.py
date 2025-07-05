import pygame, time
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("french vocab match game: sweet treats")
font = pygame.font.SysFont("calibri", 50)
score = 0
lines = []
pairs = []

images = {
       "cake": pygame.transform.scale(pygame.image.load("cake_jp.png"),(100, 100)),
    "choc": pygame.transform.scale(pygame.image.load("chocolate_jp.png"), (100, 100)),
    "icecream": pygame.transform.scale(pygame.image.load("icecream_jp.png"), (100, 100)),
    "biscuit": pygame.transform.scale(pygame.image.load("biscuit_jp.png"), (100, 100))
}

imagepos = {
        "cake": pygame.Rect(50, 175, 100, 100),
       "choc": pygame.Rect(50, 425, 100, 100),
       "icecream": pygame.Rect(50, 300, 100, 100),
       "biscuit": pygame.Rect(50, 50, 100, 100)}

textpos = {
        "un chocolat": pygame.Rect(300, 200, 100, 100),
       "un biscuit": pygame.Rect(300, 450, 100, 100),
       "un gâteau": pygame.Rect(300, 75, 100, 100),
       "une glace": pygame.Rect(300, 325, 100, 100)}

matches = {
        "cake": "un gâteau",
       "choc": "un chocolat",
       "icecream": "une glace",
       "biscuit": "un biscuit"}

for name, pos in imagepos.items():
    screen.blit(images[name], (pos.x, pos.y))

for name, pos in textpos.items():
    text = font.render(name, True, "white")
    screen.blit(text, (pos.x, pos.y))

pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            end_pos = pygame.mouse.get_pos()

            start_label = None
            end_label = None
            for key, value in imagepos.items():
                if value.collidepoint(start_pos):
                    start_label = key
                    break
            for key, value in textpos.items():
                if value.collidepoint(end_pos):
                    end_label = key
                    break
            if start_label and end_label:
                pygame.draw.line(screen, "white", start_pos, end_pos, 5)
                pygame.display.update()
                
                if matches[start_label] == end_label and (start_label, end_label) not in pairs:
                    score += 1
                    pairs.append((start_label, end_label))
                    print(f"Correct answer! Score: {score}")
                else:
                    print(f"Wrong match! Score: {score}")
                pygame.display.update()