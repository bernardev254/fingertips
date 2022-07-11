import { createRouter, createWebHistory } from "vue-router";
import App from '../App.vue';
import addBookmark from "../views/addBookmark.vue";
import myLogin from "../views/myLogin.vue";
import myRegister from "../views/myRegister.vue";
import myProfile from "../views/myProfile.vue";


const routes = [
    { path: '/index.html', name: "Myapp", component: App },
    {path: '/login', name: "Login", component: myLogin},
    {path: '/register', name: "Register", component: myRegister},
    {path: '/addBookmark', name: "Addbookmark", component: addBookmark},
    {path: '/profile', name: "Profile", component: myProfile},
    {path: '/index.html', name: "Home", component: addBookmark}
    
]
const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
  });
  
export default router;