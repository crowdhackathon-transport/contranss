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
    // Create the badges modal that we will use later
    $ionicModal.fromTemplateUrl('templates/tab-badges.html', {
        scope: $scope
    }).then(function(modal) {
        $scope.modal = modal;
    });
    // Triggered in the badges modal to close it
    $scope.closeBadges = function() {
        $scope.modal.hide();
    };
    // Open the badges modal
    $scope.badges = function() {
        $scope.modal.show();
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
    $scope.info = function(choice) {
        console.log($scope.route_id);
        $state.go('app.browse', {
            id: $scope.route_id
        });
    };
}).controller('TripCtrl', ['$scope', '$state', '$stateParams', '$cordovaGeolocation', '$localStorage', 'Socket', 'Status', 'Routes', '$timeout',
    function($scope, $state, $stateParams, $cordovaGeolocation, $localStorage, Socket, Status, Routes, $timeout) {
        console.log($stateParams.id);
        var vm = $scope;
        Routes.get({
            id: $stateParams.id
        }, function(item) {
            $scope.title = '(' + item.short_name + ') ' + item.long_name;
        });

        function callAtTimeout() {
            var notifications = [];
            Status.page({
                size: 100,
                page: 0,
                route: $stateParams.id
            }, function(status) {
                status.hits.forEach(function(item) {
                    notifications.push(item._source);
                });
            });
            $scope.notifications = notifications;
            console.log('lol');
        }
        callAtTimeout();
        $timeout(callAtTimeout, 5000);
        vm.complaint = function() {
            $state.go('app.complaints', {
                id: $stateParams.id
            });
        };
        vm.back = function() {
            $state.go('app.search');
        };
        vm.map = function() {
            $state.go('app.map', {
                id: $stateParams.id
            });
        };
    }
]).controller('TripStatsCtrl', function($scope, $state, $stateParams, $cordovaGeolocation, Routes, Status) {
    Routes.get({
        id: $stateParams.id
    }, function(item) {
        $scope.title = '(' + item.short_name + ') ' + item.long_name;
    });
    $scope.stop = function() {
        $state.go('app.browse', {
            id: $stateParams.id
        });
    };
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
    $scope.post = post;
}).controller('NotificationCtrl', function($scope, $state, $stateParams, $timeout, Status) {
    function callAtTimeout() {
        var notifications = [];
        Status.page({
            size: 100,
            page: 0
        }, function(status) {
            status.hits.forEach(function(item) {
                notifications.push(item._source);
            });
        });
        $scope.notifications = notifications;
        console.log('lol');
    }
    callAtTimeout();
    $timeout(callAtTimeout, 5000);
}).controller('MapCtrl', function($scope, $state, $stateParams, $timeout, uiGmapGoogleMapApi, Status, Socket, Routes) {
    $scope.map = {
        center: {
            latitude: 37.966667,
            longitude: 23.716667
        },
        zoom: 10
    };
    $scope.routes = [];
    uiGmapGoogleMapApi.then(function(maps) {
        Socket.onMessage(function(topic, message) {
            var topic_tokens = topic.split("/");
            Routes.get({
                id: topic_tokens[1]
            }, function(item) {
                var msg = JSON.parse(message.toString());
                var route = null;
                for (var i = 0; i < $scope.routes.length; i++) {
                    if ($scope.routes[i].id == topic_tokens[1]) {
                        route = $scope.routes[i];
                    }
                }
                $scope.title = '(' + item.short_name + ') ' + item.long_name;
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
                $scope.$apply();
            });
        });
        Socket.subscribe('track/' + $stateParams.id + '/1');
    });
    $scope.back = function() {
        $state.go('app.browse', {
            id: $stateParams.id
        });
    };
});