<template>
    <!--router-link to="/profile"> <span v-if="token" class="profile">profile</span></router-link-->
    <div id="name" class="others"><b>Fingertips</b></div>
    
    <div class="container">
        <nav class="nav-bar">
            <div class="top">
                <img src="../assets/img.png" alt="Avatar" class="others" id="avatar"/>
                <div v-if="loggedIn" class="logout">
                <button @click="logout">logout</button>
                </div>
            </div>
            
            <div class="others">

                <div>
                    <b>All bookmarks</b>
                    {{bookmarkSize}}
                </div>
                <div class="categories">
                    <p>unsorted</p>
                    <p :key="category.id" v-for="category in myCategories"></p>
                </div>
            </div>

        </nav>
        <div class="main">
            <div class="contents">
                <div class="add">
                    <button @click="my_add()" v-if="add" ><img src="../assets/star.png"><h4>Add</h4></button>
                 </div>   
                <div class="overlay" v-if="over">
                    <button class="close" @click="my_close()" v-if="close" >close</button><br><br>
                    <label id="lbl">Name</label><br>
                    <input type="text" v-model="title" required/><br>
                    <label id="lbl">Url</label><br>
                    <input type="text" v-model="url" required/><br>
                    <label id="lbl">description</label><br>
                    <textarea type="text" v-model="desc" placeholder="Saysomething about your bookmark"></textarea><br>
                    <label id="lbl">category</label><br>
                    <input type="text" v-model="category" placeholder="sort"/><br>
                    <button v-if="loggedIn" class="save" @click="onSave">Save</button>
                    <button v-else class="save" @click="onSave">login</button>
                </div>
                               
                <div class="books" @click="preview(event, bookmark.url, bookmark.id)" :key="bookmark.id" v-for="bookmark in my_bookmarks">
                    <div v-if="display" class="left">
                        <picture>
                            <source :srcset="bookmark.icon">
                            <img src="../assets/bookmark.jpg"/>
                        </picture>
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
                <div class="nobooks" v-if="!bookmarkSize">
                    <img src="../assets/ftips.png">
                    <div class="instructions">
                        <h1>No bookmarks yet!</h1>
                        <button class="addlink" @click="my_add()" >Add new</button><br>
                        <button class="browser-extension">install browser extension</button>
                    </div>
                </div>
            </div>
            <div :style="toggleStyle" v-if="show && bookmarkSize" class="web" id="web">
                
                <div class="page">
                    <div class="options" v-if="clicked">
                        <button @click="visitSite()">visit</button>
                        <button @click="toggleEdit()">edit</button>
                        <button @click="toggleWeb()">web(preview)</button>
                        <button @click="toggle_web_show()">close</button>
                    </div>
                    <div class="webpreview" v-if="web" v-html="html"></div>
                        <!--iframe height="1000px" width="400px" object-fit="contain" plugin="true" allow="fullscreen; clipboard-white" loading="eager" tabindex="-1" class="myframe" :srcdoc="html" border="none"> </iframe-->
                    
                    <div class="edit" :key="bookmark.id" v-for="bookmark in specific_bookmark">
                        <div v-if="edit">
                            <div class="edithead">
                                <div class="left">
                                    <picture>
                                        <source :srcset="bookmark.icon">
                                            <img src="../assets/bookmark.jpg"/>
                                    </picture>
                                </div>
                                <div class="right">
                                    <h3><b>{{bookmark.title}}</b></h3>
                                    <input type="text" v-model="desc" placeholder="Saysomething about your bookmark">
                                </div>    
                            </div>
                            <!--div class="mid"> 
                                <div class="a">
                                    
                                    <label id="lbl">Name</label><br><br>
                                    <label id="lbl">Url</label><br>
                                    <label id="lbl">category</label>                                    
                                </div>                               
                                <div class="b">
                                    <input type="text" v-model="title" required/><br>
                                    <input type="text" v-model="url" required/><br>                       
                                    <input type="text" v-model="category" placeholder="sort"> 
                                </div>
                                
                                
                            </div>
                                    
                            <div class="extras">
                                <div class="link">
                                    <router-link :to=bookmark.url target="_blank">visit</router-link>
                                </div>
                                <div class="delete">
                                    <button class="deleteme" @click="del(bookmark.id)">delete</button>
                                </div>
                                <div class="update">
                                    <button class="updateme" @click="up(bookmark.id)">update</button>
                                </div>
                            </div-->                                   
                        </div>
                            
                    <div>
                            
                </div>
            </div>
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
            add: true,
            close: false,

            title: "",
            url: "",
            desc: "",
            category: "unsorted",
            icon: "",

            myCategories: [],
            
            saved: false,

            
            
            my_bookmarks: [],
            specific_bookmark: [],
            display: true,
            html: null,
            
            isactive: false,
            show: false,
            over: false,
            clicked: false,
            edit: true,
            web: false,
        }

    },
    async created() {
        let access = localStorage.getItem("myToken");
        if (access){
            this.$store.dispatch('saveAccessToken', access)
        }
        else{
            this.$store.dispatch('logout')
        }
        await this.getBookmarks();
        await this.get_tabs()     
        await this.loadBookmark()
        this.index = setTimeout('getIdex', 3000)
    },
    computed:{
        loggedIn(){
            return this.$store.getters.loggedIn
        },
        token(){
            return this.$store.state.token
        } ,
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
        bookmarkSize(){
            return this.my_bookmarks.length
        },
    },
    methods: {
        logout(){
            this.$store.dispatch('logout')
        },
        specificBookmark(id){
            this.specific_bookmark = [];
            return this.my_bookmarks.filter(bookmark => bookmark.id === id)
        },
        my_add(){
            this.over = !this.over;
            this.add = !this.add;
            this.close = !this.close;          
        },
        my_close(){
            this.over = !this.over;
            this.close = !this.close;
            this.add = !this.add;
        },
        toggle_web_show() {
            this.show = !this.show;
        },
        toggleEdit(){
            if (!this.edit)
                this.edit = !this.edit
                this.web = false
        },
        toggleWeb(){
            if (!this.web){
                this.web =!this.web
                this.edit = false
            }
        },
        async fetchBookmarks() {
                const res= await fetch ("http://127.0.0.1:5000/api/v1/bookmarks/my_bookmarks",{
                    headers:{
                        "Authorization": "Bearer "+this.token
                    }
                });
                
                const my_bookmarks = await res.json();
                return(my_bookmarks.bookmarks);
        
        },
        //delete
        async del(id){
                if (confirm('Are you sure?')){
                    const res = await fetch("http://127.0.0.1:5000/api/v1/bookmarks/remove", {
                        method: "DELETE",
                        headers:{
                            "content-Type": "application/json",
                            "Authorization": "Bearer "+this.token
                        },
                        body:JSON.stringify({"id":id})
                    });
                    if (res.status === 200 ){
                        alert("updated")
                        this.getBookmarks();
                    }
                    else{
                         alert("Error updating")
                    }              
                }
            },
        //preview html
        async preview($event, url, id){
            this.web = false
            this.edit = true
            this.specific_bookmark = this.specificBookmark(id)
            this.show = true
            this.clicked = true
            const data ={"url":url}
            const res = await fetch("http://127.0.0.1:5000/api/v1/auth/proxy",{
                method: 'POST',
                mode: 'cors',
                headers: {
                    'content-Type':'application/json'
                },
                body:JSON.stringify(data)
            })
            //let reader = await res.page.body.getReader()
            //let html = await reader.read()
            //this.page = new TextDecoder().decode(html.value)
            this.html = await res.text()
            //await this.writehtml(this.page)
            //let bl = await res.blob()
            //const page = await bl.text()
            //this.page = page
            
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
        async onSave(event) {
            event.preventDefault();
            if (this.loggedIn)  {
                await this.saveBookmark();
                this.my_bookmarks = await this.fetchBookmarks();
                this.over = !this.over
                this.add = !this.add
            }
            
                        
        },
        async saveBookmark() {
            if (!this.loggedIn) {
                this.$router.push('/login');
            }
            const response1 = await fetch("http://127.0.0.1:5000/api/v1/bookmarks/getBookmarkDetails", {
                method: 'POST',
                mode: 'cors',
                headers: {
                    "content-Type": "application/json",
                    "Authorization": "Bearer "+this.token
                },
                body: JSON.stringify({'url':this.url}),
            });
            const resp = await response1.json()

            const bookmark = {
                "title":resp.title,
                "url": this.url,
                "body": this.desc,
                "category": this.category,
                "icon": resp.icon
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
#name{

    margin: 2px auto 10px;
    font-size: x-large;
    padding-bottom: 10px;
    color:  rgb(117, 159, 189);
    z-index: 2;
}


.container .nav-bar .top .logout{
    margin-left: 140%;
    margin-top: 60%;
}

.container .nav-bar .top .logout button{
    border: none;
    background-color: #fff;
    color: rgb(236, 115, 78);
    font-size:medium;
    margin-top: auto;

}
.top .logout button:hover{
    transform: translate(-4px, -4px);
}

#avatar {
  vertical-align: middle;
  margin:5px;
  margin-bottom: 10px;
  width: 4%;
  height: 4%;
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
    position:fixed;
}
p{
    color: aqua;

}
.container .nav-bar{
    justify-content: flex-start;
    position: relative;
    
    margin-top: 20px;    
    border-radius: 5px;
    
    
}
.container .main{
    display:flex;
    position: fixed;
    left: 15%;
    border-radius: 5px;
    background-color: aliceblue;
    z-index: 1;
    height:98%;
    width:85%;
    top:5px;
    
}
@media only screen and (max-width: 600px) {
    .container .main{
        flex-direction: column;

    }
}
.container .main .contents{
    overflow-y: scroll;
}
.others{
    position:fixed;
}
.add{
    height: 35px;
    margin-left: 70%;
    margin-top: 7px;
    font-size: large;
}
.add button{
    height: 35px;
    border-radius: 5px;
    background-color:#fff;
    border: none;
    font-size:large;
    align-content: center;
    display:flex
    
}
.add button img{
    object-fit: contain;
    height:25px;
    width: 25px;
}
.add button h4{
    margin-top:10%;
    
}
.add button:hover{
    border: 1px solid green;
}
.overlay{
    background-color: rgb(199, 217, 230);
    top: 0;
    width:70%;
    margin: 0 auto;
    z-index: 15;
    border-radius: 5px;
    box-shadow: #1E2749;
}
.overlay .close{
    border: none;
    margin-top: 5%;
    margin-left: 80%;
    background-color: rgb(199, 217, 230);
    border-radius: 5px;
    color: rgb(21, 31, 121);
    font-size: 14px;
    padding:3px 0;

}
.overlay .close:hover{
    color: red;
}
.overlay input , textarea{
    right: 0;
    border: none;
    width: 80%; 
    height:30px; 
    background-color: rgb(204, 247, 243);
    border-radius: 4px;
    justify-content: center;
    z-index: 5;    
    margin-left: 10%;
}
.overlay textarea
{
    max-width: 80%;
    min-width: 80%;
    min-height: 50px;
    max-height: 100px;
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
    width: 100%;
    background-color: #fff;
    border-radius: 5px;
    max-height: min-content;
    
}
.nobooks{
    width: 100%;
}
.nobooks img{
    margin-left: 30%;
    width: 60%;
    height: 50%;
}
.nobooks .instructions{
    margin-left: 40%;
}
.nobooks .instructions button{
    
    margin-left: 10%;
    font-size: large;
}
.nobooks .instructions .addlink{
    margin-bottom: 15px;
    width: 37.5%;
    height: 25%;
    
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
    background-color: rgb(198, 215, 230);
    z-index: 99;
    overflow-y: scroll;
   
}
.container .main .web .options{
    display:flex;
    justify-content: space-between;
    background-color: #fff;
    width: 98%;
    margin:auto;
    margin-top: 3px;
}
.container .main .web .options button{
    height: 30px;
/**background-color: rgb(159, 177, 192);**/
border: 1px solid white;
}
.container .main .web .options button:hover{
    /**background-color: #1E2749;**/
    transform: translate(-1px, -1px);
    border-bottom: 3px solid rgb(5, 71, 49);
    color: rgb(38, 41, 1);
}
.page{
    display:block;
}
.edithead{
    display: flex;
    margin-top: 50px;
}
.edithead .left{
    flex: 1;
}
.edithead .right{
    flex: 2;

}
.mid{
    display: flex;
    margin-top: 20px;
}
.mid input{
    margin-left: 25%;
    border: none;
    height: 20px;
    margin-bottom: 5px;
}
.mid label{
    margin-bottom: 2px;
}
.extras{
    display: flex;
    justify-content: space-between;
    margin-top: 20px;
}
#lbl{
    text-align: start;
    margin-left: 55px;
    margin-top:10px;
}

.save{

    width: 50%; 
    margin: 35px 20%;
    height: 25px;
    border-radius: 5px;
    background-color: #7CAFC4;
    color: white;
    font-size: 14px;
    padding:3px 0;

}
.save:hover{
    background-color: #1E2749;
}
/**.profile{
    width: 25%; 
    margin-top: 5px;
    height: 25px;
    border-radius: 5px;
    background-color:  white;
    color: #48cae4;
    font-size: 14px;
    float: right;
}
.profile:hover{
    color: #76c893;
    transform: translate(-4px, -4px);
}
**/
</style>