<template>
    <!--router-link to="/profile"> <span v-if="token" class="profile">profile</span></router-link-->
    <p id="name" class="others"><b>Fingertips</b></p>
    
    <div class="container">
        <nav class="nav-bar">
            <img src="../assets/img.png" alt="Avatar" class="others" id="avatar"/>
            
            <div class="others">
                <div><b>All bookmarks</b></div>
                <p>unsorted</p>
                <p>personal</p>
                <p>projects</p>
                <p>todos</p>
            </div>

        </nav>
        <div class="main">
            <div class="contents">
                <div class="add">
                    <button @click="my_add()">+ Add</button>
                 </div>   
                <div class="overlay" v-if="over">
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

                
                <div class="books" @click="preview(event, bookmark.url)" :key="bookmark.id" v-for="bookmark in my_bookmarks.bookmarks">
                    <div v-if="display" class="left">
                        <img :src="bookmark.icon" alt="img"/>
                    </div>
                    <div v-if="display" class="right">
                        <h3><b>{{bookmark.title}}</b></h3>
                        <p>{{bookmark.body}}</p>
                        <div class="options">
                            <router-link :to=bookmark.url target="_blank">visit</router-link>
                            <button class="deleteme" @click="del(bookmark.id)">delete</button>
                            <button class="updateme" @click="up(bookmark.id)">update</button>
                        </div>
                    </div>
                </div>
            </div>
            <div :style="toggleStyle" class="web" id="web">
                <div class="page" v-html="page">
                </div>
            </div>
        </div>
    </div>
    
</template>
<script scoped>

export default{
    name: "myHome",
    components:{
    
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
            index: Number,
            my_bookmarks: [],
            display: true,
            page: null,
            isactive: false,
            show: false,
            over: false,
        }

    },
    async created() {
        await this.getBookmarks();
        await this.get_tabs()     
        await this.loadBookmark()
        this.index = setTimeout('getIdex', 3000)
    },
    computed:{
        loggedIn(){
            return this.$store.getters.loggedIn
        },
        getIndex(){
            return this.getActiveTabsIndex(this.tabs)
        },
        toggleStyle(){
            if (this.show) {
                return {
                flex: 1,
                }
            }
            return{
                flex: 0,
            }
            
        },
        
    },
    methods: {
        my_add(){
            this.over = !this.over;
        },
        async fetchBookmarks() {
                const res= await fetch ("http://fingertips.bkaraba.tech/api/v1/bookmarks/my_bookmarks",{
                    headers:{
                        "Authorization": "Bearer "+this.token
                    }
                });
                const my_bookmarks = await res.json();
                return(my_bookmarks);
        
        },
        async preview($event, url){
            this.show = true
            const data ={"url":url}
            const res = await fetch("http://fingertips.bkaraba.tech/api/v1/auth/proxy",{
                method: 'POST',
                mode: 'cors',
                headers: {
                    'content-Type':'application/json'
                },
                body:JSON.stringify(data)
            })
            let reader = res.body.getReader()
            let html = await reader.read()
            this.page = new TextDecoder().decode(html.value)
            //let bl = await res.blob()
            //const page = await bl.text()
            //this.page = page
            
        },
        getActiveTabsIndex(){
            for (let idx = 0; idx < this.tabs.length; idx++){
                if (this.tabs[idx].active){
                    return idx
                }
            }
        },
        async getBookmarks() {
                if (this.token){
                    this.my_bookmarks = await this.fetchBookmarks();
                    if (!this.my_bookmarks) alert("you do not have any bookmark please add one")
                }
        },
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
            async get_tabs(){
                await chrome.tabs.query({}, tabs => {
                    this.tabs = tabs
                })
            },
            
            reloadBookmark(idx){
                let activeTab = this.tabs[parseInt(idx)];
                let title = activeTab.title;
                let url = activeTab.url;
                let icon = activeTab.favIconUrl;
                this.title = title,
                this.url = url,
                this.desc = title,
                this.icon = icon,
                this.category = "chrome-bookmark"
            },
            next(){
                if (this.index < this.tabs.length - 1){
                    this.index += 1
                }
                else if(this.index <= this.tabs.length - 1){
                    this.index = 0
                }
                this.reloadBookmark(this.index)
            },
            prev(){
                if(this.index > 0){
                    this.index -= 1
                }
                else{
                    this.index = this.tabs.length - 1
                }
                this.reloadBookmark(this.index)
            },
        async onSave(event) {
            event.preventDefault();
            if (this.loggedIn)  {
                await this.saveBookmark();
                this.over = !this.over
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

            const response = await fetch("http://fingertips.bkaraba.tech/api/v1/bookmarks/new", {
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
#name{
    margin-top: 2px;
}
#avatar {
  vertical-align: middle;
  margin:5px;
  margin-bottom: 10px;
  width: 20px;
  height: 20px;
  border-radius: 50%;
}
.others{
    margin-top: 20px;
    margin-left: 20px;
}
.others p{
    color: rgb(65, 62, 62);
}
.container{
    display: flex;
}
p{
    color: aqua;

}
.container .nav-bar{
    position: relative;
    flex: 1;
    margin-top: 20px;    
    border-radius: 5px;
    
    
}
.container .main{
    display:flex;
    flex: 5;
    border-radius: 5px;
    background-color: aliceblue;
    z-index: 2;
    
}
.others{
    position:fixed;
}
.add{
    margin-left: 70%;
    margin-top: 7px;

}
.add button{
    border-radius: 5px;
    background-color:#fff;
    border: none;
    
}.overlay{
    width:50%;
    margin-left: 30%;
    z-index: 5;
    border-radius: 5px;
}
.container .main .contents{
    flex: 1;
    display: flex;
    flex-wrap: wrap;
}
.books{
    display:flex;
    flex-wrap: wrap;
    margin:20px;
    width: 95%;
    background-color: #fff;
    border-radius: 5px;
}
.left{
    flex: 1;
    margin: auto 10%;
    height: 50%;

}
.options a{
    text-decoration: none;
    color: rgb(26, 238, 18)
}
.options button{
    border: none;
    font-size: small;
    background-color: #fff;
    margin-left: 25px;
}.updateme{
    color: blue;
}.deleteme{
    color: red;
}
.books:hover{
    transform: translate(-10px, -10px);
    border-left-style: solid;
    border-left-color: rgb(8, 107, 38);
}
.left img{
    width: 100%;
    height: 80%;
    margin: auto;

}
.right{
    margin: 5px;
    flex: 9;
    font-size: small;
}.right p{
    color: rgb(51, 46, 46);
}
.container .main .web{
    flex:0;
    display:block;
   
}
.page{
    position:absolute;
    display:block;
}
.page::v-deep * {
    display: -ms-inline-grid; 
     object-fit: contain;
     
 }
/**#lbl{
    text-align: start;
    margin-left: 20px;
}
.input input , textarea{
    width: 80%; 
    height:30px; 
    border: 1px solid aqua;
    border-radius: 4px;
    margin: auto;     
}
.input textarea
{
    max-width: 80%;
    min-width: 80%;
    min-height: 50px;
    max-height: 100px;
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
**/
</style>