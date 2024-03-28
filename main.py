import os, sys, time, multiplayer, pygame, pickle
from functionality import start, leveldesign  # Import the starty function from functions module_leve = selected_option+1l
try:
    from signIn import *
    import webclient
    webclient.update_variable("http://gregglesthegreat.pythonanywhere.com/",
                              "ConnectTest", "True")
    Online = True
except Exception as e:
    print(e)
    Online = False

global onile
try:
    from signIn import *
    import os, sys, webclient, time
    onile = "o"
except:
    print("ofline")
    onile = "i"

# with open('rlog.pkl', 'wb') as handle:
#     pickle.dump([1, "Greggles"], handle, protocol=pickle.HIGHEST_PROTOCOL)
#     handle.close()
with open('rlog.pkl', 'rb') as handle:
    a = pickle.load(handle)
    handle.close()
pygame.display.set_caption("Platformer")
# Function to be called when Start button is clicked
#server URL
SERVER_URL = "http://gregglesthegreat.pythonanywhere.com/"


#Gregory"s bit
def call_start():
    global screen
    if selected_option == 4:

        multiplayer.Main()
    else:
        if selected_option <= 2:
            start_level = selected_option + 1
            print("Function call_start() is called.", start_level)
            start(start_level, False,
                  [])  # Call the starty function from functions module
            screen = pygame.display.set_mode(res)
        elif selected_option == 3:
            print("Custom-Level start")
            #level selector here
            custom_leveldata = leveldesign()
            #then
            print("cst-ldata: " + str(custom_leveldata))
            start("cst", False, custom_leveldata)
            screen = pygame.display.set_mode(res)


#end gregory"s bit

# Initializing the constructor
pygame.init()
#edit
# Screen resolution
res = (750, 500)

# Opens up a window
screen = pygame.display.set_mode(res)

# Defining a font for the button text and dropdown
pygame.font.init()
font = pygame.font.SysFont(None, 36)  # Font for the button text
dropdown_font = pygame.font.SysFont(None, 24)  # Font for the dropdown text

# Rendering the button text
button_text = font.render("Start", True, (255, 255, 255))
exit_text = font.render("Exit", True, (255, 255, 255))
# Create a list of image filenames
image_filenames = ["img/image1.png", "img/image2.png",
                   "img/image3.png"]  # Image filenames here

# Load images
images = [
    pygame.image.load(filename).convert() for filename in image_filenames
]


# Function to draw text on button
def draw_text(text, font, color, surface, x, y):
    try:
        textobj = font.render(text, True, color)
        textrect = textobj.get_rect(center=(x, y))
        textrect.center = (x, y)
        surface.blit(textobj, textrect)
        surface.blit(textobj, textrect)
    except Exception as e:
        print("Error rendering text:", e)


# Function to perform action when button is clicked
WIDTH, HEIGHT = 800, 600
# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Define button properties
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50
BUTTON_COLOR = GRAY
BUTTON_TEXT_COLOR = BLACK
BUTTON_TEXT_SIZE = 30


# Function to create a button
def create_button(x,
                  y,
                  width,
                  height,
                  color,
                  text,
                  text_color,
                  action=None,
                  acpar=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        pygame.draw.rect(screen, BLACK, (x, y, width, height))
        if click[0] == 1 and action is not None:
            if acpar is not None:
                action(acpar)
            else:
                action()
    else:
        pygame.draw.rect(screen, color, (x, y, width, height))

    font = pygame.font.SysFont(None, BUTTON_TEXT_SIZE)
    draw_text(text, font, text_color, screen, x + width / 2, y + height / 2)


# Create a button

# Load background music
pygame.mixer.stop()
pygame.mixer.music.stop()
pygame.mixer.music.load("music/audio.mp3")
pygame.mixer.stop()  # Replace "background_music.mp3" with your music file
pygame.mixer.music.set_volume(0.5)  # Set the volume (0.0 to 1.0)
pygame.mixer.music.play(-1)  # -1 indicates loop indefinitely

clock = pygame.time.Clock()
running = True

image_index = 0
delay = 500  # milliseconds

background_x = 0  # Initialize background_x outside the loop


#sign-oute
def signoutt():
    # Save variable to a file
    with open('rlog.pkl', 'wb') as f:
        pickle.dump([0, ""], f)


# Dropdown variables
dropdown_rect = pygame.Rect(res[0] - 160, 10, 150, 30)
dropdown_options = ["Level 1", "Level 2", "Level 3", "Custom", "Multiplayer"]
selected_option = 0
#thihh
my_dictp = webclient.get_variable(SERVER_URL, "d_pgp_LOGIN")
while running:
    clock.tick(30)  # Adjusted the clock speed for smooth rendering

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            quit()

        # Check for button click
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(ev.pos):
                # Call the function when Start button is clicked
                call_start()
            elif dropdown_rect.collidepoint(ev.pos):
                # Increment the selected level when level box is clicked
                selected_option = (selected_option + 1) % len(dropdown_options)
            elif exit_rect.collidepoint(ev.pos):
                # Exit game when exit button is clickedq
                running = False
                exit()

    # Update the position of the background
    background_x -= 2  # Adjust the scrolling speed as needed

    # Draw the background image
    screen.blit(images[image_index], (background_x, 0))
    screen.blit(images[image_index], (background_x + res[0], 0))

    # Get the center of the screen
    screen_center_x, screen_center_y = screen.get_rect().center

    exit_width, exit_height = 140, 40
    exit_x = screen_center_x - exit_width / 2
    exit_y = screen_center_y + 190 - exit_height / 2
    exit_text_width, exit_text_height = exit_text.get_size()
    exit_text_x = exit_x + (exit_width - exit_text_width) / 2
    exit_text_y = exit_y + (exit_height - exit_text_height) / 2
    exit_rect = pygame.Rect(exit_x, exit_y, exit_width, exit_height)
    pygame.draw.rect(screen, (100, 100, 100), exit_rect)
    screen.blit(exit_text, (exit_text_x, exit_text_y))
    #Game Title:
    # Define a font for the main menu text
    main_menu_font = pygame.font.SysFont(
        None, 72)  # Font for the main menu text with size 72

    # Render the main menu text
    main_menu_text = main_menu_font.render(
        "Main Menu", True, (255, 255, 255))  # Render the main menu text

    # Calculate the position of the button based on the screen center
    button_width, button_height = 140, 40
    button_x = screen_center_x - button_width / 2
    button_y = screen_center_y + 20 - button_height / 2

    #Game Title:
    # Define a font for the main menu text
    main_menu_font = pygame.font.SysFont(
        None, 72)  # Font for the main menu text with size 72

    # Render the main menu text
    main_menu_text = main_menu_font.render(
        "Main Menu", True, (255, 255, 255))  # Render the main menu text

    # Calculate the position of the text based on the screen center
    screen_center_x, screen_center_y = screen.get_rect().center
    text_width, text_height = main_menu_text.get_size()
    text_x = screen_center_x - text_width / 2
    text_y = screen_center_y - 100 - text_height / 2  # Adjust the distance from the center

    # Draw the text onto the screen
    screen.blit(main_menu_text, (text_x, text_y))

    # Superimposing the text onto our button with the button font
    text_width, text_height = button_text.get_size()
    text_x = button_x + (button_width - text_width) / 2
    text_y = button_y + (button_height - text_height) / 2
    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
    pygame.draw.rect(screen, (100, 100, 100), button_rect)
    screen.blit(button_text, (text_x, text_y))

    #Mainmenu is referenced of the button.
    # Draw the dropdown below to the button
    dropdown_rect.x = button_x
    dropdown_rect.y = button_y - button_height + 130  # Adjust the distance between the button and dropdown
    pygame.draw.rect(screen, (100, 100, 100), dropdown_rect)
    dropdown_text = dropdown_font.render(dropdown_options[selected_option],
                                         True, (255, 255, 255))
    screen.blit(dropdown_text, (dropdown_rect.x + 5, dropdown_rect.y + 5))

    # Check if the background has scrolled completely, reset its position
    if background_x <= -res[0]:
        background_x = 0

        # Move to the next image in the list
        #image_index = (image_index + 1) % len(images)

        # Wait for the specified delay
        #pygame.time.delay(delay)
    # Load variable from the file
    with open('rlog.pkl', 'rb') as f:
        loaded_variablet = pickle.load(f)
    ytt = str(loaded_variablet[0])
    un = str(loaded_variablet[1])
    if Online == True:
        from signIn import *
        import webclient

        def dropdown2():
            from profileish import prof
            # my_dictp = webclient.get_variable(SERVER_URL, "d_pgp_LOGIN")
            try:
                my_coinds = my_dictp[un][1]
            except KeyError:
                my_coinds = "Error"
            create_button(540, 55, BUTTON_WIDTH, BUTTON_HEIGHT,
                          (100, 100, 100), "Profile", WHITE, prof)
            ayouu = ("Coinds:" + str(my_coinds))
            create_button(540, 102, BUTTON_WIDTH, BUTTON_HEIGHT,
                          (100, 100, 100), ayouu, WHITE)
            create_button(540, 149, BUTTON_WIDTH, BUTTON_HEIGHT,
                          (100, 100, 100), "Log-out", WHITE, signoutt)

        # Load variable from the file
        with open('rlog.pkl', 'rb') as f:
            loaded_variablet = pickle.load(f)
        ytt = str(loaded_variablet[0])
        un = str(loaded_variablet[1])
        if ytt == "0":
            create_button(540, 10, BUTTON_WIDTH, BUTTON_HEIGHT,
                          (100, 100, 100), "Sign-in", WHITE, signinuytio)
        else:
            create_button(540, 10, BUTTON_WIDTH, BUTTON_HEIGHT,
                          (100, 100, 100), un, WHITE, dropdown2)
        # Get the mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if ((mouse_x >= 550 and mouse_x <= 800) and
            (mouse_y >= 10 and mouse_y <= 200)) and (not (ytt == "0")):
            dropdown2()

    # updates the frames of the game
    pygame.display.flip()

pygame.quit()
sys.exit()
#hi
