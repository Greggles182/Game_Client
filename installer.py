try:
    import os, sys
    v3 = sys.version
    if v3 >= "1.12.2":
        print("Python up to date")
    else:
        print("You must update python to run this code.")
        print("https://www.python.org/downloads/")
    print("What should be installed?")
    inst = input("Type 1 for game, 2 for server for hosting games, and 3 for both: ")
    if inst == "1" or inst == "3":
        destination_path = "Game/"
        clone_command = "git clone https://github.com/Greggles182/Assesment-Y7.git"
        clone_with_path = clone_command + " " + destination_path
        os.system(clone_with_path)
        os.chdir(destination_path)
        try:
            import pygame, requests
        except Exception as e:
            print("There was an issue checking whether pygame and requests are installed")
            print("Error: " + e)
            print("Installing both:")
            os.system("python -m pip install --upgrade pygame")
            os.system("python -m pip install --upgrade requests")
        from importlib.metadata import version
        v1 = version('pygame')
        v2 = version('requests')
        if v1 >= "2.5.2":
            print("Pygame up to date")
        else:
            print("Updating pygame")
            os.system("python -m pip install --upgrade pygame")
        if v2 >= "2.31.2":
            print("Requests up to date")
        else:
            print("Updating requests")
            os.system("python -m pip install --upgrade requests")
    if inst == "2" or inst == "3":
        destination_path = "Game/"
        clone_command = "git clone https://github.com/Greggles182/Assesment-Y7.git"
        clone_with_path = clone_command + " " + destination_path
        os.system(clone_with_path)
        os.chdir(destination_path)
except Exception as e:
    print("There was an issue running the program.")
    print(e)