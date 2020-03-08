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

def signature_set(words):
    '''
    the sorted string of each word is its signature
    returns a list of all unique signature in the list words
    words is a list
    '''
    signature = []
    for word in words:
        signature.append(sorted(word))
    signature = list(set(signature))

    return signature

def anagram(signatures, words):
    '''
    signature is a list of signatures
    words is a list of words
    returns a dictionary of signatures as keys 
        and lists of annagram of that signature as values
    '''
    d = {}
    for signature in signatures:
        anagram = []
        for word in words:
            if signature == sorted(word):
                anagram.append(word)
        d[signature] = anagram
    
    return d

def print_anagrams(word_dict, n = 1):
    '''
    prints all the anagrams with more than n words
    '''

def sorted_dict(d):
    '''
    returns a new dictionary:
    key is numbe of words in a anagram list, 
    value is a list of anagram lists
    '''

def main():
    word_list = read_file_to_list('session09/words.txt')
    word_dict = anagram(signature_set(word_list), word_list)
    print_anagrams(word_dict)

if __name__ == "__main__":
    main()
