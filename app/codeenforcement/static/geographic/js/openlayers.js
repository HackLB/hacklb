$( document ).ready(function() {
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
    var map = new ol.Map({
        target: 'dsmap',
        layers: [
          new ol.layer.Tile({
            source: new ol.source.OSM()
          })
        ],
        view: new ol.View({
          center: ol.proj.fromLonLat([-118.1478038, 33.7960355]),
          zoom: 12
        })
    });
    return map;
}

