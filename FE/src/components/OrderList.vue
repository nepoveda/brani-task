<script lang="ts">
import {defineComponent} from 'vue'
import createOrderDialog from "./CreateOrderDialog.vue";
import {mapActions, mapState} from "vuex";

export default defineComponent({
  name: "OrderList",
  data() {
    return {
      headers: [
        {title: 'code', value: 'code'},
        {title: 'email', value: 'email'},
        {title: 'date', key: 'created', value: (item) => `${new Date(item.created).toLocaleDateString()}`}
      ],
    }
  },
  computed: mapState("orders", ["allOrders"]),
  created() {
    this.$store.dispatch('orders/fetchOrders')
  },
  components: {
    createOrderDialog
  }
})
</script>

<template>
  <v-container>
    <create-order-dialog></create-order-dialog>
    <v-data-table
      v-model="allOrders"
      :items="allOrders"
      :headers="headers"
    ></v-data-table>
  </v-container>
</template>

<style scoped>

</style>
