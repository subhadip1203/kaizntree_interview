<template>
  <div class="sidebar">
    <div class="menu"> 
      <router-link to="/">
        <img class="logo" src="../assets/icon_home.svg"> Home
      </router-link>
    </div>

    <div class="menu"> 
      <router-link to="/add-item">
        <img class="logo" src="../assets/icon_home.svg"> Add Items
      </router-link>
    </div>

    <div class="menu"> 
      <router-link to="/add-category">
        <img class="logo" src="../assets/icon_home.svg"> Add Category
      </router-link>
    </div>

    <div class="menu">
      <img class="logo" src="../assets/icon_home.svg">Stocks
    </div>
    <div class="menu">
      <img class="logo" src="../assets/icon_home.svg">Build
    </div>
    <div class="menu">
      <img class="logo" src="../assets/icon_home.svg"> Customer
    </div>
    <div class="menu">
      <img class="logo" src="../assets/icon_home.svg"> Sales Order
    </div>
    <div class="menu">
      <img class="logo" src="../assets/icon_home.svg"> Supplier
    </div>
    <div class="menu">
      <img class="logo" src="../assets/icon_home.svg"> Manufacturer
    </div>
    <div class="menu"> 
      <img class="logo" src="../assets/icon_home.svg">Purchase order
    </div>
    <div class="menu"> 
      <img class="logo" src="../assets/icon_home.svg"> Reports
    </div>
    <br/>
    <br/>
    <br/>
    <br/>
    <br/>
    <div class="menu">
      <img class="logo" src="../assets/icon_home.svg">Help
    </div>
    <div class="menu">
      <img class="logo" src="../assets/icon_home.svg">Intregration
    </div>
    <div class="menu">
      <img class="logo" src="../assets/icon_home.svg">Logout
    </div>
    <div class="menu">
      <img class="logo" src="../assets/icon_home.svg"> My Profile
    </div>

  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
.sidebar {
  display: flex;
  flex-direction: column;
  margin-right: 5px;
  border-right: 5px solid #48bae8;
}

.menu {
  margin: 8px
}

.menu img {
  margin-right: 7px 
}
</style>
