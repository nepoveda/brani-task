const state = () => ({
  tags: [],
})

const mutations = {
  setTags(state, {tags}): void {
    state.tags = tags;
  }
}

const actions = {
  async fetchTags({commit}) {
    let res = await fetch('http://localhost:8000/tags')
    if (res.ok) {
      commit('setTags', await res.json())
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
