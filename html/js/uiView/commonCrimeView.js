mainController.commonCrimeView = (function () {  var that = {},

      init = function (data, chartType) {
          console.log("commonCrimeView is up "  + data);
          initModules(data, chartType);
          return that;
      },

      initModules = function (data, chartType) {
        $('#crimeContainer').highcharts({
             chart: {
                 type: chartType,
                 backgroundColor: 'none'
             },
             title: {
                 text: false
             },
             credits: {
                 enabled: false
             },
             series: data.series
         });
      }

    that.init = init;
    return that;
})();
