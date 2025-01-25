import pygame
from pygame.locals import *

def save_image(selected, displayAccessories):
    # Create a transparent surface with the same size as the screen
    output_surface = pygame.Surface((1000, 800), pygame.SRCALPHA)
    
    # Draw the selected bubble
    if selected:
        output_surface.blit(selected, (100, 200))
    
    # Draw the accessories
    for accessory, pos in displayAccessories:
        # Adjust the position to fit inside the saved image
        adjusted_pos = (pos[0] - 560, pos[1] - 40)  # Offset based on rendering position
        output_surface.blit(accessory, adjusted_pos)
    
    # Save as a PNG
    pygame.image.save(output_surface, "Assets/Characters/mainCharacter.png")
    print("Image saved as output.png")

def makeOver():
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    clock = pygame.time.Clock()
    running = True
    xpE = 0
    ypE = 0

    background = pygame.image.load("Assets/Background/room.jpg")
    background = pygame.transform.scale(background, screen.get_size())
    darken = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
    darken.fill((0, 0, 0, int(255 * 0.4)))

    closeButton = pygame.Surface((20, 20), pygame.SRCALPHA)
    closeButton_rect = closeButton.get_rect(topleft=(1850, 40))
    pygame.draw.line(closeButton, (255, 255, 255), (0, 0), (20, 20), 3)
    pygame.draw.line(closeButton, (255, 255, 255), (0, 20), (20, 0), 3)
    saveButton = pygame.Surface((100, 50), pygame.SRCALPHA)
    saveButton_rect = saveButton.get_rect(topleft=(40, 120))
    pygame.draw.rect(saveButton, (0, 0, 255), (0, 0, 100, 50))
    font = pygame.font.Font(None, 24)
    text = font.render("Save", True, (255, 255, 255))
    saveButton.blit(text, (10, 10))

    menuButton = pygame.Surface((50, 50), pygame.SRCALPHA)
    menuButton_rect = menuButton.get_rect(topleft=(40, 40))
    pygame.draw.rect(menuButton, (0, 255, 0), (0, 0, 50, 50))

    beret = pygame.image.load("Assets/Accessories/beret.png")
    lunettes = pygame.image.load("Assets/Accessories/lunettes.webp")
    moustache = pygame.image.load("Assets/Accessories/moustache.webp")
    beard = pygame.image.load("Assets/Accessories/beard.webp")
    baguette = pygame.image.load("Assets/Accessories/baguette.webp")
    flower = pygame.image.load("Assets/Accessories/flower.png")
    noeud = pygame.image.load("Assets/Accessories/noeud.png")
    bulles = [pygame.image.load("Assets/Accessories/bulle" + colors + ".webp") for colors in ["Jaune", "Rose", "Verte", "Grise", "Bleue"]]
    pinceEpiler = pygame.image.load("Assets/SkinIssue/Pince_a_épiler.png")
    comedon = pygame.image.load("Assets/SkinIssue/comedon.png")
    savon = pygame.image.load("Assets/SkinIssue/savon.png")
    shower = pygame.image.load("Assets/SkinIssue/shower.png")

    beret = pygame.transform.scale(beret, (100, 50))
    lunettes = pygame.transform.scale(lunettes, (100, 50))
    moustache = pygame.transform.scale(moustache, (100, 50))
    beard = pygame.transform.scale(beard, (100, 50))
    baguette = pygame.transform.scale(baguette, (100, 50))
    flower = pygame.transform.scale(flower, (100, 50))
    noeud = pygame.transform.scale(noeud, (100, 50))
    bulles = [pygame.transform.scale(color, (100, 100)) for color in bulles]
    pinceEpiler = pygame.transform.scale(pinceEpiler, (100, 50))
    comedon = pygame.transform.scale(comedon, (100, 100))
    savon = pygame.transform.scale(savon, (100, 100))
    shower = pygame.transform.scale(shower, (100, 100))

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
        {"image": bulles[0], "pos": (1800, 460)},
        {"image": bulles[1], "pos": (1650, 580)},
        {"image": bulles[2], "pos": (1800, 580)},
        {"image": bulles[3], "pos": (1650, 700)},
        {"image": bulles[4], "pos": (1800, 700)}
    ]

    tools = [
        {"outil": pinceEpiler, "pos": (550, 250)},
        {"outil": comedon, "pos": (550, 620)},
        {"outil": savon, "pos": (1300, 250)},
        {"outil": shower, "pos": (1300, 620)}
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

                if saveButton_rect.collidepoint(pos):
                    save_image(selected, displayAccessories)

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
                        else:
                            displayAccessories.append((pygame.transform.scale(accessory["image"], (600, 600)), (660, 40)))
                for tool in tools:
                    if tool["outil"].get_rect(topleft=(tool["pos"][0], tool["pos"][1])).collidepoint(pos):
                        selectedTool = tool["outil"] if selectedTool != tool["outil"] else ""
            buttons = pygame.mouse.get_pressed()
            x, y = pygame.mouse.get_pos()
            xpE = x
            ypE = y

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
        screen.blit(closeButton, closeButton_rect.topleft)
        screen.blit(selected, (660, 240))
        screen.blit(saveButton, saveButton_rect.topleft)
        if selectedTool != "":
            screen.blit(selectedTool, (xpE, ypE))
        for (accesorry, pos) in displayAccessories:
            screen.blit(accesorry, pos)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

makeOver()
