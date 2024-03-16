#run if you f*cked up
import webclient
SERVER_URL = input("Enter server URL or press Enter to use default: ")
if  SERVER_URL == "":
    SERVER_URL = "http://gregglesthegreat.pythonanywhere.com/"
webclient.update_variable(SERVER_URL,"b_pgp_Playing", "0")