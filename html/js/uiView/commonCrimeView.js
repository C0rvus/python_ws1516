mainController.commonCrimeView = (function () {
      var that = {},
      years = [2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014],

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
             //colors:["#00BF77","#0B67BA","#FF9500","#FF4F00"],
             title: {
                 text: false
             },
             credits: {
                 enabled: false
             },
             xAxis: {
              categories: years
             },
             yAxis: {
                min: 0,
                title: {
                  text: false
                }
             },
             plotOptions: {
                column: {
                  stacking: 'percent'
                }
             },
             tooltip: {
                pointFormat: '<span style="color:<{series.color}">{series.name}</span>: <b>{point.y}</b> ({point.percentage:.000f}%)<br/>',
                shared: true
             },
             series: data.series
         });
      }

    that.init = init;
    return that;
})();
