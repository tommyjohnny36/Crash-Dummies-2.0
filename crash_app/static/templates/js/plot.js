// Initialized arrays
let vehicle_model = []
let outcome = []

d3.json("http://127.0.0.1:5000/accident-data/").then(function(response) {
// For loop to populate arrays
for (let i = 0; i < response.length; i++) {
    row = response[i];
    vehicle_model.push(row.vehicle_model);
    doa_status.push(row.doa_status);
  }
  
  // Trace1 for the Greek Data
  let trace1 = {
    x: vehicle_model,
    y: outcome,
    name: "Vehicle Model Accident Outcomes",
    type: "bar"
  };
    
  // Create data array
//   let data = [trace1, trace2];
  let data = [trace1]
  
  // Apply a title to the layout
  let layout = {
    title: "Fatal & Non-Fatal Outcomes by Vehicle Model"
  };
  
  // Render the plot to the div tag with id "plot"
  Plotly.newPlot("bar", data, layout);
});
