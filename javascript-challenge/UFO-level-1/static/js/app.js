// from data.js

var tableData = data;

// 1. ADDING TABLE DATA TO HTML STEP 1 TO STEP 5 //

// Get a reference to the table body

var tbody = d3.select("tbody");

// Console.log the UFO data from data.js

console.log(data);

// Step 1: Loop Through `data` and console.log each weather report object

tableData.forEach(function(ufodata) {
    
    console.log(ufodata);

// Step 2:  Use d3 to append one table row `tr` for each ufo report object

var row = tbody.append("tr");

// Step 3:  Use `Object.entries` to console.log each UFO report value

Object.entries(ufodata).forEach(function([key, value]) {
    
    console.log(key, value);

// Step 4: Use d3 to append 1 cell per ufo report value

var cell = row.append("td");

// Step 5: Use d3 to update each cell's text with
      
cell.text(value);

    });

});

// 2. FILTERING THE DATA BASED ON USER INPUT //

// Getting a reference to the button on the page with the id property set to `filter-btn`

var button = d3.select("#filter-btn");

// Setup a listner event function on the botton

button.on("click", function() {


// Getting a reference to the input element on the page with the id property set to 'datetime'

    var inputElement = d3.select("#datetime");

// Get the value property of the input element

    var inputValue = inputElement.property("value");


    console.log(inputValue);

// Filter the data based on the date

    var filteredData = tableData.filter(sighting => sighting.datetime === inputValue);

    console.log(filteredData);


// 3. Show only the filtered data by updating tbody, similar to Step 1 to 5

    tbody.html("")

    filteredData.forEach(function(sample) {

        console.log(sample);
        
        var row = tbody.append("tr");
        
        Object.entries(sample).forEach(function([key, value]) {
            
            console.log(key, value);
            
            
            var cell = row.append("td");
            
            cell.text(value);
        });
    });
    
});