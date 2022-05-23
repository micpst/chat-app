import React from 'react';

import { useChat } from '../context/ChatContext';

const ChannelHeader = () => {
    const { channel } = useChat();
    return (
        <div className="d-flex p-3 border-bottom">
            <div className="position-relative">
                <img src="https://www.bootdey.com/img/Content/avatar/avatar3.png" className="user-avatar" alt="" />
                <span className="user-online"></span>
            </div>
            <div className="ms-3">
                <h6 className="fw-bold m-b-0">{channel.recipientName}</h6>
                <small>Last seen: 2 hours ago</small>
            </div>
        </div>
    );
}

export default ChannelHeader;
