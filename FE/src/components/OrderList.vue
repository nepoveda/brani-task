<script lang="ts">
import {defineComponent} from 'vue'
import createOrderDialog from "./CreateOrderDialog.vue";

export default defineComponent({
  name: "OrderList",
  data() {
    return {
      headers: [
        {title: 'code', value: 'code'},
        {title: 'email', value: 'email'},
        {title: 'date', key: 'created', value: (item) => `${new Date(item.created).toLocaleDateString()}`}
      ],
      ordersData: null,
      loading: false,
    }
  },
  methods: {
    async fetchData() {
      this.ordersData = null
      this.loading = true
      let res = await fetch('http://127.0.0.1:8000')
      if (res.ok) {
        this.ordersData = await res.json()
      }
      this.loading = false
    },
  },
  created() {
    this.fetchData()
  },
  components: {
    createOrderDialog
  }
})
</script>

<template>
  <v-container>
    <create-order-dialog @reloadOrders="fetchData"></create-order-dialog>
    <!--    TODO somehow it's not updating table when the ordersData are changed(from child)... But it should -->
    <v-data-table
      v-model="loading"
      :items="ordersData"
      :loading="loading"
      :headers="headers"
      :hide-default-footer="true"
    ></v-data-table>
  </v-container>
</template>

<style scoped>

</style>
