var mainController,
    $,
    console;

mainController.timeCrimeView = (function () {
    'use strict';
    var that = {},

        initModules = function (data) {
            $('#timeContainer').highcharts({
                title: {
                    text: 'HOURLY CRIME RATE'
                },
                credits: false,
                xAxis: {
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
                            enabled: false
                        },
                        enableMouseTracking: true
                    }
                },
                tooltip: {
                    valueSuffix: ' Crimes'
                },
                legend: {
                    layout: 'vertical',
                    align: 'right',
                    verticalAlign: 'middle',
                    borderWidth: 0
                },
                series: data.series
            });
        },
        init = function (data) {
            console.log("timeCrimeView is up " + data);
            initModules(data);
            return that;
        };

    that.init = init;
    return that;
}());