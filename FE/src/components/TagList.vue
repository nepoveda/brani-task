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
  }
})
</script>

<template>

</template>

<style scoped>

</style>
