import pygame
from pygame.locals import *
from pygame.font import *
from os import *
from OnlineCLI import *
import mptfetch, mptupload, webclient, functionality
#https://youtu.be/l4-0_nayHac

def start(lvl, MM, cst_ldata, players):
    global SERVER_URL
    print(type(lvl))
    print("starting with Level " + str(lvl))
    pygame.init()
    pygame.font.init()
    clock = pygame.time.Clock()
    fps = 60

    screen_width = 1000
    screen_height = 1000

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Platformer")

    #define font
    font = pygame.font.SysFont("Bauhaus 93", 70)
    font_score = pygame.font.SysFont("Bauhaus 93", 30)

    #define game variables
    tile_size = 50
    game_over = 0
    main_menu = MM
    print(main_menu)
    max_lvls = 3
    score = 0

    #define colours
    white = (255, 255, 255)
    red = (255, 0, 0)
    lime = (0, 255, 0)

    #load images
    #sun_img = pygame.image.load("img/sun.png")
    bg_img = pygame.image.load("img/sky.png")
    restart_img = pygame.image.load("img/restart_btn.png")
    start_img = pygame.image.load("img/start_btn.png")
    exit_img = pygame.image.load("img/exit_btn.png")
    exit2_img = pygame.image.load("img/exit2_btn.png")
    #lvlload
    #20x20
    lvl_1_data = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8], 
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7], 
                  [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 1], 
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7], 
                  [0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 7, 1, 7], 
                  [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7], 
                  [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0], 
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0], 
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0], 
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0], 
                  [6, 6, 6, 6, 6, 6, 6, 1, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0], 
                  [1, 1, 1, 1, 1, 1, 1, 7, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0], 
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0], 
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0], 
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                  [0, 0, 1, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                  [0, 0, 5, 1, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6], 
                  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    lvl_2_data = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 1],
        [1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 2, 2, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 7, 0, 5, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1],
        [1, 7, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 7, 0, 0, 0, 0, 1],
        [1, 0, 2, 0, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 2, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  
        #[1, 0, 0, 2, 0, 0, 4, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 0, 0, 0, 2, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 2, 2, 2, 2, 1],
        [1, 0, 0, 0, 0, 0, 2, 2, 2, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]
    lvl_3_data = [
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [2, 2, 2, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 2, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 5, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 2, 2, 0, 4, 0, 0, 4, 0, 2, 6, 6, 6, 6, 6, 6, 6],
      [1, 0, 0, 5, 0, 1, 0, 0, 0, 0, 0, 0, 1, 2, 1, 1, 1, 1, 1, 1],
      [1, 0, 0, 0, 0, 1, 6, 6, 6, 6, 6, 6, 1, 1, 2, 1, 1, 1, 1, 1],
      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]
    if lvl == 1:
        lvl_data = lvl_1_data
    elif lvl == 2:
        lvl_data = lvl_2_data
    elif lvl == 3:
        lvl_data = lvl_3_data
    elif lvl == "cst":  #custom lvl
        lvl_data = cst_ldata
    else:
        print("We have not made. That level yet. ")
        raise ValueError

    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))

    class Button():

        def __init__(self, x, y, image):
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.clicked = False

        def draw(self):
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
            screen.blit(self.image, self.rect)

            return action

    class Player(pygame.sprite.Sprite):
          def __init__(self, x, y, keys):
            pygame.sprite.Sprite.__init__(self)
            self.reset(x, y)
            self.keys = keys

          def update(self, game_over):
            dx = 0
            dy = 0
            walk_cooldown = 5
            col_thresh = 20

            if game_over == 0:
                # get keypresses
                key = pygame.key.get_pressed()
                if key[self.keys["jump"]] and not self.jumped and not self.in_air:
                    self.vel_y = -15
                    self.jumped = True
                if not key[self.keys["jump"]]:
                    self.jumped = False
                if key[self.keys["left"]]:
                    dx -= 5
                    self.counter += 1
                    self.direction = -1
                if key[self.keys["right"]]:
                    dx += 5
                    self.counter += 1
                    self.direction = 1
                if not key[self.keys["left"]] and not key[self.keys["right"]]:
                    self.counter = 0
                    self.index = 0
                    if self.direction == 1:
                        self.image = self.images_right[self.index]
                    if self.direction == -1:
                        self.image = self.images_left[self.index]

                # handle animation
                if self.counter > walk_cooldown:
                    self.counter = 0
                    self.index += 1
                    if self.index >= len(self.images_right):
                        self.index = 0
                    if self.direction == 1:
                        self.image = self.images_right[self.index]
                    if self.direction == -1:
                        self.image = self.images_left[self.index]

                # add gravity
                self.vel_y += 1
                if self.vel_y > 10:
                    self.vel_y = 10
                dy += self.vel_y

                # check for collision
                self.in_air = True
                for tile in world.tile_list:
                    # check for collision in x direction
                    if tile[1].colliderect(self.rect.x + dx, self.rect.y,
                                           self.width, self.height):
                        dx = 0
                    # check for collision in y direction
                    if tile[1].colliderect(self.rect.x, self.rect.y + dy,
                                           self.width, self.height):
                        # check if below the ground i.e. jumping
                        if self.vel_y < 0:
                            dy = tile[1].bottom - self.rect.top
                            self.vel_y = 0
                        # check if above the ground i.e. falling
                        elif self.vel_y >= 0:
                            dy = tile[1].top - self.rect.bottom
                            self.vel_y = 0
                            self.in_air = False

                # check for collision with enemies
                if pygame.sprite.spritecollide(self, blob_group, False):
                    game_over = -1

                # check for collision with lava
                if pygame.sprite.spritecollide(self, lava_group, False):
                    game_over = -1

                # check for collision with exit
                if pygame.sprite.spritecollide(self, exit_group, False):
                    game_over = 1

                # check for collision with platforms
                for platform in platform_group:
                    # collision in the x direction
                    if platform.rect.colliderect(self.rect.x + dx, self.rect.y,
                                                 self.width, self.height):
                        dx = 0
                    # collision in the y direction
                    if platform.rect.colliderect(self.rect.x, self.rect.y + dy,
                                                 self.width, self.height):
                        # check if below platform
                        if abs((self.rect.top + dy) -
                               platform.rect.bottom) < col_thresh:
                            self.vel_y = 0
                            dy = platform.rect.bottom - self.rect.top
                        # check if above platform
                        elif abs((self.rect.bottom + dy) -
                                 platform.rect.top) < col_thresh:
                            self.rect.bottom = platform.rect.top - 1
                            self.in_air = False
                            dy = 0
                        # move sideways with the platform
                        if platform.move_x != 0:
                            self.rect.x += platform.move_direction

                # update player coordinates
                self.rect.x += dx
                self.rect.y += dy

            elif game_over == -1:
                self.image = self.dead_image
                draw_text("GAME OVER!", font, red, (screen_width // 2) - 200,
                          screen_height // 2)
                if self.rect.y > 200:
                    self.rect.y -= 5

            # draw player onto screen
            screen.blit(self.image, self.rect)

            return game_over
          def reset(self, x, y):
            self.images_right = []
            self.images_left = []
            self.index = 0
            self.counter = 0
            for num in range(1, 5):
                img_right = pygame.image.load(f"img/guy{num}.png")
                img_right = pygame.transform.scale(img_right, (40, 80))
                img_left = pygame.transform.flip(img_right, True, False)
                self.images_right.append(img_right)
                self.images_left.append(img_left)
            self.dead_image = pygame.image.load("img/ghost.png")
            self.image = self.images_right[self.index]
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.width = self.image.get_width()
            self.height = self.image.get_height()
            self.vel_y = 0
            self.jumped = False
            self.direction = 0
            self.in_air = True
    class OPlayer(pygame.sprite.Sprite):
          def __init__(self, x, y, num):
            pygame.sprite.Sprite.__init__(self)
            self.reset(x, y)
            self.num = num

          async def update(self, game_over):
            
            

            walk_cooldown = 5

            if game_over == 0:

                # handle animation
                if self.counter > walk_cooldown:
                    self.counter = 0
                    self.index += 1
                    if self.index >= len(self.images_right):
                        self.index = 0
                    if self.direction == 1:
                        self.image = self.images_right[self.index]
                    if self.direction == -1:
                        self.image = self.images_left[self.index]

                # # check for collision with enemies
                # if pygame.sprite.spritecollide(self, blob_group, False):
                #     game_over = -1

                # # check for collision with lava
                # if pygame.sprite.spritecollide(self, lava_group, False):
                #     game_over = -1

                # # check for collision with exit
                # if pygame.sprite.spritecollide(self, exit_group, False):
                #     game_over = 1
                
                # update player coordinates
                self.rect.x = dx
                self.rect.y = dy


            # elif game_over == -1:
            #     self.image = self.dead_image
            #     draw_text("GAME OVER!", font, red, (screen_width // 2) - 200,
            #               screen_height // 2)
            #     if self.rect.y > 200:
            #         self.rect.y -= 5

            # draw player onto screen
            screen.blit(self.image, self.rect)

            return game_over
          def reset(self, x, y):
            self.images_right = []
            self.images_left = []
            self.index = 0
            self.counter = 0
            for num2 in range(1, 5):
                img_right = pygame.image.load(f"img/guy{num2}.png")
                img_right = pygame.transform.scale(img_right, (40, 80))
                img_left = pygame.transform.flip(img_right, True, False)
                self.images_right.append(img_right)
                self.images_left.append(img_left)
            self.dead_image = pygame.image.load("img/ghost.png")
            self.image = self.images_right[self.index]
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.width = self.image.get_width()
            self.height = self.image.get_height()
            self.vel_y = 0
            self.jumped = False
            self.direction = 0
            self.in_air = True
            self.dx = 0
            self.dy = 0
    class World():

        def __init__(self, data):
            self.tile_list = []

            #load images
            dirt_img = pygame.image.load("img/dirt.png")
            grass_img = pygame.image.load("img/grass.png")

            row_count = 0
            for row in data:
                col_count = 0
                for tile in row:
                    if tile == 1:
                        img = pygame.transform.scale(dirt_img,
                                                     (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect)
                        self.tile_list.append(tile)
                    if tile == 2:
                        img = pygame.transform.scale(grass_img,
                                                     (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect)
                        self.tile_list.append(tile)
                    if tile == 3:
                        blob = Enemy(col_count * tile_size,
                                     row_count * tile_size + 15)
                        blob_group.add(blob)
                    if tile == 4:
                        platform = Platform(col_count * tile_size,
                                            row_count * tile_size, 1, 0)
                        platform_group.add(platform)
                    if tile == 5:
                        platform = Platform(col_count * tile_size,
                                            row_count * tile_size, 0, 1)
                        platform_group.add(platform)
                    if tile == 6:
                        lava = Lava(col_count * tile_size,
                                    row_count * tile_size + (tile_size // 2))
                        lava_group.add(lava)
                    if tile == 7:
                        coin = Coin(col_count * tile_size + (tile_size // 2),
                                    row_count * tile_size + (tile_size // 2))
                        coin_group.add(coin)
                    if tile == 8:
                        exit = Exit(col_count * tile_size,
                                    row_count * tile_size - (tile_size // 2))
                        exit_group.add(exit)
                    col_count += 1
                row_count += 1

        def draw(self):
            for tile in self.tile_list:
                screen.blit(tile[0], tile[1])

    class Enemy(pygame.sprite.Sprite):

        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load("img/blob.png")
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.move_direction = 1
            self.move_counter = 0

        def update(self):
            self.rect.x += self.move_direction
            self.move_counter += 1
            if abs(self.move_counter) > 50:
                self.move_direction *= -1
                self.move_counter *= -1

    class Platform(pygame.sprite.Sprite):

        def __init__(self, x, y, move_x, move_y):
            pygame.sprite.Sprite.__init__(self)
            img = pygame.image.load("img/platform.png")
            self.image = pygame.transform.scale(img,
                                                (tile_size, tile_size // 2))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.move_counter = 0
            self.move_direction = 1
            self.move_x = move_x
            self.move_y = move_y

        def update(self):
            self.rect.x += self.move_direction * self.move_x
            self.rect.y += self.move_direction * self.move_y
            self.move_counter += 1
            if abs(self.move_counter) > 50:
                self.move_direction *= -1
                self.move_counter *= -1

    class Lava(pygame.sprite.Sprite):

        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            img = pygame.image.load("img/lava.png")
            self.image = pygame.transform.scale(img,
                                                (tile_size, tile_size // 2))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

    class Coin(pygame.sprite.Sprite):

        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            img = pygame.image.load("img/coin.png")
            self.image = pygame.transform.scale(
                img, (tile_size // 2, tile_size // 2))
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)

    class Exit(pygame.sprite.Sprite):

        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            img = pygame.image.load("img/exit.png")
            self.image = pygame.transform.scale(
                img, (tile_size, int(tile_size * 1.5)))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

    player = Player(100, screen_height - 130, {"jump": pygame.K_UP, "left": pygame.K_LEFT, "right": pygame.K_RIGHT})
    player2 = OPlayer(100, screen_height - 130, 2)




    blob_group = pygame.sprite.Group()
    platform_group = pygame.sprite.Group()
    lava_group = pygame.sprite.Group()
    coin_group = pygame.sprite.Group()
    exit_group = pygame.sprite.Group()

    #create dummy coin for showing the score
    score_coin = Coin(tile_size // 2, tile_size // 2)
    coin_group.add(score_coin)
    #important, this bit is
    world = World(lvl_data)

    #create buttons
    restart_button = Button(screen_width // 2 - 190, screen_height // 2 + 100,
                            restart_img)
    exit_button_smol = Button(screen_width // 2 + 50, screen_height // 2 + 100,
                              exit2_img)
    start_button = Button(screen_width // 2 - 350, screen_height // 2,
                          start_img)
    exit_button = Button(screen_width // 2 + 150, screen_height // 2, exit_img)


    def Update():
        mptfetch.start_player_update_thread(SERVER_URL, players, currentplayer)
    run = True
    while run:

        clock.tick(fps)

        screen.blit(bg_img, (0, 0))
        #screen.blit(sun_img, (100, 100))

        if main_menu == True:
            if exit_button.draw():
                quit()
            if start_button.draw():
                main_menu = False
        else:
            world.draw()

            if game_over == 0:
                blob_group.update()
                platform_group.update()
                #update score
                #check if a coin has been collected
                if pygame.sprite.spritecollide(player, coin_group, True):
                    score += 1
                draw_text("X " + str(score) + "   Level: " + str(lvl), font_score, white, tile_size - 10,
                          10)
                if pygame.sprite.spritecollide(player2, coin_group, True):
                  score += 1
                  draw_text("X " + str(score) + "   Level: " + str(lvl), font_score, white, tile_size - 10,
                      10)

            blob_group.draw(screen)
            platform_group.draw(screen)
            lava_group.draw(screen)
            coin_group.draw(screen)
            exit_group.draw(screen)

            game_over = player.update(game_over)
            async def playerUpdate():
                await player2.update(game_over)
            #if player has died
            if game_over == -1:
                if exit_button_smol.draw():
                    exit()
                if restart_button.draw():
                    if lvl == "cst":
                        print("Restarting custom level")
                        start("cst", False, cst_ldata, players)
                    elif isinstance(lvl, int):
                      print("Restarting with Level " + str(lvl))
                      start(lvl, False, [], players)

            #if player has completed the lvl
            if game_over == 1:
                #reset game and go to next lvl
                if isinstance(lvl, int):
                  lvl += 1
                  if lvl <= max_lvls:
                      #reset lvl
                      start(lvl, False, [], players)
                      game_over = 0
                  else:
                      draw_text("YOU WIN!", font, lime,
                                (screen_width // 2) - 140, screen_height // 2)
                      if exit_button_smol.draw():
                        exit()
                      if restart_button.draw():
                          #reset lvl
                          lvl = 1
                          game_over = 0
                          score = 0
                          start(lvl, False, [], players)
                elif lvl ==  "cst":
                    draw_text("YOU WIN!", font, lime,
                                (screen_width // 2) - 140, screen_height // 2)
                    if exit_button_smol.draw():
                      exit()
                    if restart_button.draw():
                        #reset lvl
                        game_over = 0
                        score = 0
                        print("Restarting custom level")
                        start("cst", False, cst_ldata)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    return True

def Begin():
    global SERVER_URL
    SERVER_URL = Setup()
    level = int(webclient.get_variable(SERVER_URL,"b_pgp_Custom"))
    if level == 1:
        start(1, False, [], int(webclient.get_variable(SERVER_URL,"i_pgp_Players")))
    elif level == 2:
        print(type(webclient.get_variable(SERVER_URL,"l_pgp_level-data")))
        start("cst", False, eval(str(webclient.get_variable(SERVER_URL,"l_pgp_level-data"))), int(webclient.get_variable(SERVER_URL,"i_pgp_Players")))

if __name__ == "__main__":
    global PlayerN
    global SERVER_URL  # Declare SERVER_URL as global
    PlayerN, SERVER_URL = Setup()
    print(SERVER_URL) 
    level = int(webclient.get_variable(SERVER_URL,"b_pgp_Custom"))
    if level == 1:
        start(1, False, [], int(webclient.get_variable(SERVER_URL,"i_pgp_Players")))
    elif level == 2:
        print(type(webclient.get_variable(SERVER_URL,"l_pgp_level-data")))
        start("cst", False, eval(str(webclient.get_variable(SERVER_URL,"l_pgp_level-data"))), int(webclient.get_variable(SERVER_URL,"i_pgp_Players")))
