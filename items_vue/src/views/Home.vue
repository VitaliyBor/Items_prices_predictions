<template>
    <div class="home">
        <section class="hero is-medium is-dark mb-6">
            <div class="hero-body has-text-centered " style="background: linear-gradient(108.54deg, rgba(184, 51, 169,  0.83) 5.25%, rgba(80, 158, 219, 0.55) 89.24%)!important; " >
                <p class="title mb-6">
                    Ви відвідали сайт Predicting items prices
                </p>
                <p class="subtitle">
                    Сайт на якому ви зможете дізнатися майбутні ціни на товари 
                </p>
            </div>
        </section>

        <div class="colums is-multiline">
            <div class="column is-12">
                <h2 class="is-size-2 has-text-centered text-color "> Усі товари</h2>
        </div>

<!--         
              <router-link :to="`/recomendation/${userId}`" class="button  is-success"  style="margin:auto; display:block; width: 240px;margin-bottom:20px">Отримати рекомендації</router-link> -->
       
       
    <!--     <div v-if ="allHotels">
          <div class="column is-3">
            <div class="box">
            <figure class="image mb-4">
                <img v-bind:src="product.get_thumbnail">
            </figure>
            <h3 class="is-size-4">{{ product.name }}</h3>
            <p class="is-size-6 has-text-grey">${{ product.price }}</p>
            </div>
         </div>
    
        </div>
        <div v-else >
            
        </div> -->

       <!-- latest version   -->
        

        
        <div class="columns is-multiline">
        <div  v-for="product in latestProducts" v-bind:key="product.id" class="column is-4">
          
        <div class="box">
            <figure class="image mb-4">
                <img v-bind:src="product.get_thumbnail">
            </figure>
            <h3 class="is-size-4">{{ product.name }}</h3>
            <p class="is-size-6 has-text-grey">{{ product.price }} $</p>
              <router-link :to="`/items/${product.id}/`" class="button is-dark mt-4">Дізнатися деталі</router-link> 
             <!-- <router-link v-bind:to="product.get_absolute_url" class="button is-dark mt-4">View details</router-link> -->
            </div>
        </div>
        </div>
       

   <!--
       <ProductBox 
        v-for="product in latestProducts"
        v-bind:key="product.id"
        v-bind:product="product" /> 
        -->

      </div>
    </div>
</template>

<script>

import axios from 'axios'

import ProductBox from '@/components/ProductBox'

export default {
  name:"Home",
  data(){
    return{
      latestProducts:[],
      userData:{ email:'', id:'',username:''},
      allHotels:true,
      UserId:{},
      name_create:"BDsm4",
      mark_create: 3,
      hotel_id:4,
      user_id: 2,
    }
  },
  components:
  {
    ProductBox
  },
  mounted(){
    this.getLatestProducts()
  },
  methods:{
   getLatestProducts(){
     // this.latestProducts.push({id:'1',name:'collName'})
       this.userId = localStorage.getItem('userId');
      this.$store.commit('setIsLoading', true)
      console.log(this.userData);
        
            const formData = {
                name: this.name_create,
                mark: this.mark_create,
                hotel_id: this.hotel_id,
                user_id: this.user_id
            }
     axios
                .post("/api/v1/addreview/", formData)
                .then(response => {
                    localStorage.setItem("ansdw",response.data)
                })
                .catch(error => { 
                        console.log(JSON.stringify(error))  
                })

       axios
      .get('http://127.0.0.1:8000/api/v1/latest-products/', {
         firstName: 'Finn',
         lastName: 'Williams'
       })
      .then(response =>{
        this.allroducts= true
        this.latestProducts = response.data
       
      })
      .catch(error => {console.log(error)}) 

       this.$store.commit('setIsLoading', false)
    }

  }
}
</script>
