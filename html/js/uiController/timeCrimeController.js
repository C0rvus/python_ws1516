mainController.timeCrimeController = (function () {
    var that = {},
        data = null,
        selectedYear = 2001,
        topic = "timeCrime",
        urlRequest = "http://52.29.118.210:5000/" + topic

        init = function () {
            _getData();
            return that;
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
          timeCrimeView = mainController.timeCrimeView.init(data);
        }

    that.init = init;
    return that;
})();
