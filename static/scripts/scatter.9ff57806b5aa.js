'use strict'

var numericalFields;

var DEFAULT_Y = "bathrooms";
var DEFAULT_X = "bedrooms";

// initialize labels
var ylabel = "Bathrooms";
var xlabel = "Bedrooms";

var ctx;
    
$(document).ready(function() {
    $("#scatterLink").addClass("active");

    ctx = document.getElementById('scatterPlot').getContext('2d');

    // get numerical fields dictionary
    $.getJSON("/api?fields=numericalFields", function(json) {
        numericalFields = json;
    });

    // inititalize chart with default choices
    $.getJSON("/api?fields=" + DEFAULT_X + "+" + DEFAULT_Y + "&plot=x+y", function(data) {
        makeChart(data, xlabel, ylabel);
    });
});

// detects when a button is pushed
$("#pairOptions").on('change', function() {
    var buttonText = $("#pairOptions .active")[0].innerText;
    
    // set labels to proper value
    setLabelsToPair(buttonText);

    $.getJSON("/api?fields=" + descriptionToLabel(xlabel) + "+" + descriptionToLabel(ylabel) + "&plot=x+y", function(data) {
        // do some more post processing for 'years a host'
        if (xlabel == "Years a Host") {
            var data2 = [];
            var today = new Date();
            for (var i = 0; i < data.length; i++) {
                var hostSince = new Date(data[i].x);
                var years = (today.getTime() - hostSince.getTime())/ (1000 * 60 * 60 * 24 * 365);
                data2.push({
                    'x': years,
                    'y': data[i].y
                })
            }
            makeChart(data2, xlabel, ylabel);
        } else {
            makeChart(data, xlabel, ylabel);
        }
    });
});

Chart.pluginService.register({
    beforeDraw: function (chart, easing) {
        if (chart.config.options.chartArea && chart.config.options.chartArea.backgroundColor) {
            var helpers = Chart.helpers;
            var ctx = chart.chart.ctx;
            var chartArea = chart.chartArea;

            ctx.save();
            ctx.fillStyle = chart.config.options.chartArea.backgroundColor;
            ctx.fillRect(chartArea.left, chartArea.top, chartArea.right - chartArea.left, chartArea.bottom - chartArea.top);
            ctx.restore();
        }
    }
});


function setLabelsToPair(desc) {
    switch (desc) {
        case "Beds vs. Baths":
            xlabel = "Num. Bedrooms";
            ylabel = "Num. Bathrooms";
            break;
        case "Cleanliness vs. Cleaning Fee":
            xlabel = "Reviews: Cleanliness";
            ylabel = "Cleaning Fee";
            break;
        case "Years a Host vs. Rating":
            xlabel = "Years a Host";
            ylabel = "Reviews: Rating"
            break;
    }
}

function descriptionToLabel(desc) {
    if (desc == "Years a Host") {
        return "host_since"
    }
    return numericalFields[desc];
}

function makeChart(data, xlabel, ylabel) {
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
                    scaleLabel: {
                        display: true,
                        labelString: xlabel,
                        fontColor: "white"
                    },
                    ticks: {
                        fontColor: "#fff", // this here
                    },
                    gridLines: {
                        display: true,
                        color: "#333"
                    }
                }],
                yAxes: [{
                    scaleLabel: {
                        display: true,
                        labelString: ylabel,
                        fontColor: "#fff"
                    },
                    ticks: {
                        fontColor: "#fff", // this here
                    },
                    gridLines: {
                        display: true,
                        color: "#333"
                    },
                }]
            },
            legend: {
                display: false
            },
            chartArea: {
                backgroundColor: 'rgba(255, 255, 255, 0.1)'
            }
        }
    });
}