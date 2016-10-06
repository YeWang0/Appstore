angular.
  module('appDetail')
  .component('appDetail', {
    templateUrl: 'app-detail/app-detail.template.html',
    controller: ['$routeParams','$rootScope',
      function($routeParams,$rootScope) {
        this.appId = $routeParams.appId;
        this.apps=$rootScope.apps;
        this.selectedApp=$rootScope.selectedApp;
        console.log(this.selectedApp);
        console.log(this.appId);
      }
    ]
  });
