<script setup lang="ts">
import {ref, onMounted, watch} from 'vue'

let ordersData = ref(null)

async function fetchData() {
  ordersData.value = null
  let res = await fetch('http://127.0.0.1:8000')
  ordersData = await res.json()
}

onMounted(() => {
  console.log("fetching")
  fetchData()
})

watch(ordersData)
</script>

<template>
  <h1>Daníg je vůl</h1>
  <p v-for="order in ordersData">
    {{ order }}
  </p>
</template>

<style scoped>

</style>
