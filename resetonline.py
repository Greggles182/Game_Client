#run if you f*cked up
import webclient
SERVER_URL = input("Enter server URL or press Enter to use default: ")
if  SERVER_URL == "":
    SERVER_URL = "http://gregglesthegreat.pythonanywhere.com/"
server_hhost = webclient.get_variable(SERVER_URL, "hhost")
print(server_hhost)
server_hhost[0]=0
webclient.update_variable(SERVER_URL,"hhost", server_hhost)
