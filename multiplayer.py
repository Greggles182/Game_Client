import pygame
import sys
from local_functionality import start
from functionality import leveldesign # Import the starty function from functions module_leve = selected_option+1l
import subprocess
def Main():
  def Enter(s_op):
    if s_op==3:
      subprocess.run(["python", "main.py"])
    elif s_op==2:
      from Online_fuctionality import Begin
      Begin()
    elif s_op==1:
      custom_leveldata = leveldesign()
      #then
      print("cst-ldata: " + str(custom_leveldata))
      start("cst", False, custom_leveldata)
    elif s_op == 0:
      start(1, False, [])
      pygame.display.set_caption("Platformer")
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
  image_filenames = ["img/image1.png", "img/image2.png", "img/image3.png"]  # Image filenames here

  # Load images
  images = [pygame.image.load(filename).convert() for filename in image_filenames]

  # Load background music
  pygame.mixer.music.load("music/audio.mp3")  # Replace "background_music.mp3" with your music file
  pygame.mixer.music.set_volume(0.5)  # Set the volume (0.0 to 1.0)
  pygame.mixer.music.play(-1)  # -1 indicates loop indefinitely

  clock = pygame.time.Clock()
  running = True

  image_index = 0
  delay = 500  # milliseconds

  background_x = 0  # Initialize background_x outside the loop

  # Dropdown variables
  dropdown_rect = pygame.Rect(res[0] - 160, 10, 150, 30)
  dropdown_options = ["Level 1-3 Local 2p","Custom Local 2p","Online","Back"]
  selected_option = 0

  while running:
      clock.tick(30)  # Adjusted the clock speed for smooth rendering

      for ev in pygame.event.get():
          if ev.type == pygame.QUIT:
              quit()

          # Check for button click
          elif ev.type == pygame.MOUSEBUTTONDOWN:
              if button_rect.collidepoint(ev.pos):
                  # Call the function when Start button is clicked
                  Enter(selected_option)
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
      #commented out duplicated code!
      # #Game Title:
      # # Define a font for the main menu text
      # main_menu_font = pygame.font.SysFont(None, 72)  # Font for the main menu text with size 72

      # # Render the main menu text
      # main_menu_text = main_menu_font.render("Multiplayer Menu", True, (255, 255, 255))  # Render the main menu text

      # Calculate the position of the button based on the screen center
      button_width, button_height = 140, 40
      button_x = screen_center_x - button_width / 2
      button_y = screen_center_y + 20 - button_height / 2

      #Game Title:
      # Define a font for the main menu text
      main_menu_font = pygame.font.SysFont(None, 72)  # Font for the main menu text with size 72

      # Render the main menu text
      main_menu_text = main_menu_font.render("Multiplayer Menu", True, (255, 255, 255))  # Render the main menu text

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
      dropdown_rect.y = button_y - button_height + 130 # Adjust the distance between the button and dropdown
      pygame.draw.rect(screen, (100, 100, 100), dropdown_rect)
      dropdown_text = dropdown_font.render(dropdown_options[selected_option], True, (255, 255, 255))
      screen.blit(dropdown_text, (dropdown_rect.x + 5, dropdown_rect.y + 5))


      # Check if the background has scrolled completely, reset its position
      if background_x <= -res[0]:
          background_x = 0

          # Move to the next image in the list
          #image_index = (image_index + 1) % len(images)

          # Wait for the specified delay
          #pygame.time.delay(delay)

      # updates the frames of the game
      pygame.display.flip()

  pygame.quit()
  sys.exit()
  #hi
#heeeeeeeeeeeelllllllloooooooo    wooorrrlllllddddd!!!!!!!!!!!!!!!!!!1
if __name__ == "__main__":
   Main()