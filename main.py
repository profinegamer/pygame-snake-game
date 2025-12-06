import pygame
import random


pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snake game")
white = (255, 255, 255)
black = (0, 0, 0)
green = (54, 255, 0)
red = (255, 0, 0)
dark_green = (0, 150, 0)
LorR = 350
UorD = 450
big = 40
AUorD = random.randint(0, 599)
ALorR = random.randint(0, 799)
clock = pygame.time.Clock()



gamerunning = True
while gamerunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gamerunning = False
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        LorR -= 5
    elif pygame.key.get_pressed()[pygame.K_RIGHT]:
        LorR += 5
    elif pygame.key.get_pressed()[pygame.K_UP]:
        UorD -= 5
    elif pygame.key.get_pressed()[pygame.K_DOWN]:
        UorD += 5
    elif pygame.key.get_pressed()[pygame.K_ESCAPE]:
        gamerunning = False



    screen.fill(dark_green)
    Snake_rect = pygame.Rect(LorR, UorD, 40, 40)
    pygame.draw.rect(screen, green, Snake_rect)
    Apple_rect = pygame.Rect(ALorR, AUorD, 20, 20)
    pygame.draw.rect(screen, red, Apple_rect)
    Tail_rect = pygame.Rect((LorR - 50), (UorD - 50), big, big)
    pygame.draw.rect(screen, green, Tail_rect)

    clock.tick(40)
    if Snake_rect.colliderect(Apple_rect):
        big += 2
        AUorD = random.randint(0, 599)
        ALorR = random.randint(0, 799)

    pygame.display.flip()

pygame.quit()
