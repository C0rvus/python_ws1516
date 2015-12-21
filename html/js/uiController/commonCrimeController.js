mainController.commonCrimeController = (function () {
    var that = {},
        data = null,
        years = [2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,"show_every_year"],
        charts = ["column","area","line"],
        chartType = "column",
        selectedYear = 2001,
        selectedCrime = "rape",
        urlRequest = "http://52.29.118.210:5000/getData/number-of-tables"

        init = function () {
            _initSelectFields();
            _initEvents();
            _getData();
            return that;
        },

        _initEvents = function () {
          $("#commonCrimeButton").click(_buildUrl);
        },

        _initSelectFields = function () {
          var yearList = document.getElementById('commonCrimeYearSelect');
          for(var i = 0; i < years.length; i++) {
            var opt = document.createElement('option');
            opt.innerHTML = years[i];
            opt.value = years[i];
            yearList.appendChild(opt);
          }

          var chartList = document.getElementById('commonCrimeChartSelect');
          for(var i = 0; i < charts.length; i++) {
            var opt = document.createElement('option');
            opt.innerHTML = charts[i];
            opt.value = charts[i];
            chartList.appendChild(opt);
          }
        },

        _buildUrl = function () {
          var year = $("#commonCrimeYearSelect").val(),
              type = $("#commonCrimeChartSelect").val();
          urlRequest = "http://52.29.118.210:5000/"  + "commonCrime/" + "year/" + year;
          chartType = type;
          _getData();
        },

        _getData = function () {
          $.ajax({
              url: urlRequest,
              type: 'GET',
              crossDomain: true,
              dataType: 'text',
              success: function (data) {
                _initView(jQuery.parseJSON(data));
              }
          });
        },

        _initView = function (data) {
          commonCrimeView = mainController.commonCrimeView.init(data,chartType);
        }

    that.init = init;
    return that;
})();
