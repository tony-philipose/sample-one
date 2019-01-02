import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import load from '@/components/load'
import home from '@/components/home'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/h',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/',
      name: 'loading',
      component: load
    },
    {
      path: '/home',
      name: 'home',
      component: home
    }
  ]
})
