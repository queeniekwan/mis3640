'''files'''
with open('session15/new_file.txt', 'w') as f:
    for _ in range(10):
        f.write('something\n')

# context manager
# same as

# f = open('session15/new_file.txt', 'w')
# f.write('something')
# f.close()

'''pickling'''
import pickle

t = [1, 2, 3, 'alvie', 'queenie', ('a', 'b')]

with open('session15/saved.p', 'wb') as p:
    pickle.dump(t, p)