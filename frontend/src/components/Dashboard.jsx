import React from 'react';

import RequireAuth from '../components/RequireAuth';
import { useAuth } from '../context/AuthContext';

const Dashboard = () => {
    let auth = useAuth();

    const handleOnSubmit = e => {
        e.preventDefault();
        auth.logout();
    }

    return (
        <RequireAuth>
            <div>Chat page</div>
            <form onSubmit={handleOnSubmit}>
            <button type="submit">Logout</button>
        </form>
        </RequireAuth>
    );
}

export default Dashboard;
