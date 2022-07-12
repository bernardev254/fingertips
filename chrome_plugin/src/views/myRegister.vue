<template>
<div class="container">
    <myHeader text="Header"/>
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
    width: 100%;    

}
.form p{
    margin-top: 5px;
}
.input{
    display: flex;
    flex-direction: column;
}
#lbl{
    margin-left: 20px;
}
.input input{
    width: 80%; 
    height:30px;
    margin:10px 20px ;  
    border: 1px solid aqua;
    border-radius: 4px;     
}
.register{
    border-radius: 5px;
    background-color:  #7CAFC4;
    color:white;
    margin-left: 20px;
    font-size: 14px;
    margin-bottom: 20px;
    margin-right: 50px;
}
.login{
    margin-left: 20px;
    font-size: 14px;
    margin-bottom: 20px;
    border-radius: 5px;
    color: white;
    background-color: rgb(0, 183, 255);
}
button:hover{
    background-color: #1E2749;
    transform: translate(-1px, -1px);
}
</style>