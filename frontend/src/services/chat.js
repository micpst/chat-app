import axios from 'axios';

const CHAT_SERVICE_URL = "http://localhost/api/chats";

const getChannels = () => axios
    .get(`${CHAT_SERVICE_URL}`)
    .then(response => response.data);

const getChannelMessages = userId => axios
    .get(`${CHAT_SERVICE_URL}/${userId}`)
    .then(response => response.data);

const ChatService = {
    getChannels,
    getChannelMessages,
}

export default ChatService;
