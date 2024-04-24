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
        destination_path = "./Game/"
        Aftercpy = False
        if os.path.isdir(destination_path):
            Aftercpy = True
            import shutil
            source_dir = "./Game/levels"
            destination_dir = "./levels-backup"
            shutil.rmtree(destination_dir, ignore_errors=True)
            shutil.copytree(source_dir, destination_dir)
            src_path = "./Game/rlog.pkl"
            dst_path = "./rlog.pkl"
            shutil.copy(src_path, dst_path)
            print('Created backup of local levels and signin status')
            shutil.rmtree(destination_path, ignore_errors=True)
            input("Please ensure the folder 'Game' no longer exists, THEN press Enter")
        clone_command = "git clone https://github.com/Greggles182/Game_Client.git"
        clone_with_path = clone_command + " " + destination_path
        os.system(clone_with_path)
        os.chdir(destination_path)
        try:
            import pygame, requests, passlib
        except Exception:
            print("There was an issue checking whether necesary are installed")
            print("Installing all:")
            os.system("python -m pip install --upgrade pygame")
            os.system("python -m pip install --upgrade requests")
            os.system("python -m pip install --upgrade passlib")
        from importlib.metadata import version
        v1 = version('pygame')
        v2 = version('requests')
        v4 = version('passlib')
        if v1 >= "2.5.2":
            print("Pygame up to date")
        else:
            print("Updating pygame")
            os.system("python -m pip install --upgrade pygame")
        if v2 >= "2.31.1":
            print("Requests up to date")
        else:
            print("Updating requests")
            os.system("python -m pip install --upgrade requests")
        if v2 >= "1.7.4":
            print("Hashing tool up to date")
        else:
            print("Updating passlib")
            os.system("python -m pip install --upgrade passlib")
        if Aftercpy:
            print("You will need to replace the levels folder in the Game directory with levels-backup in the current directory, and replace the rlog.pkl file.")
        print("Install complete. Please run main.py in the Game directory to launch")
    if inst == "2" or inst == "3":
        try:
            from importlib.metadata import version
            import flask
            v1 = version('flask')
            if v1 >= "3.0.3":
                print("Flask up to date")
            else:
                print("Updating flask")
                os.system("python -m pip install --upgrade flask")
        except Exception:
            print("There was an issue checking whether flask is installed")
            print("Installing flask:")
            os.system("python -m pip install --upgrade flask")
        destination_path = "Server/"
        if os.path.isdir(destination_path):
            shutil.rmtree(destination_path, ignore_errors=True)
            input("Please ensure the 'Server' folder no longer exists, THEN press Enter")
        clone_command = "git clone https://github.com/Greggles182/Game_Server.git"
        clone_with_path = clone_command + " " + destination_path
        os.system(clone_with_path)
        os.chdir(destination_path)
        print("Install Success!")
    else:
        raise ValueError
except ModuleNotFoundError:
    print("There was an Module error running the program.")
except Exception:
    print("There was an issue running the program.")