angular.module('starter.controllers', []).controller('AppCtrl', function($scope, $ionicModal, $timeout) {
    // With the new view caching in Ionic, Controllers are only called
    // when they are recreated or on app start, instead of every page change.
    // To listen for when this page is active (for example, to refresh data),
    // listen for the $ionicView.enter event:
    //$scope.$on('$ionicView.enter', function(e) {
    //});
    // Form data for the login modal
    $scope.loginData = {};
    // Create the login modal that we will use later
    $ionicModal.fromTemplateUrl('templates/login.html', {
        scope: $scope
    }).then(function(modal) {
        $scope.modal = modal;
    });
    // Triggered in the login modal to close it
    $scope.closeLogin = function() {
        $scope.modal.hide();
    };
    // Open the login modal
    $scope.login = function() {
        $scope.modal.show();
    };
    // Perform the login action when the user submits the login form
    $scope.doLogin = function() {
        console.log('Doing login', $scope.loginData);
        // Simulate a login delay. Remove this and replace with your login
        // code if using a login system
        $timeout(function() {
            $scope.closeLogin();
        }, 1000);
    };
}).controller('PlaylistsCtrl', function($scope) {
    $scope.playlists = [{
        title: 'Reggae',
        id: 1
    }, {
        title: 'Chill',
        id: 2
    }, {
        title: 'Dubstep',
        id: 3
    }, {
        title: 'Indie',
        id: 4
    }, {
        title: 'Rap',
        id: 5
    }, {
        title: 'Cowbell',
        id: 6
    }];
}).controller('PlaylistCtrl', function($scope, $stateParams) {}).controller('StartCtrl', function($scope, $state, $stateParams, Routes) {
    $scope.search = function(query) {
        Routes.search({
            "search": query
        }, function(data) {
            console.log(data);
            $scope.routes = data.results;
        });
    };
    $scope.route_id = "";
    $scope.change_route = function(id) {
        $scope.route_id = id;
        console.log($scope.route_id);
    };
    $scope.search("");
    $scope.start = function(choice) {
        console.log($scope.route_id);
        var route_id = $scope.route_id;
        $scope.route_id = null;
        $state.go('app.browse', {
            id: route_id
        });
    };
}).controller('TripCtrl', ['$scope', '$state', '$stateParams', '$cordovaGeolocation', '$localStorage', 'Socket', 'Status',
    function($scope, $state, $stateParams, $cordovaGeolocation, $localStorage, Socket, Status) {
        var post = function(post_type) {
            var posOptions = {
                timeout: 10000,
                enableHighAccuracy: false
            };
            $cordovaGeolocation.getCurrentPosition(posOptions).then(function(position) {
                var post = {
                    "timestamp": new Date(),
                    "type": post_type,
                    "route": $stateParams.id,
                    "comment": "Demo text",
                    "coords": [position.coords.longitude, position.coords.latitude],
                    "user": {
                        "id": 1,
                        "name": "George Theofilis",
                        "type": "passenger"
                    }
                };
                Status.add_status({}, post, function(data) {
                    console.log(data);
                });
            }, function(err) {
                // error
            });
        };
        post(8);

        function distance(lat1, lon1, lat2, lon2, unit) {
            var radlat1 = Math.PI * lat1 / 180;
            var radlat2 = Math.PI * lat2 / 180;
            var radlon1 = Math.PI * lon1 / 180;
            var radlon2 = Math.PI * lon2 / 180;
            var theta = lon1 - lon2;
            var radtheta = Math.PI * theta / 180;
            var dist = Math.sin(radlat1) * Math.sin(radlat2) + Math.cos(radlat1) * Math.cos(radlat2) * Math.cos(radtheta);
            dist = Math.acos(dist);
            dist = dist * 180 / Math.PI;
            dist = dist * 60 * 1.1515;
            if (unit == "K") {
                dist = dist * 1.609344;
            }
            if (unit == "N") {
                dist = dist * 0.8684;
            }
            return dist;
        }

        function bearing(lat1, lon1, lat2, lon2) {
            var dLon = (Math.PI * (lon2 - lon1)) / 180;
            lat1 = Math.PI * lat1 / 180;
            lat2 = Math.PI * lat2 / 180;
            var y = Math.sin(dLon) * Math.cos(lat2);
            var x = Math.cos(lat1) * Math.sin(lat2) - Math.sin(lat1) * Math.cos(lat2) * Math.cos(dLon);
            var rad = Math.atan2(y, x);
            var brng = rad * 180 / Math.PI;
            return (brng + 360) % 360;
        }
        var vm = $scope;
        var watchId = {},
            watchOptions = {
                frequency: 20 * 60 * 1000,
                timeout: 5 * 60 * 1000,
                enableHighAccuracy: false
            };
        watchId = $cordovaGeolocation.watchPosition(watchOptions);
        watchId.then(null, function(err) {
            console.log(err);
        }, function(position) {
            var position_serialized = {
                timestamp: position.timestamp,
                coords: {
                    accuracy: position.coords.accuracy,
                    altitude: position.coords.altitude,
                    altitudeAccuracy: position.coords.altitudeAccuracy,
                    latitude: position.coords.latitude,
                    longitude: position.coords.longitude,
                    heading: position.coords.heading,
                    speed: position.coords.speed
                }
            };
            var previus_position = $localStorage.getObject('previus_position', JSON.stringify(position_serialized));
            var coords = $localStorage.getObject('coords', '[]');
            if (coords.length > 0) {
                if (previus_position) {
                    // If dt is lower than a second ignore the observation.
                    if (Math.abs(position_serialized.timestamp - previus_position.timestamp) < 1000) {
                        return;
                    }
                    // If the object not moved ignore the observation.
                    var lat = position.coords.latitude,
                        lon = position.coords.longitude;
                    if (previus_position.coords.latitude === lat && previus_position.coords.longitude === lon) {
                        console.log('Not moved');
                        return;
                    }
                }
            }
            // Calculate speed and heading
            position_serialized.coords.distance = distance(previus_position.coords.latitude, previus_position.coords.longitude, position.coords.latitude, position.coords.longitude, 'K');
            position_serialized.coords.bearing = bearing(previus_position.coords.latitude, previus_position.coords.longitude, position.coords.latitude, position.coords.longitude);
            coords.unshift(position_serialized);
            // Keep only last twenty observation on system cache. 
            if (coords.length > 20) {
                coords.pop();
            }
            // Update view model
            vm.coords = coords;
            Socket.publish('track/' + $stateParams.id + '/1', JSON.stringify(position_serialized));
            // Save the observations on LocalStorage (Cached)
            $localStorage.setObject('keyGPS', watchId);
            $localStorage.setObject('coords', coords);
            $localStorage.setObject('previus_position', position_serialized);
        });
        vm.coords = $localStorage.getObject('coords', '[]');
        vm.stop = function() {
            watchId.clearWatch();
            post(9);
            $state.go('app.stats');
        };
        vm.post = post;
    }
]).controller('TripStatsCtrl', function($scope, $state, $stateParams) {
    $scope.ok = function() {
        $state.go('app.search');
    };
});