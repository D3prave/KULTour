import React, { useState, useEffect } from 'react';
import { MapContainer, TileLayer, Marker, Popup, Circle, GeoJSON } from 'react-leaflet';
import { Card } from 'react-bootstrap';
import 'leaflet/dist/leaflet.css';
import axios from 'axios';
import L from 'leaflet';  // Import Leaflet to use L.divIcon for custom markers

// City data
const cities = [
  { 
    name: 'Vienna', 
    coordinates: [48.2082, 16.3738], 
    description: 'Capital of Austria, known for its artistic and cultural heritage.',
    imageUrl: 'https://upload.wikimedia.org/wikipedia/commons/d/d1/Google_Maps_pin.svg' // Custom image for button
  },
  { 
    name: 'Salzburg', 
    coordinates: [47.8095, 13.0550], 
    description: 'Famous for being Mozart’s birthplace and its baroque architecture.',
    imageUrl: 'https://upload.wikimedia.org/wikipedia/commons/d/d1/Google_Maps_pin.svg' // Custom image for button
  },
  { 
    name: 'Innsbruck', 
    coordinates: [47.2692, 11.4041], 
    description: 'Known for its ski resorts and winter sports.',
    imageUrl: 'https://upload.wikimedia.org/wikipedia/commons/d/d1/Google_Maps_pin.svg' // Custom image for button
  },
];

function MapComponent() {
  const [selectedCity, setSelectedCity] = useState(null);
  const [austriaGeoJson, setAustriaGeoJson] = useState(null);

  useEffect(() => {
    // Fetch the Austria GeoJSON data
    axios.get('/geojson/austria.geojson')
      .then(response => {
        setAustriaGeoJson(response.data);
      })
      .catch(error => console.error('Error loading the GeoJSON file', error));
  }, []);

  const handleViewDetails = (city) => {
    setSelectedCity(city);
  };

  const getColor = (population) => {
    if (population > 100000000) return 'darkred';
    else if (population > 50000000) return 'orange';
    else if (population > 10000000) return 'yellow';
    return 'lightgreen';
  };

  const countryStyle = (feature) => {
    const population = feature.properties?.population || 0;
    const color = getColor(population);

    return {
      color: 'black',
      weight: 3,
      opacity: 1,
      fillOpacity: 0.5,
      fillColor: color,
    };
  };

  return (
    <div style={{ display: 'flex', position: 'relative', height: '500px' }}>
      <MapContainer center={[47.5162, 14.5501]} zoom={7.3} style={{ height: "100vh", width: "100%" }}>
        <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          attribution='&copy; <a href="https://osm.org/copyright">OpenStreetMap</a> contributors'
        />
        
        {cities.map((city) => (
          <React.Fragment key={city.name}>
            <Marker 
              position={city.coordinates}
              icon={L.divIcon({
                className: 'leaflet-custom-icon',  // You can use this class to style the image
                html: `<img src="${city.imageUrl}" style="width: 30px; height: 30px;"/>` // Custom marker icon as image
              })}
            >
              <Popup>
                <div>
                  <h6>{city.name}</h6>
                  <p>{city.description}</p>
                  <button 
                    onClick={() => handleViewDetails(city)}
                    style={{ display: 'flex', alignItems: 'center', padding: '8px', backgroundColor: '#007bff', color: 'white', border: 'none', borderRadius: '4px' }}
                  >
                    <img 
                      src={city.imageUrl}  // Use the image URL from city data
                      alt="View Details" 
                      style={{ width: '20px', height: '20px', marginRight: '8px' }} 
                    />
                    View Details
                  </button>
                </div>
              </Popup>
            </Marker>

            <div className="circle-container" style={{ position: 'absolute', left: '50%', top: '50%', transform: 'translate(-50%, -50%)' }}>
              
              <button 
                onClick={() => handleViewDetails(city)} 
                style={{
                  position: 'absolute',
                  top: '50%',
                  left: '50%',
                  transform: 'translate(-50%, -50%)',
                  padding: '8px 16px',
                  backgroundColor: '#007bff',
                  color: 'white',
                  border: 'none',
                  borderRadius: '4px',
                  zIndex: 10,
                }}
              >
                View Details
              </button>
            </div>
          </React.Fragment>
        ))}

        {austriaGeoJson && (
          <GeoJSON
            data={austriaGeoJson}
            style={countryStyle}
          />
        )}
      </MapContainer>

      {selectedCity && (
        <div className="city-card" style={{ paddingLeft: '20px' }}>
          <Card style={{ width: '18rem' }}>
            <Card.Img variant="top" src={selectedCity.imageUrl} alt={selectedCity.name} />
            <Card.Body>
              <Card.Title>{selectedCity.name}</Card.Title>
              <Card.Text>{selectedCity.description}</Card.Text>
              <button onClick={() => setSelectedCity(null)} style={{ padding: '6px 12px', backgroundColor: '#6c757d', color: 'white', border: 'none', borderRadius: '4px' }}>
                Close
              </button>
            </Card.Body>
          </Card>
        </div>
      )}
    </div>
  );
}

export default MapComponent;
