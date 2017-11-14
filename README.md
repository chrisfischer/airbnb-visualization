# Airbnb Visualization and Optimization

Made for the Capital One MindSumo Challenge. 

We predict the best listing price by finding homes which had the lowest vacancies in that area with similar characteristics.

Estimated weekly income is calculated by using the Google Maps API to convert coordinates to an address, which is then passed to Zillow's API to retrieve the house cost. From here the average mortgage payment is calculated and subtracted from the estimated revenue using the same metrics as with price optimization.

# Citations

[Chart.js](http://www.chartjs.org/)
[Heatmap.js](https://www.patrick-wied.at/static/heatmapjs/)
[Google Maps JS API](https://developers.google.com/maps/documentation/javascript/)
[Zillow Valuations API](https://www.zillow.com/howto/api/HomeValuationAPIOverview.htm)
[Mortgage Payment Calculator](https://github.com/jbmohler/mortgage)
[Bootstrap](https://getbootstrap.com/)
