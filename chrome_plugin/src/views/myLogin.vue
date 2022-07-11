<template>
    <myHeader text="Login"/>  
    <div class="form">
            <label id="lbl">Email</label>
            <input type="text" v-model="email" placeholder="username@gmail.com" required/>
            <label id="lbl">Password</label>
            <input type="password" v-model="password" placeholder="password" required/>
            
    </div>
    <button class="login" @click="onLogin">login</button>
    <router-link to="/register"><button>Sign up</button></router-link>
    
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

            const response = await fetch("http://127.0.0.1:5000/api/v1/auth/login",{
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
                this.$router.push("/addBookmark");
                this.$store.dispatch('saveAccessToken', res.user.access)

            }
            else if (response.status === 404) {
                alert("don't have an account?...sign up")
                //this.$router.push('/register')

            }else if (response.status === 401) {
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
    margin: 10px auto;
    width: 100%;
}
#lbl{
    margin-left: 20px;
}
.form input{
    width: 80%; 
    height:30px;
    margin:10px 20px;  
    border: 1px solid aqua;
    border-radius: 4px;     
}
.login{
    border-radius: 5px;
    background-color:  #7CAFC4;
    color:white;
    margin-left: 20px;
    font-size: 14px;
    margin-bottom: 20px;
    margin-right: 50px;
}
.signup{
    margin-left: 20px;
    font-size: 14px;
    margin-bottom: 20px;
    border-radius: 5px;
    color: red;
}
button:hover{
    background-color: #1E2749;
}
</style>