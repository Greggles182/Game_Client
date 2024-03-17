import os, sys, webclient, time
SERVER_URL = "http://gregglesthegreat.pythonanywhere.com/"
my_dict = webclient.get_variable(SERVER_URL,"d_pgp_LOGIN")
print(my_dict)
my_dict = webclient.update_variable(SERVER_URL, "d_pgp_LOGIN", {'sauvage': ["letest", "900"]})
my_dict = webclient.get_variable(SERVER_URL,"d_pgp_LOGIN")
print(my_dict)