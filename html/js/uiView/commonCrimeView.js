mainController.commonCrimeView = (function () {  var that = {},

      init = function (data) {
          console.log("commonCrimeView is up "  + data);
          initModules();
          return that;
      },

      initModules = function () {
        $('#crimeContainer').highcharts({
             chart: {
                 type: 'area',
                 backgroundColor: 'none'
             },
             title: {
                 text: false
             },
             xAxis: {
                 categories: ['Apples', 'Oranges', 'Pears', 'Grapes', 'Bananas']
             },
             credits: {
                 enabled: false
             },
             series: [{
                 name: 'John',
                 data: [5, 3, 4, 7, 2]
             }, {
                 name: 'Jane',
                 data: [2, -2, -3, 2, 1]
             }, {
                 name: 'Joe',
                 data: [3, 4, 4, -2, 5]
             }]
         });
      }

    that.init = init;
    return that;
})();
