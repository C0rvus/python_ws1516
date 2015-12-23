mainController.commonCrimeController = (function () {
    var that = {},
        data = null,
        years = [2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,"show_every_year"],
        charts = ["column","area","line","pie"],
        chartType = "column",
        selectedYear = 2001,
        topic = "commonCrime",
        urlRequest = "http://52.29.118.210:5000/" + topic

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
          _createSelectField(years, 'YearSelect');
          _createSelectField(charts, 'ChartSelect')
        },

        _createSelectField = function (array, nameSelection) {
          var selectList = document.getElementById(topic + nameSelection);
          for(var i = 0; i < array.length; i++) {
            var opt = document.createElement('option');
            opt.innerHTML = array[i];
            opt.value = array[i];
            selectList.appendChild(opt);
          }
        }

        _buildUrl = function () {
          selectedYear = $("#" + topic + "YearSelect").val();
          chartType = $("#" + topic + "ChartSelect").val();
          urlRequest = "http://52.29.118.210:5000/"  + topic + "/" + "year/" + selectedYear;
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
