function createMap(accidents) {

    // Create the tile layer that will be the background of our map.
    var streetmap = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    });
  
    // Create a baseMaps object to hold the streetmap layer.
    var baseMaps = {
      "Street Map": streetmap
    };
  
    // Create an overlayMaps object to hold the accidents layer.
    var overlayMaps = {
      "Bike Stations": accidents
    };
  
    // Create the map object with options.
    var map = L.map("map-id", {
      center: [40.73, -74.0059],
      zoom: 12,
      layers: [streetmap, accidents]
    });
  
    // Create a layer control, and pass it baseMaps and overlayMaps. Add the layer control to the map.
    L.control.layers(baseMaps, overlayMaps, {
      collapsed: false
    }).addTo(map);
  }
  
  function createMarkers(metaData) {
  
    // Pull the "stations" property from response.data.
    // var stations = response.data.stations;
  
    // Initialize an array to hold bike markers.
    var accidentMarkers = [];
  
    // Loop through the stations array.
    for (var i = 0; i < metaData.length; i++) {
      var accident = metaData[i];
  
      // For each station, create a marker, and bind a popup with the station's name.
      var accidentMarker = L.marker([metaData.lat, metaData.lon])
        .bindPopup("<h5>City: " + metaData.city + "</h5><h5>Outcome: " + metaData.doa_status + "</h5><h5>Manner of Collision: " + metaData.man_collision + "</h5><h5>Route: " + metaData.route);
  
      // Add the marker to the bikeMarkers array.
      accidentMarkers.push(accidentMarker);
    }
  
    // Create a layer group that's made from the bike markers array, and pass it to the createMap function.
    createMap(L.layerGroup(accidentMarkers));
  }
  
  // Perform an API call to the Citi Bike API to get the station information. Call createMarkers when it completes.
  d3.json("http://127.0.0.1:9000/bike-data/?q=3").then(createMarkers);