<template>
<div>

       <div class="column is-12">
                <h2 class="is-size-2 has-text-centered"> Рекомендовані готелі</h2>
        </div>
           <div class="columns is-multiline">
        <div  v-for="product in latestProducts" v-bind:key="product.id" class="column is-4">
          
        <div class="box">
           <figure class="image mb-4">
                <img v-bind:src="product.get_thumbnail">
            </figure>
            <h3 class="is-size-4">{{ product.name }}</h3>
            <p class="is-size-6 has-text-grey">{{ product.price }} грн</p>
          
            </div>
        </div>
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
      allHotels:true,
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
   async getLatestProducts(){
     // this.latestProducts.push({id:'1',name:'collName'})
      this.$store.commit('setIsLoading', true)

      const id = this.$route.params.id

      await axios
      .get(`http://127.0.0.1:8000/api/v1/recomendation-products/${id}`)
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