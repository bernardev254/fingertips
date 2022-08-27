export default (await import('vue')).default.extend({
name: 'myProfile',
components: {
myHeader,
},
data() {
return {
my_bookmarks: [],
token: this.$store.state.token,
display: false,
title: true,
description: false,
category: false,
popup: false
};
},
async created() {
await this.toggleBookmarks();
},
methods: {
async fetchBookmarks() {
const res = await fetch("http://127.0.0.1:5000/api/v1/bookmarks/my_bookmarks", {
headers: {
"Authorization": "Bearer " + this.token
}
});
const my_bookmarks = await res.json();
return (my_bookmarks);
},
async up(id) {
this.popup = true;
if (confirm('Are you sure?')) {
const res = await fetch("http://127.0.0.1:5000/api/v1/bookmarks/update", {
method: "PATCH",
headers: {
"content-Type": "application/json",
"Authorization": "Bearer " + this.token
},
body: JSON.stringify({ "id": id })
});
if (res.status === 200) {
this.getBookmarks();
}
else {
alert("Error deleting");
}
}
},
async del(id) {
if (confirm('Are you sure?')) {
const res = await fetch("http://127.0.0.1:5000/api/v1/bookmarks/remove", {
method: "DELETE",
headers: {
"content-Type": "application/json",
"Authorization": "Bearer " + this.token
},
body: JSON.stringify({ "id": id })
});
if (res.status === 200) {
alert("updated");
this.getBookmarks();
}
else {
alert("Error updating");
}
}
},
async getBookmarks() {
if (this.token) {
this.my_bookmarks = await this.fetchBookmarks();
if (!this.my_bookmarks)
alert("you do not have any bookmark please add one");
}

},
async toggleBookmarks() {
await this.getBookmarks();
this.display = !this.display;
},
add_bookmark() {
this.$router.push('addBookmark');

},
logout() {
this.$store.dispatch('logout');
}
}
});
