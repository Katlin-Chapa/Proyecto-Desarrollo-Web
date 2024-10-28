<template>
    <tr>
        <td><router-link :to="item.product.get_absolute_url">{{ item.product.name }}</router-link></td>
        <td>Q. {{ item.product.price }}</td>
        <td>
            {{ item.quantity }}
            <a @click="decrementQuantity(item)">&nbsp;&nbsp;-</a>
            <a @click="incrementQuantity(item)">&nbsp;&nbsp;&nbsp;&nbsp;+</a>
        </td>
        <td> Q. {{ getItemTotal(item).toFixed(2) }}</td>
        <td><button class="delete" @click="openModal"></button></td>
    </tr>

    <div class="modal" :class="{ 'is-active': isModalActive }">
        <div class="modal-background" @click="closeModal"></div>
        <div class="modal-card">
            <header class="modal-card-head">
                <p class="modal-card-title">Confirmación</p>
                <button class="delete" aria-label="close" @click="closeModal"></button>
            </header>
            <section class="modal-card-body">
                <p>¿Está seguro que desea eliminar este producto del carrito?</p>
            </section>
            <footer class="modal-card-foot">
                <button class="button is-success" @click="confirmRemoval">Sí, eliminar</button>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                <button class="button" @click="closeModal">Cancelar</button>
            </footer>
        </div>
    </div>
</template>

<script>
export default {
    name: 'CartItem',
    props: {
        initialItem: Object
    },
    data() {
        return {
            item: this.initialItem,
            isModalActive: false
        }
    },
    methods: {
        getItemTotal(item) {
            return item.quantity * item.product.price;
        },
        decrementQuantity(item) {
            item.quantity -= 1;

            if (item.quantity === 0) {
                this.$emit('removeFromCart', item);
            }

            this.updateCart();
        },
        incrementQuantity(item) {
            item.quantity += 1;

            this.updateCart();
        },
        updateCart() {
            localStorage.setItem('cart', JSON.stringify(this.$store.state.cart));
        },
        openModal() {
            this.isModalActive = true;  
        },
        closeModal() {
            this.isModalActive = false;  
        },
        confirmRemoval() {
            this.$emit('removeFromCart', this.item);  
            this.updateCart();  
            this.closeModal();  
        },
    }
}
</script>

<style scoped>
.modal {
    display: none;
}
.modal.is-active {
    display: flex;
}
</style>
