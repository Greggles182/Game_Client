def Setup():
    import os, sys, time, webclient, subprocess
    SERVER_URL = None  # Initialize SERVER_URL to None
    funct = int(input("Enter 1 to host a game, 2 to join a game, or 3 to go back: "))
    if funct == 1:
        SERVER_URL = input("Enter server URL or press Enter to use default: ")
        if SERVER_URL == "":
            SERVER_URL = "http://gregglesthegreat.pythonanywhere.com/"
        PlayingQ = str(webclient.get_variable(SERVER_URL, "b_pgp_Playing"))
        if PlayingQ == "None" or PlayingQ == "0":
            print("PlayerCheck complete")
            # playersQ = int(input("How many players do you want(2-4): "))
            # if playersQ < 2 or playersQ > 4:
            #     print("Invalid number of players!")
            #     returned = Setup()  # Recursively call Setup() on invalid input
            #     return returned
            # else:
            print("Connecting...")
            webclient.update_variable(SERVER_URL, "i_pgp_LobbyPlayers", "1")
            webclient.update_variable(SERVER_URL, "b_pgp_Playing", "1")
            print("Will start with level 1...")
            # webclient.update_variable(SERVER_URL, "i_pgp_Players", playersQ)
            # cstQ = input("Do you want to start normal levels (1) or custom ones (2): ")
            # if cstQ == "1" or cstQ == "2":
            #     webclient.update_variable(SERVER_URL, "b_pgp_Custom", cstQ)
            #     if cstQ == "2":
            #         print("Please draw a level in the opened window.")
            #         from functionality import leveldesign
            #         webclient.update_variable(SERVER_URL, "l_pgp_level-data", leveldesign())
            # else:
            #     print("Invalid input!")
            #     returned = Setup()
            #     return returned
            # print("Waiting for players...")
            while 2 != int(webclient.get_variable(SERVER_URL, "i_pgp_LobbyPlayers")):
                pass
                time.sleep(0.5)
            webclient.update_variable(SERVER_URL, "b_pgp_Playing", "2")
            PlayerN = 1
            print("Game has begun!")
        else:
            print("A game is currently in progress on this URL.")
            returned = Setup()
            return returned
    elif funct == 2:
        SERVER_URL = input("Enter server URL or press Enter to use default: ")
        if SERVER_URL == "":
            SERVER_URL = "http://gregglesthegreat.pythonanywhere.com/"
        if str(webclient.get_variable(SERVER_URL, "b_pgp_Playing")) == "1":
            print("Game is currently lobbying...")
            cj = input("Confirm join (y/n): ")
            if cj.lower() == "y":
                if int(webclient.get_variable(SERVER_URL, "i_pgp_Players")) > int(webclient.get_variable(SERVER_URL, "i_pgp_LobbyPlayers")):
                    print("Joining Game...")
                    PlayerN = int(webclient.get_variable(SERVER_URL, "i_pgp_LobbyPlayers"))+1
                    webclient.update_variable(SERVER_URL, "i_pgp_LobbyPlayers", int(webclient.get_variable(SERVER_URL, "i_pgp_LobbyPlayers"))+1)
                    print("Waiting for game to begin...")
                    while str(webclient.get_variable(SERVER_URL, "b_pgp_Playing")) == "1":
                        pass
                        time.sleep(0.5)
                    print("Game has begun!")
                else:
                    print("Invalid input!")
                    returned = Setup()
                    return returned
            elif cj.lower() == "n":
                print("Ok. Exiting.")
                returned = Setup()
                return returned
            else:
                print("Illegal Input!")
                returned = Setup()
                return returned
        else:
            print("Game cannot be joined at this point in time. Please try again later.")
            returned = Setup()
            return returned
    elif funct == 3:
        return True, True
    else:
        print("Invalid Option! Try Again.")
        returned = Setup()
        return returned
    return PlayerN, SERVER_URL

if __name__ == "__main__":
    server_url = Setup()  # Assign the returned SERVER_URL to a variable
    print(server_url)  # Print the SERVER_URL outside the function
