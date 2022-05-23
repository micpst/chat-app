import {createContext, useCallback, useContext, useEffect, useState} from 'react';

import ChatService from '../services/chat';
import { useSocket } from './SocketContext';
import { useAuth } from './AuthContext';

const ChatContext = createContext(null);

export const ChatProvider = ({ children }) => {
    const { user } = useAuth();
    const { socket } = useSocket();
    const [channels, setChannels] = useState([]);
    const [messages, setMessages] = useState([]);
    const [selectedChannelId, setSelectedChannelId] = useState(0);

    useEffect(() => {
        ChatService.getChannels()
            .then(data => setChannels([...data]))
            .catch(console.log);
    }, []);

    useEffect(() => {
        ChatService.getChannelMessages(selectedChannelId)
            .then(data => setMessages([...data]))
            .catch(console.log);
    }, [selectedChannelId]);

    useEffect(() => {
        if (socket == null) return;
        socket.on('receive', data => {
            const message = JSON.parse(data);
            setMessages([...messages, message]);
        });
        socket.on('error', console.log);
        return () => socket.off('receive');
    }, [socket, messages]);

    const sendMessage = (body) => {
        const message = { recipientId: selectedChannelId, senderId: user.id, body };
        socket.emit('send', message);
        setMessages([...messages, message])
    }

    const openChannel = channelId => {
        setSelectedChannelId(channelId);
    }

    return <ChatContext.Provider
        value={{
            channels,
            messages,
            sendMessage,
            openChannel
        }}
        children={children}
    />;
}

export const useChat = () => useContext(ChatContext);
