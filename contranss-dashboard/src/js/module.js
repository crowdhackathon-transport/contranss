angular.module('Dashboard', ['ui.bootstrap', 'ui.router', 'ngCookies', 'uiGmapgoogle-maps', 'ncy-angular-breadcrumb', 'ngResource', 'angularMoment']);

angular.module('Dashboard').config(function(uiGmapGoogleMapApiProvider) {
    uiGmapGoogleMapApiProvider.configure({
        v: '3.17',
        libraries: 'weather,geometry,visualization'
    });
});

angular.module('Dashboard').config(['$breadcrumbProvider', function($breadcrumbProvider) {
    $breadcrumbProvider.setOptions({
      templateUrl: 'templates/breadcrumb.html'
    });
  }
]);

angular.module('Dashboard').constant('angularMomentConfig', {
    timezone: 'Europe/Athens' // optional
});

angular.module('Dashboard').run(function($rootScope, $state, $window, AuthService) {
    $rootScope.$on('$stateChangeStart', function(event, toState, toParams, fromState, fromParams) {
        if (toState.authenticate && !AuthService.isAuthenticated()) {
            console.log('Error');
            event.preventDefault();
            $state.transitionTo('login');
        }
    });
});

angular.module('Dashboard').run(function(Socket) {
    Socket.connect('46.101.249.46', 3000, 'admin', 'admin');
});