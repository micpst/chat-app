import React from 'react';

import { useChat } from '../context/ChatContext';
import ChannelHeader from './ChannelHeader';
import MessageList from './MessageList';
import MessageInput from './MessageInput';

const Chat = () => {
    const { channel } = useChat();
    return (
        <div className="col-9 h-fill d-flex flex-column p-0">
            {channel && (
                <>
                    <ChannelHeader />
                    <MessageList />
                    <MessageInput />
                </>
            )}
        </div>
    );
}

export default Chat;
