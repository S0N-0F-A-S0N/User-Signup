from flask import Flask, request # boom
import lepl.apps.rfc3696
email_validator = lepl.apps.rfc3696.Email()


app = Flask(__name__)
app.config['DEBUG'] = True


form = ''.join(open('signup.html', 'r').readlines())

@app.route("/") # Landing page
def index():
    return form

@app.route("/path/") # This is the path that will be returned.
def path():
    return form.format(name='', pass1='', pass2='', email='', name_error='', pass1_error='', pass2_error='', email_error='')

@app.route("/path/", methods=['POST']) # This is the path that will be returned.
def validate():

    name = request.form['name']
    pass1 = request.form['pass1']
    pass2 = request.form['pass2']
    email = request.form['email']

    name_error = ""
    pass1_error = ""
    pass2_error = ""
    email_error = ""

    if not (name):
        name_error = "Name can't be empty!"

    if not (pass1):
        pass1_error = "Password can't be empty!"

    if not (pass2):
        pass2_error = "Password can't be empty!"
    elif (pass2 != pass1):
        pass2_error = "Password does not match!"

    if not (email):
        email_error = "Email can't be empty!"
    elif not email_validator(email):
        email_error = "Invalid email format!"


    if not name_error and not pass1_error and not pass2_error and not email_error:
        return ("Welcome, " + name + "!")
    else:
        return form.format(name_error = name_error, pass1_error = pass1_error, pass2_error = pass2_error, email_error = email_error,
     name = name, pass1 = '', pass2 = '', email = email,)

app.run(debug=True, host="10.0.0.100", port=8080)
