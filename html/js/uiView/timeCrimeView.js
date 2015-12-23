mainController.timeCrimeView = (function () {
      var that = {},
      years = [2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014]

      init = function (data) {
          console.log("timeCrimeView is up "  + data);
          initModules(data);
          return that;
      },

      initModules = function (data) {
          $('#timeContainer').highcharts({
              title: {
                  text: 'Hourly crime rate',
                  x: -20 //center
              },
              subtitle: {
                  text: 'Cumulated yearly number of crimes at the specific time'
              },
              xAxis: {
                  type: 'datetime',
                  title: {
                  	text: 'Time'
                  },
                  categories: ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']
              },
              yAxis: {
                  title: {
                      text: 'Number of crimes'
                  },
                  plotLines: [{
                      value: 0,
                      width: 1,
                      color: '#808080'
                  }]
              },
              plotOptions: {
                  line: {
                      dataLabels: {
                          enabled: true
                      },
                      enableMouseTracking: false
                  }
              },
              tooltip: {
                  valueSuffix: '°C'
              },
              legend: {
                  layout: 'vertical',
                  align: 'right',
                  verticalAlign: 'middle',
                  borderWidth: 0
              },
              series: data.series
          });
        }
      that.init = init;
      return that;
})();
