from flask import Flask , render_template, request, redirect, url_for, session
from database import connection,load_info
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

       

@app.route('/signup')
def signup():
    return render_template('create_account.html')

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
