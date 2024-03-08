import pygame
import sys  # Import the starty function from functions module_leve = selected_option+1l
def yehaa():
  pygame.display.set_caption('Platformer')
  # Function to be called when Start button is clicked
  def startyyyy():
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
    button_text = font.render('Start', True, (255, 255, 255))
    exit_text = font.render('Exit', True, (255, 255, 255))
    # Create a list of image filenames
    image_filenames = ['img/image1.png', 'img/image2.png', 'img/image3.png']  # Image filenames here

    # Load images
    images = [pygame.image.load(filename).convert() for filename in image_filenames]

    # Load background music
    pygame.mixer.music.load('music/audio.mp3')  # Replace 'background_music.mp3' with your music file
    pygame.mixer.music.set_volume(0.5)  # Set the volume (0.0 to 1.0)
    pygame.mixer.music.play(-1)  # -1 indicates loop indefinitely

    clock = pygame.time.Clock()
    running = True

    image_index = 0
    delay = 500  # milliseconds

    background_x = 0  # Initialize 
  startyyyy()
#heeeeeeeeeeeelllllllloooooooo    wooorrrlllllddddd!!!!!!!!!!!!!!!!!!1