#This algorithm takes a string and mirrors the alphabetical index. If the index of the letter in the string is 3, the output index is 3 from the right. example: c -> x. using the string "abc" would output "zyx"  I call it Mirror Cipher

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(letter):
    num = alphabet.index(letter)
    negative = -1 * (num + 1)
    return alphabet[negative]

output = ''
myPlainText = input("Enter your plaintext mister madam: ").lower()


for l in myPlainText:
    if l == ' ':
        output += l
    else:
        output += encrypt(l)

print(output)
