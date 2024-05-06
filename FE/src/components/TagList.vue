<script lang="ts">
import {mapState} from "vuex";
import {defineComponent} from 'vue'

export default defineComponent({
  name: "TagList",
  computed: mapState("tags", ["allTags"]),
  created() {
    this.$store.dispatch('tags/fetchTags')
  }
})
</script>

<template>
  <v-container>
    <CreateTagDialog/>
    <div class="d-flex justify-center ">
      <v-chip
        class="ma-2"
        v-for="tag in allTags"
        labstore.state="outlined"
        prepend-icon="mdi-tag"
      >
        {{ tag.name }} ({{tag.orders.length}})
      </v-chip>

    </div>
  </v-container>

</template>

<style scoped>

</style>
