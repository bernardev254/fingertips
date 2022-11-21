<template>
    <myHeader text="Login"/>  
    <div class="form">
            <label id="lbl">Email</label>
            <input type="text" v-model="email" placeholder="username@gmail.com" required/>
            <label id="lbl">Password</label>
            <input type="password" v-model="password" placeholder="password" required/>          
    </div>
    <div  class="bts">
        <button class="login" @click="onLogin">login</button>
        <router-link to="/register"><button class="signup">Sign up</button></router-link>
    </div>
    
    
</template>
<script>
import myHeader from '../components/myHeader.vue'


export default{
    name: "myLogin",
    components:{
        myHeader,
    },
    
    data() {
        return {
            email: "",
            password: "",
            authData: Object
        }
    },
   computed: {
        token(){
            return this.$store.state.token
        }
        
    },
    methods: {      
        async onLogin(event){
            event.preventDefault();
            await this.login();
        }
    ,
        
        async login() {
            const userData = {
                "email": this.email,
                "password": this.password
            };

            this.authData = userData;

            const response = await fetch("http://127.0.0.1:5000/api/v1/auth/login",{
                method: "POST",
                mode: "cors",
                headers: {
                    "content-Type": "application/json",
                },
                body: JSON.stringify(userData)
            });
            // eslint-disable-next-line
            const res = await response.json();
                        
            this.email = "";
            this.password ="";
            
            
            if (response.status === 200) {
                console.log(this.token)
                if (!this.token){
                    localStorage.setItem('myToken', res.access)
                }                    
                let access = localStorage.getItem("myToken");            
                this.$store.dispatch('saveAccessToken', access)
                console.log(this.token)
                this.$router.push("/home");
                

            }
            else if (response.status === 404) {
                alert("don't have an account?...sign up")
            }

            else if (response.status === 401) {
                alert("wrong credentials");
            }

        },
    }


}
</script>
<style scoped>

.form{ 
    display: flex;
    flex-direction: column;
    margin: 0 25%;
    width: 50%;
    
   
}
.bts{
    margin:0 25%;
}
#lbl{
    margin-left: 20px;
    margin-top: 20px;
    font-size: 20px;
}
.form input{
    width: 80%; 
    height:60px;
    margin:10px 20px;  
    border: none;
    border-radius: 4px;     
}
.bts .login{
    border-radius: 5px;
    background-color:  #199264;
    color:white;
    height: 60px;
    width: 50%;
    margin:10px 20px;
    font-size: x-large;
    border: none;
    
    
}
.bts .signup{
    margin:20px;
    font-size: large;
    border-radius: 5px;
    height: 60px;
    background-color:  #7CAFC4;
    width: 25%;
    color: white;
    border: none;
}
.bts button:hover{
    background-color: #1E2749;
}
</style>