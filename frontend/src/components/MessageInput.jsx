import React, { useState } from 'react';

import { useChat } from '../context/ChatContext';

const MessageInput = () => {
    const [message, setMessage] = useState('');
    const { sendMessage } = useChat();

    const onChangeMessage = e => {
        setMessage(e.target.value.replace(/\n|\r/g, ''));
    }

    const onKeyDown = e => {
        if (e.key === 'Enter') {
            sendMessage(message);
            setMessage('');
        }
    }

    return (
        <div className="p-2 border-top">
        <textarea
            name="message-input"
            className="form-control message-textarea"
            placeholder="Type your message..."
            value={message}
            onChange={onChangeMessage}
            onKeyDown={onKeyDown}
        />
        </div>
    );
}

export default MessageInput;
