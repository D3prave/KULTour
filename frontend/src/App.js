import React from 'react';
import MapComponent from './MapComponent';  // Import your MapComponent
import './App.css';  // Import the CSS file

function App() {
  return (
    <div className="App">
      {/* Hero Section with Background Image */}
      <div className="hero">
        <div>
          <h1>Explore a Variaty of Activities</h1>
          <h2>stuff</h2>
        </div>
      </div>

      {/* Map Section */}
      <div style={{ padding: '20px' }}>
        <h2>Discover New Stuffs</h2>
        <MapComponent /> {/* Render the MapComponent here */}
      </div>
    </div>
  );
}

export default App;
