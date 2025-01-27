import pygame
import random
import math
import sys
from pygame.locals import *

beret = pygame.image.load("Assets/Accessories/beret.png")
lunettes = pygame.image.load("Assets/Accessories/lunettes.webp")
moustache = pygame.image.load("Assets/Accessories/moustache.webp")
beard = pygame.image.load("Assets/Accessories/beard.webp")
baguette = pygame.image.load("Assets/Accessories/baguette.webp")
flower = pygame.image.load("Assets/Accessories/flower.png")
noeud = pygame.image.load("Assets/Accessories/noeud.png")
eyelash = pygame.image.load("Assets/Accessories/eyelash.webp")
nailRight = pygame.image.load("Assets/Accessories/nailRight.webp")
nailLeft = pygame.image.load("Assets/Accessories/nailLeft.webp")
bulles = [pygame.image.load("Assets/Accessories/bulle" + colors + ".webp") for colors in ["Jaune", "Rose", "Verte", "Grise", "Bleue"]]

beret = pygame.transform.scale(beret, (100, 50))
lunettes = pygame.transform.scale(lunettes, (100, 50))
moustache = pygame.transform.scale(moustache, (100, 50))
beard = pygame.transform.scale(beard, (100, 50))
baguette = pygame.transform.scale(baguette, (100, 50))
flower = pygame.transform.scale(flower, (100, 50))
noeud = pygame.transform.scale(noeud, (100, 50))
eyelash = pygame.transform.scale(eyelash, (100, 50))
nailRight = pygame.transform.scale(nailRight, (100, 50))
nailLeft = pygame.transform.scale(nailLeft, (100, 50))
bulles = [pygame.transform.scale(color, (100, 100)) for color in bulles]

def save_image(selected, displayAccessories):
    output_surface = pygame.Surface((1200, 800), pygame.SRCALPHA)
    if selected:
        output_surface.blit(selected, (300, 200))
    for accessory, pos in displayAccessories:
        adjusted_pos = (pos[0] - 360, pos[1] - 40)
        output_surface.blit(accessory, adjusted_pos)
    pygame.image.save(output_surface, "Pop_ular Attraction/game/images/me normal.png")

def generate_random_point_in_circle(center_x, center_y, radius):
    angle = random.uniform(0, 2 * math.pi)
    distance = math.sqrt(random.uniform(0, 1)) * radius
    x = center_x + distance * math.cos(angle)
    y = center_y + distance * math.sin(angle)
    return x, y

def ball(selectedAccessories, displayAccessories, selected):
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    clock = pygame.time.Clock()
    time = 0
    running = True

    background = pygame.image.load("Assets/Background/cleanroom.jpg")
    background = pygame.transform.scale(background, screen.get_size())
    darken = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
    darken.fill((0, 0, 0, int(255 * 0.4)))

    saveButton = pygame.image.load("Assets/Background/save.webp")
    saveButton = pygame.transform.scale(saveButton, (200, 100))
    saveButton_rect = saveButton.get_rect(topleft=(40, 120))

    menuButton = pygame.image.load("Assets/Background/menu.webp")
    menuButton = pygame.transform.scale(menuButton, (50, 50))
    menuButton_rect = menuButton.get_rect(topleft=(40, 40))

    noeudpap = pygame.image.load("Assets/Accessories/noeudpap.webp")
    pearlNecklace = pygame.image.load("Assets/Accessories/pearlnecklace.png")

    noeudpap = pygame.transform.scale(noeudpap, (100, 50))
    pearlNecklace = pygame.transform.scale(pearlNecklace, (100, 50))

    accessories = [
        {"image": beret, "pos": (1650, 100)},
        {"image": lunettes, "pos": (1800, 100)},
        {"image": moustache, "pos": (1650, 220)},
        {"image": beard, "pos": (1800, 220)},
        {"image": baguette, "pos": (1650, 340)},
        {"image": flower, "pos": (1800, 340)},
        {"image": noeud, "pos": (1650, 460)},
        {"image": eyelash, "pos": (1800, 460)},
        {"image": nailRight, "pos": (1650, 580)},
        {"image": nailLeft, "pos": (1800, 580)},
        {"image": noeudpap, "pos": (1650, 700)},
        {"image": pearlNecklace, "pos": (1800, 700)},
        {"image": bulles[0], "pos": (1650, 820)},
        {"image": bulles[1], "pos": (1800, 820)},
        {"image": bulles[2], "pos": (1650, 940)},
        {"image": bulles[3], "pos": (1800, 940)},
        {"image": bulles[4], "pos": (1650, 1060)}
    ]

    menu_visible = False
    menu_x = 2000
    menu_speed = 20

    while running:
        time += clock.get_time()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                if menuButton_rect.collidepoint(pos):
                    menu_visible = not menu_visible

                if saveButton_rect.collidepoint(pos):
                    save_image(selected, displayAccessories)
                    running = False
                    break

                for accessory in accessories:
                    if accessory["image"] in bulles:
                        if accessory["image"].get_rect(topleft=(accessory["pos"][0], accessory["pos"][1])).collidepoint(pos):
                            selected = accessory["image"]
                            selected = pygame.transform.scale(selected, (600, 600))
                    elif accessory["image"] in selectedAccessories:
                        if accessory["image"].get_rect(topleft=(accessory["pos"][0], accessory["pos"][1])).collidepoint(pos):
                            displayAccessories.remove(displayAccessories[selectedAccessories.index(accessory["image"])])
                            selectedAccessories.remove(accessory["image"])
                    elif accessory["image"].get_rect(topleft=(accessory["pos"][0], accessory["pos"][1])).collidepoint(pos):
                        selectedAccessories.append(accessory["image"])
                        if accessory["image"] == flower:
                            displayAccessories.append((pygame.transform.scale(accessory["image"], (700, 400)), (610, 140)))
                        elif accessory["image"] == beret:
                            displayAccessories.append((pygame.transform.scale(accessory["image"], (800, 400)), (600, 150)))
                        elif accessory["image"] == noeud:
                            displayAccessories.append((pygame.transform.scale(accessory["image"], (600, 400)), (660, 150)))
                        elif accessory["image"] == lunettes:
                            displayAccessories.append((pygame.transform.scale(accessory["image"], (600, 300)), (660, 350)))
                        elif accessory["image"] == moustache:
                            displayAccessories.append((pygame.transform.scale(accessory["image"], (300, 100)), (810, 550)))
                        elif accessory["image"] == beard:
                            displayAccessories.append((pygame.transform.scale(accessory["image"], (700, 350)), (610, 450)))
                        elif accessory["image"] == baguette:
                            displayAccessories.append((pygame.transform.scale(accessory["image"], (400, 400)), (1110, 350)))
                        elif accessory["image"] == nailRight:
                            displayAccessories.append((pygame.transform.scale(accessory["image"], (400, 400)), (1110, 350)))
                        elif accessory["image"] == nailLeft:
                            displayAccessories.append((pygame.transform.scale(accessory["image"], (300, 300)), (450, 400)))
                        elif accessory["image"] == eyelash:
                            displayAccessories.append((pygame.transform.scale(accessory["image"], (600, 600)), (660, 240)))
                        elif accessory["image"] == pearlNecklace:
                            displayAccessories.append((pygame.transform.scale(accessory["image"], (580, 300)), (680, 550)))
                        elif accessory["image"] == noeudpap:
                            displayAccessories.append((pygame.transform.scale(accessory["image"], (600, 200)), (660, 550)))
                        else:
                            displayAccessories.append((pygame.transform.scale(accessory["image"], (600, 600)), (660, 40)))
        
        if not running:
            break

        if menu_visible and menu_x > 1600:
            menu_x -= menu_speed
        elif not menu_visible and menu_x < 2000:
            menu_x += menu_speed
        screen.blit(background, (0, 0))
        screen.blit(darken, (0, 0))
        if menu_visible or menu_x < 2000:
            pygame.draw.rect(screen, (50, 50, 50), (menu_x, 0, 600, screen.get_height()))
            if menu_x <= 1600:
                for accessory in accessories:
                    screen.blit(accessory["image"], (accessory["pos"][0], accessory["pos"][1]))
        
        screen.blit(menuButton, menuButton_rect.topleft)
        screen.blit(selected, (660, 240))
        screen.blit(saveButton, saveButton_rect.topleft)
        for (accesorry, pos) in displayAccessories:
            screen.blit(accesorry, pos)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

def makeOver():
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    clock = pygame.time.Clock()
    time = 0
    running = True
    xpE = 0
    ypE = 0
    dirty_op = 255
    cleaning_op = 0

    background = pygame.image.load("Assets/Background/room.jpg")
    background = pygame.transform.scale(background, screen.get_size())
    darken = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
    darken.fill((0, 0, 0, int(255 * 0.4)))

    saveButton = pygame.image.load("Assets/Background/save.webp")
    saveButton = pygame.transform.scale(saveButton, (200, 100))
    saveButton_rect = saveButton.get_rect(topleft=(40, 120))

    menuButton = pygame.image.load("Assets/Background/menu.webp")
    menuButton = pygame.transform.scale(menuButton, (50, 50))
    menuButton_rect = menuButton.get_rect(topleft=(40, 40))
    
    pinceEpiler = pygame.image.load("Assets/SkinIssue/Pince_a_épiler.png")
    comedon = pygame.image.load("Assets/SkinIssue/comedon.png")
    savon = pygame.image.load("Assets/SkinIssue/savon.png")
    shower = pygame.image.load("Assets/SkinIssue/shower.png")

    acne = pygame.image.load("Assets/SkinIssue/acne.png")
    acneperced = pygame.image.load("Assets/SkinIssue/acnepercé.png")
    dirt = pygame.image.load("Assets/SkinIssue/dirt.png")
    bodyHair = pygame.image.load("Assets/SkinIssue/poil.png")
    cleaningEffect = pygame.image.load("Assets/SkinIssue/effetsavon.png")

    pinceEpiler = pygame.transform.scale(pinceEpiler, (100, 50))
    comedon = pygame.transform.scale(comedon, (100, 100))
    savon = pygame.transform.scale(savon, (100, 100))
    shower = pygame.transform.scale(shower, (100, 100))

    acne = pygame.transform.scale(acne, (100, 100))
    acneperced = pygame.transform.scale (acneperced, (100, 100))
    dirt = pygame.transform.scale (dirt, (600, 600))
    bodyHair = pygame.transform.scale(bodyHair, (50, 100))
    cleaningEffect = pygame.transform.scale(cleaningEffect, (600, 600))

    dirt.set_alpha(dirty_op)
    cleaningEffect.set_alpha(cleaning_op)

    selected = bulles[3]
    selected = pygame.transform.scale(selected, (600, 600))
    selectedAccessories = []
    displayAccessories = []
    selectedTool = ""

    accessories = [
        {"image": beret, "pos": (1650, 100)},
        {"image": lunettes, "pos": (1800, 100)},
        {"image": moustache, "pos": (1650, 220)},
        {"image": beard, "pos": (1800, 220)},
        {"image": baguette, "pos": (1650, 340)},
        {"image": flower, "pos": (1800, 340)},
        {"image": noeud, "pos": (1650, 460)},
        {"image": eyelash, "pos": (1800, 460)},
        {"image": nailRight, "pos": (1650, 580)},
        {"image": nailLeft, "pos": (1800, 580)},
        {"image": bulles[0], "pos": (1650, 700)},
        {"image": bulles[1], "pos": (1800, 700)},
        {"image": bulles[2], "pos": (1650, 820)},
        {"image": bulles[3], "pos": (1800, 820)},
        {"image": bulles[4], "pos": (1650, 940)}
    ]

    tools = [
        {"outil": pinceEpiler, "pos": (550, 250)},
        {"outil": comedon, "pos": (550, 620)},
        {"outil": savon, "pos": (1300, 250)},
        {"outil": shower, "pos": (1300, 620)}
    ]

    skinIssues = [
        {"skin": acne, "pos": (1200, 500)},
        {"skin": acneperced, "pos": (1200, 520)},
        {"skin": bodyHair, "pos": (1200, 500)}
    ]

    menu_visible = False
    menu_x = 2000
    menu_speed = 20

    pimples = []
    for i in range(5):
        pimples.append([generate_random_point_in_circle(960, 540, 200), False])
    
    hairs = []
    for i in range(5):
        hairs.append([generate_random_point_in_circle(960, 540, 200), random.randint(0, 360)])

    while running:
        time += clock.get_time()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                if hairs == [] and pimples == [] and cleaning_op + dirty_op == 0 and menuButton_rect.collidepoint(pos):
                    menu_visible = not menu_visible

                if hairs == [] and pimples == [] and cleaning_op + dirty_op == 0 and saveButton_rect.collidepoint(pos):
                    save_image(selected, displayAccessories)
                    running = False
                    break

                for accessory in accessories:
                    if accessory["image"] in bulles:
                        if accessory["image"].get_rect(topleft=(accessory["pos"][0], accessory["pos"][1])).collidepoint(pos):
                            selected = accessory["image"]
                            selected = pygame.transform.scale(selected, (600, 600))
                    elif accessory["image"] in selectedAccessories:
                        if accessory["image"].get_rect(topleft=(accessory["pos"][0], accessory["pos"][1])).collidepoint(pos):
                            displayAccessories.remove(displayAccessories[selectedAccessories.index(accessory["image"])])
                            selectedAccessories.remove(accessory["image"])
                    elif accessory["image"].get_rect(topleft=(accessory["pos"][0], accessory["pos"][1])).collidepoint(pos):
                        selectedAccessories.append(accessory["image"])
                        if accessory["image"] == flower:
                            displayAccessories.append((pygame.transform.scale(accessory["image"], (700, 400)), (610, 140)))
                        elif accessory["image"] == beret:
                            displayAccessories.append((pygame.transform.scale(accessory["image"], (800, 400)), (600, 150)))
                        elif accessory["image"] == noeud:
                            displayAccessories.append((pygame.transform.scale(accessory["image"], (600, 400)), (660, 150)))
                        elif accessory["image"] == lunettes:
                            displayAccessories.append((pygame.transform.scale(accessory["image"], (600, 300)), (660, 350)))
                        elif accessory["image"] == moustache:
                            displayAccessories.append((pygame.transform.scale(accessory["image"], (300, 100)), (810, 550)))
                        elif accessory["image"] == beard:
                            displayAccessories.append((pygame.transform.scale(accessory["image"], (700, 350)), (610, 450)))
                        elif accessory["image"] == baguette:
                            displayAccessories.append((pygame.transform.scale(accessory["image"], (400, 400)), (1110, 350)))
                        elif accessory["image"] == nailRight:
                            displayAccessories.append((pygame.transform.scale(accessory["image"], (400, 400)), (1110, 350)))
                        elif accessory["image"] == nailLeft:
                            displayAccessories.append((pygame.transform.scale(accessory["image"], (300, 300)), (450, 400)))
                        elif accessory["image"] == eyelash:
                            displayAccessories.append((pygame.transform.scale(accessory["image"], (600, 600)), (660, 240)))
                        else:
                            displayAccessories.append((pygame.transform.scale(accessory["image"], (600, 600)), (660, 40)))

                for tool in tools:
                    if tool["outil"].get_rect(topleft=(tool["pos"][0], tool["pos"][1])).collidepoint(pos):
                        selectedTool = tool["outil"] if selectedTool != tool["outil"] else ""
                
                for pimple in pimples:
                    if selectedTool == comedon and acne.get_rect(topleft=pimple[0]).collidepoint(pos):
                        if pimple[1]:
                            pimples.remove(pimple)
                        else:
                            pimple[1] = True
                
                for hair in hairs:
                    if selectedTool == pinceEpiler and bodyHair.get_rect(topleft=hair[0]).collidepoint(pos):
                        hairs.remove(hair)

            if event.type == pygame.MOUSEMOTION:
                if selectedTool == savon and time >= 25:
                    if dirty_op != 0:
                        dirty_op -= 1
                    if cleaning_op != 255:
                        cleaning_op += 1
                    dirt.set_alpha(dirty_op)
                    cleaningEffect.set_alpha(cleaning_op)
                    time = 0
                if selectedTool == shower and time >= 25:
                    if cleaning_op != 0:
                        cleaning_op -= 1
                    cleaningEffect.set_alpha(cleaning_op)
                    time = 0
                    

            buttons = pygame.mouse.get_pressed()
            x, y = pygame.mouse.get_pos()
            xpE = x
            ypE = y

        if not running:
            break

        if menu_visible and menu_x > 1600:
            menu_x -= menu_speed
        elif not menu_visible and menu_x < 2000:
            menu_x += menu_speed
        screen.blit(background, (0, 0))
        screen.blit(darken, (0, 0))
        if menu_visible or menu_x < 2000:
            pygame.draw.rect(screen, (50, 50, 50), (menu_x, 0, 600, screen.get_height()))
            if menu_x <= 1600:
                for accessory in accessories:
                    screen.blit(accessory["image"], (accessory["pos"][0], accessory["pos"][1]))
        for tool in tools:
            screen.blit(tool["outil"], (tool["pos"][0], tool["pos"][1]))

        screen.blit(menuButton, menuButton_rect.topleft)
        screen.blit(selected, (660, 240))
        screen.blit(saveButton, saveButton_rect.topleft)
        if dirty_op != 0:
            screen.blit(dirt, (660, 240))
        if cleaning_op != 0:
            screen.blit(cleaningEffect, (660, 240))
        for pimple in pimples:
            if not pimple[1]:
                screen.blit(acne, pimple[0])
            else:
                screen.blit(acneperced, pimple[0])
        for hair in hairs:
            screen.blit(pygame.transform.rotate(bodyHair, hair[1]), hair[0])
        if selectedTool != "":
            screen.blit(selectedTool, (xpE, ypE))
        for (accesorry, pos) in displayAccessories:
            screen.blit(accesorry, pos)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    return selectedAccessories, displayAccessories, selected

if __name__ == "__main__":
    makeOver()  # Ou `ball([], [], None)`
