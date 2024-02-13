import { createRouter, createWebHistory } from 'vue-router'

import LoginView from '../views/LoginView.vue'
import signupView from '../views/signupView.vue'
import verifyEmailView from '../views/VerifyEmailView.vue'

import HomeView from '../views/HomeView.vue'
import NewCategoryView from '../views/NewCategoryView.vue'
import NewItemView from '../views/NewItemView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/add-category',
      name: 'addCategory',
      component: NewCategoryView
    },
    {
      path: '/add-item',
      name: 'addItem',
      component: NewItemView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/signup',
      name: 'signup',
      component: signupView
    },
    {
      path: '/verify-email',
      name: 'verifyEmail',
      component: verifyEmailView
    }
  ]
})


// routes that doesnot require authentication
const noAuthRoutes = ['login', 'signup', 'verifyEmail'];

router.beforeEach((to, from, next) => {

  const accessToken = sessionStorage.getItem("accessToken");
  
  if (!noAuthRoutes.includes(to.name) && !accessToken) {
    next({ name: 'login' });
  } else {
    next();
  }
});

export default router
