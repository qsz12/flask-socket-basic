from flask import Flask,render_template
from flask_socketio import SocketIO, emit, send
import os
from loguru import logger
import requests
import random

app=Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", "")
socketio=SocketIO(app,cors_allowed_origins="*")

@socketio.on('my event')
def handle_myevent(json):
    print('received data from client ....................',str(json))
    # socketio.emit('my response',json)

@socketio.on('formfill')
def handle_formfill(json):
    print('posted username and message ....................',str(json))
    socketio.emit('my response',json)

@app.route('/')
def index():
    return render_template('chatapp.html')



if __name__ == '__main__':
    socketio.run(app,debug=True)