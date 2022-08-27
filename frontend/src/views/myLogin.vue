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
    methods: {
        async onLogin(event){
            event.preventDefault();
            await this.login();
        },
        
        async login() {
            const userData = {
                "email": this.email,
                "password": this.password
            };

            this.authData = userData;

            const response = await fetch("http://fingertips.bkaraba.tech/api/v1/auth/login",{
                method: "POST",
                mode: "cors",
                headers: {
                    "content-Type": "application/json",
                },
                body: JSON.stringify(userData)
            });
            const res = await response.json();
                        
            this.email = "";
            this.password ="";
            
            
            if (response.status === 200) {
                this.$router.push("/home");
                
                this.$store.dispatch('saveAccessToken', res.access)

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
    /**background-color:#dadada**/
}
.bts{
    margin:0 25%;
}
#lbl{
    margin-left: 20px;
    margin-top: 20px;
}
.form input{
    width: 80%; 
    height:30px;
    margin:10px 20px;  
    border: 1px solid aqua;
    border-radius: 4px;     
}
.bts .login{
    border-radius: 5px;
    background-color:  #7CAFC4;
    color:white;
    height: 30px;
    width: 20%;
    margin:10px 20px;
    font-size: 14px;
    
}
.bts .signup{
    margin:20px;
    font-size: 14px;
    border-radius: 5px;
    height: 30px;
    background-color:  #199264;
    width: 20%;
    color: white;
}
.bts button:hover{
    background-color: #1E2749;
}
</style>