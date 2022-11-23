<template>
    <!--router-link to="/profile"> <span v-if="token" class="profile">profile</span></router-link-->
    <div class="head">
        <div class="logo">
            <div class="logo-img">
                <img src="../assets/logo.png">
            </div>
            <div class="name">
                <b> Fingertips</b>
            </div>
            
            
        </div>
        <button @click="openMyApp">open app</button>
    </div>
    
    
    <div class="main">
        <div class="left">
            <p>Fingertips Bookmarking Manager</p>
                
            <h2>...all your bookmarks on your fingertips</h2>
            <div class="foot">
                <button @click="openMyApp"> open app</button>
                <button @click="register">Get started</button>
            </div>
        </div>
        <div class="right">
            <img src="../assets/fingertips.png">                        
        </div>
        
    </div> 
</template>

<script scoped>
export default{
    name: "myRoot",
    components:{},

    methods:{
        openMyApp(){
            this.$router.push('/login')
    },
    register(){
        this.$router.push('/register')
    }
}
}
</script>

<style scoped>
.head{
    display: flex;
    justify-content: space-between;
    height: 7%;
}.head .logo{
    height: 100%;    
}
.head .logo .logo-img{
    margin-left: 0;
    object-fit: contain;
    
}
.head .logo .logo-img img{
  object-fit: contain;
  vertical-align: middle;
  margin-top: -20%;  
  margin-left: -10%;
  height:150px;
  width: 150px;
}
.head .logo .name{
    color:rgb(43, 43, 109);
    font-size: 30px;
    margin-left: 75%;
    margin-top: -58%;
}
.head button{
    margin-top: .2%;
    margin-left: 5%;
    height: 50px;
    width: 120px;
    background: rgb(5, 3, 29);
    font-size: x-large;
    color: rgb(178, 210, 218);
}

.main{
    display: flex;
    height: 100%;

}
.main .left{
    flex:2;
    height: 100%;
    margin-left: 5%;
    margin-top: 1%;
   
}
.main .left p{
    font-size: 50px;
    font-weight: bolder;
    color: rgb(3, 27, 63);
}
.main .left h2{
    margin-left: 15%;
    font-weight: bolder;
}
.main .left button{
    margin-top: 20%;
    margin-left: 15%;
    height: 50px;
    width: 150px;
    background: rgb(5, 3, 29);
    font-size: x-large;
    color: rgb(178, 210, 218);
}
.main .right{
    flex: 1;
    margin-top: 1%;  
    background-color: rgba(94, 10, 10, 0);
}

.main .right img{
    height: 90%;    
    width: 98%;
    object-fit: contain;
    z-index: 5;
    border-radius: 5%;
    border: 1px  bold rgb(0, 0, 0);
}
</style>