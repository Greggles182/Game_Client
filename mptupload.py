import threading
import time
from webclient import update_variable  # Assuming update_variable function is defined in webclient.py

def update_player_variables(SERVER_URL, current_player, player_data):
    update_variable(SERVER_URL, f"l_pgp_Player_{current_player}", player_data)

def start_variable_update_thread(SERVER_URL, current_player, x, y, direction, current_level):
    player_data = [x, y, direction, current_level]
    update_thread = threading.Thread(target=update_player_variables, args=(SERVER_URL, current_player, player_data))
    #update_thread.daemon = True  # Daemonize the thread to exit when the main program exits
    update_thread.start()
if __name__ == "__main__":
    SERVER_URL = input("Enter server URL or press Enter to use default: ")
    if SERVER_URL == "":
        SERVER_URL = "http://gregglesthegreat.pythonanywhere.com/"
    current_player = int(input("Enter current player: "))
    x = int(input("Enter x position: "))
    y = int(input("Enter y position: "))
    direction = int(input("Enter direction (-1, 0, 1): "))
    current_level = int(input("Enter current level: "))

    start_variable_update_thread(SERVER_URL, current_player, x, y, direction, current_level)
