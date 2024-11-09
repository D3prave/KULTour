import React, { useState, useEffect } from 'react';
import { MapContainer, TileLayer, Marker, Popup, Circle, GeoJSON } from 'react-leaflet';
import { Card } from 'react-bootstrap';
import 'leaflet/dist/leaflet.css';
import axios from 'axios';

const cities = [
  { 
    name: 'Vienna', 
    coordinates: [48.2082, 16.3738], 
    description: 'Capital of Austria, known for its artistic and cultural heritage.',
    imageUrl: 'https://upload.wikimedia.org/wikipedia/commons/1/18/Vienna_-_view_from_Karlskirche.jpg'
  },
  { 
    name: 'Salzburg', 
    coordinates: [47.8095, 13.0550], 
    description: 'Famous for being Mozart’s birthplace and its baroque architecture.',
    imageUrl: 'https://upload.wikimedia.org/wikipedia/commons/9/9b/Salzburg_-_Hohensalzburg_Castle.jpg'
  },
  { 
    name: 'Innsbruck', 
    coordinates: [47.2692, 11.4041], 
    description: 'Known for its ski resorts and winter sports.',
    imageUrl: 'https://upload.wikimedia.org/wikipedia/commons/e/e4/Alpenpanorama_bei_Innsbruck.jpg'
  },
];

function MapComponent() {
  const [selectedCity, setSelectedCity] = useState(null);
  const [austriaGeoJson, setAustriaGeoJson] = useState(null);

  useEffect(() => {
    // Fetch the Austria GeoJSON data
    axios.get('https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/austria.geojson')
      .then(response => {
        setAustriaGeoJson(response.data);
      })
      .catch(error => console.error('Error loading the GeoJSON file', error));
  }, []);

  const handleMarkerClick = (city) => {
    setSelectedCity(city);
  };

  return (
    <div style={{ position: 'relative', height: '100vh' }}>
      {/* Map container */}
      <MapContainer center={[47.5162, 14.5501]} zoom={7.3} style={{ height: "100%", width: "100%" }}>
        <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          attribution='&copy; <a href="https://osm.org/copyright">OpenStreetMap</a> contributors'
        />
        {cities.map((city, index) => (
          <React.Fragment key={index}>
            {/* Marker for the city */}
            <Marker
              position={city.coordinates}
              eventHandlers={{
                click: () => handleMarkerClick(city),
              }}
            >
              <Popup>{city.name}</Popup>
            </Marker>

            {/* Purple circle around the city */}
            <Circle 
              center={city.coordinates} 
              radius={20000} 
              color="purple"
              fillColor="purple"
              fillOpacity={0.2}
            />
          </React.Fragment>
        ))}

        {/* GeoJSON for Austria border with red outline */}
        {austriaGeoJson && (
          <GeoJSON
            data={austriaGeoJson}
            style={{
              color: 'red',
              weight: 3,
              opacity: 1,
            }}
          />
        )}
      </MapContainer>

      {/* Card component with smooth rounded corners, overlaying the map */}
      {selectedCity && (
        <div className="city-card" style={{
          position: 'absolute',
          top: '10%',  // You can adjust this to control vertical positioning
          right: '5%',  // Positions the card 5% from the right side
          zIndex: 1000,
          width: '18rem',
          paddingLeft: '20px'
        }}>
          <Card style={{ borderRadius: '15px', backgroundColor: "white", paddingLeft:"10px",  paddingRight:"10px"}}>
            <Card.Img variant="top" src={selectedCity.imageUrl} alt={selectedCity.name} />
            <Card.Body>
              <Card.Title>{selectedCity.name}</Card.Title>
              <Card.Text>{selectedCity.description}</Card.Text>
            </Card.Body>
          </Card>
        </div>
      )}
    </div>
  );
}

export default MapComponent;
