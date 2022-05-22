import React from 'react';
import { Routes, Route, Navigate } from 'react-router-dom';


import { AuthProvider } from "./context/AuthContext";
import { ChatPage, LoginPage, SignupPage } from './pages';

const App = () => (
    <AuthProvider>
        <Routes>
            <Route
                path="/"
                element={<Navigate to="/chats" replace />}
            />
            <Route
                path="/chats"
                element={<ChatPage />}
            />
            <Route
                path="/login"
                element={<LoginPage />}
            />
            <Route
                path="/signup"
                element={<SignupPage />}
            />
        </Routes>
    </AuthProvider>
);

export default App;
