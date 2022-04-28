let chats = [];
let messages = [];

const $ = selector => document.querySelector(selector);
const chatTemplate = $('#chat-template').innerHTML;

const socket = io();

socket.on('receive', message => {
    console.log(message);
});

socket.on('error', message => {
    console.log(message);
});

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

window.addEventListener('DOMContentLoaded', async e => {
    chats = await getChats();
    if (chats.length) {
        chats.forEach(({ recipientName, senderName, body, createdAt }) => {
            const html = Mustache.render(chatTemplate,{
                recipientName,
                senderName,
                body,
                createdAt: moment(createdAt).format('HH:mm')
            });
            $('#chats').insertAdjacentHTML('beforeend', html);
        });
    }
});
