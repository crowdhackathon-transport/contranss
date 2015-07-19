/**
 * Route configuration for the RDash module.
 */
angular.module('Dashboard').config(['$stateProvider', '$urlRouterProvider',
    function($stateProvider, $urlRouterProvider) {
        // For unmatched routes
        $urlRouterProvider.otherwise('/');
        // Application routes
        $stateProvider
            .state('dashboard', {
              abstract: true,
              templateUrl: 'templates/dashboard.html',
              authenticate: true
            })
            .state('dashboard.index', {
                url: '/',
                templateUrl: 'templates/index.html',
                // authenticate: true,
                ncyBreadcrumb: {
                    label: 'Αρχική / Πίνακας Ελέγχου'
                }
            }).state('dashboard.reports', {
                url: '/reports',
                templateUrl: 'templates/tables.html',
                // authenticate: true,
                ncyBreadcrumb: {
                    label: 'Ανάλυση Δεδομένων'
                }
            }).state('login', {
                url: '/login',
                templateUrl: 'templates/login.html',
                authenticate: false
            }).state('register', {
                url: '/register',
                templateUrl: 'templates/register.html',
                authenticate: false
            });
    }
]);