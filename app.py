#random password generator
from flask import Flask, render_template, request
import random
import string
import secrets as secret

#should be more robust and not rely on library functions

sp= ["!", "@", "#", "$", "%", "^", "&", "*", "-", "_", "=", "+", "|", ":", ";", "'", "<", ">", ",", ".", "?", "/"]

app= Flask(__name__)

def generate_password(length):
    password=[]
    password1=""
    for i in range(length):
        if i%4== 0:
            password.append(secret.choice(random.choice(sp))) # adding in a mandatory special character
        else:
            password.append(secret.choice(string.ascii_letters + string.digits))

    random.shuffle(password) # shuffling this should be rewritten to be more secure than using an existing library

    for i in range(len(password)):
        password1=password1+ str(password[i])
      
    return password1




#coding logic rewrite complexity

@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        length = int(request.form['length'])
        password = generate_password(length)
        return render_template('index.html', password=password)
    return render_template('index.html', password=None)



if __name__ == '__main__':
    app.run(debug=True)