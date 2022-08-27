<template>
   <router-view></router-view>
   <myFooter/>
   </template>

<script>
//import myProfile from './components/myProfile.vue'
//import myLogin from './components/myLogin.vue'
//import addBookmark from './components/addBookmark.vue'
//import myRegister from './components/myRegister.vue'
import myFooter from './components/myFooter.vue'
export default {
  name: 'App',
  components: {
    myFooter,
  },
  created(){
    this.$router.push('/login');
  }
}
</script>

<style scoped>
*{
    padding: 0;
    margin: 0;
    /*box-sizing: border-box;*/
    min-width: 300px;
    }
#app{
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
    border: 1px solid steelblue;
    margin: auto;
    color: #2c3e50;
}
</style>
