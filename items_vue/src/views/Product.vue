<template>
    <div class="page-product" style=" padding: 1.4rem;" >
        <div class="columns is-multiline" style="background-color: #fff;border-radius:10px;padding: 10px;">
            <div class="column is-4">
                <h1 class="title">{{ product.name }}</h1>
                <figure class="image mb-6">
                   <img v-bind:src="product.get_image"> 
                </figure>
            

                
                  
                

              
            </div>

            <div class="column is-8" v-if="product.name" >
                <p class="subtitle">Інформація</p>
                 <p>{{ product.description }}</p>
                <p><strong>Price: </strong>${{ product.price }}</p>
                <p><strong> Середнє квадратичне відхилення: </strong>{{ product.mse }} </p>
                <p> <strong>Корінь середнього квадратичного відхилення: </strong>{{ product.rmse }} </p>
                <p> На майбутній період <strong>(100 дні)</strong> саме  <strong>{{ product.mindate }}</strong>  буде найкраща ціна <strong>{{ product.minprice }} $</strong> </p>
                   <figure class="image mb-6" >
                    <span  v-if="item_id === '1'">
                     <img src="../assets/1.png"> 
                    </span>
                    <span v-else-if="item_id === '2'">
                     <img src="../assets/2.png"> 
                    </span>
                     <span v-else-if="item_id === '3'">
                     <img src="../assets/3.png"> 
                    </span>
                     <span v-else-if="item_id === '4'">
                     <img src="../assets/4.png"> 
                    </span>
                     <span v-else-if="item_id === '5'">
                     <img src="../assets/5.png"> 
                    </span>
                     <span v-else-if="item_id === '6'">
                     <img src="../assets/6.png"> 
                    </span>
                     <span v-else-if="item_id === '7'">
                     <img src="../assets/7.png"> 
                    </span>
                     <span v-else-if="item_id === '8'">
                     <img src="../assets/8.png"> 
                    </span>
                        <span v-else-if="item_id === '9'">
                     <img src="../assets/9.png"> 
                    </span>
                    
                </figure>
                <!-- <div class="field has-addons mt-6">
                    <div class="control">
                        <input type="number" class="input" min="1" v-model="quantity">
                    </div>

                    <div class="control">
                        <a class="button is-dark"  @click="addToCart">Add to cart</a>
                    </div>
                </div> -->
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import {toast} from 'bulma-toast'

export default {
    name: 'Product',
    data() {
        return {
            product: {},
            quantity: 1,
            priceChart:'',
            item_id: '',
        }
    },
      mounted() {
        this.getProduct() 
    },
    methods:{
        async getProduct(){
             this.$store.commit('setIsLoading', true)
             
             const userName = this.$route.params.username
             const id = this.$route.params.id
             this.item_id =id
             const category_slug = this.$route.params.category_slug
             const product_slug = this.$route.params.product_slug

             await axios
                .get(`http://127.0.0.1:8000/api/v1/products2/${userName}/${id}`)
                .then(response =>{
                    this.product = response.data;
                    this.priceChart = 'http://localhost:8080/img/foo.c6e3cb68.png';
                })
                .catch(error => {
                    console.log(error)
                })

                this.$store.commit('setIsLoading', false)
 
        },
        addToCart() {
            if (isNaN(this.quantity) || this.quantity < 1) {
                this.quantity = 1
            }
            const item = {
                product: this.product,
                quantity: this.quantity
            }
            this.$store.commit('addToCart', item)


               toast({
                message: 'The product was added to the cart',
                type: 'is-success',
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: 'bottom-right',
            })
        }
        

    }
}
</script>