import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/Home.vue'
import Login from '../components/login.vue'
import { getAuth } from "firebase/auth";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/:catchAll(.*)',
      redirect: '/login'
    },
    {
      path: '/',
      redirect: '/login'
    },
    {
      path: '/home',
      name: 'home',
      component: HomeView,
      meta:{
        islogin: true
      }
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    }
  ]
})


router.beforeEach((to, from, next)=>{
  const auth = getAuth();
  let user = auth.currentUser;
  console.log(user);
  let allow = to.matched.some(record => record.meta.islogin);

  if(allow && !user){
    next('/login');
  }else if(!allow && user){
    next('/home');
  }else{
    next();
  }
})

export default router;
