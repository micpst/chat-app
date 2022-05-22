import { createContext, useContext, useEffect, useState } from 'react';

import AuthService from '../services/auth.service';

const AuthContext = createContext(null);

export const AuthProvider = ({ children }) => {
    const [authenticated, setAuthenticated] = useState(false);

    const signup = user => AuthService.signup(user)
        .then(() => setAuthenticated(true));

    const login = user => AuthService.login(user)
        .then(() => setAuthenticated(true));

    const logout = () => AuthService.logout()
        .then(() => setAuthenticated(false));

    useEffect(() => {
        setAuthenticated(AuthService.isAuthenticated());
    }, []);

    return <AuthContext.Provider value={{ authenticated, signup, login, logout }}>{children}</AuthContext.Provider>;
}

export const useAuth = () => useContext(AuthContext);
