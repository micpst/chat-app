import React from 'react';

import Message from './Message';
import { useChat } from '../context/ChatContext';

const MessageList = () => {
    const { messages } = useChat();
    return (
        <ul className="h-fill-chat d-flex flex-column list-unstyled overflow-auto m-0 p-2">
            {messages.map((message, i) => <Message key={i} {...message} />)}
        </ul>
    );
}

export default MessageList;
