import React from 'react';

import { useChat } from '../context/ChatContext';

const Channel = ({ recipientId, recipientName, senderName, body, createdAt }) => {
    const { openChannel } = useChat();

    const onClick = e => {
        openChannel(recipientId);
    }

    return (
        <li className="d-flex justify-content-center align-items-center flex-md-row flex-column list-group-item list-group-item-action p-3 border-0"
            role="button"
            onClick={onClick}
        >
            <div className="position-relative">
                <img src="https://www.bootdey.com/img/Content/avatar/avatar3.png" className="user-avatar" alt="" />
                <span className="user-online" />
            </div>
            <div className="w-100 ms-3 text-truncate d-none d-md-block">
                <div>
                    <span className="fs-6 fw-bold">{recipientName}</span>
                </div>
                <div className="d-flex justify-content-between">
                    <small className="text-muted text-truncate">{senderName}: {body}</small>
                    <small className="text-muted">
                        {new Date(createdAt).toLocaleTimeString(undefined, { hour: '2-digit', minute:'2-digit' })}
                    </small>
                </div>
            </div>
            <div className="mt-2 d-md-none text-center fs-7 fw-bold">
                {recipientName}
            </div>
        </li>
    );
}

export default Channel;
