'use strict'

var DEFAULT_X = "price";
var DEFAULT_Y = "bedrooms";
var xlabel = "Price";
var ylabel = "Bedrooms";

$(function() {
    // inititalize chart with default choices
    $.getJSON("/api/?fields=" + DEFAULT_X + "+" + DEFAULT_Y + "&plot=x+y", function(data) {
        make_chart(data, xlabel, ylabel);
    });

    // detects when a button is pushed
    $("#options").on('change', function() {
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
        xlabel = buttonText;
        $.getJSON("/api/?fields=" + "bedrooms" + "+" + label + "&plot=x+y", function(data) {
            make_chart(data, xlabel, ylabel);
        });
    });
});

function make_chart(data, xlabel, ylabel) {
    console.log(data);
    var ctx = document.getElementById('scatterPlot').getContext('2d');
    ctx = new Chart(ctx, {
        type: 'scatter',
        data: {
            datasets: [{
                label: 'Scatter Dataset',
                data: data,
                pointBorderColor: 'blue',
                pointBackgroundColor: '#ffffff',
            }]
        },
        options: {
            showLines: false,
            animation: false,
            scales: {
                xAxes: [{
                    type: 'linear',
                    position: 'bottom',
                    display: true,
                    scaleLabel: {
                        labelString: xlabel
                    },
                }],
                yAxes: [{
                  scaleLabel: {
                    display: true,
                    labelString: ylabel
                  }
                }]
            }     
        }
    });
}