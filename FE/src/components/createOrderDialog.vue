<template>
  <div class="text-center pa-4">
    <v-btn @click="dialog = true">Create order</v-btn>

    <v-dialog v-model="dialog" width="auto">
      <v-card
        max-width="400"
        prepend-icon="mdi-update"
        text="Please send your email"
        title="Create order"
      >
        <v-form validate-on="submit lazy" @submit.prevent="submit">
          <v-text-field
            v-model="email"
            label="E-mail"
          ></v-text-field>

          <v-btn
            :loading="loading"
            class="mt-2"
            text="Submit"
            type="submit"
            block
          ></v-btn>
        </v-form>
        <template v-slot:actions>
          <v-btn class="ms-auto" text="Ok" @click="dialog = false"></v-btn>
        </template>
      </v-card>
    </v-dialog>
  </div>
</template>

<script lang="ts">
export default {
  data() {
    return {
      dialog: false,
      loading: false,
      email: '',
    }
  },
  methods: {
    async submit(event) {
      this.loading = true

      console.log(event)
      const response = await fetch('http://localhost:8000',
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({"email": this.email})
        }
      )
      if (response.ok) {
        await this.$emit("reloadOrders")
        this.loading = false
        this.dialog = false
        this.email = ''
      }
    },
  },
  emits: ['reloadOrders']
}
</script>
