<template>
  <div class="home">
<<<<<<< HEAD
    <section class="hero is-medium is-dark mb-6">
        <div class="hero-body has-text-centered">
            <p class="title mb-6">
                Welcome to Djacket
            </p>
            <p class="subtitle">
                The best jacket store online
            </p>
        </div>
    </section>

    <div class="columns is-multiline">
      <div class="column is-12">
          <h2 class="is-size-2 has-text-centered">Latest products</h2>
      </div>

      <ProductBox 
        v-for="producto in ultimosProductos"
        v-bind:key="producto.id"
        v-bind:product="producto" />
    </div>
=======
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Bienvenido a nuestra página"/>
>>>>>>> 688b37ab2de5c452f61343eaaac45042f000121b
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'HomeView',
  components: {
  }
}
</script>
