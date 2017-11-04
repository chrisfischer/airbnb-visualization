'use strict'

// run when ready  
$(function() {
    // detects when a button is pushed
    $("#options").on('change', function() {
        var buttonText = $("#options .active")[0].innerText;
        switch (buttonText) {
            case "Price":
                updateMap("price");
                break;
            case "Bedrooms":
                updateMap("bedrooms");
                break;
            case "Bathrooms":
                updateMap("bathrooms");
                break;
            case "Square footage":
                updateMap("square_feet");
                break;
            case "Average Review Score":
                updateMap("review_scores_rating");
                break;
            case "Length of Description":
                // TODO
                break;
        }
    });
});

var map;
var heatmap;

function initMap() {
    heatmap = new google.maps.visualization.HeatmapLayer();
    var sanFrancisco = new google.maps.LatLng(37.75800, -122.453523);
    map = new google.maps.Map(document.getElementById('map'), {
        zoom: 13,
        center: sanFrancisco,
        mapTypeId: 'hybrid'
    });

    var dataUrl = "/api/?fields=price&groupBy=location"
    $.getJSON(dataUrl, eqfeed_callback)
}

function updateMap(field) {
    console.log(field)
    var dataUrl = "/api/?fields=" + field + "&groupBy=location"
    $.getJSON(dataUrl, eqfeed_callback)
}

function eqfeed_callback(results) {
    heatmap = new HeatmapOverlay(map, 
      {
        // radius should be small ONLY if scaleRadius is true (or small radius is intended)
        "radius": 2,
        "maxOpacity": 1, 
        // scales the radius based on map zoom
        "scaleRadius": true, 
        // if set to false the heatmap uses the global maximum for colorization
        // if activated: uses the data maximum within the current map boundaries 
        //   (there will always be a red spot with useLocalExtremas true)
        "useLocalExtrema": true,
        // which field name in your data represents the latitude - default "lat"
        latField: 'lat',
        // which field name in your data represents the longitude - default "lng"
        lngField: 'lng',
        // which field name in your data represents the data value - default "value"
        valueField: 'weight'
      }
    );
    var heatmapData = [];
    for (var i = 0; i < results.length; i++) {
        var coords = results[i][0].split(' ');
        var lat = coords[0]
        var long = coords[1]
        //var latLng = new google.maps.LatLng(lat, long);
        var v = {
            lat: lat,
            long: long,
            weight: results[i][1]
        }
        heatmapData.push(v);
    }
    //heatmap.setMap(null);
    /*heatmap = new google.maps.visualization.HeatmapLayer({
        data: heatmapData,
        dissipating: false,
        radius: 1,
        gradient: [
            "rgba(0, 255, 255, 0)",
            "rgba(0, 200, 255, 1)",
            "rgba(0, 100, 255, 1)",
            "rgba(0, 50, 225, 1)",
            "rgba(0, 0, 255, 1)",
            "rgba(20, 0, 227, 1)",
            "rgba(50, 0, 200, 1)",
            "rgba(100, 0, 100, 1)",
            "rgba(150, 0, 75, 1)",
            "rgba(200, 0, 50, 1)",
            "rgba(255, 0, 0, 1)"
        ],
        map: map
    });
    */
    heatmap.setData(heatmapData);
}