Exercise 09: Websocket
======================

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

About the username functionality
--------------------------------
The original example app provided by Miguel Grinberg in his Github repo for 
Flask-SocketIO demonstrated only fundamental functions his module, and so it did
not include a mechanism of identifying users.

In my modified app, I added a mechanism for assigning yourself a username from the 
client-side application. Initially, all users connect as guest. The client will 
then check the cookies for a saved username. If found, the user will proceed with 
that username. Else, they proceed as a guest with the username 'Guest'. The 
username is passed back and forth from the client to the server on events that 
requires the user to be identified in the chatroom, such as connects, room messages,
broadcast messages, room joins, and username changes.

#### Storing and changing username

The client app provides a form field to submit a new username if the user wants to
change username. Online users can change their username and the client app will 
store it in the form of cookies. Changes are stored locally in the client's machine
as cookies, instead of being stored in the server. 

```javascript
$('form#username').submit(function(event) {
    var new_name = $('input#username_data').val();
    // ignore same name or empty field
    if (new_name.length == 0 || new_name == username) {	
    return false;
    }
    // emit 'change username' event to server
    socket.emit('change username', {
    old_name: username, 
    new_name: new_name
    });
    // set new username and store to cookie
    username = new_name;
    $.cookie("username", username)
    return false;
});
```

When a user changes their username, the change is broadcasted to all members of the
chat. The client emits a `'change username'` event to the server, which will be
handled by the server by emitting a a broadcast message to all connected clients.

```python
@socketio.on('change username', namespace='/test')
def change_username(message):
    old_name = message['old_name']
    new_name = message['new_name']
    emit('change username', {
		 'old_name': old_name, 'new_name': new_name}, broadcast=True)
```

When the client receives the broadcasted `emit`, 


When users visit the page again, the client app will try to find the exisiting cookie 
and retrieve the username. If the client fails to do so, the user will then proceed 
as 'Guest', as if they have never changed their username.

```javascript
$(document).ready(function(){
    // set and get username via cookies on document ready
    var cookie = $.cookie("username");
    if (cookie == null) {	// cookie not found
        username = 'Guest';
    } else {
        username = cookie;
        $('input#username_data').val(username)
    }
	...
```

#### Broadcasting username

Usernames are broadcasted on user events such as:
- broadcast messages, 
- room messages, 
- joining a room, 
- leaving a room, 
- connects, 
- disconnects, 
- and username changes.

The username will be provided in a colored font on the chat logs, as shown by the code
below that prints the chat messages:

```javascript
socket.on('chat', function(msg) {
// highlight username
$('#log').append('<span class="uname">' + msg.user + 
				 '</span>: ' + msg.data + '<br>');
	...
```
The mechanism on other messages work the same, with room events also printing highlighted
room names along with the highlighted username.