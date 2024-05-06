import {createStore} from 'vuex'

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

export default store
