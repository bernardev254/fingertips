<template>
    <div class="header">
        <h2>FingerTips</h2>
        <h4>all my bookmarks at my fingertips</h4>
        <h2 id="tittle">{{text}}</h2>
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
    background-color: #cbcecf;
    
    height: 100px;
    padding: 30px;
    color: #1fb2c5;
    text-align: center;
}
#tittle{
    padding-top: 20px;
}

</style>