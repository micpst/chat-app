import React from 'react';

import Channel from './Channel';
import { useChat } from '../context/ChatContext';

const ChannelList = () => {
    const { channels } = useChat();
    return (
        <ul className="m-0 p-0 overflow-auto">
            {channels.map((channel, i) => <Channel key={i} {...channel} />)}
        </ul>
    );
}

export default ChannelList;
