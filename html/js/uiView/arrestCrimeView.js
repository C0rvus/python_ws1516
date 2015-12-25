var mainController,
    $,
    console;

mainController.arrestCrimeView = (function () {
    'use strict';
    var that = {},

        initModules = function (data) {
          $('#arrest-chart').highcharts({
              chart: {
                  backgroundColor: 'none',
                  plotBackgroundColor: null,
                  plotBorderWidth: null,
                  plotShadow: false,
                  type: 'pie'
              },
              title: {
                  text: 'Arrest Crimes',
                  x: -20 //center
              },
              subtitle: {
                  text: 'Shows how many crimes are carred out'
              },
              tooltip: {
                  pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
              },
              plotOptions: {
                  pie: {
                      allowPointSelect: true,
                      cursor: 'pointer',
                      dataLabels: {
                          enabled: false
                      },
                      showInLegend: true
                  }
              },
              series: [{
                  name: 'Brands',
                  colorByPoint: true,
                  data: [{
                      name: 'Microsoft Internet Explorer',
                      y: 56.33
                  }, {
                      name: 'Chrome',
                      y: 24.03,
                      sliced: true,
                      selected: true
                  }, {
                      name: 'Firefox',
                      y: 10.38
                  }, {
                      name: 'Safari',
                      y: 4.77
                  }, {
                      name: 'Opera',
                      y: 0.91
                  }, {
                      name: 'Proprietary or Undetectable',
                      y: 0.2
                  }]
              }]
          });
        },


        init = function (data) {
            console.log(data);
            initModules(data);
            return that;
        };

    that.init = init;
    return that;
}());
