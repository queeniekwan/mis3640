"""
1. read the file save the words into a list
2. sort the word
'rumeer' --> 'eemrru' (signature of the word)
'reemur' --> 'eemrru'
'kenzi' --> 'ekinz'

create empty list for each signature
create a dictionary to store all signatures
e.g. {'eemrru':['rumeer', 'reemur'], 'ekinz':['kenzi']}

3. get the values from the dict, probably only the lists with more than one word

4. sort the anagram with its length, create a dict(length: a list of lists)

"""
def read_file_to_list(path):
    '''
    reads all the words from the file
    returns a list of words
    '''
    f = open(path)
    word_list = f.read().lower().split()

    return word_list

def anagram(words):
    '''
    returns a dictionary of anagrams
    keys is a signature (sorted string) of the anagram words 
    values is a list of anagram words
    '''
    d = {}
    for word in words:
        s = ''.join(sorted(word))
        d.setdefault(s, []).append(word)

    return d

def print_anagrams(word_dict, n = 1):
    '''
    prints all the anagrams with more than n words
    '''
    for signature, words in word_dict.items():
        if len(words) > n:
            print(f'{signature}: {words}')

def sorted_dict(d):
    '''
    returns a new dictionary:
    key is numbe of words in a anagram list, 
    value is a list of anagram lists
    '''
    sd = {}
    for words in d.values():
        sd.setdefault(len(words), []).append(words)

    return sd

def main():
    word_list = read_file_to_list('session09/words.txt')
    word_dict = anagram(word_list)
    print_anagrams(word_dict, 2)
    sd = sorted_dict(word_dict)
    # print_anagrams(sd, 10)

if __name__ == "__main__":
    main()
