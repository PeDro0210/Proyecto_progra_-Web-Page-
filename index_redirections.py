from flask import *
import json
from flask_socketio import SocketIO, send
from Login import data


#DE HOY EN ADELENTAE, SIEMPRE VAS A COMENTAR ENSERIO

data_users = json.load(open(r'The_program\csv\users_manifest.json'))
real_data=data(data_users)
app=Flask(__name__, template_folder=r'templates', static_folder='static')
app.config['SECRET'] = "secret!123"
socketio = SocketIO(app,cors_allowed_origins="*")

 
    
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


        if real_data.check_passwords(username, password):

            return redirect(url_for('chat', username=username, password=password))
        
        else:
            
            return render_template('login.html')
        
    else:
        
        return render_template('login.html')


# this part migth not be necessary anymore
# @app.route('/chat', methods=['GET', 'POST'])
# def chat():
#     if request.method == 'POST':
#         message=request.form['message']
        
#         return render_template('chat_program.html', message=message)
    
#     else:
#         return render_template('chat_program.html')
        
        
        
        

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        print('get')
        
        username = request.args.get('username')
        password = request.args.get('password')
        
        print(username, password)

        if real_data.check_passwords(username, password):
            
            return render_template('home.html', user=username, passs=password)
        
        
        
              







