import random
import string
import secrets as secret

#should be be more robust and not rely on library functions

sp= ["!", "@", "#", "$", "%", "^", "&", "*", "-", "_", "=", "+", "|", ":", ";", "'", "<", ">", ",", ".", "?", "/"]


def generate_password(length):
    password=[]
    password=""
    for i in range(length):
        if i%4== 0:
            password.append(secret.choice(sp)) # adding in a mandatory special character
        else:
            password.append(secret.choice (string.ascii_letters or string.digits ))

    random.shuffle(password) # shuffling this should be rewriten to be more secure then using and exsisting library

    for i in range(len(password)):
        password=password+ str(password[i])
      
    return password


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





print(generate_password(8))