def encrypt(letter, key):
  value = ord(letter) - 97
  value = (value + key) % 26
  return chr(value + 97)

output = ''
myPlainText = input("Enter your plaintext mister madam: ").lower()
string = myPlainText[::-1]


for l in string: 
  if l == ' ':
    output += l
  else:
    output += encrypt(l, 1)

print(output)
