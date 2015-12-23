var mainController,
    $,
    console;

mainController.arrestCrimeView = (function () {
    'use strict';
    var that = {},

        initModules = function (data) {
            $('#arrest-chart').highcharts({
              chart: {
                plotBackgroundColor: null,
                plotBorderWidth: null,
                plotShadow: false,
                type: 'pie'
              },
              title: {
                  text: 'Browser market shares January, 2015 to May, 2015'
              },
              tooltip: {
                  pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
              },
              plotOptions: {
                  pie: {
                      allowPointSelect: true,
                      cursor: 'pointer',
                      dataLabels: {
                          enabled: true,
                          format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                          style: {
                              color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                          }
                      }
                  }
              },
              series: data.series
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
