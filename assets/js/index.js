window.$ = window.jQuery = require('jquery');
require('bootstrap-sass');
import Vue from 'vue';
import VueResource from 'vue-resource'
Vue.use(VueResource);

import Demo from "./components/Demo.vue";
import Risklist from "./components/Risklist.vue";

const app = new Vue({
    el: '#app',
    components: {
        Demo,
        Risklist
    }
});