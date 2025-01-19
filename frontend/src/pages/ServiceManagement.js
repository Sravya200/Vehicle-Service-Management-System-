import React, { useState, useEffect } from 'react';
import axios from 'axios';

function ServiceManagement() {
  const [services, setServices] = useState([]);

  useEffect(() => {
    axios
      .get('http://127.0.0.1:8000/api/services/')
      .then((response) => setServices(response.data))
      .catch((error) => console.error('Error fetching services:', error));
  }, []);

  return (
    <div>
      <h2>Service Management</h2>
      <ul>
        {services.map((service) => (
          <li key={service.id}>
            {service.name} - Labor Cost: ${service.labor_cost}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ServiceManagement;
