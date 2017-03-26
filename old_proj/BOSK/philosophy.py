# Caesar.py

# by Rodrigo Serrão

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

print("Caesar Cypher 1.0")
print()
print("Please input the message")
msg = input(">> ").upper()

print("Please type in the encryption letter")
while True:
    l = input(">> ").strip().upper()
    if l in alphabet:
        key = alphabet.index(l)
        break


encrypted = list(map(lambda x: alphabet[
    (alphabet.index(x)+key)%len(alphabet)
    ] if x in alphabet else x, msg))

# obfuscated way of writing:
'''
encrypted = []
for char in msg:
    if char in alphabet:
        char_i = alphabet.index(char)
        new_char_i = (char_i + key) % len(alphabet)
        new_char = alphabet[new_char_i]
        encrypted.append(new_char)
'''

new_msg = ""
for item in encrypted:
    new_msg += item

print("The encrypted message is:")
print(new_msg)