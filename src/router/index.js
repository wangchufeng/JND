import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/page/Home'
import Team from '@/page/Team'
import Publication from '@/page/Publication'

Vue.use(Router);

export default new Router({
    mode: 'history',
    routes:[
        {
            path: '/',
            name: 'Home',
            component:Home
        },
        {
            path: '/team',
            name: 'Team',
            component: Team
        },
        {
            path: '/publication',
            name: 'Publication',
            component: Publication
        }
    ]
})