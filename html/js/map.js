$(document).ready(function() {
    var map, heatmap;
    function initMap() {
        document.getElementById("crime-map").style.height = "500px";
        map = new google.maps.Map(document.getElementById("crime-map"), {
            center: {lat: 41.855363, lng: -87.636700},
            zoom: 10
        });
        heatmap = new google.maps.visualization.HeatmapLayer({
            data: getPoints(),
            map: map
        });
    }
    function getPoints() {
        var c = new Array();
        for (var i = 0; i < 100000; i++) {
            c[i] = new google.maps.LatLng(37.782551, -122.445368);
        }
        return c;
        
    }
    google.maps.event.addDomListener(window, 'load', initMap);
});