'use strict'

// run when ready  
$(function() {
    // detects when a button is pushed
    $("#options").on('change', function() {
        console.log("change")
        var buttonText = $("#options .active")[0].innerText;
        var label;
        switch (buttonText) {
            case "Price":
                label = "price";
                break;
            case "Bedrooms":
                label = "bedrooms";
                break;
            case "Bathrooms":
                label = "bathrooms";
                break;
            case "Square footage":
                label = "square_feet";
                break;
            case "Average Review Score":
                label = "review_scores_rating";
                break;
            case "Length of Description":
                // TODO
                break;
        }
        console.log(label)
    });

    initMap()
});

var map;
var heatmap;

function initMap() {
    var sanFrancisco = new google.maps.LatLng(37.75800, -122.453523);
    map = new google.maps.Map(document.getElementById('map'), {
        zoom: 13,
        center: sanFrancisco,
        mapTypeId: 'hybrid'
    });

    var dataUrl = "/api/?fields=price&groupBy=location"
    $.getJSON(dataUrl, addOverlay)
}

function updateMap(field) {
    console.log(field)
    var dataUrl = "/api/?fields=" + field + "&groupBy=location"
    $.getJSON(dataUrl, addOverlay)
}

function addOverlay(results) {
    var heatmap = new HeatmapOverlay(map, 
      {
        // radius should be small ONLY if scaleRadius is true (or small radius is intended)
        "radius": 35,
        "maxOpacity": 1, 
        // scales the radius based on map zoom
        "scaleRadius": false, 
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
        //var latLng = new google.maps.LatLng(lat, long);
        var v = {
            lat: parseFloat(coords[0]),
            lng: parseFloat(coords[1]),
            weight: parseFloat(results[i][1])
        }
        heatmapData.push(v);
    }
    console.log(heatmapData)
    
    heatmap.setData({
        min: 0, 
        max: 8700, 
        data: heatmapData
    });
}