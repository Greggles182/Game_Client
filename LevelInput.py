#DOWNLOAD THIS
import os
def cli(Ldata=[
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 1],
        [1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 2, 2, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 7, 0, 5, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1],
        [1, 7, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 7, 0, 0, 0, 0, 1],
        [1, 0, 2, 0, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 2, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 0, 0, 0, 2, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 2, 2, 2, 2, 1],
        [1, 0, 0, 0, 0, 0, 2, 2, 2, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]):
    print("""Welcome to the LevelEditor CLI!
          Please type a number below to trigger the command
          1: Export the current level to file
          2: Load a level file
          3: Paste in a level seed
          4: Print seed for current level, and begin it.
          5: Exit the program.
          """)
    Opt = input("Type 1-5 then press Enter to proceed: ")
    Opt = int(Opt)
    if Opt > 5:
        print("Invalid Option")
        raise ValueError
    elif  Opt == 1:
        fname = input("What filename do you want to export to? ")
        PATH = f'./levels/{fname}.txt'
        if os.path.isfile(PATH): # and os.access(PATH, os.R_OK):
            print("File exists and is readable")
        else:
            print("FileCheck - OK")
            print(f"Writing to {fname}.txt...")
            with open(PATH, "w") as FILE:
                FILE.write(str(Ldata))
                print(str(Ldata))
                FILE.close()
            input("Success. Press enter to close the CLI")
            return True
    elif  Opt == 2:
        from os import listdir
        from os.path import isfile, join
        PATH = './levels/'
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
            nfname = LISTFILES[nfname]
            FPATH = PATH + nfname
            if os.path.isfile(FPATH) and os.access(FPATH, os.R_OK):
                print("File exists and is readable")
                with open (FPATH,'r') as FDATA:
                    DATA = FDATA.read()
                    DATA = eval(DATA)
                    print(DATA)
                    print(type(DATA))
                    return DATA
            else:
                print("Either the file is missing or not readable")
        else:
            print("That was an invalid option.")
            raise ValueError
if __name__ == "__main__":
    cli()