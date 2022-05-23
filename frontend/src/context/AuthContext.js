import { createContext, useContext, useEffect, useState } from 'react';
import {useLocation, useNavigate} from 'react-router-dom';

import AuthService from '../services/auth';
import UserService from '../services/user';

const AuthContext = createContext(null);

export const AuthProvider = ({ children }) => {
    const [user, setUser] = useState(null);
    const navigate = useNavigate();
    const location = useLocation();

    const signup = user => AuthService.signup(user);
    const login = user => AuthService.login(user);
    const logout = () => AuthService.logout();

    useEffect(() => {
        UserService.getCurrentUser()
            .then(user => {
                setUser(user);
                const origin = location.state?.from?.pathname || '/chats';
                navigate(origin);
            })
            .catch(err => setUser(null));

    }, [signup, login, logout]);

    return <AuthContext.Provider
        value={{ user, signup, login, logout }}
        children={children}
    />;
}

export const useAuth = () => useContext(AuthContext);
