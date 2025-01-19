import React, { useState, useEffect } from 'react';
import axios from 'axios';

function VehicleManagement() {
  const [vehicles, setVehicles] = useState([]);

  useEffect(() => {
    axios
      .get('http://127.0.0.1:8000/api/vehicles/')
      .then((response) => setVehicles(response.data))
      .catch((error) => console.error('Error fetching vehicles:', error));
  }, []);

  return (
    <div>
      <h2>Vehicle Management</h2>
      <ul>
        {vehicles.map((vehicle) => (
          <li key={vehicle.id}>
            {vehicle.make} {vehicle.model} ({vehicle.year})
          </li>
        ))}
      </ul>
    </div>
  );
}

export default VehicleManagement;
