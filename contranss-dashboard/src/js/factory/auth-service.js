angular
	.module('Dashboard')
	.factory('AuthService', AuthService);

function AuthService($rootScope, $q, $window) {
    return {
        isAuthenticated: function() {
            return $window.localStorage.token;
        }
    };
}