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
import store from "./store";

const app = createApp(App)


// Install the store instance as a plugin
app.use(store)

registerPlugins(app)

app.mount('#app')
