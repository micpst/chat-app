import React from 'react';

import SearchBar from './SearchBar';
import ChannelList from './ChannelList';

const SideBar = () => {
    return (
        <div className="container-fluid col-3 h-fill d-flex flex-column border-right">
            <SearchBar />
            <ChannelList />
        </div>
    );
}

export default SideBar;
