<template>
    <myHeader text="Added Bookmark"/>
    <router-link to="/profile"> <span v-if="token" class="profile">profile</span></router-link>
      <div class="input">
        <label id="lbl">Name</label>
        <input type="text" v-model="title" required/>
        <label id="lbl">Url</label>
        <input type="text" v-model="url" required/>
        <label id="lbl">description</label>
        <textarea type="text" v-model="desc" placeholder="Saysomething about your bookmark"></textarea>
        <label id="lbl">category</label>
        <input type="text" v-model="category" placeholder="sort"/>
        <button v-if="loggedIn" class="save" @click="onSave">Save</button>
        <button v-else class="save" @click="onSave">login</button>


        
       

     </div>
</template>
<script>
import myHeader from '../components/myHeader.vue'
export default{
    name: "addBookmark",
    components:{
        myHeader,
    },
    data() {
        return {
            title: "",
            url: "",
            desc: "",
            category: "",
            icon: "",
            token: this.$store.state.token,
            saved: false,
            tabs: [],
            index: Number
            
        }

    },
    async created() {     
        await this.loadBookmark()
    },
    computed:{
        loggedIn(){
            return this.$store.getters.loggedIn
        },
    },
    methods: {
        async loadBookmark() { 
            await chrome.tabs.query({active: true, currentWindow: true}, tabs => {
                let activeTab = tabs[0];
                let title = activeTab.title;
                let url = activeTab.url;
                let icon = activeTab.favIconUrl;
                this.title = title,
                this.url = url,
                this.desc = title,
                this.icon = icon,
                this.category = "chrome-bookmark"
            });
        },   
        async onSave(event) {
            event.preventDefault();
            if (this.loggedIn)  {
                await this.saveBookmark();
                //this.$router.push('/profile');
            }
            else{
                this.$router.push('/login');
            }
            
                        
        },
        async saveBookmark() {
            if (!this.loggedIn) {
                this.$router.push('/login');
            }
            
            const bookmark = {
                "title":this.title,
                "url": this.url,
                "body": this.desc,
                "category": this.category,
                "icon": this.icon
            };

            const response = await fetch("http://127.0.0.1:5000/api/v1/bookmarks/new", {
                method: 'POST',
                mode: 'cors',
                headers: {
                    "content-Type": "application/json",
                    "Authorization": "Bearer "+this.token
                },
                body: JSON.stringify(bookmark),
            });   

            if (response.status == 401) {
                alert("not found");
            }
            else if (response.status === 201) {
                this.saved = true;
            }
            else if (response.status === 203){
                alert("not created");
            }

            this.title = "";
            this.url = "";
            this.desc = "";
            this.icon = "";
            this.category = "";
        },
    }          
            

}

</script>

<style scoped>
.input{

    display: flex;
    flex-direction: column;
    justify-content: center;
    margin-top: 30px;
}
#lbl{
    text-align: start;
    margin-left: 20px;
}
.input {
    width: 80%; 
    height:30px; 
    border: 1px solid aqua;
    border-radius: 4px;
    margin: auto;     
}
.input textarea
{
    resize: none;
    max-width: 80%;
    min-width: 80%;
    min-height: 50px;
    max-height: 50px;
}
.save{
    width: 50%; 
    margin: 20px auto;
    height: 25px;
    border-radius: 5px;
    background-color: #7CAFC4;
    color: white;
    font-size: 14px;
    padding:3px 0;

}.profile{
    width: 25%; 
    margin-top: 5px;
    height: 25px;
    border-radius: 5px;
    background-color:  white;
    color: #48cae4;
    font-size: 14px;
    float: right;
}
.save:hover{
    background-color: #1E2749;

}
.profile:hover{
    color: #76c893;
    transform: translate(-4px, -4px);
}

</style>