angular.module('app', []);

var appCtrl = function ($scope, loc8rData, geolocation) {
    $scope.message = "Checking your location";
}

angular
    .module('app')
    .controller('appCtrl', appCtrl);