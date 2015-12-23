//JSLINT Error-Avoidance here
/*jslint nomen: true*/ //necessary for underscore-error-avoidance

var $,
    mainController,
    commonCrimeView,
    jQuery;

mainController.commonCrimeController = (function () {
    'use strict';
    var that = {},
        data = null,
        years = [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, "show_every_year"],
        charts = ["column", "area", "line", "pie"],
        chartType = "column",
        selectedYear = 2001,
        topic = "commonCrime",
        urlRequest = "http://52.29.118.210:5000/" + topic,

        _createSelectField = function (array, nameSelection) {
            var selectList = document.getElementById(topic + nameSelection),
                i,
                opt;
            for (i = 0; i < array.length; i = i + 1) {
                opt = document.createElement('option');
                opt.innerHTML = array[i];
                opt.value = array[i];
                selectList.appendChild(opt);
            }
        },

        _initSelectFields = function () {
            //_createSelectField(years, 'YearSelect');
            _createSelectField(charts, 'ChartSelect');
        },

        _initView = function (data) {
            commonCrimeView = mainController.commonCrimeView.init(data, chartType);
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

        _buildUrl = function () {
            selectedYear = $("#" + topic + "YearSelect").val();
            chartType = $("#" + topic + "ChartSelect").val();
            urlRequest = "http://52.29.118.210:5000/" + topic;
            _getData();
        },

        _initEvents = function () {
            $("#commonCrimeButton").click(_buildUrl);
        },

        init = function () {
            //_initSelectFields();
            //_initEvents();
            _getData();
            return that;
        };

    that.init = init;
    return that;
}());