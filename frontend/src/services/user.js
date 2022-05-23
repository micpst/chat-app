import axios from 'axios';

const getUsers = () => axios
    .get(`${process.env.REACT_APP_USERS_SERVICE_URL}`)
    .then(response => response.data);

const getUser = userId => axios
    .get(`${process.env.REACT_APP_USERS_SERVICE_URL}/${userId}`)
    .then(response => response.data);

const getCurrentUser = () => axios
    .get(`${process.env.REACT_APP_USERS_SERVICE_URL}/me`)
    .then(response => response.data);

const UserService = {
    getUsers,
    getUser,
    getCurrentUser,
}

export default UserService;
