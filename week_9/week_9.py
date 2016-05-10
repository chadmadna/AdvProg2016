#!/usr/bin/env python

# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on available packages.
async_mode = None

if async_mode is None:
    try:
        import eventlet
        async_mode = 'eventlet'
    except ImportError:
        pass

    if async_mode is None:
        try:
            from gevent import monkey
            async_mode = 'gevent'
        except ImportError:
            pass

    if async_mode is None:
        async_mode = 'threading'

    print('async_mode is ' + async_mode)

# monkey patching is necessary because this application uses a background
# thread
if async_mode == 'eventlet':
    import eventlet
    eventlet.monkey_patch()
elif async_mode == 'gevent':
    from gevent import monkey
    monkey.patch_all()

import time
from threading import Thread
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None


def background_thread():
    """Example of how to send server generated events to clients."""
    pass


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('my broadcast event', namespace='/test')
def test_broadcast_message(message):
    emit('chat',
         {'data': message['data'], 'user': message['user']},
         broadcast=True)


@socketio.on('join', namespace='/test')
def join(message):
    join_room(message['room'])
    emit('join',
         {'user': message['user'], 'room': message['room']},
         broadcast=True)


@socketio.on('leave', namespace='/test')
def leave(message):
    leave_room(message['room'])
    emit('my response',
         {'data': 'In rooms: ' + ', '.join(rooms()),
          'count': session['receive_count']})


@socketio.on('close room', namespace='/test')
def close(message):
    emit('my response', {'data': 'Room ' + message['room'] + ' is closing.'},
         room=message['room'])
    close_room(message['room'])


@socketio.on('my room event', namespace='/test')
def send_room_message(message):
    emit('room chat',
         {'data': message['data'], 'user': message['user'],
          'room': message['room']}, room=message['room'])


@socketio.on('disconnect request', namespace='/test')
def disconnect_request():
    emit('my response',
         {'data': 'Disconnected!'})
    disconnect()


@socketio.on('connect', namespace='/test')
def test_connect():
    emit('my response', {'data': 'Connecting..'})


@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected', request.sid)


@socketio.on('my connect event', namespace='/test')
def test_connect_message(message):
    emit('my response',
        {'data': message['data']})


@socketio.on('change username', namespace='/test')
def change_username(message):
    old_name = message['old_name']
    new_name = message['new_name']
    emit('change username', {
        'old_name': old_name, 'new_name': new_name}, broadcast=True)
   


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
