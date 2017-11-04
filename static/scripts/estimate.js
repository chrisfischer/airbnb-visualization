'use strict'

var marker = false; // has the user plotted their location marker?
var map;

$(document).ready(function() {
    $("#estimateLink").addClass("active");
    initMap();
});

// when enter is pressed, update marker and price
$('#latitude').change(function () {
    var latlng = new google.maps.LatLng(parseFloat(this.value), marker.getPosition().lng());
    marker.setPosition(latlng);
    updateIncome()
});

// when enter is pressed, update marker and price
$('#longitude').change(function () {
    var latlng = new google.maps.LatLng(marker.getPosition().lat(), parseFloat(this.value));
    marker.setPosition(latlng);
    updateIncome()
});

// initialize map
function initMap() {
    var sanFrancisco = new google.maps.LatLng(37.75800, -122.453523);
    map = new google.maps.Map(document.getElementById('map'), {
        zoom: 12,
        center: sanFrancisco,
        mapTypeId: 'roadmap'
    });

    // Listen for any clicks on the map.
    google.maps.event.addListener(map, 'click', function(event) {                
        // Get the location that the user clicked.
        var clickedLocation = event.latLng;
        // If the marker hasn't been added.
        if(marker === false){
            // Create the marker.
            marker = new google.maps.Marker({
                position: clickedLocation,
                map: map,
                draggable: true // make it draggable
            });
            // Listen for drag events
            google.maps.event.addListener(marker, 'dragend', function(event){
                markerLocation();
            });
        } else{
            // Marker has already been added, so just change its location
            marker.setPosition(clickedLocation);
        }
        // Get the marker's location
        markerLocation();
    });
}

// This function will get the marker's current location and then add the lat/long
// values to our textfields so that we can save the location

function markerLocation() {
    // Get location.
    var currLoc = marker.getPosition();
    // Add lat and lng values to a field that we can save.
    document.getElementById('latitude').value = currLoc.lat(); // latitude
    document.getElementById('longitude').value = currLoc.lng(); // longitude
    updateIncome()
}

// Make an api call to get the maximizing price
function updateIncome() {
    var currLoc = marker.getPosition();
    var url = '/predict_api?income=' + currLoc.lat() + '+' + currLoc.lng()
    $.getJSON(url, function(json) {
        $('#result')[0].innerText = '$' + json;
    }).fail(function() {
        $('#result')[0].innerText = '';
    })
}