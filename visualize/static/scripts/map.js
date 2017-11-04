'use strict'

var numericalFields;

// run when ready  
$("#options").change(function() {
    var buttonText = $("#options .active")[0].innerText;
    updateMap(descriptionToLabel(buttonText));
});

$(document).ready(function() {
    $("#mapLink").addClass("active");

    initMap();
    $.getJSON("/api?fields=numericalFields", function(json) {
        numericalFields = json;
    });
});


function descriptionToLabel(desc) {
    var label;
    switch (desc) {
        case "Price":
            label = "price";
            heatmap.cfg.radius = 35;
            break;
        case "Bedrooms":
            label = "bedrooms";
            heatmap.cfg.radius = 20;
            break;
        case "Bathrooms":
            label = "bathrooms";
            heatmap.cfg.radius = 25;
            break;
        case "Square Feet":
            label = "square_feet";
            heatmap.cfg.radius = 60;
            break;
        case "Number of Reviews":
            label = "number_of_reviews";
            heatmap.cfg.radius = 25;
            break;
        case "Length of House Rules":
            label = "length(house_rules)"
            heatmap.cfg.radius = 30;
            break;
    }
    if (label) {
        return label
    }
    if (desc.indexOf('Len. ') != -1) {
        heatmap.cfg.radius = 20;
    } else if (desc.indexOf('Reviews') != -1) {
        heatmap.cfg.radius = 15;
    }
    return numericalFields[desc]

}

var map;
var heatmap;

function initMap() {
    var sanFrancisco = new google.maps.LatLng(37.75800, -122.453523);
    map = new google.maps.Map(document.getElementById('map'), {
        zoom: 13,
        center: sanFrancisco,
        mapTypeId: 'terrain'
    });

    heatmap = new HeatmapOverlay(map, 
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

    // default data
    var dataUrl = "/api/?fields=price&groupBy=location";
    $.getJSON(dataUrl, function(json) {
        setOverlay(jsonToData(json));
    });
}

function updateMap(field) {
    var dataUrl = "/api/?fields=" + field + "&groupBy=location"
    $.getJSON(dataUrl, function(json) {
        setOverlay(jsonToData(json));
    });
}

function setOverlay(data) {
    heatmap.setData({
        min: 0, 
        max: 8700, 
        data: data
    });
}

function jsonToData(json) {
    var heatmapData = [];
    for (var i = 0; i < json.length; i++) {
        var coords = json[i][0].split(' ');
        //var latLng = new google.maps.LatLng(lat, long);
        var v = {
            lat: parseFloat(coords[0]),
            lng: parseFloat(coords[1]),
            weight: parseFloat(json[i][1])
        }
        heatmapData.push(v);
    }
    return heatmapData;
}