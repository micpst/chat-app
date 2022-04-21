const socket = io();

socket.on('receive', message => {
    console.log(message);
});

socket.emit('send', { body: 'test1', recipientId: 0 });
