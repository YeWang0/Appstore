'use strict';

// Define the `phonecatApp` module
angular.module('huaweiApp', [
  // ...which depends on the `phoneList` module
  'appDetail',
  'appTool',
  'ngRoute',
  'appHead',
  'ngMaterial'
])
// .service('appsService', function() {
//     this.get_apps=function(){

//     }

// }) 
.factory('appsService', function($http) {
  return {
    async: function() {
      return $http.get('apps/apps.json');  //1. this returns promise
    }
  };
})
.controller('AppCtrl', function(appsService,$scope,$rootScope,$filter) {
  // $scope.imagePath = 'img/washedout.png';
    $scope.apps= [];
    $scope.currentPage = 0;
    $scope.pageSize = 40;

    appsService.async().then(function(d) { //2. so you can use .then()
      console.log("success!");
      $scope.apps = d.data;
      $rootScope.apps=$scope.apps;
    });
    
    $scope.getData = function () {
      // needed for the pagination calc
      // https://docs.angularjs.org/api/ng/filter/filter
      return $filter('filter')($scope.apps, $scope.query);
    }

    $scope.numberOfPages=function(){
        return Math.ceil($scope.getData().length/$scope.pageSize);                
    }



    $scope.getAppData = function(data) {
        $rootScope.selectedApp=data;
    } 


}
)
.filter('startFrom', function() {
    return function(input, start) {
        start = +start; //parse to int
        return input.slice(start);
    }
})
.config(function($mdThemingProvider) {
  $mdThemingProvider.theme('dark-green').backgroundPalette('green').dark();
  $mdThemingProvider.theme('dark-red').backgroundPalette('red').dark();
  $mdThemingProvider.theme('dark-amber').backgroundPalette('amber').dark();
  $mdThemingProvider.theme('dark-pink').backgroundPalette('pink').dark();
  $mdThemingProvider.theme('dark-orange').backgroundPalette('orange').dark();
  $mdThemingProvider.theme('dark-purple').backgroundPalette('deep-purple').dark();
  $mdThemingProvider.theme('dark-blue').backgroundPalette('blue').dark();
  $mdThemingProvider.theme('dark-blue-grey').backgroundPalette('blue-grey').dark();
  $mdThemingProvider.theme('dark-teal').backgroundPalette('teal').dark();
});
