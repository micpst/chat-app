import axios from 'axios';

const AUTH_SERVICE_URL = "http://localhost/api/auth";

const signup = user => axios
    .post(`${AUTH_SERVICE_URL}/signup`, user)
    .then(response => console.log(response))
    .catch(error => console.log(error));

const login = user => axios
    .post(`${AUTH_SERVICE_URL}/login`, user)
    .then(response => console.log(response))
    .catch(error => console.log(error));

const logout = () => axios
    .post(`${AUTH_SERVICE_URL}/login`, user)
    .then(response => console.log(response))
    .catch(error => console.log(error));

const getCurrentUser = () => {
    return JSON.parse(localStorage.getItem("user"));
};

const AuthService = {
    signup,
    login,
    logout,
    getCurrentUser,
}

export default AuthService;
