import { createContext, useContext, useEffect, useState } from 'react';
import { io } from 'socket.io-client';

const SocketContext = createContext(null);

export const SocketProvider = ({ children }) => {
     const [socket, setSocket] = useState(null)

    useEffect(() => {
        const newSocket = io(`http://localhost/`, { path: '/api/socket.io' });
        setSocket(newSocket);
        return () => newSocket.close();
    }, []);

    return <SocketContext.Provider
        value={{ socket }}
        children={children}
    />;
}

export const useSocket = () => useContext(SocketContext);
