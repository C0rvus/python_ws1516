mainController.mapView = (function () {  
      var that = {},
      map,
      heatmap
      
      init = function (data) {
        document.getElementById("crime-map").style.height = "500px";
        map = new google.maps.Map(document.getElementById("crime-map"), {
            center: {lat: 41.855363, lng: -87.636700},
            zoom: 9
        });
        heatmap = new google.maps.visualization.HeatmapLayer({
            data: _getPoints(data),
            map: map
        });
        return that;
      },

      _getPoints = function (data) {
        var c = new Array();
        for (var i = 0; i < data.series.length; i++) {
          //console.log(data.series[i]);
          c.push({location: new google.maps.LatLng(data.series[i].lat, data.series[i].lng), weight: data.series[i].weight});
        }
        console.log(c[100]);
        return c;

        //location: new google.maps.LatLng(37.782, -122.447), weight: 0.5}
        
      }
      //google.maps.event.addDomListener(window, 'load', init); 

      
    that.init = init;
    return that;
})();
