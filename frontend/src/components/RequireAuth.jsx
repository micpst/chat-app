import React from 'react';
import { Navigate, useLocation } from 'react-router-dom';

import { useAuth } from '../context/AuthContext';

function RequireAuth({ children }) {
    const auth = useAuth();
    const location = useLocation();

    if (!auth.user) {
        return <Navigate to="/login" state={{ from: location }} replace />;
    }

    return children;
}

export default RequireAuth;