import pygame
from pygame.locals import *
from pygame.font import *
from os import *
#https://youtu.be/l4-0_nayHac

def start(lvl, MM, cst_ldata):
    print(type(lvl))
    print("starting with Level " + str(lvl))
    pygame.init()
    pygame.font.init()
    clock = pygame.time.Clock()
    fps = 60

    screen_width = 1000
    screen_height = 1000

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Platformer')

    #define font
    font = pygame.font.SysFont('Bauhaus 93', 70)
    font_score = pygame.font.SysFont('Bauhaus 93', 30)

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
    #sun_img = pygame.image.load('img/sun.png')
    bg_img = pygame.image.load('img/sky.png')
    restart_img = pygame.image.load('img/restart_btn.png')
    start_img = pygame.image.load('img/start_btn.png')
    exit_img = pygame.image.load('img/exit_btn.png')
    exit2_img = pygame.image.load('img/exit2_btn.png')
    #lvlload
    #20x9
    # There are two functionalities because I accidentaly deleted something.
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

    class Player():

        def __init__(self, x, y):
            self.reset(x, y)

        def update(self, game_over):
            dx = 0
            dy = 0
            walk_cooldown = 5
            col_thresh = 20

            if game_over == 0:
                #get keypresses
                key = pygame.key.get_pressed()
                if key[pygame.
                       K_SPACE] and self.jumped == False and self.in_air == False:
                    self.vel_y = -15
                    self.jumped = True
                if key[pygame.K_SPACE] == False:
                    self.jumped = False
                if key[pygame.K_LEFT]:
                    dx -= 5
                    self.counter += 1
                    self.direction = -1
                if key[pygame.K_RIGHT]:
                    dx += 5
                    self.counter += 1
                    self.direction = 1
                if key[pygame.K_LEFT] == False and key[
                        pygame.K_RIGHT] == False:
                    self.counter = 0
                    self.index = 0
                    if self.direction == 1:
                        self.image = self.images_right[self.index]
                    if self.direction == -1:
                        self.image = self.images_left[self.index]

                #handle animation
                if self.counter > walk_cooldown:
                    self.counter = 0
                    self.index += 1
                    if self.index >= len(self.images_right):
                        self.index = 0
                    if self.direction == 1:
                        self.image = self.images_right[self.index]
                    if self.direction == -1:
                        self.image = self.images_left[self.index]

                #add gravity
                self.vel_y += 1
                if self.vel_y > 10:
                    self.vel_y = 10
                dy += self.vel_y

                #check for collision
                self.in_air = True
                for tile in world.tile_list:
                    #check for collision in x direction
                    if tile[1].colliderect(self.rect.x + dx, self.rect.y,
                                           self.width, self.height):
                        dx = 0
                    #check for collision in y direction
                    if tile[1].colliderect(self.rect.x, self.rect.y + dy,
                                           self.width, self.height):
                        #check if below the ground i.e. jumping
                        if self.vel_y < 0:
                            dy = tile[1].bottom - self.rect.top
                            self.vel_y = 0
                        #check if above the ground i.e. falling
                        elif self.vel_y >= 0:
                            dy = tile[1].top - self.rect.bottom
                            self.vel_y = 0
                            self.in_air = False

                #check for collision with enemies
                if pygame.sprite.spritecollide(self, blob_group, False):
                    game_over = -1

                #check for collision with lava
                if pygame.sprite.spritecollide(self, lava_group, False):
                    game_over = -1

                #check for collision with exit
                if pygame.sprite.spritecollide(self, exit_group, False):
                    game_over = 1

                #check for collision with platforms
                for platform in platform_group:
                    #collision in the x direction
                    if platform.rect.colliderect(self.rect.x + dx, self.rect.y,
                                                 self.width, self.height):
                        dx = 0
                    #collision in the y direction
                    if platform.rect.colliderect(self.rect.x, self.rect.y + dy,
                                                 self.width, self.height):
                        #check if below platform
                        if abs((self.rect.top + dy) -
                               platform.rect.bottom) < col_thresh:
                            self.vel_y = 0
                            dy = platform.rect.bottom - self.rect.top
                        #check if above platform
                        elif abs((self.rect.bottom + dy) -
                                 platform.rect.top) < col_thresh:
                            self.rect.bottom = platform.rect.top - 1
                            self.in_air = False
                            dy = 0
                        #move sideways with the platform
                        if platform.move_x != 0:
                            self.rect.x += platform.move_direction

                #update player coordinates
                self.rect.x += dx
                self.rect.y += dy

            elif game_over == -1:
                self.image = self.dead_image
                draw_text('GAME OVER!', font, red, (screen_width // 2) - 200,
                          screen_height // 2)
                if self.rect.y > 200:
                    self.rect.y -= 5

            #draw player onto screen
            screen.blit(self.image, self.rect)

            return game_over

        def reset(self, x, y):
            self.images_right = []
            self.images_left = []
            self.index = 0
            self.counter = 0
            for num in range(1, 5):
                img_right = pygame.image.load(f'img/guy{num}.png')
                img_right = pygame.transform.scale(img_right, (40, 80))
                img_left = pygame.transform.flip(img_right, True, False)
                self.images_right.append(img_right)
                self.images_left.append(img_left)
            self.dead_image = pygame.image.load('img/ghost.png')
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

    class World():

        def __init__(self, data):
            self.tile_list = []

            #load images
            dirt_img = pygame.image.load('img/dirt.png')
            grass_img = pygame.image.load('img/grass.png')

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
            self.image = pygame.image.load('img/blob.png')
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
            img = pygame.image.load('img/platform.png')
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
            img = pygame.image.load('img/lava.png')
            self.image = pygame.transform.scale(img,
                                                (tile_size, tile_size // 2))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

    class Coin(pygame.sprite.Sprite):

        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            img = pygame.image.load('img/coin.png')
            self.image = pygame.transform.scale(
                img, (tile_size // 2, tile_size // 2))
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)

    class Exit(pygame.sprite.Sprite):

        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            img = pygame.image.load('img/exit.png')
            self.image = pygame.transform.scale(
                img, (tile_size, int(tile_size * 1.5)))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

    player = Player(100, screen_height - 130)

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
                draw_text('X ' + str(score) + "   Level: " + str(lvl), font_score, white, tile_size - 10,
                          10)

            blob_group.draw(screen)
            platform_group.draw(screen)
            lava_group.draw(screen)
            coin_group.draw(screen)
            exit_group.draw(screen)

            game_over = player.update(game_over)
            #if player has died
            if game_over == -1:
                if exit_button_smol.draw():
                    exit()
                if restart_button.draw():
                    if lvl == "cst":
                        print("Restarting custom level")
                        start("cst", False, cst_ldata)
                    elif isinstance(lvl, int):
                      print("Restarting with Level " + str(lvl))
                      start(lvl, False, [])

            #if player has completed the lvl
            if game_over == 1:
                #reset game and go to next lvl
                if isinstance(lvl, int):
                  lvl += 1
                  if lvl <= max_lvls:
                      #reset lvl
                      start(lvl, False, [])
                      game_over = 0
                  else:
                      draw_text('YOU WIN!', font, lime,
                                (screen_width // 2) - 140, screen_height // 2)
                      if exit_button_smol.draw():
                        exit()
                      if restart_button.draw():
                          #reset lvl
                          lvl = 1
                          game_over = 0
                          score = 0
                          start(lvl, False, [])
                elif lvl ==  "cst":
                    draw_text('YOU WIN!', font, lime,
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

def leveldesign():
    pygame.font.init()
    import LevelInput
    clock = pygame.time.Clock()
    FPS = 60

    #game window
    SCREEN_WIDTH = 640
    SCREEN_HEIGHT = 640
    LOWER_MARGIN = 100
    SIDE_MARGIN = 320

    screen = pygame.display.set_mode(
        (SCREEN_WIDTH + SIDE_MARGIN, SCREEN_HEIGHT + LOWER_MARGIN))
    pygame.display.set_caption('Level Editor')

    #define game variables
    ROWS = 20
    MAX_COLS = 20
    TILE_SIZE = SCREEN_HEIGHT // ROWS
    TILE_TYPES = 9
    current_tile = 0
    scroll = 0

    #load images
    #pine1_img = pygame.image.load('img2/Background/pine1.png').convert_alpha()
    #pine2_img = pygame.image.load('img2/Background/pine2.png').convert_alpha()
    #mountain_img = pygame.image.load('img2/Background/mountain.png').convert_alpha()
    sky_img = pygame.image.load(
        'img2/Background/background.png').convert_alpha()
    #store tiles in a list
    img_list = []
    for x in range(TILE_TYPES):
        img = pygame.image.load(f'img2/tile/{x}.png').convert_alpha()
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        img_list.append(img)

    save_img = pygame.image.load('img2/save_btn.png').convert_alpha()
    load_img = pygame.image.load('img2/load_btn.png').convert_alpha()

    #define colours
    GREEN = (144, 201, 120)
    WHITE = (255, 255, 255)
    RED = (200, 25, 25)

    #define font
    font = pygame.font.SysFont('Futura', 30)

    #create empty tile list
    world_data = []
    for row in range(ROWS):
        r = [-1] * MAX_COLS
        world_data.append(r)

    #create ground
    for tile in range(0, MAX_COLS):
        world_data[ROWS - 1][tile] = 0

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
    load_button = Button(SCREEN_WIDTH // 2 + 200,
                         SCREEN_HEIGHT + LOWER_MARGIN - 50, load_img, 1)
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
            import copy
            Mod_world_data = copy.deepcopy(world_data)
            for row in range(ROWS):
                for col in range(MAX_COLS):
                    if (Mod_world_data[row][col] == -1):
                        Mod_world_data[row][col] = 0
            return Mod_world_data
        
        if load_button.draw(screen):
            rsp = LevelInput.cli(world_data)
            world_data = rsp
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
if __name__ == "__main__":
    sel_option = input("Enter level number (1-3) or 'cst' to continue: ")
    if sel_option == "cst":
        print("Custom-Level start")
        #level selector here
        custom_leveldata = leveldesign()
        #then
        print("cst-ldata: " + str(custom_leveldata))
        start("cst", False, custom_leveldata)
    elif int(sel_option)<=3:
        sel_option = int(sel_option)
        print("Function call_start() is called.",sel_option)
        start(sel_option, False, [])  # Call the starty function from functions module
    