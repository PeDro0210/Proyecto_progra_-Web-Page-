from index_redirections import app
from message_flask import *
if __name__ == '__main__':
    socketio.run(app, host="localhost")
    app.run(debug=True)     