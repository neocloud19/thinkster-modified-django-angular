/**
* Register controller
* @namespace thinkster.authentication.controllers
*/
(function(){
    'use strict()';

    angular
        .module('thinkster.authentication.controllers')
        .controller('RegisterController', RegisterController);

    RegisterController.$inject = ['$location', '$scope', 'Authentication'];

    /**
     * @namespace RegisterController
     */
    function RegisterController($location, $scope, Authentication){
        var vm = this;

        vm.register = register;
        
        activate();

        /**
         * @name activate
         * @desc Actions to be performed when this controller is instantiated
         * @memberOf thinkster.authentication.controllers.RegisterController
         */
         function activate() {
            // If the user is authenticated, they should not be here.

            console.log('activating');

            if (Authentication.isAuthenticated()) {

                console.log('routing to index');
                $location.url('/');
            }
        }

        /**
         * @name register
         * @desc Register a new user
         * @memberOf thinkster.authentication.controller.RegisterController
         */
        function register(){
            Authentication.register(vm.email, vm.password, vm.username);
        }
    }

})();