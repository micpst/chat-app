import { createContext, useContext, useEffect, useState } from 'react';
import AuthService from '../services/auth.service';

const AuthContext = createContext(null);

export const AuthProvider = ({ children }) => {
    let [user, setUser] = useState(null);

    let login = (newUser, callback) => {
        return AuthService.login(() => {
            setUser(newUser);
            callback();
        });
    };

    let logout = callback => {
        return AuthService.logout(() => {
            setUser(null);
            callback();
        });
    };

    let signup = callback => {
        return AuthService.signup(() => {
            setUser(null);
            callback();
        });
    };

    useEffect(() => auth
        .loadUser()
        .then(({ user }) => setUser(user))
        .catch(err => setUser(null))
    , []);

    return <AuthContext.Provider value={{ user, login, logout, signup }}>{children}</AuthContext.Provider>;
}

export const useAuth = () => useContext(AuthContext);
