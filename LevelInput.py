#DOWNLOAD THIS
import os
import pickle
import webclient
def cli(Ldata):
    print("""Welcome to the LevelEditor CLI!
          Please type a number below to trigger the command
          1: Export the current level to file
          2: Load a level file
          3: Print seed for current level
          4: Paste in a level seed (must be valid)
          5: Write the level to the server
          6: Load a level from the server
          7: Exit the program.
          """)
    Opt = input("Type 1-7 then press Enter to proceed: ")
    Opt = int(Opt)
    if Opt > 7 or  Opt < 1:
        print("Invalid Option")
        exit()
    elif  Opt == 1:
        fname = input("What filename do you want to export to? ")
        PATH = f"./levels/{fname}.txt"
        if os.path.isfile(PATH): # and os.access(PATH, os.R_OK):
            cont = input("File exists - do you want to continue? Y/N: ")
            if cont.lower() == "y":
                print("FileCheck - OK")
                print(f"Writing to {fname}.txt...")
                with open(PATH, "w") as FILE:
                    FILE.write(str(Ldata))
                    print(str(Ldata))
                    FILE.close()
                input("Success. Press enter to close the CLI")
                exit()
            else:
                pass
        else:
            print("FileCheck - OK")
            print(f"Writing to {fname}.txt...")
            with open(PATH, "w") as FILE:
                FILE.write(str(Ldata))
                print(str(Ldata))
                FILE.close()
            input("Success. Press enter to close the CLI")
            exit()
    elif  Opt == 2:
        from os import listdir
        from os.path import isfile, join
        PATH = "./levels/"
        LISTFILES = [f for f in listdir(PATH) if isfile(join(PATH, f))]
        #print(LISTFILES)
        a = 1
        for i in LISTFILES:
            print(f"{str(a)}. {i}")
            a = a+1
        nfname = input("Please enter the number of the file you want to load: ")
        if nfname.isdigit():
            nfname = int(nfname)
            if nfname <= 0 or nfname > len(LISTFILES):
                print("That was an invalid option.")
                raise ValueError
            nfname = LISTFILES[nfname-1]
            FPATH = PATH + nfname
            if os.path.isfile(FPATH) and os.access(FPATH, os.R_OK):
                print("File exists and is readable")
                with open (FPATH,"r") as FDATA:
                    DATA = FDATA.read()
                    DATA = eval(DATA)
                    print(DATA)
                    print(type(DATA))
                    return DATA
            else:
                print("Either the file is missing or not readable")
                exit()
        else:
            print("That was an invalid option.")
            raise ValueError
    elif Opt == 3:
        print(Ldata)
        return Ldata
    elif Opt == 4:
        LDLIST = input("Enter a valid level data list: ")
        LDLIST = eval(LDLIST)
        return LDLIST
    elif Opt == 5:
        SERVER_URL = "http://gregglesthegreat.pythonanywhere.com/"
        with open('rlog.pkl', 'rb') as handle:
            a = pickle.load(handle)
            handle.close()
        #print(a)
        if type(a) != list:
            raise ValueError
        if a[0] == 0:
            print("You must sign in to use this functionality!")
        elif a[0] == 1:
            print("Signed In As: ", a[1])
        saven = input("What name should this be saved as? ")
        users = webclient.get_variable(SERVER_URL,"d_pgp_LOGIN")
        userinfo = users.get(a[1])
        OSLevels = userinfo[2]
        print(OSLevels.keys())
        if saven in OSLevels:
            print("This level already exists!")
            
        OSLevels[saven] = Ldata
    elif Opt == 6:
        pass
    elif Opt == 7:
        exit()
if __name__ == "__main__":
    print(cli([]))