from flask import *
import csv
import os


          
app=Flask(__name__, template_folder=r'templates', static_folder='static')



# en el caso que no funcione a la primera, solo ingresar manuelmente la ruta 
@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        print(username, password)
        
        if username and password in open(r'csv\usuarios.csv').read():
            return render_template('login.html')
        else:
            if username == '' or password == '':
                return render_template('sign_up.html', error='No puede haber campos vacíos')
            else:
                with open(r'csv\usuarios.csv', 'a') as file:
                    writer = csv.writer(file)
                    writer.writerow([username, password])
                return redirect(url_for('login'))

    else:
        return render_template('sign_up.html')
    



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        
        username = request.form['username']
        password = request.form['password']


        if username and password in open(r'csv\usuarios.csv').read():

            return redirect(url_for('chat', username=username, password=password))
        
        else:
            
            return render_template('login.html')
        
    else:
        
        return render_template('login.html')



@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        message=request.form['message']
        
        return render_template('chat_program.html', message=message)
    
    else:
        return render_template('chat_program.html')
        
        
        
        

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        print('get')
        
        username = request.args.get('username')
        password = request.args.get('password')
        
        print(username, password)

        if username and password in open(r'csv\usuarios.csv').read():
            
            return render_template('home.html', user=username, passs=password)
        
        
        
              







