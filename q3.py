def encrypt(letter, key):
  value = ord(letter) - 97
  value = (value + key) % 26
  return chr(value + 97)

output = ''
myPlainText = input("Enter your plaintext mister madam: ").lower()
string = myPlainText[::-1]


for n in range(0, len(myPlainText), 1):
  l = myPlainText[n]
  if l == ' ':
    output += l
  else:
    if n % 2 == 0:
      output += encrypt(l, 3)
    else:
      output += encrypt(l, 5)

print(output)
