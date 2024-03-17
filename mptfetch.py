import threading
import time
from webclient import get_variable  # Assuming get_variable function is defined in webclient.py

Online_playerdata = []  # Global variable to store player data

def fetch_player_info(SERVER_URL, players, current_player):
    global Online_playerdata
    while True:
        player_info = []
        for i in range(players):
            if i + 1 != current_player:
                data = get_variable(SERVER_URL, f"l_pgp_Player_{i+1}")
                player_info.append(data)
        Online_playerdata = player_info  # Update the global variable
        print("Player info updated:", Online_playerdata)
        time.sleep(0.2)  # Adjust sleep time as per your needs

def start_player_update_thread(SERVER_URL, players, current_player):
    update_thread = threading.Thread(target=fetch_player_info, args=(SERVER_URL, players, current_player))
    update_thread.daemon = True  # Daemonize the thread to exit when the main program exits
    update_thread.start()
if __name__ == "__main__":
    SERVER_URL = input("Enter server URL or press Enter to use default: ")
    if SERVER_URL == "":
        SERVER_URL = "http://gregglesthegreat.pythonanywhere.com/"
    players = int(input("Enter total number of players: "))
    current_player = int(input("Enter current player: "))

    start_player_update_thread(SERVER_URL, players, current_player)

    # Now you can access Online_playerdata in your main script
    while True:
        print("Main script running...")
        print("Online player data:", Online_playerdata)
        time.sleep(10)  # Adjust sleep time as per your needs
