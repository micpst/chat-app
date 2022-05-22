import axios from 'axios';

const AUTH_SERVICE_URL = "http://localhost/api/auth";

const signup = user => axios
    .post(`${AUTH_SERVICE_URL}/signup`, user)
    .then(response => {
        localStorage.setItem('authenticated', JSON.stringify(true));
        return response.data;
    });

const login = user => axios
    .post(`${AUTH_SERVICE_URL}/login`, user)
    .then(response => {
        localStorage.setItem('authenticated', JSON.stringify(true));
        return response.data;
    });

const logout = () => axios
    .post(`${AUTH_SERVICE_URL}/logout`)
    .then(response => {
        localStorage.setItem('authenticated', JSON.stringify(false));
        return response.data;
    });

const isAuthenticated = () => {
    return JSON.parse(localStorage.getItem('authenticated'));
};

const AuthService = {
    signup,
    login,
    logout,
    isAuthenticated,
}

export default AuthService;
