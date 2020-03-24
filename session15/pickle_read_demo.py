import pickle

with open('session15/saved.p', 'rb') as p:
    t = pickle.load(p)

print(t)
print(type(t))