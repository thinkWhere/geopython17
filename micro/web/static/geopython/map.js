// global vars
var map, layer;
// symbol definition
var options = {
    style: function (feature) {
        return {
            color: "#ff0000",
            weight: 3,
            opacity: 1
            };
        }
    };

// calback to add geojson to map from text
function geojson_callback(geojson_text) {
    features = JSON.parse(geojson_text);
    if(layer) layer.remove();
    layer = L.geoJSON(null,options).addTo(map);
    layer.addData(features);
}

// loads data from a file (change to web service)
function readTextFile(file, callback) {
    var rawFile = new XMLHttpRequest();
    rawFile.overrideMimeType("application/json");
    rawFile.open("GET", file, true);
    rawFile.onreadystatechange = function() {
        if (rawFile.readyState === 4 && rawFile.status == "200") {
            callback(rawFile.responseText);
        }
    }
    rawFile.send(null);
}

// initialises the map
function map_setup(id) {
    // set up the map
    map = new L.Map(id);

    // create the tile layer with correct attribution
    var osmUrl='http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
    var osmAttrib='Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors';
    var osm = new L.TileLayer(osmUrl, {minZoom: 3, maxZoom: 16, attribution: osmAttrib});

    // set the initial view
    map.setView(new L.LatLng(47.551515958577205, 7.595899711664164), 12);
    map.addLayer(osm);

    // load the initial geojson
    //readTextFile("http://localhost:5000/api/v1/mapping/ac", geojson_callback);
}
