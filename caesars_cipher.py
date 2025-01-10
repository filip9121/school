#make a caeser cipher that can encrypt
letters='abcdefghijklmnopqrstuvwxyz'
key=5
plain_text=("")
def encrypt(plain_text,letters,key):
   cipher_text=("")
   for char in plain_text:
    if char in letters: 
     new_index = (letters.index(char) + key) % len(letters)
    cipher_text += letters[new_index]  
   else:
    cipher_text += char
    return cipher_text

print("Do you want to encrypt?")
userinput = input("yes/no: ").lower()
print()

if userinput == "yes":
    print("ENCRYPTION MODE SELECTED")
    plain_text = input("Enter text to encrypt: ").lower()
    encrypted_text = encrypt(plain_text,letters, key)
    print(f"Encrypted text: {encrypted_text}")
elif userinput == "no":
    print("Ok, I guess not xd.")
else:
    print("Invalid input, please type 'yes' or 'no'.")
