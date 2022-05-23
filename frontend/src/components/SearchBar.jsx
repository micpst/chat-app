import React from 'react';

import UserService from '../services/user';

const SearchBar = () => {
    return (
        <div className="d-flex align-items-center my-2">
            <input type="search" className="form-control" placeholder="Search" aria-label="Search"/>
        </div>
    );
}

export default SearchBar;
