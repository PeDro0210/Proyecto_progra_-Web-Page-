from flask import *
import json
from flask_socketio import SocketIO, send
from Login import data


#DE HOY EN ADELENTAE, SIEMPRE VAS A COMENTAR ENSERIO

data_users = json.load(open(r'The_program\csv\users_manifest.json'))
real_data=data(data_users)
app=Flask(__name__, template_folder=r'templates', static_folder='static')
app.config['SECRET'] = "UWUTHE_SECRET_KEY"
socketio = SocketIO(app) #I thing I fucked up this shit
#the fucking firewalls, the don't let me use the html on the college 

 
    
@app.route('/', methods=['GET', 'POST'])
def start_page():
    return redirect(url_for('sign_up'))


@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        print(type(username), type(password))
        
        print(username, password)
        
        if real_data.check_passwords(username, password):
            print('already in think')
            return redirect(url_for('login'))
        
        else:
            
            if username == '' or password == '':
                return render_template('sign_up.html', error='No puede haber campos vacíos')
            else:
                real_data.create_user(username, password)
                return redirect(url_for('login'))

    else:
        return render_template('sign_up.html')
    


#ver cual es el punto del json, honestamente ya no recuerdas
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        
        username = request.form['username']
        password = request.form['password']

        print(username, password)

        if real_data.check_passwords(username, password):

            if password == real_data.json_file[username]['password']:
                print('post')
                return redirect(url_for('home', username=username, password=password))
            else:
                # haha, is just a joke haha, unless...
                print('wrong password, bitch')
                return render_template('login.html')
        
        else:
            print('get')
            return render_template('login.html')
        
    else:
        print('get')
        return render_template('login.html')


@app.route('/home', methods=['GET', 'POST'])
def home(): #I have to do all the user home for this shit
    if request.method == 'GET':
        print('get')
        global username
        username = request.args.get('username')
        password = request.args.get('password')


        if real_data.check_passwords(username, password):
            
            return render_template('home.html', user=username, passs=password)
    
    else:
        return redirect('chat_part',username=username)
        

@app.route('/chat', methods=['GET', 'POST'])
def chat_part():

    username_1= username
    print(f"username:{username_1}")
    return render_template ("chat_box.html", user=username_1)
        
        
        
              







