from os import startfile
from tkinter import *
from tkinter import messagebox as box
from tk1 import TKinput as input
import subprocess, pygame, os, game, sys, threading, webclient, pickle, random, time
def graphicdesign():
    pygame.font.init()
    import LevelInput
    clock = pygame.time.Clock()
    FPS = 60

    #game window
    SCREEN_WIDTH = 630
    SCREEN_HEIGHT = 630
    LOWER_MARGIN = 100
    SIDE_MARGIN = 320

    screen = pygame.display.set_mode(
        (SCREEN_WIDTH + SIDE_MARGIN, SCREEN_HEIGHT + LOWER_MARGIN))
    pygame.display.set_caption("Level Editor")

    #define game variables
    ROWS = 21
    MAX_COLS = 21
    TILE_SIZE = SCREEN_HEIGHT // ROWS
    TILE_TYPES = 10
    current_tile = 0
    scroll = 0

    sky_img = pygame.image.load(
        "img/Block-editor/Background/background.png").convert_alpha()
    #store tiles in a list
    img_list = []
    for x in range(TILE_TYPES):
        img = pygame.image.load(f"img/Block-editor/tile/{x}.png").convert_alpha()
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        img_list.append(img)

    save_img = pygame.image.load("img/Block-editor/play_btn.png").convert_alpha()

    #define colours
    GREEN = (144, 201, 120)
    WHITE = (255, 255, 255)
    RED = (200, 25, 25)

    #define font
    font = pygame.font.SysFont("Futura", 30)

    #create empty tile list
    world_data = []
    for row in range(ROWS):
        r = [0] * MAX_COLS
        world_data.append(r)
    
    class Button():

        def __init__(self, x, y, image, scale):
            width = image.get_width()
            height = image.get_height()
            self.image = pygame.transform.scale(
                image, (int(width * scale), int(height * scale)))
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            self.clicked = False

        def draw(self, surface):
            action = False

            #get mouse position
            pos = pygame.mouse.get_pos()

            #check mouseover and clicked conditions
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed(
                )[0] == 1 and self.clicked == False:
                    action = True
                    self.clicked = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

            #draw button
            surface.blit(self.image, (self.rect.x, self.rect.y))

            return action

    #function for outputting text onto the screen
    # def draw_text(text, font, text_col, x, y):
    # 	img = font.render(text, True, text_col)
    # 	screen.blit(img, (x, y))

    #create function for drawing background
    def draw_bg():
        screen.fill(GREEN)
        width = sky_img.get_width()
        for x in range(4):
            screen.blit(sky_img, ((x * width) - scroll * 0.5, 0))
            #screen.blit(mountain_img, ((x * width) - scroll * 0.6, SCREEN_HEIGHT - mountain_img.get_height() - 300))
            #screen.blit(pine1_img, ((x * width) - scroll * 0.7, SCREEN_HEIGHT - pine1_img.get_height() - 150))
            #screen.blit(pine2_img, ((x * width) - scroll * 0.8, SCREEN_HEIGHT - pine2_img.get_height()))

    #draw grid
    def draw_grid():
        #vertical lines
        for c in range(MAX_COLS + 1):
            pygame.draw.line(screen, WHITE, (c * TILE_SIZE - scroll, 0),
                             (c * TILE_SIZE - scroll, SCREEN_HEIGHT))
        #horizontal lines
        for c in range(ROWS + 1):
            pygame.draw.line(screen, WHITE, (0, c * TILE_SIZE),
                             (SCREEN_WIDTH, c * TILE_SIZE))

    #function for drawing the world tiles
    def draw_world():
        for y, row in enumerate(world_data):
            for x, tile in enumerate(row):
                if tile >= 0:
                    screen.blit(img_list[tile],
                                (x * TILE_SIZE - scroll, y * TILE_SIZE))

    #create buttons
    save_button = Button(SCREEN_WIDTH // 2, SCREEN_HEIGHT + LOWER_MARGIN - 50,
                         save_img, 1)
    #make a button list
    button_list = []
    button_col = 0
    button_row = 0
    for i in range(len(img_list)):
        tile_button = Button(SCREEN_WIDTH + (75 * button_col) + 50,
                             75 * button_row + 50, img_list[i], 1)
        button_list.append(tile_button)
        button_col += 1
        if button_col == 3:
            button_row += 1
            button_col = 0

    run = True
    while run:

        clock.tick(FPS)

        draw_bg()
        draw_grid()
        draw_world()

        #run levelbuilder
        if save_button.draw(screen):
            return world_data
        
        #draw tile panel and tiles
        pygame.draw.rect(screen, GREEN,
                         (SCREEN_WIDTH, 0, SIDE_MARGIN, SCREEN_HEIGHT))
        
        #choose a tile
        button_count = 0
        for button_count, i in enumerate(button_list):
            if i.draw(screen):
                current_tile = button_count

        #highlight the selected tile
        pygame.draw.rect(screen, RED, button_list[current_tile].rect, 3)

        #add new tiles to the screen
        #get mouse position
        pos = pygame.mouse.get_pos()
        x = (pos[0] + scroll) // TILE_SIZE
        y = pos[1] // TILE_SIZE

        #check that the coordinates are within the tile area
        if pos[0] < SCREEN_WIDTH and pos[1] < SCREEN_HEIGHT:
            #update tile value
            if pygame.mouse.get_pressed()[0] == 1:
                if world_data[y][x] != current_tile:
                    world_data[y][x] = current_tile
            if pygame.mouse.get_pressed()[2] == 1:
                world_data[y][x] = -1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

        #Designs a single level.
    
def create():
    name = input("Welcome to the custom block builder. What should it be named?")
    def askloopnum():
        num = input("How many custom blocks do you want (1-3)")
        num = int(num)
        if num > 3 or num < 1:
            print("Please enter a number between 1 and 3")
            askloopnum()
        else:
            return num
    num = askloopnum()
    maps = [[],[],[]]
    for i in range(num):
        input("Now we need to create a graphic.", False)
        maps[i] = graphicdesign()
        input("Now that we have the graphic, we need to create code.\n See http://gregglesthegreat.pythonanywhere.com/help for assistance.", False)
        os.system(f"start notepad.exe ./levels/code/{name}{i}.py")
        input("Press Ctrl+S on the code to save, close the editor and then press Submit.", False)
    if os.path.isfile(f"levels/{name}.pkl"):
        if box.askokcancel("File Exists!", "Continue?") == 1:
            pass
        else:
            create()
    else:
        pass
    with open(f"levels/{name}.pkl", "wb"):
        pickle.dump({"data":[], "leveldata":[], "code": open(f"levels/code/{name}.py", "rt").read(), "graphics":{"1":map}})

    

create()
