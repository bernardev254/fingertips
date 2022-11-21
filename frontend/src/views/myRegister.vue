<template>
<div class="container">
    <myHeader text="Register"/>
    <div class="form">
        <div class="input">
            <label id="lbl">Username</label>
            <input v-model="username" type="text" placeholder="Username" required/>
            <label id="lbl">Email</label>
            <input v-model="email" type="text" placeholder="username@gmail.com" required/>
            <label id="lbl">Password</label>
            <input v-model="password" type="password" placeholder="password" required/>
            
            

        </div>
        <button class="register" @click="onFinish">Register</button>
        <button class="login" @click="login">login</button>

    </div>
</div>
</template>
<script>
import myHeader from '../components/myHeader.vue'
export default{
    name: "myRegister",
    components:{
        myHeader,
    },
    data(){
        return{
            username: '',
            email: '',
            password: ''
        }
    },
    methods: {
        async onFinish(event){
            event.preventDefault();

            await this.getUserData();
        },
        login(){
            this.$router.push('/login')
        },
        
        async getUserData() {
            const userData = {
                "username": this.username,
                "email": this.email,
                "password": this.password
            };

            const response = await fetch("http://127.0.0.1:5000/api/v1/auth/register",{
                method: "POST",
                mode: "cors",
                headers: {
                    "content-Type": "application/json",
                },
                body: JSON.stringify(userData)
            });
            const res = await response.json();
            
            this.username = "";
            this.email = "";
            this.password ="";
            
            if (response.status === 201) {
                this.$router.push('/login')

            }
            if (response.status === 400) {
                    alert(res.error)
                }
                //alert("all fields are mandatory")
            }

        }

    }

</script>
<style scoped>
.form{
    width: 50%;
    margin: 0 25%;  

}
.form p{
    margin-top: 5px;
}
.input{
    margin-top: 30px;
    display: flex;
    flex-direction: column;
}
#lbl{
    margin-left: 20px;
    font-size: 20px;
}
.input input{
    width: 80%; 
    height:50px;
    margin:10px 20px ;  
    border-radius: 4px;
    background-color: rgb(232, 240, 254);
    border: none;   
}
.register{
    border-radius: 5px;
    background-color: rgb(6, 70, 27);
    color:white;
    width: 40%;
    height: 50px;
    margin-left: 20px;
    font-size: x-large;
    margin-bottom: 20px;
    margin-right: 50px;
    margin-top: 15px;
    
}
.login{
    margin-left: 20px;
    font-size: 24px;
    margin-bottom: 20px;
    border-radius: 5px;
    width: 30%;
    height: 50px;
    color: white;
    background-color:  #7CAFC4;
}
button:hover{
    background-color: #1E2749;
    transform: translate(-1px, -1px);
}
</style>