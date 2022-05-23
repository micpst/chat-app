import axios from 'axios';

const USER_SERVICE_URL = "http://localhost/api/users";

const getUsers = () => axios
    .get(`${USER_SERVICE_URL}`)
    .then(response => response.data);

const getUser = userId => axios
    .get(`${USER_SERVICE_URL}/${userId}`)
    .then(response => response.data);

const getCurrentUser = () => axios
    .get(`${USER_SERVICE_URL}/me`)
    .then(response => response.data);

const UserService = {
    getUsers,
    getUser,
    getCurrentUser,
}

export default UserService;
