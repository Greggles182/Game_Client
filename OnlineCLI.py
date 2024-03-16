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
            #if not (playersQ >= 2 and playersQ  <= 4):
            if False:
                print ("Invalid number of players!")
                Setup()
            else:
                print("Connecting...")
                webclient.update_variable(SERVER_URL,"i_pgp_LobbyPlayers", "1")
                webclient.update_variable(SERVER_URL,"i_pgp_Players", playersQ)
                cstQ = input("Do you want to start normal levels (1) or custom ones (2): ")
                if cstQ == "1":
                    webclient.update_variable(SERVER_URL,"b_pgp_Custom", cstQ)
                elif cstQ == "2":
                    webclient.update_variable(SERVER_URL,"b_pgp_Custom", cstQ)
                    print("Please draw a level in the opened window.")
                    from functionality import leveldesign
                    webclient.update_variable(SERVER_URL,"l_pgp_level-data", leveldesign())
                print("Waiting for players...")
                webclient.update_variable(SERVER_URL,"b_pgp_Playing", "1")
                begin = False
                while begin == False:
                    if int(webclient.get_variable(SERVER_URL,"i_pgp_Players")) == int(webclient.get_variable(SERVER_URL,"i_pgp_LobbyPlayers")):
                        webclient.update_variable(SERVER_URL,"b_pgp_Playing", "2")
                        begin == True
                        print("Game has begun!")
                        return SERVER_URL
        elif PlayingQ == "1":
            print("A game is currently in the lobby on this address. Please enter 2 and type in the server URL again to join.")
            Setup()
        elif PlayingQ == "2":
            print("A game is currently in progress on this URL")
            Setup()
    elif funct == 2:
        SERVER_URL = input("Enter server URL or press Enter to use default: ")
        if  SERVER_URL == "":
            SERVER_URL = "http://gregglesthegreat.pythonanywhere.com/"
        if str(webclient.get_variable(SERVER_URL,"b_pgp_Playing")) =="1":
            print("Game is currently lobbying...")
            cj = input("Confirm join (y/n): ")
            if cj.lower() =="y":
                if int(webclient.get_variable(SERVER_URL,"i_pgp_Players")) > int(webclient.get_variable(SERVER_URL,"i_pgp_LobbyPlayers")):
                    print("Joining Game...")
                    webclient.update_variable(SERVER_URL,"i_pgp_LobbyPlayers", int(webclient.get_variable(SERVER_URL,"i_pgp_LobbyPlayers"))+1)
                    print("Waiting for game to begin...")
                    while str(webclient.get_variable(SERVER_URL,"b_pgp_Playing")) =="1":
                        pass
                    print("Game has begun!")
                    return SERVER_URL
            else:
                Setup()
        else:
            print("Game cannot be joined at this point in time. Please try again later.")
            Setup()
if __name__ == "__main__":
    Setup()