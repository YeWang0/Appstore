angular.
  module('huaweiApp').
  config(['$locationProvider', '$routeProvider',
    function config($locationProvider, $routeProvider) {
      $locationProvider.hashPrefix('!');

      $routeProvider.
        when('/apps', {
          template: '<app-head></app-head><app-tool></app-tool>'
        }).
        when('/apps/:appId', {
          template: '{{$ctrl.appId}} <app-head></app-head><app-detail></app-detail>'
        }).
        otherwise('/apps');
    }
  ]);