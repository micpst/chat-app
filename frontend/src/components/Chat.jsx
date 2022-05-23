import React from 'react';

import ChannelHeader from './ChannelHeader';
import MessageList from './MessageList';
import MessageInput from './MessageInput';

const Chat = () => (
    <div className="col-9 h-fill d-flex flex-column p-0">
        <ChannelHeader />
        <MessageList />
        <MessageInput />
    </div>
);

export default Chat;
