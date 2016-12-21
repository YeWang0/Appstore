angular.
  module('appDetail')
  .component('appDetail', {
    templateUrl: 'app-detail/app-detail.template.html',
    controller: ['$routeParams','$rootScope',
      function($routeParams,$rootScope) {
        this.appId = $routeParams.appId;
        this.apps=$rootScope.apps;
        // console.log($rootScope.apps);
        if(this.appId==$rootScope.selectedApp.app_id)
          this.selectedApp=$rootScope.selectedApp;
        else{
          var i=0;
          while(i<$rootScope.apps.length){
              if($rootScope.apps[i].app_id==this.appId){
                this.selectedApp=$rootScope.apps[i];
                break;
              }
              i++;
          }
        }
        // console.log(this.selectedApp);
        // console.log(this.appId);
      }
    ]
  });
