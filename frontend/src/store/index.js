import { createStore } from 'vuex';
import router from '../router';



// Create a new store instance.
const store = createStore({
  state() {
      return {
        token: !!localStorage.getItem('myToken')
        
    }
  },
  mutations: {
    setToken(state, token) {
      state.token = token;
    },
    logout(state){
      state.token = "";
      localStorage.removeItem('myToken')
      router.push("/login")
    }
  },
  getters:{
    loggedIn: state => !!state.token
  },
  actions: {
    saveAccessToken(context, access) {
      context.commit('setToken', access)
    },
    logout({commit}){
      commit('logout')
    }
  }
});
export default store