/**
 * Master Controller
 */
angular.module('Dashboard').controller('MasterCtrl', ['$scope', '$cookieStore', 'uiGmapGoogleMapApi', 'Socket', MasterCtrl]);

function MasterCtrl($scope, $cookieStore, uiGmapGoogleMapApi, Socket) {
    /**
     * Sidebar Toggle & Cookie Control
     */
    var mobileView = 1200;
    $scope.getWidth = function() {
        return window.innerWidth;
    };
    $scope.$watch($scope.getWidth, function(newValue, oldValue) {
        if (newValue >= mobileView) {
            if (angular.isDefined($cookieStore.get('toggle'))) {
                $scope.toggle = !$cookieStore.get('toggle') ? false : true;
            } else {
                $scope.toggle = true;
            }
        } else {
            $scope.toggle = false;
        }
    });
    $scope.toggleSidebar = function() {
        $scope.toggle = !$scope.toggle;
        $cookieStore.put('toggle', $scope.toggle);
    };
    window.onresize = function() {
        $scope.$apply();
    };
}