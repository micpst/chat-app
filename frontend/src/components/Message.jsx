import React from 'react';
import { useAuth } from '../context/AuthContext';

const Message = ({ senderId, body }) => {
    const { user } = useAuth();
    return (
        <li className={`p-3 mb-2 rounded-2 ${(senderId === user.id) ? 'message-me' : 'message-you'}`}>
            {body}
        </li>
    );
}

export default Message;
