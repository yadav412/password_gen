import random
import string
import secrets as secret

#should be be more robust and not rely on library functions

sp= ["!", "@", "#", "$", "%", "^", "&", "*", "-", "_", "=", "+", "|", ":", ";", "'", "<", ">", ",", ".", "?", "/"]


def generate_password(length):
    password=[]
    password1=""
    for i in range(length):
        if i%4== 0:
            password.append(secret.choice(sp)) # adding in a mandatory special character
        else:
            password.append(secret.choice (string.ascii_letters or string.digits ))

    random.shuffle(password) # shuffling this should be rewriten to be more secure then using and exsisting library

    for i in range(len(password)):
        password1=password1+ str(password[i])
      
    return password1


def generate_pin(length):
    password=[]
    password11=""
    for i in range(length):
        if i%4== 0:
            password.append(secret.choice(sp)) # adding in a mandatory special character
        else:
            password.append(secret.choice (string.ascii_letters or string.digits ))

    random.shuffle(password) # shuffling this should be rewriten to be more secure then using and exsisting library

    for i in range(len(password)):
        password11=password11+ str(password[i])
      
    return password11

#coding logic rewrite complexity

#basic encryption logic // ceaser(modded) cipher shift 

common_words =["the", "be", "to", "of", "and", "a", "in", "that", "have", "I", "dog", "cat", "man", "woman", "child", "car", "house", "tree", "food", "water"]
Plain = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
Cipher = ["X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W"]

#encrypt function (old ceaser cipher)
#chaining multiple encryptions together to make it more complex - the encryption 

#the encryption engine will be made more complex in future iterations "Chimera Encryption Engine"
    

def encryptceaser(message):
    em=""
    for i in range(len(message)):
        for j in range(len(Plain)):
            if message[i] == Plain[j]:
                em= em + Cipher[j]
            elif message[i] == " ":
                em= em + " "
    
    return em

def Dencryptceaser(message): #works are ceaser cipher ecryption (happy accident)
    
    em=""
    for i in range(len(message)):
        for j in range(len(Plain)):
            if message[i] == Cipher[j]:
                em= em + Plain[j]
            elif message[i] == " ":
                em= em + " "
    return em

gp = generate_password(8)
gp = gp.upper()

for i in range(len(common_words)):
    if gp.lower()== common_words[i]:
        print("Regenerate password")
        gp = generate_password(8)
        gp = gp.upper()
#  weak password catch


print(gp)
d=(encryptceaser(gp))
print(d)
print(Dencryptceaser(d))


#the decryption logic works basic decryption and encryption is functional


# 3 dig encryption key in front of the password used to identify the user ie 8 dig 3 pin then random generator pk


#password engine, - add user database

