def Setup():
    import os, sys, webclient, time
    funct = int(input("Enter 1 to host a game, or 2 to join a game: "))
    if funct == 1:
        SERVER_URL = input("Enter server URL or press Enter to use default: ")
        if  SERVER_URL == "":
            SERVER_URL = "http://gregglesthegreat.pythonanywhere.com/"
        PlayingQ = str(webclient.get_variable(SERVER_URL,"b_pgp_Playing"))
        if PlayingQ == "None" or PlayingQ == "0":
            print("PlayerCheck complete")
            playersQ = int(input("How many players do you want(2-4): "))
            if not (playersQ >= 2 and playersQ  <= 4):
                print ("Invalid number of players!")
                Setup()
            print("Connecting...")
            webclient.update_variable(SERVER_URL,"i_pgp_Players", playersQ)
            cstQ = input("Do you want to start the normal levels (1) or custom ones (2): ")
            webclient.update_variable(SERVER_URL,"b_pgp_Custom", cstQ)
            if cstQ == "1":
                pass
            elif cstQ == "2":
                print("Please draw a level in the opened window.")
                from functionality import leveldesign
                webclient.update_variable(SERVER_URL,"l_pgp_level-data", leveldesign())
Setup()