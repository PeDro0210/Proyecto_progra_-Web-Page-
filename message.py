from flask import Flask, render_template
from flask_socketio import SocketIO, send


#put it with index_redirection.py.
app = Flask(__name__)
app.config['SECRET'] = "secret!123"

socketio = SocketIO(app,cors_allowed_origins="*")

@socketio.on("message")
def handle_message (message):
     print ("Received message: " + message)
     if message != "User connected!":
         send (message, broadcast=True)

@app.route('/')
def chat_part():
    return render_template ("index. html")

# incorporate with the app, don't run it separately.
if __name__ == "__main__":
    socketio.run (app, host="10.100.5.108")
