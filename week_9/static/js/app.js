$(document).ready(function(){
	
	// set and get username via cookies
	var cookie = $.cookie("username");
	if (cookie == null) {
		username = 'Guest';
	} else {
		username = cookie;
		$('input#username_data').val(username)
	}
		        
    namespace = '/test'; // change to an empty string to use the global namespace

    // the socket.io documentation recommends sending an explicit package upon connection
    // this is specially important when using the global namespace
    var socket = io.connect('http://' + document.domain + ':' + location.port + namespace);
    
    // event handler for new connections
    socket.on('connect', function(msg) {
        socket.emit('my connect event', {
	        data: 'Connected to chat.',
	        user: username});
    });
    
    // event handler for server sent data
    // the data is displayed in the '#log' section of the page
    
    socket.on('my response', function(msg) {
        $('#log').append(msg.data + '<br>');
        $('#log').scrollTop($('#log').prop('scrollHeight'));
    });

    socket.on('chat', function(msg) {
        $('#log').append('<span class="uname">' + msg.user + 
            '</span>: ' + msg.data + '<br>');
            $('#log').scrollTop($('#log').prop('scrollHeight'));
    });
    
    socket.on('room chat', function(msg) {
        $('#log').append(
        '<span class="uname">' + msg.user + ' ' + 
        '[' + msg.room + ']</span>: ' + msg.data + '<br>');
            $('#log').scrollTop($('#log').prop('scrollHeight'));
    });

    socket.on('change username', function(msg) {
        var msg_log = '<span class="uname">' + msg.old_name + '</span>' +
                    ' has changed its name into ' +
                    '<span class="uname">' + msg.new_name + '</span>!<br>';
        $('#log').append(msg_log);
        $('#log').scrollTop($('#log').prop('scrollHeight'));
    });
    
    socket.on('join', function(msg) {
        var msg_log = '<span class="uname">' + msg.user + '</span>' +
                    ' has joined the room ' +
                    '<span class="uname">[' + msg.room + ']</span>!<br>';
        $('#log').append(msg_log);
        $('#log').scrollTop($('#log').prop('scrollHeight'));
    });

    socket.on('leave', function(msg) {
        var msg_log = '<span class="uname">' + msg.user + '</span>' +
                    ' has left the room ' +
                    '<span class="uname">[' + msg.room + ']</span>.<br>';
        $('#log').append(msg_log);
        $('#log').scrollTop($('#log').prop('scrollHeight'));
    });

    socket.on('close', function(msg) {
        var msg_log = '<span class="uname">' + msg.user + '</span>' +
                    ' is closing the room ' +
                    '<span class="uname">[' + msg.room + ']</span>.<br>';
        $('#log').append(msg_log);
        $('#log').scrollTop($('#log').prop('scrollHeight'));
    });
    
    socket.on('connect notification', function(msg) {
        var msg_log = '<span class="uname">' + msg.user + '</span>' +
                    ' is online!<br>';
        $('#log').append(msg_log);
        $('#log').scrollTop($('#log').prop('scrollHeight'));
    });
    
    socket.on('disconnect notification', function(msg) {
        var msg_log = '<span class="uname">' + msg.user + '</span>' +
                    ' disconnected from chat.<br>';
        $('#log').append(msg_log);
        $('#log').scrollTop($('#log').prop('scrollHeight'));
    });

    // handlers for the different forms in the page
    // these send data to the server in a variety of ways
    $('form#username').submit(function(event) {
        var new_name = $('input#username_data').val();
        if (new_name.length == 0 || new_name == username) {
	        return false;
        }
        socket.emit('change username', {
            old_name: username, 
            new_name: new_name
        });
        username = new_name;
        $.cookie("username", username)
        return false;
    });
    $('form#broadcast').submit(function(event) {
        var value = $('#broadcast_data').val();
        if (value.length == 0 || value == "Send message..") {
	        return false;
        }
        socket.emit('my broadcast event', {
            data: $('#broadcast_data').val(),
            user: username
        });
        $('#broadcast_data').val('');
        return false;
    });
    $('form#send_room').submit(function(event) {
        var roomval = $('#room_name').val();
        var msgval = $('#room_data').val();
        if (roomval.length == 0 || msgval.length == 0 || 
        	msgval == "Send message..") {
	        return false;
        }
        socket.emit('my room event', {
            room: $('#room_name').val(),
            data: $('#room_data').val(), 
            user: username
        });
        $('#room_data').val('');
        return false;
    });
    $('form#join').submit(function(event) {
        socket.emit('join', {
            room: $('#join_room').val(),
            user: username
        });
        return false;
    });
    $('form#leave').submit(function(event) {
        socket.emit('leave', {
            room: $('#leave_room').val(),
            user: username
        });
        return false;
    });
    $('form#close').submit(function(event) {
        socket.emit('close', {
            room: $('#close_room').val(),
            user: username
        });
        return false;
    });
    $('form#disconnect').submit(function(event) {
        socket.emit('disconnect request', {user: username});
        return false;
    });
    
    // enter to send
    $('#broadcast_data').keypress(function(event) {
        if (event.which == 13) {
	        event.preventDefault();
	        $('form#broadcast').submit();
        }
    });
    $('#room_data').keypress(function(event) {
        if (event.which == 13) {
	        event.preventDefault();
	        $('form#send_room').submit();
        }
    });
    
    // mousedown-mouseup button effects
    $('input[type="submit"]').mousedown(function() {
	    $(this).toggleClass('.button')
	    $(this).toggleClass('.button-clicked')
    });
    
    $('input[type="submit"]').mouseup(function() {
	    $(this).toggleClass('.button')
	    $(this).toggleClass('.button-clicked')
    });
    
    $('.dialogBoxButtons span').mousedown(function() {
	    $(this).toggleClass('.button-span')
	    $(this).toggleClass('.button-span-clicked')
    });
    
    $('.dialogBoxButtons span').mouseup(function() {
	    $(this).toggleClass('.button-span')
	    $(this).toggleClass('.button-span-clicked')
    });
    
    // js for easytabs
    $('#tab-container').easytabs({animate: false});
    
    // draggable
    $('#overlay').draggable({containment: "parent", cancel: "#windowwrap"});
});