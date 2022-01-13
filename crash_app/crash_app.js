const url = "https://crashviewer.nhtsa.dot.gov/CrashAPI//crashes/GetCaseList?states=1,51&fromYear=2014&toYear=2015&minNumOfVehicles=1&maxNumOfVehicles=6&format=json";

// Promise Pending
const dataPromise = d3.json(url);
console.log("Data Promise: ", dataPromise);

// Fetch the JSON data and console log it
d3.json(url).then(function(data) {
  console.log(data);
});

const canvas = d3.select(".canva");

// Add an svg element
const svg = canvas.append("svg")
            .attr("width", 600)
            .attr("height", 600 );


const margin = {
        top: 20,
        right: 20,
        bottom: 70,
        left: 70
}
