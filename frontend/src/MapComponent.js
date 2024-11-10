import React, { useState, useEffect } from 'react';
import { MapContainer, TileLayer, Marker, Popup, GeoJSON, LayersControl } from 'react-leaflet';
import { Card, FormControl } from 'react-bootstrap';
import 'leaflet/dist/leaflet.css';
import axios from 'axios';
import L from 'leaflet';

const { BaseLayer, Overlay } = LayersControl;

const pinImageUrl = 'https://upload.wikimedia.org/wikipedia/commons/d/d1/Google_Maps_pin.svg';

function MapComponent() {
  const [selectedPlace, setSelectedPlace] = useState(null);
  const [austriaGeoJson, setAustriaGeoJson] = useState(null);
  const [places, setPlaces] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [filteredPlaces, setFilteredPlaces] = useState([]);

  useEffect(() => {
    axios.get('https://ipapi.co/json/')
      .then(response => console.log('User Country:', response.data.country_name))
      .catch(error => console.error('Error fetching user location', error));
  }, []);

  const category = 'bar';

  useEffect(() => {
    axios.get('/geojson/austria.geojson')
      .then(response => setAustriaGeoJson(response.data))
      .catch(error => console.error('Error loading the GeoJSON file', error));
  }, []);

  useEffect(() => {
    axios.get(`http://localhost:5000/api/place?category=${category}`)
      .then(response => {
        setPlaces(response.data);
        setFilteredPlaces(response.data);
      })
      .catch(error => console.error('Error fetching places', error));
  }, [category]);

  useEffect(() => {
    setFilteredPlaces(
      places.filter(place => place.name.toLowerCase().includes(searchTerm.toLowerCase()))
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
        <LayersControl position="topright">
         
          <BaseLayer name="Google Streets">
            <TileLayer
              url="http://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}"
              maxZoom={20}
              subdomains={['mt0', 'mt1', 'mt2', 'mt3']}
            />
          </BaseLayer>
          <BaseLayer name="Satellite">
            <TileLayer
              url="http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}"
              maxZoom={20}
              subdomains={['mt0', 'mt1', 'mt2', 'mt3']}
            />
          </BaseLayer>
          

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
                    style={{
                      display: 'flex', alignItems: 'center', padding: '8px',
                      backgroundColor: '#007bff', color: 'white', border: 'none', borderRadius: '4px'
                    }}
                  >
                    View Details
                  </button>
                </div>
              </Popup>
            </Marker>
          ))}

          {austriaGeoJson && (
            <Overlay name="Austria GeoJSON">
              <GeoJSON data={austriaGeoJson} style={countryStyle} />
            </Overlay>
          )}
        </LayersControl>
      </MapContainer>

      {selectedPlace && (
        <div className="location-card">
          <Card className='location-inner-card' style={{ paddingTop: "60px", borderRadius: '4px' }}>
            <Card.Img variant="top" src={selectedPlace.photo} alt={selectedPlace.name} />
            <Card.Body>
              <Card.Title>{selectedPlace.name}</Card.Title>
              <Card.Text>{selectedPlace.description}</Card.Text>
              <button onClick={() => setSelectedPlace(null)} style={{
                padding: '6px 12px', backgroundColor: '#6c757d', color: 'white',
                border: 'none', borderRadius: '4px'
              }}>
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
