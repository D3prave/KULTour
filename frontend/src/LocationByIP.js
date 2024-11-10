const getGeolocation = () => {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        (position) => {
          const { latitude, longitude } = position.coords;
          console.log(`Latitude: ${latitude}, Longitude: ${longitude}`);
        },
        (error) => {
          console.error("Geolocation error: ", error);
          alert("Could not get location");
        }
      );
    } else {
      alert("Geolocation is not supported by this browser.");
    }
  };
  
  // Call the function to get the geolocation
  getGeolocation();
  