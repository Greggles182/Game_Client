import pickle
with open('rlog.pkl', 'wb') as handle:
    pickle.dump([0, "", True], handle, protocol=pickle.HIGHEST_PROTOCOL)
    handle.close()