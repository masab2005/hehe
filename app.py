from flask import Flask , render_template, request, redirect, url_for, session
from database import load_info, insert_info, check_user
import importlib
import database
importlib.reload(database)

app = Flask(__name__)
app.secret_key='pooop'

@app.route('/', methods=['GET', 'POST'])
def home():
    mesage = ''
    info = []
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        info = load_info(username,password)
        if info:
            session['loggedin'] = True
            session['username'] = info['username']
            session['password'] = info['password']
            mesage = 'Logged in successfully !'
            return render_template('loggedin.html', mesage = mesage)
        else:
            mesage = 'Please enter correct email / password !'
    return render_template('home.html',mesage = mesage,info=info)
     

@app.route('/signup', methods=['GET','POST'])
def signup():
    mesage = ''
    info = []
    if request.method == 'POST':
        email    = request.form['email']
        username = request.form['username']
        password = request.form['password']
        confirm_pwd = request.form['confirm_pwd']
        info = check_user(email,username)
        if info: 
            mesage = 'Email or Username already exists!'
        else:
             if password == confirm_pwd:
                 insert_info(email,username,password)
                 session['loggedin'] = True
                 session['username'] = username
                 mesage = 'Account Created!'
                 return render_template('loggedin.html',mesage = mesage)
             else:
                 mesage = 'Password not matched !'
    
    return render_template('create_account.html',mesage = mesage)

@app.route('/loggedin')
def loggedin():
  return render_template('loggedin.html')
    
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('userid', None)
    session.pop('email', None)
    return redirect(url_for('home'))

app.run(host='0.0.0.0', debug=True)
