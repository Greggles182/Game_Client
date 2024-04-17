def Setup():
    import os, sys, time, webclient, subprocess
    #server URL
    SERVER_URL = "http://gregglesthegreat.pythonanywhere.com/"
    # Creating a dictionary
    server_hhost = webclient.get_variable(SERVER_URL,"hhost")
    if server_hhost[0]==0:
        hostqmark= input("Do you want to be host?y/n")
        if hostqmark=="y":
            time.sleep(0.5)
            server_hhost[0]=1
            webclient.update_variable(SERVER_URL,"hhost", server_hhost)
            while True:
              time.sleep(0.5)
              server_hhost = webclient.get_variable(SERVER_URL,"hhost")
              nopil= server_hhost[1]
              stg= input(f"""You have {nopil} people in lobby. Press enter to start or press space and enter to refresh!""")
              print(stg)
              if stg=="":
                  print("break")
                  break
        else:
            sw= input("Waiting for host to start.Press exit and enter to exit queue.")
            time.sleep(0.5)
            server_hhost = webclient.get_variable(SERVER_URL,"hhost")
            server_hhost[1]+=1
            time.sleep(0.5)
            webclient.update_variable_variable(SERVER_URL, "hhost", server_hhost)
    else:
        sw= input("Waiting for host to start.Press exit and enter to exit queue.")
        time.sleep(0.5)
        server_hhost = webclient.get_variable(SERVER_URL,"hhost")
        server_hhost[1]+=1
        time.sleep(0.5)
        webclient.update_variable_variable(SERVER_URL, "hhost", server_hhost)
            

if __name__=="__main__":
    Setup()
