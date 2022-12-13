<template>
<div class="wrapper">
    <nav class="navbar is-dark header-color" >
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"><strong>Predicting items prices</strong></router-link>

        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu = !showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu }">

        <div class="navbar-end">

          <div class="navbar-item">
            <div class="buttons">
              <template v-if="$store.state.isAuthenticated">
                <router-link to="/my-account" class="button is-light header-button">Мій аккаунт</router-link>
              </template>

              <template v-else>
                <router-link to="/log-in" class="button is-light header-button">Увійти</router-link>
              </template>

             <!--  <router-link to="/cart" class="button is-success">
                <span class="icon"><i class="fas fa-shopping-cart"></i></span>
                <span>Cart ({{ cartTotalLength }})</span>
              </router-link> -->
            </div>
          </div>
        </div>
      </div>
    </nav>

    <div class="is-loading-bar has-text-centered" :class="{'is-loading': $store.state.isLoading }">
      <div class="lds-dual-ring"></div>
    </div>

  <section class="section">
      <router-view/>
  </section>

   <footer class="footer footer-color">
    <p class="has-text-centered text-color">Copyright (c) 2022</p>
   </footer>
</div>
</template> 

<script>
import axios from 'axios'

export default{
  data(){
    return {
      showMobileMenu: false,
      cart: {
        items: []
      },
    }
  },
  create(){
   this.calculateLenght();
  },
  mounted(){
     this.cart = this.$store.state.cart
  },  
   beforeCreate() {
    this.$store.commit('initializeStore')

     const token = this.$store.state.token

    if (token) {
        axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
        axios.defaults.headers.common['Authorization'] = ""
    }
    },
    computed:{
      cartTotalLength() {
          let totalLength = 0
          for (let i = 0; i < this.cart.items.length; i++) {
              totalLength += this.cart.items[i].quantity
          }
          return totalLength
      }
    },
    methods:{
    }
}
</script>

<style lang="scss">
@import '../node_modules/bulma';

.navbar.is-dark .navbar-brand > a.navbar-item:focus, .navbar.is-dark .navbar-brand > a.navbar-item:hover, .navbar.is-dark .navbar-brand > a.navbar-item.is-active, .navbar.is-dark .navbar-brand .navbar-link:focus, .navbar.is-dark .navbar-brand .navbar-link:hover, .navbar.is-dark .navbar-brand .navbar-link.is-active
{
  background-color: transparent!important;
}

.footer-color{
 background-color: #79baec;
}

.text-color{
  color:#fff!important;
}

body{
  background-image: linear-gradient(to bottom, #933867, #933867, #933867, #933867, #933867, #984578, #9b5388, #9e6098, #9777b6, #8d8ece, #81a5e0, #79baec);
}

.header-color{
  background-color: #822862 !important;
  border-bottom: 2px solid #fff !important;
  min-height: 80px;
}

.header-button{
    background-color: #f5f5f500!important;
    border-color: white!important;
    color: rgb(255 255 255)!important;
}

.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}
.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}
@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
.is-loading-bar {
  height: 0;
  overflow: hidden;
  -webkit-transition: all 0.3s;
  transition: all 0.3s;
  &.is-loading {
    height: 80px;
  }
}
</style>