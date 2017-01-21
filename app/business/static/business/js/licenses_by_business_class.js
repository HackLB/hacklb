var liveChart, ctx;

$( document ).ready(function() {
    console.log("ready: licenses_by_business_class");

    loadChart();

});

function loadChart() {
    $.get( "/business/licenses_by_business_class/data.json", function(data) {
        lineGraph(data);
    });
}


function deleteBusinessClass(bizClass) {
    for (ds in liveChart.data.datasets) { 
        if (liveChart.data.datasets[ds].label == bizClass) {
            liveChart.data.datasets.splice(ds, 1);
        };
    };
    lineGraph(liveChart.data);
}

function lineGraph(data) {
    console.log('drawing licenses_by_business_class...');
    ctx = $("#hacklbChart");

    liveChart = new Chart(ctx, {
        type: 'line',
        data: data,
        options: {
             // Container for pan options
                pan: {
                    // Boolean to enable panning
                    enabled: false,

                    // Panning directions. Remove the appropriate direction to disable 
                    // Eg. 'y' would only allow panning in the y direction
                    mode: 'xy'
                },

                // Container for zoom options
                zoom: {
                    // Boolean to enable zooming
                    enabled: false,

                    // Zooming directions. Remove the appropriate direction to disable 
                    // Eg. 'y' would only allow zooming in the y direction
                    mode: 'y',
                },


            scales: {
                yAxes: [{
                    display: true,
                    ticks: {
                        // suggestedMax: 2000,    // minimum will be 0, unless there is a lower value.
                        // OR //
                        beginAtZero: true   // minimum value will be 0.
                    }
                }]
            }


        }
    });
}