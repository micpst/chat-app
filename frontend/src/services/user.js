import axios from 'axios';

const USER_SERVICE_URL = "http://localhost/api/users";

const getUsers = () => axios
    .post(`${USER_SERVICE_URL}/`)
    .then(response => response.data);

const getUser = userId => axios
    .post(`${USER_SERVICE_URL}/${userId}`)
    .then(response => response.data);

const UserService = {
    getUsers,
    getUser,
}

export default UserService;
