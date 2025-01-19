import React, { useState, useEffect } from 'react';
import axios from 'axios';

function ComponentManagement() {
  const [components, setComponents] = useState([]);

  useEffect(() => {
    axios
      .get('http://127.0.0.1:8000/api/components/')
      .then((response) => setComponents(response.data))
      .catch((error) => console.error('Error fetching components:', error));
  }, []);

  return (
    <div>
      <h2>Component Management</h2>
      <ul>
        {components.map((component) => (
          <li key={component.id}>
            {component.name} - ${component.price} - Stock: {component.stock_quantity}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ComponentManagement;
