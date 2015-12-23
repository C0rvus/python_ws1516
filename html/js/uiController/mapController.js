mainController.mapController = (function() {
	var that = {},
	data = null,
	years = [2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014],
	selectedYear = 2011,
	urlRequest = "http://52.29.118.210:5000/locationCrime/year/" + selectedYear,

	init = function() {
		_initTimefield(years);
		_initEvent();
		_getData();
		return that;
	},

	_initEvent = function() {
        $("#mapButton").click(_buildUrl);
	},

	_buildUrl = function() {
		selectedYear = $("#mapYearSelect").val();
		console.log(selectedYear);
        urlRequest = "http://52.29.118.210:5000/locationCrime/year/" + selectedYear;
        console.log(urlRequest);
        _getData();
	},

	_initTimefield = function(years) {
		var list = document.getElementById("mapYearSelect");
		for(var i = 0; i < years.length; i++) {
			var c = document.createElement('option');
			c.innerHTML = years[i];
			c.value = years[i];
			list.appendChild(c);
		}
	},

	_getData = function() {
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

	_initView = function(data) {
		mapView = mainController.mapView.init(data);
	}

	that.init = init;
	return that;
})();