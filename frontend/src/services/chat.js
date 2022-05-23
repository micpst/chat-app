import axios from 'axios';

const getChannels = () => axios
    .get(`${process.env.REACT_APP_CHATS_SERVICE_URL}`)
    .then(response => response.data);

const getChannelMessages = userId => axios
    .get(`${process.env.REACT_APP_CHATS_SERVICE_URL}/${userId}`)
    .then(response => response.data);

const ChatService = {
    getChannels,
    getChannelMessages,
}

export default ChatService;
