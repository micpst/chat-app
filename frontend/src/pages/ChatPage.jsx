import React from 'react';

import RequireAuth from '../components/RequireAuth';

const ChatPage = () => (
    <RequireAuth>
        <div>Chat page</div>
    </RequireAuth>
);

export default ChatPage;
