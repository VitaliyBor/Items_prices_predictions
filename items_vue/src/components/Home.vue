<template>
    <div class="home">
        <section class="hero is-medium is-dark mb-6">
            <div class="hero-body has-text-centered" >
                <p class="title mb-6">
                    Welcome to Djacket
                </p>
                <p class="subtitle">
                    The best jacket store online
                </p>
            </div>
        </section>

        <div class="colums is-multiline">
            <div class="column is-12">
                <h2 class="is-size-2 has-text-centered"> Latest products</h2>
            </div>
        </div>
        <!-- <div class="column is-3" 
        v-for="product in latestProducts"
        :key="product.id"
        >
        <div class="box">
            <figure class="image mb-4">
                <img :src="product.get_thumbnail" alt="">
            </figure>
            <h3 class="is-size-4">{{product.name}}</h3>
            <p class="is-size-6 has-text-grey">${{product.price}} </p>
             View details
        </div>

    </div> -->
    </div>
</template>

<script>


export default {
    name:"Home",
    components:{

    }
}
</script>
