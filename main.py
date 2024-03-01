import pygame
import sys
from functionality import start  # Import the starty function from functions module

# Function to be called when Start button is clicked
def call_start():
    if start_level<=2:
        start_level= selected_option+1
        print("Function call_start() is called.",start_level)
        start(start_level, False)  # Call the starty function from functions module
    elif start_level == 3:
        print("Custom-Level start")
        print("Feature in development")
        #level selector here

# Initializing the constructor
pygame.init()
#edit
# Screen resolution
res = (720, 500)

# Opens up a window
screen = pygame.display.set_mode(res)

# Defining a font for the button text and dropdown
pygame.font.init()
font = pygame.font.SysFont(None, 36)  # Font for the button text
dropdown_font = pygame.font.SysFont(None, 24)  # Font for the dropdown text

# Rendering the button text
button_text = font.render('Start', True, (255, 255, 255))

# Create a list of image filenames
image_filenames = ['image1.png', 'banana.jfif', 'image3.png']  # Add your image filenames here

# Load images
images = [pygame.image.load(filename).convert() for filename in image_filenames]

# Load background music
pygame.mixer.music.load('audio.mp3')  # Replace 'background_music.mp3' with your music file
pygame.mixer.music.set_volume(0.5)  # Set the volume (0.0 to 1.0)
pygame.mixer.music.play(-1)  # -1 indicates loop indefinitely

clock = pygame.time.Clock()
running = True

image_index = 0
delay = 500  # milliseconds

background_x = 0  # Initialize background_x outside the loop

# Dropdown variables
dropdown_rect = pygame.Rect(res[0] - 160, 10, 150, 30)
dropdown_options = ['Level 1', 'Level 2', 'Level 3', "Custom"]
selected_option = 0

while running:
    clock.tick(30)  # Adjusted the clock speed for smooth rendering

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False

        # Check for button click
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(ev.pos):
                # Call the function when Start button is clicked
                call_start()

            elif dropdown_rect.collidepoint(ev.pos):
                # Increment the selected level when level box is clicked
                selected_option = (selected_option + 1) % len(dropdown_options)

        # ... (other event handling)

    # Update the position of the background
    background_x -= 2  # Adjust the scrolling speed as needed

    # Draw the background image
    screen.blit(images[image_index], (background_x, 0))
    screen.blit(images[image_index], (background_x + res[0], 0))

    # Get the center of the screen
    screen_center_x, screen_center_y = screen.get_rect().center

    # Calculate the position of the button based on the screen center
    button_width, button_height = 140, 40
    button_x = screen_center_x - button_width / 2
    button_y = screen_center_y - button_height / 2

    # Superimposing the text onto our button with the button font
    text_width, text_height = button_text.get_size()
    text_x = button_x + (button_width - text_width) / 2
    text_y = button_y + (button_height - text_height) / 2
    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
    pygame.draw.rect(screen, (100, 100, 100), button_rect)
    screen.blit(button_text, (text_x, text_y))

    # Draw the dropdown next to the button
    dropdown_rect.x = button_x + button_width + 10  # Adjust the distance between the button and dropdown
    dropdown_rect.y = button_y
    pygame.draw.rect(screen, (100, 100, 100), dropdown_rect)
    dropdown_text = dropdown_font.render(dropdown_options[selected_option], True, (255, 255, 255))
    screen.blit(dropdown_text, (dropdown_rect.x + 5, dropdown_rect.y + 5))

    # Check if the background has scrolled completely, reset its position
    if background_x <= -res[0]:
        background_x = 0

        # Move to the next image in the list
        image_index = (image_index + 1) % len(images)

        # Wait for the specified delay
        pygame.time.delay(delay)

    # updates the frames of the game
    pygame.display.flip()

pygame.quit()
sys.exit()