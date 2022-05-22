import React from 'react';
import { Navigate, useLocation } from 'react-router-dom';

import { useAuth } from "../context/AuthContext";

function RequireAuth({ children }) {
    let auth = useAuth();
    let location = useLocation();
    
    if (!auth.authenticated) {
        return <Navigate to="/login" state={{ from: location }} replace />;
    }

    return children;
}

export default RequireAuth;