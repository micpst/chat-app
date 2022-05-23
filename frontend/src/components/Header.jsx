import React from 'react';

import { useAuth } from '../context/AuthContext';

const Header = () => {
    const auth = useAuth();
    return (
        <div className="col-12 d-flex justify-content-between align-items-center py-2 border-bottom">
            <h1 className="m-0">Chats</h1>
            <button onClick={() => auth.logout()} className="btn btn-outline-secondary">Logout</button>
        </div>
    );
}

export default Header;
