/**
 * Created by alejo on 17/07/16.
 */
(function(){
    'use strict';

    angular
        .module('thinkster.authentication', [
            'thinkster.authentication.controllers',
            'thinkster.authentication.services'
        ]);

    angular
        .module('thinkster.authentication.controllers', []);

    angular
        .module('thinkster.authentication.services', ['ngCookies']);

})();