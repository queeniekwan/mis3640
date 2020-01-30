# Built-in Functions
print(round(3.5))

print(min(3,6,2,5,6,7))

print(ord('a'))
print(chr(97)) # inverse of ord()
print(chr(ord('a') + 2))

# Python challenge 2
encrypted = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
msg_list = []

for letter in encrypted:
    if letter.isalpha():
        decrypted_letter = chr(ord(letter) + 2)
    else:
        decrypted_letter = letter
    msg_list.append(decrypted_letter)

decrypted_msg = ''.join(msg_list)
print(decrypted_msg)

msg = []
for letter in 'map':
    if letter.isalpha():
        decrypted_letter = chr(ord(letter) + 2)
    else:
        decrypted_letter = letter
    msg.append(decrypted_letter)

message = ''.join(msg)
print(message)


# Function demo
def print_lyrics():
    print("Hey jude. Dont make it bad")
    print("take a sad song and make it better")

# print_lyrics()
# print(type(print_lyrics))

def repeat_lyrics():
    print_lyrics()
    print('na-na-na-na-na-na-na')
    print_lyrics()

# repeat_lyrics()

def print_twice(whatever):
    print(whatever)
    print(whatever)

print_twice('a')

