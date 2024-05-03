<template>
  <h2>Tags</h2>
  <TagList />
  <h2>Orders</h2>
  <OrderList />
</template>

<script lang="ts">
import { defineComponent } from "vue";
import OrderList from "../components/OrderList.vue";
import TagList from "../components/TagList.vue";
export default {
  components: {OrderList, TagList},
  // data() {
  //   return {
  //     loading: false,
  //     tags: null,
  //   }
  // },
  // methods: {
  //     async fetchTags() {
  //       console.log("jsem vůl")
  //       this.tags = null
  //       this.loading = null
  //       let res = await fetch('http://localhost:8000/tags')
  //       if (res.ok) {
  //         this.tags = await res.json()
  //       }
  //       this.loading = false
  //       this.$forceUpdate()
  //     },
  // },
}

</script>
