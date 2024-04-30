<script lang="ts">
import {defineComponent} from 'vue'

export default defineComponent({
  name: "TagList",
  data() {
    return {
      loading: false,
      tags: null
    }
  },
  methods: {
    async fetchData() {
      this.tags = null
      this.loading = null
      let res = await fetch('http://localhost:8000/tags')
      if (res.ok) {
        this.tags = await res.json()
      }
      this.loading = false

    }
  },
  created() {
      this.fetchData()
  },
})
</script>

<template>
  <CreateTagDialog @reloadTags="fetchData"/>
  <div class="d-flex justify-center">
    <v-chip
      class="ma-2"
      v-model="tags"
      v-for="tag in tags"
      label
      variant="outlined"
      prepend-icon="mdi-tag"
    >
      {{tag.name}}
    </v-chip>

  </div>

</template>

<style scoped>

</style>
