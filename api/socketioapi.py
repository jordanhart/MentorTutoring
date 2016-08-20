from flask import Flask
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)

@socketio.on('message')
def handleMessage(msg):
    print('Message: ' + msg)
    emit('message', 'message recieved')

if __name__ == '__main__':
	socketio.run(app, host='0.0.0.0', port=5000, debug=True)

