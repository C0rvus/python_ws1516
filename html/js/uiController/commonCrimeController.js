mainController.commonCrimeController = (function () {
    var that = {},
        data = null

        init = function () {
            console.log("commonCrimeController is up");
            getData();
            initView();
            return that;
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
