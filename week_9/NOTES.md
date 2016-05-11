Exercise 09: Websocket
==========================================================

IKI20810 - Advanced Programming @ Faculty of Computer Science
Universitas Indonesia, Even Semester 2015/2016

* * *

*Friday, April 29nd 2016*

Your main tasks in this week exercise is to explore
available library of websocket in python and learn how it works.
You need to run the example and do small modification to show
your understanding of how it works and able to explain it.


Mandatory Tasks Description
---------------------------

There are several available libraries for websocket in python.
You are free to choose any of them to create a very simple
web-based chatting application.

Mandatory Checklist
-------------------
- Write some notes with your own words that explain how the web-based chat works. 
Write it as a markdown text file in your repository.

How the app works
-----------------
This web-based chat application operates on the websocket protocol that enables low
latency, lightweight asynchronous requests between hosts, instead of the slower and
less efficient option of long-polling. The websocket protocol is useful for games,
chat apps, and video call since they all require data to be downloaded immediately
by the client as soon as it becomes available on the server. The server then
'pushes' the data to the client.

The app uses Flask-SocketIO for full-duplex websocket implementation of a chat app.
It uses SocketIO for transport layer abstraction, gevent for async services, and
Flask as its web application framework. The client uses jQuery and SocketIO 

- The server initialises itself by importing all the needed modules (async
services, Flask, threading, etc).

- The server then runs itself on SocketIO by listening to an address (localhost:5000
by default).

- The dynamically generated web page sends async requests via SocketIO which is
then received by the server. This can be a message in the form of string, a name
change event, or any kind of event that is registered in the server’s handlers.
Example:

	```javascript
    $('form#join').submit(function(event) {
                socket.emit('join', {room: $('#join_room').val()});
                return false;
    ```
    This example requests the server for the client to join a room.

- The server handles the requests using one of its handler methods depending on
what event is sent to it. It can use Flask-SocketIO’s built-in functions such as
`emit` to send messages (both client and server can use `emit`), `join_room` to
create a sub-group of the conversation, and many more.
Example:

	```python
	@socketio.on('join', namespace='/test')
	def join(message):
	    join_room(message['room'])
	    emit('join',
	         {'user': message['user'], 'room': message['room']},
	         broadcast=True)
	```
	This example handles a join request from the client by putting the client in 
	a room and broadcasting to the entire chatroom an event that will be handled
	later by the client, along with the data needed.

- The server then uses `emit` to communicate server responses with a client or
many clients (using `broadcast=True` or rooms).

- The client may then receive a response from the server, usually also in the 
form of `emit`.
Example:
	```javascript
	socket.on('join', function(msg) {
        var msg_log = '<span class="uname">' + msg.user + '</span>' +
                    ' has joined the room ' +
                    '<span class="uname">[' + msg.room + ']</span>!<br>';
        $('#log').append(msg_log);
        $('#log').scrollTop($('#log').prop('scrollHeight'));
    });
    ```
    This example handles a broadcasted response from the earlier example by 
    printing out a formatted text that informs all the users (since all clients
    receive the event) that a certain user has joined a certain room.

- Optionally, the server may have multiple threads runnning to broadcast server-
generated events. Server generated events can be in the form of `emit`s that the
server broadcasts every set time interval. This app does not have that feature.
Example:
	
	```python
	def background_thread():
	    """Example of how to send server generated events to clients."""
	    count = 0
	    while True:
	        time.sleep(10)
	        count += 1
	        socketio.emit('my response',
	                      {'data': 'Server generated event', 'count': count},
	                      namespace='/test')
	```