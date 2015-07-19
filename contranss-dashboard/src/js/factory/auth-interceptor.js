angular
  .module('Dashboard')
  .factory('authInterceptor', authInterceptor);

angular.module('Dashboard').config(function($httpProvider) {
  $httpProvider.interceptors.push('authInterceptor');
});

function authInterceptor($rootScope, $q, $window) {
  return {
    request: function(config) {
      config.headers = config.headers || {};
      if ($window.localStorage.token) {
        config.headers.Authorization = 'JWT ' + $window.localStorage.token;
      }
      return config;
    },
    responseError: function(rejection) {
      if (rejection.status === 403) {
        delete $window.localStorage.token;
        delete $window.localStorage.pbx;
        sweetAlert({
          title: 'Oops...',
          text: 'Your login session has expired.',
          type: 'error',
          confirmButtonColor: '#DD6B55',
          confirmButtonText: 'Login Again!'
        }, function() {});
      }
      return $q.reject(rejection);
    }
  };
}