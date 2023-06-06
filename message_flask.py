from index_redirections import *


@socketio.on("message")
def handle_message (message):
     print ("Received message: " + message)
     if message != "User connected!":
         send (message, broadcast=True)


