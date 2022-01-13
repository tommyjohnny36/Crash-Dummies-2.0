// const url = "https://crashviewer.nhtsa.dot.gov/CrashAPI//crashes/GetCaseList?states=1,51&fromYear=2014&toYear=2015&minNumOfVehicles=1&maxNumOfVehicles=6&format=json";
// // Promise Pending
// const dataPromise = d3.json(url);
// console.log("Data Promise: ", dataPromise);
// // Fetch the JSON data and console log it
// d3.json(url).then(function(data) {
//   console.log(data);
// });
// const canvas = d3.select(".canva");
// // Add an svg element
// const svg = canvas.append("svg")
//             .attr("width", 600)
//             .attr("height", 600 );
// const margin = {
//         top: 20,
//         right: 20,
//         bottom: 70,
//         left: 70
// }

// change location of json file and column names
// DropDown Menu function
function dropdownmenu() {

  let dropdown = d3.select("#selDataset");
  d3.json("samples.json").then(function (data) {
      let IDs = data.names;
      IDs.forEach(ID => {
          dropdown.append("option").text(ID).property("value", ID)

      });
  });
};

// Create the plotting function
function plotting(sampleID) {

  // Read in samples.json
  d3.json("samples.json").then(function (data) {
      
      // Filtering the json file
      let Data = data.samples.filter(i => i.id == sampleID)[0];

      // Set the metrics for bar plot
      let trace1 = {
          x: Data.sample_values.slice(0, 10).reverse(),
          y: Data.otu_ids.slice(0, 10).map(otu_id => `OTU #${otu_id}`).reverse(),
          text: Data.otu_labels.slice(0, 10).reverse(),
          type: "bar",
          orientation: "h",
          marker: {
            color: 'rgb(154, 140, 152)',
            line: {
               width: 3
           }
          }
      };

      let layoutBar = { 
        title: "<b>Top 10 OTU Individuals</b>" ,
        xaxis: {title: 'Number of Samples Collected'},
       yaxis: {title: 'OTU ID'},
       width: 480, height: 640
      };

      // Use plotly to plot Bar Chart
      Plotly.newPlot("bar", [trace1], layoutBar, {responsive: true});

// Set the metrics for the bubble plot
      let trace2 = {
        x: Data.otu_ids,
        y: Data.sample_values,
        mode: "markers",
        marker: {
            size: Data.sample_values,
            color: Data.otu_ids
        },
        text: Data.otu_labels,
        
    };

    let layoutBubble = { 
        title: '<b>Bubble Chart For Each Sample</b>',
        xaxis: {title: 'OTU ID'},
        yaxis: {title: 'Number of Samples Collected'},
        height: 700,
        width: 1200
};

    // Use plotly to plot bubble chart
    Plotly.newPlot("bubble", [trace2], layoutBubble);

});
};

// Create the demographic information
function demo(sampleID) {

let boxData = d3.select("#sample-metadata");
d3.json("samples.json").then(function (data) {
    let boxData = data.metadata.filter(x => x.id == sampleID)[0];
    d3.select("#sample-metadata").html("");
    Object.entries(boxData).forEach(element => {
        d3.select("#sample-metadata").append("h6").text(`${element[0]}: ${element[1]}`)
    });

});
}

// Create a function for changing sampleID
function optionChanged(sampleID) {
plotting(sampleID);
demo(sampleID);
gaugeplot(sampleID)
};

// Generate the gauge plot
function gaugeplot(sampleID) {
  d3.json("samples.json").then(function (data) {
      let sampleMetadata = data.metadata.filter(i => i.id == sampleID)[0];

      // Set the metrics for the gauge plot
      let Gauge = [
          {
              domain: { x: [0, 1], y: [0, 1] },
              value: sampleMetadata.wfreq,
              title: { text: "<b>Belly Button Washing Frequency</b> <br> Scrubs Per Week" },
              type: "indicator",
              mode: "gauge+number",
              gauge: { axis: { range: [0, 9] },
              bar: { color: "#f2e9e4" },
              steps: [
                { range: [0, 1], color: "#e5d5d0" },
                { range: [1, 2], color: "#dbc7c2" },
                { range: [2, 3], color: "#d2b9b4" },
                { range: [3, 4], color: "#c9ada7" },
                { range: [4, 5], color: "#ac9899" },
                { range: [5, 6], color: "#8a7e88" },
                { range: [6, 7], color: "#7d7482" },
                { range: [7, 8], color: "#706a7b" },
                { range: [8, 9], color: "#4a4e69" }
                      
              ], }
          }
      ];

      let layoutGauge = { width: 480, height: 640, margin: { t: 0, b: 0 } };

      // Use plotly to plot Gauge Chart
      Plotly.newPlot("gauge", Gauge, layoutGauge);
  });
};

// Populating the plots
function createPlots() {

  d3.json("samples.json").then(function (data) {
      let IDs = data.names[0];
      plotting(IDs);
      demo(IDs);
      gaugeplot(IDs);
      dropdownmenu();
  });
};

createPlots();
