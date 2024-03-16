import threading
import webclient
#[x, y, self.direction]
SERVER_URL = "http://gregglesthegreat.pythonanywhere.com/"
num = 2
dx = 0
dy = 0
direction = 0
playerdata = [0, 0 , 0]
def get_data():
    global playerdata
    global dx
    global dy
    global direction
    playerdata = eval(webclient.get_variable(SERVER_URL,f"l_pgp_Player{num}"))
    dx = playerdata[0]
    dy = playerdata[1]
    direction = playerdata[2]
x = threading.Thread(target=get_data)
x.start()
print(x)
while True:
    print(playerdata)   
    print(str(dx) + ", " + str(dy) + ", " + str(direction))