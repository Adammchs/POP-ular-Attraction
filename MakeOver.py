import pygame
from pygame.locals import *

def makeOver():
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    clock = pygame.time.Clock()
    running = True

    background = pygame.image.load("Assets/Background/room.jpg")
    background = pygame.transform.scale(background, screen.get_size())

    closeButton = pygame.Surface((20, 20), pygame.SRCALPHA)
    closeButton_rect = closeButton.get_rect(topleft=(1850, 40))
    pygame.draw.line(closeButton, (255, 255, 255), (0, 0), (20, 20), 3)
    pygame.draw.line(closeButton, (255, 255, 255), (0, 20), (20, 0), 3)

    menuButton = pygame.Surface((50, 50), pygame.SRCALPHA)
    menuButton_rect = menuButton.get_rect(topleft=(40, 40))
    pygame.draw.rect(menuButton, (0, 255, 0), (0, 0, 50, 50))

    beret = pygame.image.load("Assets/Accessories/beret.png")
    lunettes = pygame.image.load("Assets/Accessories/lunettes.webp")
    moustache = pygame.image.load("Assets/Accessories/moustache.webp")
    baguette = pygame.image.load("Assets/Accessories/baguette.webp")
    flower = pygame.image.load("Assets/Accessories/flower.png")
    noeud = pygame.image.load("Assets/Accessories/noeud.png")
    bulles = [pygame.image.load("Assets/Accessories/bulle" + colors + ".webp") for colors in ["Jaune", "Rose", "Verte", "Grise", "Bleue"]]

    beret = pygame.transform.scale(beret, (100, 100))
    lunettes = pygame.transform.scale(lunettes, (100, 50))
    moustache = pygame.transform.scale(moustache, (100, 50))
    baguette = pygame.transform.scale(baguette, (100, 50))
    flower = pygame.transform.scale(flower, (100, 50))
    noeud = pygame.transform.scale(noeud, (100, 50))
    bulles = [pygame.transform.scale(color, (100, 100)) for color in bulles]

    accessories = [
        {"image": beret, "pos": (1650, 100)},
        {"image": lunettes, "pos": (1800, 100)},
        {"image": moustache, "pos": (1650, 220)},
        {"image": baguette, "pos": (1800, 220)},
        {"image": flower, "pos": (1650, 340)},
        {"image": noeud, "pos": (1800, 340)},
        {"image": bulles[0], "pos": (1650, 460)},
        {"image": bulles[1], "pos": (1800, 460)},
        {"image": bulles[2], "pos": (1650, 580)},
        {"image": bulles[3], "pos": (1800, 580)},
        {"image": bulles[4], "pos": (1650, 700)}
    ]

    menu_visible = False
    menu_x = 2000
    menu_speed = 20

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
        
                if menuButton_rect.collidepoint(pos):
                    menu_visible = not menu_visible

        if menu_visible and menu_x > 1600:
            menu_x -= menu_speed
        elif not menu_visible and menu_x < 2000:
            menu_x += menu_speed
        screen.blit(background, (0, 0))
        if menu_visible or menu_x < 2000:
            pygame.draw.rect(screen, (50, 50, 50), (menu_x, 0, 600, screen.get_height()))
            for accessory in accessories:
                screen.blit(accessory["image"], (accessory["pos"][0], accessory["pos"][1]))
        screen.blit(menuButton, menuButton_rect.topleft)
        screen.blit(closeButton, closeButton_rect.topleft)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

makeOver()
