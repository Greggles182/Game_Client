def hiytu():
  import pickle
  # Save variable to a file
  with open('rlog.pkl', 'wb') as f:
    pickle.dump([0], f)
def signinuytio():
  import pygame
  import sys
  import subprocess
  import os, sys, webclient, time
  import pickle


  #server URL
  SERVER_URL = "http://gregglesthegreat.pythonanywhere.com/"


  
  # Initialize Pygame
  pygame.init()

  # Creating a dictionary
  my_dict = webclient.get_variable(SERVER_URL,"d_pgp_LOGIN")

  # Set up display
  WIDTH, HEIGHT = 750, 500
  screen = pygame.display.set_mode((WIDTH, HEIGHT))
  pygame.display.set_caption("Signup Menu")

  # Load background image
  background_img = pygame.image.load("img2/Background/background.png").convert()

  # Colors
  WHITE = (255, 255, 255)
  BLACK = (0, 0, 0)
  GRAY = (200, 200, 200)
  DARK_GRAY = (100, 100, 100)
  BLUE = (106, 159, 181)
  LIGHT_BLUE = (144, 194, 215)

  # Fonts
  font = pygame.font.Font(None, 36)

  # Input box class
  class InputBox:
      def __init__(self, x, y, width, height, text='', password=False):
          self.rect = pygame.Rect(x, y, width, height)
          self.text = text
          self.font_color = BLACK
          self.active = False
          self.password = password

      def handle_event(self, event):
          if event.type == pygame.MOUSEBUTTONDOWN:
              if self.rect.collidepoint(event.pos):
                  self.active = True
              else:
                  self.active = False
          if event.type == pygame.KEYDOWN:
              if self.active:
                  if event.key == pygame.K_RETURN:
                      # Submit the text
                      self.active = False
                  elif event.key == pygame.K_BACKSPACE:
                      self.text = self.text[:-1]
                  else:
                      self.text += event.unicode

      def draw(self, screen):
          pygame.draw.rect(screen, WHITE, self.rect)
          if self.password:
              masked_text = '*' * len(self.text)
              text_surface = font.render(masked_text, True, self.font_color)
          else:
              text_surface = font.render(self.text, True, self.font_color)
          screen.blit(text_surface, (self.rect.x + 10, self.rect.y + 10))

  # Clickable text class
  class ClickableText:
      def __init__(self, x, y, text, color, function):
          self.rect = pygame.Rect(x, y, len(text)*20, 30)
          self.text = text
          self.font_color = color
          self.function = function

      def handle_event(self, event):
          if event.type == pygame.MOUSEBUTTONDOWN:
              if self.rect.collidepoint(event.pos):
                  self.function()

      def draw(self, screen):
          text_surface = font.render(self.text, True, self.font_color)
          screen.blit(text_surface, (self.rect.x, self.rect.y))

  # Create input boxes
  username_box = InputBox(250, 200, 300, 50, "[Username]")
  password_box = InputBox(250, 300, 300, 50, "EasterEgg", password=True)

  # Function for sign-in action
  def si2gninuytio():
      print("Sign-in function triggered")

  # Create clickable text
  sign_in_text = ClickableText(175, 420, "Already have an account? Sign-in!", BLUE, si2gninuytio)

  # Main loop
  running = True
  while running:
      screen.fill(WHITE)

      # Draw background image
      screen.blit(background_img, (0, 0))

      #Check for right username and password
      username = username_box.text
      password = password_box.text
      # print("Username:", username)
      # print("Password:", "***")
      if username in my_dict:
    # Retrieve the password associated with the username
        stored_password = my_dict[username][0]
        if stored_password == password:
          print("worked")
          # Save variable to a file
          with open('rlog.pkl', 'wb') as f:
            pickle.dump([1,username], f)
          # Run another Python file
          subprocess.run(["python", "main.py"])
        


      # Event handling
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              running = False
          username_box.handle_event(event)
          password_box.handle_event(event)
          sign_in_text.handle_event(event)

      # Draw input boxes
      username_box.draw(screen)
      password_box.draw(screen)

      # Add labels
      title_label = font.render("Signup Form", True, BLACK)
      username_label = font.render("Username:", True, BLACK)
      password_label = font.render("Password:", True, BLACK)
      screen.blit(title_label, (330, 100))
      screen.blit(username_label, (100, 210))
      screen.blit(password_label, (100, 310))

      # Draw clickable text
      sign_in_text.draw(screen)

      pygame.display.flip()

  pygame.quit()
  sys.exit()