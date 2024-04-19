import os, sys, webclient, time, pickle
SERVER_URL = "http://gregglesthegreat.pythonanywhere.com/"
my_dict = webclient.get_variable(SERVER_URL,"d_pgp_LOGIN")
print(my_dict)
print(type(my_dict))
import hasher
webclient.update_variable(SERVER_URL, "d_pgp_LOGIN", {'sauvage': [hasher.hash("letest"), "900", {}], 'Greggles': [hasher.hash("Greggles001"), "21", {}], "Test": [hasher.hash("Test"), "21", {}]})
my_dict = webclient.get_variable(SERVER_URL,"d_pgp_LOGIN")
print(my_dict)
# Save variable to a file
with open('rlog.pkl', 'wb') as f:
    pickle.dump([1,"Test", True], f)