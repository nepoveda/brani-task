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
}

</script>
