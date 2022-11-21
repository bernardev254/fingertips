<template>
    <div class="first">
        <div class="header">
            <myHeader/>
            <img src="../assets/avatar.png" alt="Avatar" class="avatar"/>
            <div class="links">
                <!--span class="linkbtn" @click="toggleBookmarks">my bookmarks</span-->
                <span class="linkbtn" @click="add_bookmark">add Bookmark</span>
                <span class="linkbtn" @click="logout">Logout</span>
            </div>
        </div>
        <div class="books" :key="bookmark.id" v-for="bookmark in my_bookmarks.bookmarks">
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
        <!--div v-if="popup" class="popup">
            <div class="title_buttons">
                <button class="title"></button>
                <button class="desc"></button>
                <button class="category"></button>
            </div>
            <div v-if="title" class="update_fields">
                <label id="lbl">title</label>
                <input type="text" v-model="title" required/>
            </div>
            <div v-if="description" class="update_fields">
                <label id="lbl">description</label>
                <input type="text" v-model="description" required/>
            </div>
            <div v-if="category" class="update_fields">
                <label id="lbl">category</label>
                <input type="text" v-model="category" required/>
            </div>
        </div-->      
    </div>
</template>
<script >
import myHeader from '../components/myHeader.vue'
    export default {
        name: 'myProfile',
        components:{
            myHeader,
        },
        data() {
            return {
                my_bookmarks:[],
                token: this.$store.state.token,
                display: false,
                title:true,
                description: false,
                category: false,
                popup: false

            }
        },
        async created() {
            await this.toggleBookmarks();
        },
        methods: {
            async fetchBookmarks() {
                const res= await fetch ("http://127.0.0.1:5000/api/v1/bookmarks/my_bookmarks",{
                    headers:{
                        "Authorization": "Bearer "+this.token
                    }
                });
                const my_bookmarks = await res.json();
                return(my_bookmarks);
            },
            async up(id){
                this.popup = true
                if (confirm('Are you sure?')){
                    const res = await fetch("http://127.0.0.1:5000/api/v1/bookmarks/update", {
                        method: "PATCH",
                        headers:{
                            "content-Type": "application/json",
                            "Authorization": "Bearer "+this.token
                        },
                        body:JSON.stringify({"id":id})
                    });
                    if (res.status === 200 ){
                        this.getBookmarks();
                    }
                    else{
                         alert("Error deleting")
                    }              
                }
            },
            
            async getBookmarks() {
                if (this.token){
                    this.my_bookmarks = await this.fetchBookmarks();
                    if (!this.my_bookmarks) alert("you do not have any bookmark please add one")
                }
                   
            },
            async toggleBookmarks(){
                await this.getBookmarks();
                this.display = !this.display;
            },
            add_bookmark() {
                this.$router.push('addBookmark');
                
            },
            logout(){
                this.$store.dispatch('logout')
            }
        }
        

    }
</script>

<style scoped>
.avatar {
  vertical-align: middle;
  margin:-35px 42% 0 ;
  width: 70px;
  height: 70px;
  border-radius: 50%;
}
.links{   
    float: right;
    margin-top: 15px;    
}
.links span{
    width: 25%;
    margin-left:15px; 
    margin-top: 15px;
    height: 25px;
    border-radius: 5px;
    background-color:  white;
    color: #48cae4;
    font-size: 14px;
    cursor:pointer;
    font-size: x-small;
    
}
.linkbtn:hover{
    color: #76c893;
    transform: translate(-4px, -4px);
    border-right-style: solid;
    border-left-style: solid;
    border-right-color: rgb(8, 107, 38);
    border-left-color: rgb(8, 107, 38);
    
}

.books{
    display:flex;
    width: 90%;
    margin: 20px auto;
}
.books:hover{
    transform: translate(-10px, -10px);
    border-left-style: solid;
    border-left-color: rgb(8, 107, 38);

}
.update_field{
    background-color: #76c893;
}
.books a{
    text-decoration: none;
    color: rgb(26, 238, 18);
}
.books .deleteme{
    border: none;
    font-size: x-small;
    color: rgb(192, 34, 6);
    margin-left: 5px;
}
.books .popup{
    border: 1px solid;
    font-size: x-small;
    color: rgb(49, 6, 168);
    margin-left: 5px;
    z-index: 1;
}
.books .popup .title_button{
    width: 100%;
}
.books .popup .title_button button{
    width: 33%;
}


.left{
    flex: 1;
    margin: auto;
    height: 50%;

}
.left img{
    width: 100%;
    height: 80%;
    margin: auto;

}
.right{
    margin: 5px;
    flex: 9;
    font-size: xx-small;
}
</style>