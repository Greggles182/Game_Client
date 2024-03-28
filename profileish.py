
def prof():
  import os, sys, time, multiplayer, pickle
  import pygame
  import pickle
  import webclient
  from functionality import start, leveldesign  # Import the starty function from functions module_leve = selected_option+1l
  global onile

  # with open('rlog.pkl', 'wb') as handle:
  #     pickle.dump([1, "Greggles", True], handle, protocol=pickle.HIGHEST_PROTOCOL)
  #     handle.close()
  with open('rlog.pkl', 'rb') as handle:
      a = pickle.load(handle)
      handle.close()
  pygame.display.set_caption("Platformer")
  # Function to be called when Start button is clicked
  # server URL
  SERVER_URL = "http://gregglesthegreat.pythonanywhere.com/"

  # Initializing the constructor
  pygame.init()
  #edit
  # Screen resolution
  res = (750, 500)

  # Opens up a window
  screen = pygame.display.set_mode(res)

  # Load background image
  background = pygame.image.load("img2/Background/background.png").convert()

  # Defining a font for the button text and dropdown
  pygame.font.init()
  font = pygame.font.SysFont(None, 36)  # Font for the button text
  dropdown_font = pygame.font.SysFont(None, 24)  # Font for the dropdown text

  # Rendering the button text
  # Create a list of image filenames
  image_filenames = ["img/image1.png", "img/image2.png",
                    "img/image3.png"]  # Image filenames here

  # Load images
  images = [
      "img2/Background/background.png"
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
          pickle.dump([0, "", True], f)
  #thihh
  my_dictp = webclient.get_variable(SERVER_URL, "d_pgp_LOGIN")
  while running:
      clock.tick(30)  # Adjusted the clock speed for smooth rendering

      for ev in pygame.event.get():
          if ev.type == pygame.QUIT:
              quit()

      # Update the position of the background
      background_x -= 2  # Adjust the scrolling speed as needed

      # Draw the background image
      screen.blit(background, (background_x, 0))

      # Get the center of the screen
      screen_center_x, screen_center_y = screen.get_rect().center

      # Calculate the position of the button based on the screen center
      button_width, button_height = 140, 40
      button_x = screen_center_x - button_width / 2
      button_y = screen_center_y + 20 - button_height / 2

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

      

      # updates the frames of the game
      pygame.display.flip()

  pygame.quit()
  sys.exit()
  #hi