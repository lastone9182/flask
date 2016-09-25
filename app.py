# -*- coding: UTF-8 -*-
from flask import Flask, url_for, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('getusermedia.html')

@socketio.on('message')
def handle_message(message):
	print('received message: ' + message)

@socketio.on('my event')
def handle_my_custom_event(json):
	print('received json: ' + str(json))

@socketio.on('my event', namespace='/test')
def handle_my_custom_namespace_event(json):
	print('received json: ' + str(json))

if __name__ == '__main__':
    socketio.run(app)

