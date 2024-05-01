#DOWNLOAD THIS
import os
import pickle
import webclient
import time
from tk1 import TKinput as input
import tkinter.messagebox as box

def cli(Ldata):
    Opt = input("""Welcome to the LevelEditor CLI!
          Please type a number below to trigger the command
          1: Export the current level to file
          2: Load a level file
          3: Paste in a level seed (must be valid)
          4: Save the current level to your user account
          5: Load a level from your user account
          6: Exit the program.
            Type 1-7 then press Enter to proceed: """)
    
    Opt = int(Opt)
    if Opt > 7 or Opt < 1:
        box.showerror("Error", "Invalid option")
        exit()
    elif Opt == 1:
        fname = input("What filename do you want to export to? ")
        PATH = f"./levels/{fname}.txt"
        if os.path.isfile(PATH):  # and os.access(PATH, os.R_OK):
            #cont = input("File exists - do you want to continue? Y/N: ")
            cont = box.askyesno("File exists", "Continue")
            if cont == 1:
                with open(PATH, "w") as FILE:
                    FILE.write(str(Ldata))
                    FILE.close()
                input("Success. Press ok to close the CLI")
                exit()
            else:
                pass
        else:
            with open(PATH, "w") as FILE:
                FILE.write(str(Ldata))

                FILE.close()
            input("Success. Press ok to close the CLI")
            exit()
    elif Opt == 2:
        from os import listdir
        from os.path import isfile, join
        PATH = "./levels/"
        LISTFILES = [f for f in listdir(PATH) if isfile(join(PATH, f))]
        a = 1
        text = ""
        for i in LISTFILES:
            text = text + (f"{str(a)}. {i}\n")
            a = a + 1
        nfname = input(
            f"{text}Please enter the number of the file you want to load: ")
        if nfname.isdigit():
            nfname = int(nfname)
            if nfname <= 0 or nfname > len(LISTFILES):
                box.showerror("Error","That was an invalid option.")
                exit()
            nfname = LISTFILES[nfname - 1]
            FPATH = PATH + nfname
            if os.path.isfile(FPATH) and os.access(FPATH, os.R_OK):
                with open(FPATH, "r") as FDATA:
                    DATA = FDATA.read()
                    DATA = eval(DATA)
                    return DATA
            else:
                box.showerror("Error:","Either the file is missing or not readable")
                exit()
        else:
            box.showerror("Error:","That was an invalid option.")
            exit()
    elif Opt == 3:
        LDLIST = input("Enter a valid level data list: ")
        LDLIST = eval(LDLIST)
        return LDLIST
    elif Opt == 4:
        SERVER_URL = "http://gregglesthegreat.pythonanywhere.com/"
        with open('rlog.pkl', 'rb') as handle:
            a = pickle.load(handle)
            handle.close()
        if type(a) != list:
            raise ValueError
        if a[0] == 0:
            box.showwarning("Error:","You must sign in to use this functionality!")
        elif a[0] == 1:
            box.showinfo("Info","Signed In As: ", a[1])
        saven = input("What name should this be saved as? ")
        users = webclient.get_variable(SERVER_URL, "d_pgp_LOGIN")
        userinfo = users.get(a[1])
        OSLevels = userinfo[2]
        if saven in OSLevels:
            confirm = box.askyesno("Error:","This level already exists!\nDo you want to continue? (y/n): ")
            if confirm == 1:
                pass
            else:
                exit()
        users = webclient.get_variable(SERVER_URL, "d_pgp_LOGIN")
        userinfo = users.get(a[1])
        OSLevels = userinfo[2]
        OSLevels[saven] = Ldata
        userinfo[2] = OSLevels
        users[a[1]] = userinfo
        webclient.update_variable(SERVER_URL, "d_pgp_LOGIN", users)
        return Ldata
    elif Opt == 5:
        SERVER_URL = "http://gregglesthegreat.pythonanywhere.com/"
        with open('rlog.pkl', 'rb') as handle:
            a = pickle.load(handle)
            handle.close()
        if type(a) != list:
            raise ValueError
        if a[0] == 0:
            box.showwarning("Error:","You must sign in to use this functionality!")
        elif a[0] == 1:
            box.showinfo("Info","Signed In As: ", a[1])
        users = webclient.get_variable(SERVER_URL, "d_pgp_LOGIN")
        userinfo = users.get(a[1])
        OSLevels = userinfo[2]
        i = 1
        levels = []
        text = ""
        for key in OSLevels:
            text = text + (f"{i}. {key}\n")
            i += 1
            levels.append(key)
        def getIndex(levels, text):
            load = input(f"{text}Type the number of the level you want to play: ")
            try:
                load = int(load)
                if load > len(levels) or load < 1:
                    getIndex(levels, text)
                return load
            except ValueError:
                box.showerror("Error:","You have entered an invalid option.")
                getIndex(levels, text)
        loadItm = getIndex(levels, text)
        keyed = levels[int(loadItm) - 1]
        finalGet = OSLevels.get(keyed)
        return finalGet
    elif Opt == 6:
        exit()