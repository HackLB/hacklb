$(document).ready(function() {
    console.log('Welcome to geographic datasets');
    map = mapInit('dsmap');

    // addLayer(map, 
    //     'Bikeways', 
    //     '/media/geographic/Bikeways.geojson', 
    //     'line', 
    //     'rgba(61,153,80,0.55)');

    // addLayer(map, 
    //     'Districts', 
    //     '/media/geographic/Bikeways.geojson', 
    //     'area', 
    //     '#000000');
    
});

function mapInit(mapid) {
	mapboxgl.accessToken = 'pk.eyJ1Ijoicm9nZXJob3dhcmQiLCJhIjoiY2lrOXlnZHFvMGc5ZnY0a3ViMHkyYTE0dyJ9.CWAOOChPtxviw8fVB0R1mQ';
	var map = new mapboxgl.Map({
	    container: 'dsmap',
	    style: 'mapbox://styles/mapbox/streets-v9',
        center: [-118.1478038, 33.7960355],
        zoom: 11,
	});
    console.log('map!')
	return map;
}

function addLayer(map, name, url, type, color) {
    console.log('adding layer');

    map.on('load', function() {
        console.log('loading map source');
        map.addSource(name, {
            type: 'geojson',
            data: url,
        });
        console.log('loaded map source');

        if (type === 'area') {
            console.log('making area layer from source');
            map.addLayer({
                id: name,
                type: 'fill',
                source: name,
                'source-layer': name,
                layout: {
                    visibility: 'visible'
                },
                paint: {
                  'fill-color': color
                }
            });

        } else {
            console.log('making line layer from source');
            map.addLayer({
                id: name,
                type: "line",
                source: name,
                "layout": {
                    "line-join": "round",
                    "line-cap": "round"
                },
                "paint": {
                    "line-color": color,
                    "line-width": 3
                }
            });
        }

    });

}

