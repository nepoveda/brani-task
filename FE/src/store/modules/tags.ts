const state = () => ({
  allTags: [],
})

const mutations = {
  setTags(state, tags): void {
    state.allTags = tags;
  }
}

const actions = {
  async fetchTags({commit}) {
    let res = await fetch('http://localhost:8000/tags')
    if (res.ok) {
      const tags = await res.json()
      commit('setTags', tags)
    } else {
      commit('setTags', [])
    }
  },
}

export default {
  namespaced: true,
  state,
  mutations,
  actions
}
