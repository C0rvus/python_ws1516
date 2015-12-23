//JSLINT Error-Avoidance here
/*jslint nomen: true*/ //necessary for underscore-error-avoidance

var $,
    mainController,
    arrestCrimeView,
    jQuery;

mainController.arrestCrimeController = (function () {
    'use strict';
    var that = {},
        data = null,
        chartType = "pie",
        topic = "arrestCrime",
        urlRequest = "http://52.29.118.210:5000/" + topic,

        _initView = function (data) {
            arrestCrimeView = mainController.arrestCrimeView.init(data);
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

        init = function () {
            _getData();
            return that;
        };

    that.init = init;
    return that;
}());
