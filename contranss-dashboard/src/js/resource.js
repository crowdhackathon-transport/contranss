angular.module('Dashboard')

.factory('Routes', function($resource) {
  return $resource('http://46.101.249.46/api/routes/:id/', {
		id: '@_id'
	},{
		search: {
			method: 'GET',
			url: 'http://46.101.249.46/api/routes/?search=:search',
			params: {				
				// page: '@_page',
				search: '@_search'
			},
			headers: {
				'Content-Type': 'application/json'
			}
		}
	}, {
		stripTrailingSlashes: false
	});
})

.factory('Status', function($resource) {
  return $resource('http://46.101.249.46/api/status/', {
		id: '@_id'
	},{
		page: {
			method: 'GET',
			url: 'http://46.101.249.46/api/status/?page=:page&size=:size',
			params: {				
				// page: '@_page',
				page: '@_page',
				size: '@_size'
			},
			headers: {
				'Content-Type': 'application/json'
			}
		}
	}, {
		stripTrailingSlashes: false
	});
});