<template>
    <div class="header">
        <h1>FingerTips</h1>
        <h2>...all your bookmarks at your fingertips</h2>
        <h1 id="tittle">{{text}}</h1>
    </div>
    
</template>
<script>
export default{
    name: "myHeader",
    props: {
        text:String,
    }

}
</script>
<style scoped>

.header{
    background-color:aliceblue;
    
    height: 160px;
    padding: 30px;
    color: #010808;
    text-align: center;
}
#tittle{
    padding-top: 20px;
}

</style>