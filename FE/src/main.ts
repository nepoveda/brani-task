/**
 * main.ts
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

// Plugins
import {registerPlugins} from './plugins'

// Components
import App from './App.vue'

// Composables
import {createApp} from 'vue'
import {createStore} from 'vuex'

// Create a new store instance.
const store = createStore({
  state() {
    return {
      tags: []
    }
  },
  mutations: {
    loadTags(state, tags) {
      state.tags = tags
    }
  },
  actions: {
    async fetchTags({commit}) {
      let res = await fetch('http://localhost:8000/tags')
      if (res.ok) {
        commit('loadTags', await res.json())
      } else {
        commit('loadTags', [])
      }
    },
  }
})


const app = createApp(App)

// Install the store instance as a plugin
app.use(store)

registerPlugins(app)

app.mount('#app')
