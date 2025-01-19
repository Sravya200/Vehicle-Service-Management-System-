import React from 'react';
import { Link } from 'react-router-dom';

function Home() {
  return (
    <div>
      <h2>Welcome to Vehicle Service Management System</h2>
      <nav>
        <ul>
          <li>
            <Link to="/vehicles">Manage Vehicles</Link>
          </li>
          <li>
            <Link to="/components">Manage Components</Link>
          </li>
          <li>
            <Link to="/services">Manage Services</Link>
          </li>
        </ul>
      </nav>
    </div>
  );
}

export default Home;
