from index_redirections import app
from message_flask import *


if __name__ == '__main__':
    app.run(debug=True) 
    socketio.run(app, host="127.0.0.1")    