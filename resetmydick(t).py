import os, sys, webclient, time, pickle
SERVER_URL = "http://gregglesthegreat.pythonanywhere.com/"
my_dict = webclient.get_variable(SERVER_URL,"d_pgp_LOGIN")
print(my_dict)
webclient.update_variable(SERVER_URL, "d_pgp_LOGIN", {'sauvage': ["letest", "900", {}], 'Greggles': ["Greggles001", "20", {}]})
my_dict = webclient.get_variable(SERVER_URL,"d_pgp_LOGIN")
print(my_dict)
# Save variable to a file
with open('rlog.pkl', 'wb') as f:
    pickle.dump([0,""], f)