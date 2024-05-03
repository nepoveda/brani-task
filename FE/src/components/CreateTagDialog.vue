<script lang="ts">
import {defineComponent} from 'vue'
import {mapActions} from "vuex";

export default defineComponent({
  name: "CreateTagDialog",
  data() {
    return {
      dialog: false,
      loading: false,
      errorMessages: [],
      name: '',
    }
  },
  methods: {
    ...mapActions(['fetchTags']),
    async submit(event: Event) {
      this.loading = true
      this.errorMessages = []

      const response = await fetch('http://localhost:8000/tags',
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({"name": this.name})
        }
      )
      if (response.ok) {
        await this.fetchTags()
        this.dialog = false
        this.name = ''
      } else{
        this.errorMessages = [response.statusText]
      }
      this.loading = false
    },
  },
  emits: ['reloadTags']
})
</script>

<template>
  <div class="text-center pa-4">
    <v-btn @click="dialog = true">Create Tag</v-btn>

    <v-dialog v-model="dialog" width="auto">
      <v-card
        max-width="400"
        prepend-icon="mdi-plus-box"
        title="Create tag"
      >
        <v-form validate-on="submit lazy" @submit.prevent="submit">
          <v-text-field
            v-model="name"
            label="Name of tag"
            :errorMessages="errorMessages"
          ></v-text-field>

          <v-btn
            :loading="loading"
            class="mt-2"
            text="Submit"
            type="submit"
            block
          ></v-btn>
        </v-form>
      </v-card>
    </v-dialog>
  </div>

</template>

<style scoped>

</style>
