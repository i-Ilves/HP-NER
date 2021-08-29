import { createStore } from 'vuex'

const state = {
  texts: []
}

const mutations = {
  setTexts(state, texts){
    state.texts = texts
  },

  appendText(state, text){
    state.texts.push(text)
  }
}

const actions = {
  async initTexts(store){
    let texts = await fetch('/api/texts')
    texts = await texts.json()
    store.commit('setTexts', texts)
    console.log(state.texts);
  }
}

export default createStore({state, mutations, actions})