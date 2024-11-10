# Frontend ReadMe - MapComponent for Tourism Personalization

## Overview

Welcome to the frontend component of our Tourism Personalization project. This initiative aims to enhance the experience of tourists by providing personalized location recommendations based on the user's country. 

To achieve this, the frontend leverages React and Leaflet to display an interactive map of Austria, populated with recommended places tailored to each visitor's preferences.


## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Components](#components)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [API Endpoints](#api-endpoints)
- [Contributors](#contributors)

## Installation
To set up the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/tourism-personalization.git
.... 

## Usage
Here's how to use the MapComponent:

1. **Run the Application**: Start the React application using the steps mentioned above.
2. **Interactive Map**: Explore the interactive map of Austria, which displays recommended places based on the user's location.
3. **Search Functionality**: Use the search bar to filter places by name.
4. **View Details**: Click on a marker to view detailed information about the place.

## Components

### MapComponent
This is the main component that renders the map and handles user interactions.

- **State Management**: Manages the state of selected place, GeoJSON data, places, search term, filtered places, and category using `useState`.
- **Effect Hooks**: Fetches user location, category, GeoJSON data, and places based on the category using `useEffect`.
- **Map and Layers**: Uses `react-leaflet` components like `MapContainer`, `TileLayer`, `Marker`, `Popup`, `GeoJSON`, and `LayersControl` to display the map and layers.
- **Search Functionality**: Filters places based on the search term entered by the user.

## Features
- **User Location Detection**: Fetches the user's country based on their IP address.
- **Category Fetching**: Determines the category of recommendations based on the user's country.
- **GeoJSON Layer**: Loads and displays the GeoJSON data for Austria.
- **Search and Filter**: Allows users to search for places by name.
- **Detailed Information**: Displays detailed information about each place in a popup and a detailed card.

## Technologies Used
- **React**: A JavaScript library for building user interfaces.
- **React-Leaflet**: A React wrapper for Leaflet, a leading open-source JavaScript library for mobile-friendly interactive maps.
- **Axios**: A promise-based HTTP client for the browser and Node.js.
- **Bootstrap**: A popular CSS framework for developing responsive and mobile-first websites.
- **Font Awesome**: A toolkit for vector icons and social logos.

## API Endpoints
- **GET `https://ipapi.co/json/`**: Fetches the user's location based on their IP address.
- **POST `http://127.0.0.1:5000/category`**: Fetches the recommended category based on the user's country.
- **GET `http://localhost:5001/api/place?category={category}`**: Fetches places based on the recommended category.

## Contributors
- **Eternals** - GitHub_Repository: `https://github.com/denishotii/TourismTechnologyFestival`

- **Southik Nath Banerjee** - GitHub: `Southik Nath Banerjee`
- **Veronika Rybak** - GitHub: `CoraEpiro`
- **Denis Hoti** - GitHub: `denishotii`

