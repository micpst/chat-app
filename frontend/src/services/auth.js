import axios from 'axios';

const AUTH_SERVICE_URL = "http://localhost/api/auth";

const signup = user => axios
    .post(`${AUTH_SERVICE_URL}/signup`, user)
    .then(response => response.data);

const login = user => axios
    .post(`${AUTH_SERVICE_URL}/login`, user)
    .then(response => response.data);

const logout = () => axios
    .post(`${AUTH_SERVICE_URL}/logout`)
    .then(response => response.data);

const AuthService = {
    signup,
    login,
    logout,
}

export default AuthService;
