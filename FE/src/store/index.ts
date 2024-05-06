import {createStore} from 'vuex'
import tags from './modules/tags'
import orders from './modules/orders'

const store = createStore({
  modules: {
    tags,
    orders
  },
  strict: false
})

export default store
