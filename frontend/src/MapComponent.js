import React, { useState, useEffect } from 'react';
import { MapContainer, TileLayer, Marker, Popup, GeoJSON } from 'react-leaflet';
import { Card, FormControl } from 'react-bootstrap';
import 'leaflet/dist/leaflet.css';
import axios from 'axios';
import L from 'leaflet';

const pinImageUrl = 'https://upload.wikimedia.org/wikipedia/commons/d/d1/Google_Maps_pin.svg'; // Custom PIN image

function MapComponent() {
  const [selectedPlace, setSelectedPlace] = useState(null);
  const [austriaGeoJson, setAustriaGeoJson] = useState(null);
  const [places, setPlaces] = useState([]);
  const [searchTerm, setSearchTerm] = useState(''); // Search term for filtering places
  const [filteredPlaces, setFilteredPlaces] = useState([]); // Filtered places based on search term

  useEffect(() => {
    // Fetch the user's IP address and country
    axios.get('https://ipapi.co/json/')
      .then(response => {
        const userCountry = response.data.country_name;
        console.log('User Country:', userCountry);
        // You can save the country name in a state variable if needed
      })
      .catch(error => console.error('Error fetching user location', error));
  }, []);

  const category = 'bar'; // Default category

  useEffect(() => {
    // Fetch the Austria GeoJSON data
    axios.get('/geojson/austria.geojson')
      .then(response => {
        setAustriaGeoJson(response.data);
      })
      .catch(error => console.error('Error loading the GeoJSON file', error));
  }, []);

  useEffect(() => {
    // Fetch places based on the category
    axios.get(`http://localhost:5000/api/place?category=${category}`)
      .then(response => {
        setPlaces(response.data);
        setFilteredPlaces(response.data); // Initialize filtered places with all places
      })
      .catch(error => console.error('Error fetching places', error));
  }, [category]);

  useEffect(() => {
    // Filter places based on the search term
    setFilteredPlaces(
      places.filter(place =>
        place.name.toLowerCase().includes(searchTerm.toLowerCase())
      )
    );
  }, [searchTerm, places]);

  const handleViewDetails = (place) => {
    setSelectedPlace(place);
  };

  const handleSearchChange = (event) => {
    setSearchTerm(event.target.value);
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
    <div style={{ position: 'relative', height: '100vh' }}>
      {/* Search bar */}
      <div className='searchSection'>
        <FormControl
          type="text"
          placeholder="Search place..."
          value={searchTerm}
          onChange={handleSearchChange}
          className='searchBar'
        />
      </div>

      <MapContainer center={[47.5162, 14.5501]} zoom={7.3} style={{ height: "100vh", width: "100%" }}>
        <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          attribution='&copy; <a href="https://osm.org/copyright">OpenStreetMap</a> contributors'
        />
        
        {filteredPlaces.map((place) => (
          <Marker 
            key={place.name}
            position={[place.location.lat, place.location.lng]}
            icon={L.divIcon({
              className: 'leaflet-custom-icon',
              html: `<img src="${pinImageUrl}" style="width: 30px; height: 30px;"/>`
            })}
          >
            <Popup>
              <div>
                <h6>{place.name}</h6>
                <p>{place.description}</p>
                <button 
                  onClick={() => handleViewDetails(place)}
                  style={{ display: 'flex', alignItems: 'center', padding: '8px', backgroundColor: '#007bff', color: 'white', border: 'none', borderRadius: '4px' }}
                >
                  <img 
                    src={pinImageUrl}
                    alt="View Details" 
                    style={{ width: '20px', height: '20px', marginRight: '8px' }} 
                  />
                  View Details
                </button>
              </div>
            </Popup>
          </Marker>
        ))}

        {austriaGeoJson && (
          <GeoJSON
            data={austriaGeoJson}
            style={countryStyle}
          />
        )}
      </MapContainer>

      {selectedPlace && (
        <div className="location-card">
          <Card className='location-inner-card'>
            <Card.Img variant="top" src={selectedPlace.photo} alt={selectedPlace.name} />
            <Card.Body>
              <Card.Title>{selectedPlace.name}</Card.Title>
              <Card.Text>{selectedPlace.description}</Card.Text>
              <button onClick={() => setSelectedPlace(null)} style={{ padding: '6px 12px', backgroundColor: '#6c757d', color: 'white', border: 'none', borderRadius: '4px' }}>
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
