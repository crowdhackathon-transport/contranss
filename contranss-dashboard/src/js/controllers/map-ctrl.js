/**
 * Master Controller
 */
angular.module('Dashboard').controller('MapCtrl', ['$scope', '$cookieStore', 'uiGmapGoogleMapApi', 'Socket', 'Routes', MapCtrl]);

function MapCtrl($scope, $cookieStore, uiGmapGoogleMapApi, Socket, Routes) {
    $scope.map = {
        center: {
            latitude: 37.966667,
            longitude: 23.716667
        },
        zoom: 10
    };
    $scope.windowoptions = {
        pixelOffset: new google.maps.Size(0, 0, 'px', 'px')
    };
    $scope.marker = {
        latitude: 37.966667,
        longitude: 23.716667
    };
    $scope.routes = [];
    uiGmapGoogleMapApi.then(function(maps) {
        Socket.onMessage(function(topic, message) {
            var topic_tokens = topic.split("/");
            Routes.get({
                id: topic_tokens[1]
            }, function(item) {
                var msg = JSON.parse(message.toString());
                // $scope.map = {
                //     center: {
                //         latitude: msg.coords.latitude,
                //         longitude: msg.coords.longitude
                //     }
                // };
                var route = null;
                console.log($scope.routes);
                for (var i = 0; i < $scope.routes.length; i++) {
                    if ($scope.routes[i].id == topic_tokens[1]) {
                        route = $scope.routes[i];
                    }
                }
                if (route) {
                	route.latitude = msg.coords.latitude;
                    route.longitude = msg.coords.longitude;
                } else {
                    route = {
                        id: topic_tokens[1],
                        short_name: item.short_name,
                        text_color: item.text_color,
                        color: item.color,
                        latitude: msg.coords.latitude,
                        longitude: msg.coords.longitude,
                        show: false,
                        time: msg.timestamp
                    };
                    route.onClick = function() {
                        route.show = !route.show;
                    };
                    $scope.routes.push(route);
                }
                console.log($scope.routes);
            });
            $scope.$apply();
        });
        Socket.subscribe('track/#');
    });
}