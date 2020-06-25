// REFER TO Python.ipynb on how the below list was created
// EXTRACTED the Top list from samples.json using pyton


// 1. BAR CHART

var trace1 = {
    y: ["OTU 1167", "OTU 2859", "OTU 482", "OTU 2264", "OTU 41", "OTU 1189", "OTU 352", "OTU 189", "OTU 2318", "OTU 1977"],

    x: [163.0, 126.0, 113.0, 78.0, 71.0, 51.0, 50.0, 47.0, 40.0, 40.0],

    text:['Bacteria;Bacteroidetes;Bacteroidia;Bacteroidales;Porphyromonadaceae;Porphyromonas',
    'Bacteria;Firmicutes;Clostridia;Clostridiales;IncertaeSedisXI;Peptoniphilus',
    'Bacteria',
    'Bacteria;Firmicutes;Clostridia;Clostridiales;IncertaeSedisXI',
    'Bacteria',
    'Bacteria;Bacteroidetes;Bacteroidia;Bacteroidales;Porphyromonadaceae;Porphyromonas',
    'Bacteria',
    'Bacteria',
    'Bacteria;Firmicutes;Clostridia;Clostridiales;IncertaeSedisXI;Anaerococcus',
    'Bacteria;Firmicutes;Clostridia;Clostridiales'],

    orientation: 'h',

    
    type: "bar"
};

var data = [trace1];


Plotly.newPlot('bar', data);


// 2. BUBBLE CHART

var trace2 = {

    y: sample_values_list,

    x: otu_id_list,

    text:otu_labels_list,

    mode: 'markers',

    marker: {

        color: otu_id_list,

        size: sample_values_list
    }

};

var layout2 = {
    xaxis: { title: "OTU ID"},
};

var data2 = [trace2];


Plotly.newPlot('bubble', data2, layout2);


// 3. Filtering


// Update the panel

function updatepanel(newdata) {

    var sample_metadata = d3.select("#selDataset");

    data_char[new_data];

}

// Get the data

function getdata(dataset)  {

    var data = [];

    switch(dataset) {
    case "dataset1":
        data = data_char['940'];
        

    }


    updatepanel(data)

}

