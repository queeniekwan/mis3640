def histogram(word_list):
    d = {}
    
    for word in word_list:
        d[word] = d.get(word, 0) + 1

    return d

f = open('session11/song_lyrics.txt')
lyrics = f.read().lower().replace(',','').replace('...','').split()
# print(lyrics)

h = histogram(lyrics)
print(h)
