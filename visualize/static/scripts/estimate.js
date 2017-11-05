'use strict'

var marker = false; // has the user plotted their location marker?
var map;
var geocoder;

$(document).ready(function() {
    $("#estimateLink").addClass("active");

    geocoder = new google.maps.Geocoder;
    initMap();
});

// when enter is pressed, update marker and price
$('#latitude').change(function () {
    var latlng = new google.maps.LatLng(parseFloat(this.value), marker.getPosition().lng());
    marker.setPosition(latlng);
    geocodeLatLng()
});

// when enter is pressed, update marker and price
$('#longitude').change(function () {
    var latlng = new google.maps.LatLng(marker.getPosition().lat(), parseFloat(this.value));
    marker.setPosition(latlng);
    geocodeLatLng()
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
        if (marker === false) {
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
    geocodeLatLng()
}

// Converts lat and lng to an address and then calls updateIncome when done
function geocodeLatLng() {
    var currLoc = marker.getPosition();
    var latlng = {lat: currLoc.lat(), lng: currLoc.lng()};
    geocoder.geocode({'location': latlng}, function(results, status) {
        if (status === 'OK') {
            if (results[0]) {
                var r = results[0]['address_components'];
                var number = r[0]['long_name'];
                var street = r[1]['long_name'];
                var zipcode = r[7]['long_name'];
                var d = {
                    'number': number,
                    'street': street,
                    'zipcode': zipcode
                };
                updateIncome(d)
            }
        } else {
            console.log('Geocoder failed due to: ' + status);
        }
    });
}

// makes an api query with lat, lng, and the address (if present)
// updates the text display with the calculated income
function updateIncome(address) {
    var currLoc = marker.getPosition();
    var url = '/predict_api?income=' + currLoc.lat() + '+' + currLoc.lng() 
    if (address) {
        url = url + '+' + address.number + '^' + address.street.replace(/\s+/g, "-") + '^' + address.zipcode
    }

    $.getJSON(url, function(income) {
        if (income == null) {
            fail();
        } else if (income < 0) {
            $('#result')[0].innerText = '-$' + -income + ' / week';
        } else {
            $('#result')[0].innerText = '$' + income + ' / week';
        }
    }).fail(function() {
        fail();
    })
}

function fail() {
    $('#result')[0].innerText = 'could not find house data';
}