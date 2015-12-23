mainController.mapView = (function () {
      var that = {},
      heatmap,
      asd = true;
      

      init = function (data) {
        document.getElementById("crime-map").style.height = "500px";
        _setupMap(data);
        return that;
      },

      _setupMap = function(data) {
          map = new google.maps.Map(document.getElementById("crime-map"), {
          center: {lat: 41.855363, lng: -87.636700},
          zoom: 14,
          styles: [{"featureType":"landscape","stylers":[{"saturation":-100},{"lightness":65},{"visibility":"on"}]},{"featureType":"poi","stylers":[{"saturation":-100},{"lightness":51},{"visibility":"simplified"}]},{"featureType":"road.highway","stylers":[{"saturation":-100},{"visibility":"simplified"}]},{"featureType":"road.arterial","stylers":[{"saturation":-100},{"lightness":30},{"visibility":"on"}]},{"featureType":"road.local","stylers":[{"saturation":-100},{"lightness":40},{"visibility":"on"}]},{"featureType":"transit","stylers":[{"saturation":-100},{"visibility":"simplified"}]},{"featureType":"administrative.province","stylers":[{"visibility":"off"}]},{"featureType":"water","elementType":"labels","stylers":[{"visibility":"on"},{"lightness":-25},{"saturation":-100}]},{"featureType":"water","elementType":"geometry","stylers":[{"hue":"#ffff00"},{"lightness":-25},{"saturation":-97}]}]

          });
          heatmap = new google.maps.visualization.HeatmapLayer({
            data: _getPoints(data),
            map: map
          });
          heatmap.setMap(map);
          //_changeGradient();
          _changeRadius();
      },

      _changeRadius = function() {
        heatmap.set('radius', heatmap.get('radius') ? null : 50);
      }

      _changeGradient = function() {
        var gradient = [
        'rgba(29, 155, 108, 0)',
        'rgba(20, 130, 120, 1)',
        'rgba(14, 110, 140, 1)',
        'rgba(7, 90, 160, 1)',
        'rgba(0, 63, 180, 1)',
        'rgba(0, 0, 200, 1)',
        'rgba(0, 0, 223, 1)',
        'rgba(0, 0, 191, 1)',
        'rgba(0, 0, 159, 1)',
        'rgba(0, 0, 127, 1)',
        'rgba(63, 0, 91, 1)',
        'rgba(127, 0, 63, 1)',
        'rgba(191, 0, 31, 1)',
        'rgba(255, 0, 0, 1)'
        ]
        heatmap.set('gradient', heatmap.get('gradient') ? null : gradient);
      },

      _getPoints = function (data) {
        var c = new Array();
        for (var i = 0; i < data.series.length; i++) {
          //console.log(data.series[i]);
          c.push({location: new google.maps.LatLng(data.series[i].lat, data.series[i].lng), weight: data.series[i].weight});
        }
        //console.log(c[100]);
        return c;

        //location: new google.maps.LatLng(37.782, -122.447), weight: 0.5}

      }
      //google.maps.event.addDomListener(window, 'load', init);


    that.init = init;
    return that;
})();
