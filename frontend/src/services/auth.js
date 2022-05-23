import axios from 'axios';

const signup = user => axios
    .post(`${process.env.REACT_APP_AUTH_SERVICE_URL}/signup`, user)
    .then(response => response.data);

const login = user => axios
    .post(`${process.env.REACT_APP_AUTH_SERVICE_URL}/login`, user)
    .then(response => response.data);

const logout = () => axios
    .post(`${process.env.REACT_APP_AUTH_SERVICE_URL}/logout`)
    .then(response => response.data);

const AuthService = {
    signup,
    login,
    logout,
}

export default AuthService;
