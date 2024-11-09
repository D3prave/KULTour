// src/App.js
import React from 'react';
import MapComponent from './maps.js';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  return (
    <div className="App">

      <h1>Sights to see</h1>

      <MapComponent />
    </div>
  );
}

export default App;
