<template @deleted="del">
    <div class="first">
        <div class="header">
            <myHeader/>
            <div class="links">
                <span @click="toggleBookmarks">my bookmarks</span>
                <span @click="add_bookmark">add Bookmark</span>
                <span @click="logout">Logout</span>
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
                <a :href="bookmark.url" target="_blank">visit</a>
                <button class="deleteme" @click="del(bookmark.id)">delete</button>
              </div>
           </div>
        </div>
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
                display: false
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
                const my_bookmarks= await res.json();
                return(my_bookmarks);
            },
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
.links{   
    float: right;
}
.links span{
    width: 25%;
    margin-left:15px; 
    margin-top: 5px;
    height: 25px;
    border-radius: 5px;
    background-color:  white;
    color: #48cae4;
    font-size: 14px;
    cursor:pointer;
    
}
.books{
    display:flex;
    width: 80%;
    margin: auto;
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
.left{
    flex: 5;
    margin-top: 20px;

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
}
</style>