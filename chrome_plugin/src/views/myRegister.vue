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
            <button @click="onFinish">Finish</button>
            

        </div>

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
            await response.json();
            
            this.username = "";
            this.email = "";
            this.password ="";
            
            if (response.status === 201) {
                await this.$router.push('/login')

            }
            if (response.status === 400) {
                this.$router.push("/login");
                //alert("all fields are mandatory")
            }

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
button{
    width: 50%; 
    margin:20px auto;
    height: 25px;
    border-radius: 5px;
    background-color:  #7CAFC4;
    color:white;
    font-size: 14px;
    padding:3px 0;
}
button:hover{
    background-color: #1E2749;
}
</style>