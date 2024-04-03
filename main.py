import subprocess, pygame, os, game, sys, threading, webclient, pickle, random, time
def Chk():
    import subprocess, pygame, os, game, sys, threading, webclient, pickle, random, time
    global Online, a
    # Run git status
    try:
        process = subprocess.Popen(['git', 'fetch'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if process.returncode == 0:
            print('Git status output:')
            print(stdout.decode())
        else:
            print('Error:')
            print(stderr.decode())
        process = subprocess.Popen(['git', 'pull'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if process.returncode == 0:
            print('Git fetch output:')
            print(stdout.decode())
        else:
            print('Error:')
            print(stderr.decode())
    except Exception as e:
        print(e)
    #Hello World!
    try:
        import webclient
        webclient.update_variable("http://gregglesthegreat.pythonanywhere.com/",
                                "ConnectTest", "True")
        webclient.get_variable("http://gregglesthegreat.pythonanywhere.com/","ConnectTest")
        Online = True
    except Exception as e:
        print(e)
        Online = False
    # with open('rlog.pkl', 'wb') as handle:
    #     pickle.dump([1, "Greggles", True], handle, protocol=pickle.HIGHEST_PROTOCOL)
    #     handle.close()
    with open('rlog.pkl', 'rb') as handle:
        a = pickle.load(handle)
        handle.close()
        if Online == False:
            print("You are offline")
            a[2] = False
        elif Online == True:
            print("You are online")
            a[2] = True
    with open("rlog.pkl", "wb") as f:
        pickle.dump(a,f)
        f.close()
pygame.init()

# Screen and font
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Loading Bar!")

FONT = pygame.font.SysFont("Roboto", 100)

# Clock
CLOCK = pygame.time.Clock()

# Work
WORK = 50000000

# Loading BG
LOADING_BG = pygame.image.load("img/Loading Bar Background.png")
LOADING_BG_RECT = LOADING_BG.get_rect(center=(640, 360))
# Loading BG
LOADING_TEXT = pygame.image.load("img/Platformer.png")
LOADING_TEXT_RECT = LOADING_TEXT.get_rect(center=(640, 200))
# Loading Bar and variables
loading_bar = pygame.image.load("img/Loading Bar.png")
loading_bar_rect = loading_bar.get_rect(midleft=(280, 360))
loading_finished = False
loading_progress = 0
loading_bar_width = 8

def doWork():
    # Do some math WORK amount times
    global loading_finished, loading_progress

    for i in range(WORK):
        math_equation = 523687 / 789456 * 89456
        #time.sleep(0.000001)
        loading_progress = i 

    loading_finished = True

# Finished text
finished = FONT.render("Done!", True, "white")
finished_rect = finished.get_rect(center=(640, 360))

# Thread
threading.Thread(target=doWork).start()
# Game loop
a = True
CHkThr = threading.Thread(target=Chk)
CHkThr.daemon = True
CHkThr.start()
while a:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill("#0d0e2e")
    if loading_finished:
        a = False
    # if not loading_finished:
    # 	loading_bar_width = loading_progress / WORK * 720

    # 	loading_bar = pygame.transform.scale(loading_bar, (int(loading_bar_width), 150))
    # 	loading_bar_rect = loading_bar.get_rect(midleft=(280, 360))

    # 	screen.blit(LOADING_BG, LOADING_BG_RECT)
    # 	screen.blit(loading_bar, loading_bar_rect)
    # else:
    # 	screen.blit(finished, finished_rect)
    loading_bar_width = loading_progress / WORK * 720

    loading_bar = pygame.transform.scale(loading_bar, (int(loading_bar_width), 150))
    loading_bar_rect = loading_bar.get_rect(midleft=(280, 360))

    screen.blit(LOADING_BG, LOADING_BG_RECT)
    screen.blit(loading_bar, loading_bar_rect)
    screen.blit(LOADING_TEXT, LOADING_TEXT_RECT)

    pygame.display.update()
    CLOCK.tick(60)
CHkThr.join()
game.start_game(Online, a)
