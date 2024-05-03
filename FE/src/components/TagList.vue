<script lang="ts">
import {defineComponent} from 'vue'
import {mapActions} from "vuex";

export default defineComponent({
  name: "TagList",
  computed: {
    tags() {
      return this.$store.state.tags
    }
  },
  methods: {
    ...mapActions(['fetchTags'])
  },
  created() {
    this.fetchTags()
  }
})
</script>

<template>
  <v-container>
    <CreateTagDialog/>
    <div class="d-flex justify-center ">
      <v-chip
        class="ma-2"
        v-model="this.$store.state.tags"
        v-for="tag in this.$store.state.tags"
        labstore.state="outlined"
        prepend-icon="mdi-tag"
      >
        {{ tag.name }}
      </v-chip>

    </div>
  </v-container>

</template>

<style scoped>

</style>
