import pickle

with open("saved.p", "rb") as p:
    t2 = pickle.load(p)
print(t2)
