(function(){
    'use strict';

    angular
        .module('thinkster', [
            'thinkster.config',
            'thinkster.routes',
            'thinkster.layout',
            'thinkster.authentication',
            'thinkster.posts',
            'thinkster.utils'
        ]);
    
    angular
        .module('thinkster.config', []);

    angular
        .module('thinkster.routes', ['ngRoute']);

    angular
        .module('thinkster')
        .run(run);

    /**
     * @name run
     * @desc Update xsrf $http headers to align with Django's defaults
     */
    function run($http){

        $http.defaults.xsrfHeaderName = 'X-CSRFToken';
        $http.defaults.xsrfCookieName = 'csrftoken';
    }
})();
