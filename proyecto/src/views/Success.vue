<template>
    <div class="page-success">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Gracias</h1> 
                <p>Su pedido será procesado en un plazo de 48 horas.</p> 
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Success',
    mounted() {
        document.title = 'Éxito | Ferretería'; 

        if (!localStorage.getItem('reloaded')) {
            localStorage.setItem('reloaded', 'true'); 
            setTimeout(() => {
                location.reload();
            }, 10);
        } else {
            localStorage.removeItem('reloaded');
        }
    },
};
</script>
