import pygame
from pygame.locals import *

def makeOver():
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    running = True

    background = pygame.image.load("room.jpg")
    background = pygame.transform.scale(background, screen.get_size())

    closeButton = pygame.Surface((20, 20), pygame.SRCALPHA)
    closeButton_rect = closeButton.get_rect(topleft=(1880, 10))

    line_color = (255, 255, 255)
    line_thickness = 4
    pygame.draw.line(closeButton, line_color, (0, 0), (20, 20), line_thickness)
    pygame.draw.line(closeButton, line_color, (0, 20), (20, 0), line_thickness)

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                break
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if closeButton_rect.collidepoint(pos):
                    running = False
                    break

        screen.blit(background, (0, 0))
        screen.blit(closeButton, closeButton_rect.topleft)
        pygame.display.flip()

    pygame.quit()

makeOver()
