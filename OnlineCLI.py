def Setup():
    import os, sys, time, webclient, subprocess, online_funtionality, functionality
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
                  ytuo= input("What do you want to do?lvl1/lvl2/lvl3/cst")
                  if ytuo=="lvl1":
                      print("lvl1")
                      online_funtionality.start(1, False, [])
                  elif ytuo=="lvl2":
                      print("lvl2")
                      online_funtionality.start(2, False, [])
                  elif ytuo=="lvl3":
                      print("lvl3")
                      online_funtionality.start(3, False, [])
                  elif ytuo=="cst":
                      custom_leveldata = functionality.leveldesign()
                      print("cst")
                      online_funtionality.start("cst", False, custom_leveldata)
                  else:
                      print("fail")
        else:
            print("Waiting for host to start.")
            time.sleep(0.5)
            server_hhost = webclient.get_variable(SERVER_URL,"hhost")
            server_hhost[1]+=1
            time.sleep(0.5)
            webclient.update_variable(SERVER_URL, "hhost", server_hhost)
            time.sleep(0.5)
            server_hhosrt = webclient.get_variable(SERVER_URL,"num_p")
            pnum=server_hhost[1]
            server_hhosrt["player", pnum]=["img/guy1", (0, 0)]
            time.sleep(0.5)
            webclient.update_variable(SERVER_URL, "num_p", server_hhosrt)
            while True:
              time.sleep(0.5)
              server_hhost = webclient.get_variable(SERVER_URL,"hhost")
              if server_hhost[2]==1:
                  print("commence")
    else:
        print("Waiting for host to start.")
        time.sleep(0.5)
        server_hhost = webclient.get_variable(SERVER_URL,"hhost")
        server_hhost[1]+=1
        time.sleep(0.5)
        webclient.update_variable(SERVER_URL, "hhost", server_hhost)
        time.sleep(0.5)
        server_hhosrt = webclient.get_variable(SERVER_URL,"num_p")
        pnum=server_hhost[1]
        server_hhosrt["player", pnum]=["img/guy1", (0, 0)]
        time.sleep(0.5)
        webclient.update_variable(SERVER_URL, "num_p", server_hhosrt)
        while True:
          time.sleep(0.5)
          server_hhost = webclient.get_variable(SERVER_URL,"hhost")
          if server_hhost[2]==1:
              print("commence")
            

if __name__=="__main__":
    Setup()
