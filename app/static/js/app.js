const socket = io();

const $ = selector => document.querySelector(selector);

// const $messageForm = document.querySelector('#message-form');
// const $messageFormInput = $messageForm.querySelector('input');
// const $messageFormButton = $messageForm.querySelector('button');
// const $sendLocationButton = document.querySelector('#send-location');
// const $messages = document.querySelector('#messages');
//
// //Templates:
// const messageTemplate = document.querySelector('#message-template').innerHTML;
// const locationTemplate = document.querySelector('#location-template').innerHTML;
// const sidebarTemplate = document.querySelector('#sidebar-template').innerHTML;


const autoscroll = () => {
    // New message element:
    const $newMessage = $messages.lastElementChild;

    // Height of the message:
    const newMessageStyles = getComputedStyle($newMessage);
    const newMessageMargin = parseInt(newMessageStyles.marginBottom);
    const newMessageHeight = $newMessage.offsetHeight + newMessageMargin;

    //Visible height:
    const visibleHeight = $messages.offsetHeight;

    //Height of messages container:
    const containerHeight = $messages.scrollHeight;

    //How far have I scorlled:
    const scrollOffset = $messages.scrollTop + visibleHeight;

    if (containerHeight - newMessageHeight <= scrollOffset) {
        $messages.scrollTop = $messages.scrollHeight;
    }
};

const getUsers = async () => {
    const response = await fetch('/api/users');
    return await response.json();
}

const getChats = async () => {
    const response = await fetch('/api/users/me/chats');
    return await response.json();
}

const getChatMessages = async chatId => {
    const response = await fetch(`/api/users/me/chats/${chatId}/messages`);
    return await response.json();
}

const serachUsers = e => {

}

$('#user-search-input').addEventListener('input', e => {
    console.log(e)
});

socket.on('receive', message => {
    console.log(message);

    // const html = Mustache.render(messageTemplate, {
    //     user: message.user,
    //     message: message.text,
    //     createdAt: moment(message.createdAt).format('HH:mm')
    // });
    // $messages.insertAdjacentHTML('beforeend', html);
    // autoscroll();
});


socket.on('error', message => {
    console.log(message);

});
socket.emit('send', { body: 'test1', recipientId: 1 });

// $messageForm.addEventListener('submit', e => {
//     e.preventDefault();
//
//     $messageFormButton.setAttribute('disabled', 'disabled');
//
//     const message = e.target.elements.message.value;
//     socket.emit('send', message, (status) => {
//         // $messageFormButton.removeAttribute('disabled');
//         // $messageFormInput.value = '';
//         // $messageFormInput.focus();
//         console.log(status);
//     });
// });

window.addEventListener('DOMContentLoaded', async e => {
    getChatMessages(2)
    const chats = await getChats();
    console.log(chats);
});