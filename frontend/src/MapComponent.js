import React, { useState, useEffect } from 'react';
import { MapContainer, TileLayer, Marker, Popup, GeoJSON, LayersControl } from 'react-leaflet';
import { Card, FormControl } from 'react-bootstrap';
import 'leaflet/dist/leaflet.css';
import axios from 'axios';
import L from 'leaflet';
import { FaTimes } from 'react-icons/fa';
import FirstTimeVisitor from './FirstTimeVisitor'; // Adjust the path based on the file location

const { BaseLayer, Overlay } = LayersControl;

const pinImageUrl = 'https://upload.wikimedia.org/wikipedia/commons/d/d1/Google_Maps_pin.svg';

function MapComponent() {
  const [selectedPlace, setSelectedPlace] = useState(null);
  const [austriaGeoJson, setAustriaGeoJson] = useState(null);
  const [places, setPlaces] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [filteredPlaces, setFilteredPlaces] = useState([]);
  const [category, setCategory] = useState('');
  const [isChecked, setIsChecked] = useState(false); // Declare 'isChecked' state here.


  useEffect(() => {
    axios.get('https://ipapi.co/json/')
      .then(response => {
        const countryName = response.data.country_name;
        console.log('User Country:', countryName);
        fetchCategory(countryName.toLowerCase());
        //fetchCategory("germany");
      })
      .catch(error => console.error('Error fetching user location', error));
  }, []);

  const fetchCategory = (countryName) => {
    axios.post('http://127.0.0.1:5000/category', { user_id: countryName })
      .then(response => {
        const category = response.data.category;
        setCategory(category);
        console.log('Category:', category);
      })
      .catch(error => console.error('Error fetching category', error));
  };

  const handleCheckboxChange = () => {
    setIsChecked(prevState => !prevState); // Toggle checkbox state
  };

  useEffect(() => {
    axios.get('data.GeoJSON')
      .then(response => setAustriaGeoJson(response.data))
      .catch(error => console.error('Error loading the GeoJSON file', error));
  }, []);

  useEffect(() => {
    if (category) {
      axios.get(`http://localhost:5001/api/place?category=${category}`)
        .then(response => {
          setPlaces(response.data);
          setFilteredPlaces(response.data);
        })
        .catch(error => console.error('Error fetching places', error));
    }
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
        <FirstTimeVisitor />
      </div>
      <div>

    </div>



      <MapContainer center={[47.5162, 14.5501]} zoom={7.3} style={{ height: "100vh", width: "100%" }}>

      <LayersControl position="topright">
        <BaseLayer name="Google Streets" checked={true}>
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
                  <h6 style={{
                    margin: '10px 0',
                    fontSize: '16px',
                    fontWeight: 'bold',
                    textAlign: 'center',
                    color: '#333',  // Dark color for better contrast
                    textTransform: 'uppercase',  // To make it stand out more
                  }}>{place.name}</h6>
                  <button
                    onClick={() => handleViewDetails(place)}
                    style={{
                      alignItems: 'center', // Center-align all child elements (name and button)
                      display: 'flex',
                      justifyContent: 'center',
                      padding: '6px 12px', // Reduced padding for a smaller button
                      backgroundColor: '#007bff',
                      color: 'white',
                      border: 'none',
                      borderRadius: '4px',
                      fontSize: '10px', // Smaller font size
                      fontWeight: '600',
                      cursor: 'pointer',
                      transition: 'background-color 0.3s ease',
                      marginTop: '1 0px',  // Adds space above the button
                      width: 'auto',  // Smaller font size
   
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
            <FaTimes
              onClick={() => setSelectedPlace(null)}
              style={{
                position: 'absolute', top: '10px', right: '10px', cursor: 'pointer',
                color: '#6c757d', fontSize: '20px'
              }}
            />
            <Card.Img className='location-card-image' variant="top" src={selectedPlace.photo} alt={selectedPlace.name} />
            <Card.Body className='location-card-body'>
              <Card.Title className='location-card-title'>{selectedPlace.name}</Card.Title>
              <Card.Text className='location-card-description'>{selectedPlace.description}</Card.Text>
              {selectedPlace.opening_hours && (
                <Card.Text className='location-card-opening-hours'>
                  <strong>Opening Hours:</strong>
                  <ul>
                    {selectedPlace.opening_hours.map((hour, index) => (
                      <li key={index}>{hour}</li>
                    ))}
                  </ul>
                </Card.Text>
              )}
              {selectedPlace.user_ratings_total && (
                <Card.Text className='location-card-user-ratings'>
                  <strong>User Ratings Total:</strong> {selectedPlace.user_ratings_total}
                </Card.Text>
              )}
              {selectedPlace.price_level && (
                <Card.Text className='location-card-price-level'>
                  <strong>Price Level:</strong> {selectedPlace.price_level}
                </Card.Text>
              )}
              {selectedPlace.website && (
                <Card.Text className='location-card-website'>
                  <strong>Website:</strong> <a href={selectedPlace.website} target="_blank" rel="noopener noreferrer">{selectedPlace.website}</a>
                </Card.Text>
              )}
              {selectedPlace.phone_number && (
                <Card.Text className='location-card-phone-number'>
                  <strong>Phone Number:</strong> {selectedPlace.phone_number}
                </Card.Text>
              )}
            </Card.Body>
          </Card>
        </div>
      )}
    </div>
  );
}

export default MapComponent;
