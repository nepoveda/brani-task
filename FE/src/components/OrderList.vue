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
        {title: 'date', key: 'created', value: (item) => `${new Date(item.created).toLocaleDateString()}`},
        {title: 'tags', key: 'tags'},
        {title: "actions", key: 'actions', sortable: false}
      ],
      dialogAdd: false
    }
  },
  computed: {
    ...mapState("orders", ["allOrders"]),
    ...mapState("tags", ["allTags"])
  },
  methods: {
    addTag(item) {
      console.log("editing order",item.id)
      this.dialogAdd = true
    },
    submitAddTag(event: Event){
      console.log("ahoj blbečku")
    }
  },
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
    >

      <template v-slot:item.actions="{ item }">
        <v-dialog v-model="dialogAdd">
          <v-card title="Add tag to order">
            <v-form validate-on="submit lazy" @submit.prevent="submitAddTag">
              <v-select
                :items="allTags"
                item-title="name"
                item-value="id"
                :multiple=true
              >
              </v-select>
              <v-btn
                class="mt-2"
                text="Submit"
                type="submit"
                block
              ></v-btn>
            </v-form>
          </v-card>
        </v-dialog>
        <v-icon class="me-2" size="small" @click="addTag(item)">
          mdi-plus
        </v-icon>
      </template>

    </v-data-table>
  </v-container>
</template>

<style scoped>

</style>
