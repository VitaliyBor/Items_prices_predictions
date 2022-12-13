<template>
<div>
    <div class="page-product">
        <div class="columns is-multiline">
            <div class="column is-5">
                <figure class="image mb-6">
                    <img style="width:600px; margin:auto" src="../assets/1.jpg">
                </figure>


            </div>

            <div class="column is-7">
                                <h1 class="title">Хілтон Київ</h1>
                <h2 class="subtitle">Інформація</h2>

                 <p>Вікна від підлоги до стелі, робочий стіл, тропічний душ, стандартний Wi-Fi.

Прокинься в цьому світлому номері з вікнами від підлоги до стелі. Працюйте за письмовим столом зі стандартним Wi-Fi, відпочивайте у неформальній зоні відпочинку або насолоджуйтесь фільмами на замовлення по телевізору.

Відпочиньте у ванній кімнаті з тропічним душем або насолоджуйтесь чашкою чаю або кави в номері. </p>

                <h4 style="margin-bottom:15px;margin-top:15px;"> <strong>Ціна: </strong>  5000 грн </h4>
                <h4 style="margin-bottom:15px"> <strong>Номер телефону: </strong> 0983252548 </h4>
                <h4 style="margin-bottom:15px"> <strong>Адресса : </strong>Бульвар Тараса Шевченко, 33, Київ, 01030, Україна </h4>
                <div class="control">
                        <a class="button is-dark"  @click="addToCart">Залишии відгук </a>
               </div>
            </div>
        </div>
    </div>
     <div class="modal is-active ">
        <div class="modal-background"></div>
        <div class="modal-card">
          <header class="modal-card-head bacground_model_color">
            <p class="modal-card-title modal_text">Залишити відгук про готель</p>
            <button class="delete" aria-label="close"></button>
          </header>
          <section class="modal-card-body">
            <p class="mb10">Назва відгуку</p>
            <input class="input " type="text" placeholder="Назва відгуку">
            <p class="mb10 mt10">Текстовий опис відгуку</p>
            <textarea class="textarea " placeholder="Сам відгук "></textarea>
            <p class="mb10 mt10">Оцініть готель, будь ласка</p>
            <div class="select ">
             <select>
               <option disabled>Оцініть готель </option>
               <option>1</option>
               <option>2</option>
               <option>3</option>
               <option>4</option>
               <option>5</option>
             </select>
           </div>
          </section>
          <footer class="modal-card-foot bacground_model_color">
              <div style="margin:auto">
            <button class="button is-success">Відправити відгук</button>
            <button class="button">Закрити вікно</button>
            </div>
          </footer>
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
            quantity: 1
        }
    },
      mounted() {
        this.getProduct() 
    },
    methods:{
        async getProduct(){
             this.$store.commit('setIsLoading', true)
            
             const category_slug = this.$route.params.category_slug
             const product_slug = this.$route.params.product_slug

             await axios
                .get(`http://127.0.0.1:8000/api/v1/products/${category_slug}/${product_slug}`)
                .then(response =>{
                    this.product = response.data
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

<style scoped>
.bacground_model_color{
    background-color:#363636;
}
.modal_text{
    color: #ffffff !important;
}
.mb10{
    margin-bottom: 10px;
}
.mt10{
    margin-top: 10px;
}


</style>