$( document ).ready(function() {
    console.log("ready: licenses_by_district");

    $.get( "/business/licenses_by_district/data.json", function( data ) {
        console.log(data);
        lineGraph(data);
    });

});


function lineGraph(data) {
    console.log('starting');
    var ctx = $("#hacklbChart");

    var myChart = new Chart(ctx, {
        type: 'line',
        data: data,
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    }
                }]
            }
        }
    });
}