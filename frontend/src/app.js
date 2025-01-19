import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from './pages/Home';
import VehicleManagement from './pages/VehicleManagement';
import ComponentManagement from './pages/ComponentManagement';
import ServiceManagement from './pages/ServiceManagement';

function App() {
  return (
    <Router>
      <div>
        <h1>Vehicle Service Management System</h1>
        <Switch>
          <Route exact path="/" component={Home} />
          <Route path="/vehicles" component={VehicleManagement} />
          <Route path="/components" component={ComponentManagement} />
          <Route path="/services" component={ServiceManagement} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
