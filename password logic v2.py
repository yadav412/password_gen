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
            password.append(secret.choice(random.choice(sp))) # adding in a mandatory special character
        else:
            password.append(secret.choice (string.ascii_letters or string.digits ))

    random.shuffle(password) # shuffling this should be rewriten to be more secure then using and exsisting library

    for i in range(len(password)):
        password1=password1+ str(password[i])
      
    return password1




#coding logic rewrite complexity





print(generate_password(8))