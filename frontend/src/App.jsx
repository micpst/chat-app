import React from 'react';
import { Routes, Route, Navigate } from 'react-router-dom';

import 'bootstrap/dist/css/bootstrap.min.css';
import { AuthProvider } from "./context/AuthContext";
import { Dashboard, Login, Signup } from './components';
import RequireAuth from './components/RequireAuth';

const App = () => (
    <AuthProvider>
        <Routes>
            <Route
                path="/"
                element={<Navigate to="/chats" replace />}
            />
            <Route
                path="/chats"
                element={<RequireAuth children={<Dashboard />} />}
            />
            <Route
                path="/login"
                element={<Login />}
            />
            <Route
                path="/signup"
                element={<Signup />}
            />
        </Routes>
    </AuthProvider>
);

export default App;
