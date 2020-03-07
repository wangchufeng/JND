import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/page/Home'
import Team from '@/page/Team'
import Publication from '@/page/Publication'
import HelloWorld from '@/page/HelloWorld'
import Analysis from '@/page/Analysis'

Vue.use(Router);

export default new Router({
    mode: 'history',
    routes:[
        {
            path: '/',
            name: 'HelloWorld',
            component:HelloWorld
        },
        {
            path: '/analysis',
            name: 'Analysis',
            component:Analysis
        },
        {
            path: '/home',
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