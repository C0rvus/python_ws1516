mainController.commonCrimeController = (function () {
    var that = {},
        data = null

        init = function () {
            console.log("commonCrimeController is up");
            initEvents;
            getData();
            initView();
            return that;
        },

        initEvents = function () {
          $("#commonCrimeButton").click(getData());
        },

        getData = function () {
          console.log("data");
        },

        initView = function () {
          commonCrimeView = mainController.commonCrimeView.init(data);
        }


    that.init = init;
    return that;
})();
