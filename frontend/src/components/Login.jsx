import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';

import { useAuth } from '../context/AuthContext';
import logo from '../img/logo.svg';

const Login = () => {
    const auth = useAuth();
    const navigate = useNavigate();

    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const onChangeEmail = e => setEmail(e.target.value);
    const onChangePassword = e => setPassword(e.target.value);

    const handleOnSubmit = e => {
        e.preventDefault();
        auth.login({ email, password })
            .then(() => navigate('/chats', { replace: true }))
            .catch(err => {
                setEmail('');
                setPassword('');
            });
    }

    return (
        <div className="container mw-330 vh-100 text-center">
            <img className="my-6" src={logo} alt="" width="70" height="70" />
            <form onSubmit={handleOnSubmit}>
                <div className="form-floating mb-3">
                    <input
                        type="text"
                        name="email"
                        value={email}
                        onChange={onChangeEmail}
                        className="form-control"
                        placeholder="Email"
                    />
                    <label>Email</label>
                </div>
                <div className="form-floating mb-3">
                    <input
                        type="password"
                        name="password"
                        value={password}
                        onChange={onChangePassword}
                        className="form-control"
                        placeholder="Password"
                    />
                    <label>Password</label>
                </div>
                <button type="submit" className="w-100 btn btn-lg btn-primary mb-5">Log In</button>
            </form>
            <Link to="/signup" className="w-100 btn btn-lg btn-success" role="button">Create new account</Link>
            <p className="mt-5 text-muted">Michał Pstrąg &copy; 2022</p>
        </div>
    );
};

export default Login;
