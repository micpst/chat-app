import React from 'react';

import { SocketProvider } from "../context/SocketContext";
import { ChatProvider } from "../context/ChatContext";
import Header from './Header';
import SideBar from './SideBar';
import Chat from './Chat';

const Dashboard = () => (
    <SocketProvider>
        <ChatProvider>
            <div className="row vh-100 mx-1">
                <Header />
                <SideBar />
                <Chat />
            </div>
        </ChatProvider>
    </SocketProvider>
);

export default Dashboard;
