mainController = {
    init: function (page) {
        mainController.commonCrimeController.init();
        mainController.timeCrimeController.init();
        mainController.arrestCrimeController.init();
        mainController.mapController.init();
    }
};
