
const state = () => ({
  allOrders: []
})

const mutations = {
  setOrders(state, orders): void{
    state.allOrders = orders;
  }
}

const actions = {
  async fetchOrders({commit}) {
    let res = await fetch('http://127.0.0.1:8000')
    if (res.ok) {
      const orders = await res.json()
      commit('setOrders', orders)
    } else {
      commit('setOrders', [])
    }
  },
}

export default {
  namespaced: true,
  state,
  mutations,
  actions
}
