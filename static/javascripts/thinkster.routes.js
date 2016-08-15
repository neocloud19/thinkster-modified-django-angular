/**
 * Created by alejo on 17/07/16.
 */
(function(){
    'use strict';

    angular
        .module('thinkster.routes')
        .config(config);

    config.$inject = ['$routeProvider'];

    /**
     * @name config
     * @desc Define valid application routes
     */
    function config($routeProvider){

        $routeProvider.when('/register', {

            controller: 'RegisterController',
            controllerAs: 'vm',
            templateUrl: '/static/templates/authentications/register.html'

        }).when('/login', {

            controller: 'LoginController',
            controllerAs: 'vm',
            templateUrl: '/static/templates/authentications/login.html'

        }).when('/', {

            controller: 'IndexController',
            controllerAs: 'vm',
            templateUrl: '/static/templates/layout/index.html'

        }).otherwise('/');
    }

})();
