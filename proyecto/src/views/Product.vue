<template>
    <div class="page-product">
        <div class="columns is-multiline">
            <div class="column is-7">
                <figure class="image mb-6">
                    <img v-bind:src="product.get_image" class="fixed-image-size">
                </figure>

                <h1 class="title">{{ product.name }}</h1>
                <p>{{ product.description }}</p> 
            </div>

            <div class="column is-3">
                <h2 class="subtitle">Información</h2> 
                <p><strong>Precio: </strong>Q. {{ product.price }}</p> 

                <div class="field has-addons mt-6">
                    <div class="control">
                        <input type="number" class="input" min="1" v-model="quantity">
                    </div>

                    <div class="control">
                        <a class="button is-dark" @click="addToCart()">Agregar al carrito</a> 
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

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
    methods: {
        async getProduct() {
            this.$store.commit('setIsLoading', true)

            const category_slug = this.$route.params.category_slug
            const product_slug = this.$route.params.product_slug

            await axios
                .get(`/api/v1/products/${category_slug}/${product_slug}`)
                .then(response => {
                    this.product = response.data

                    document.title = this.product.name + ' | Ferretería' 
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
                message: 'El producto ha sido agregado al carrito', 
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
  .image {
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
    width: 600px;    
    height: 300px;  
    overflow: hidden;
    display: flex;  
    align-items: center;
    justify-content: center;
}

.image img {
    width: 100%;
    height: 100%;
    object-fit: contain; 
}
</style>