import axios from 'axios';

const CHAT_SERVICE_URL = "http://localhost/api/chats";

const getUserChats = () => axios
    .post(`${CHAT_SERVICE_URL}/`)
    .then(response => response.data);

const getChatMessages = userId => axios
    .post(`${CHAT_SERVICE_URL}/${userId}`)
    .then(response => response.data);

const ChatService = {
    getUserChats,
    getChatMessages,
}

export default ChatService;
