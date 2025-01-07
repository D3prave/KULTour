// server.js
const express = require('express');
const axios = require('axios');
const cors = require('cors');
require('dotenv').config();

const app = express();
app.use(cors());

app.get('/api/place', async (req, res) => {
  const { category } = req.query;

  try {
    const response = await axios.get(`https://maps.googleapis.com/maps/api/place/textsearch/json`, {
      params: {
        query: category,
        key: process.env.GOOGLE_API_KEY,
        location: '47.5162,14.5501',  // Center of Austria
        radius: 50000  // 50 km radius to cover the whole Austria
      }
    });

    const filteredPlaces = response.data.results.filter(place => place.rating > 4 && place.formatted_address.includes('Austria'));

    const places = filteredPlaces.map(place => ({
      name: place.name,
      location: place.geometry.location,
      photo: place.photos ? `https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=${place.photos[0].photo_reference}&key=${process.env.GOOGLE_API_KEY}` : null,
      rating: place.rating,
      description: place.formatted_address,
      opening_hours: place.opening_hours ? place.opening_hours.weekday_text : null,
      user_ratings_total: place.user_ratings_total,
      price_level: place.price_level,
      website: place.website,
      phone_number: place.formatted_phone_number
    }));

    if (places.length > 0) {
      res.json(places);
    } else {
      res.status(404).json({ error: `No places found with rating above 4` });
    }
  } catch (error) {
    console.error('Error fetching data from Google Places API:', error);
    res.status(500).json({ error: 'Error fetching place details' });
  }
});

const PORT = 5001;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
