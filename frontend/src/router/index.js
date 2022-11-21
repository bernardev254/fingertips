import { createRouter, createWebHistory } from "vue-router";
import App from '../App.vue';
import addBookmark from "../views/addBookmark.vue";
import myLogin from "../views/myLogin.vue";
import myRegister from "../views/myRegister.vue";
import myProfile from "../views/myProfile.vue";
import myHome from "../views/myHome.vue";
import myRoot from "../views/myRoot.vue";


const routes = [
    { path: '/index.html', name: "Myapp", component: App },
    {path: '/login', name: "Login", component: myLogin},
    {path: '/register', name: "Register", component: myRegister},
    {path: '/addBookmark', name: "Addbookmark", component: addBookmark},
    {path: '/profile', name: "Profile", component: myProfile},
    {path: '/home', name: "home", component: myHome},
    {path: '/index.html', name: "Home", component: addBookmark},
    {path: '/root', name: 'root', component: myRoot}
    
]
const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
  });
  
export default router;