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
                  
                  data: [{"y": 141880, "name": "2001"},
                  {"y": 141518, "name": "2002"},
                  {"y": 141557, "name": "2003"},
                  {"y": 144661, "name": "2004"},
                  {"y": 140882, "name": "2005"},
                  {"y": 135367, "name": "2006"}, {"y": 131818, "name": "2007"}, {"y": 109931, "name": "2008"},
                  {"y": 110534, "name": "2009"}, {"y": 10038, "name": "2010"}, {"y": 96115, "name": "2011"},
                  {"y": 90333, "name": "2012"}, {"y": 86136, "name": "2013"}, {"y": 78833, "name": "2014"}]
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
