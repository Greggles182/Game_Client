import pickle
with open('rlog.pkl', 'wb') as handle:
    pickle.dump([1, "Greggles", True], handle, protocol=pickle.HIGHEST_PROTOCOL)
    handle.close()