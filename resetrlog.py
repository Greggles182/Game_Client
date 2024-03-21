import pickle
with open('rlog.pkl', 'wb') as handle:
    pickle.dump([1, "Greggles", 0, {}], handle, protocol=pickle.HIGHEST_PROTOCOL)
    handle.close()