<template>
  <main>
    <router-link to="/"><img class="Luca" src="/src/assets/Luca.jpg" alt="Luca"></router-link>
    <form class="text-wrapper" @submit.prevent="submitText">
      <textarea v-model="text" name="" id="" cols="100" rows="10"></textarea>
      <div class="controls">
        <select v-model="selected" name="type">
          <!-- <option value="ALL">All Entities</option> -->
          <option value="CHARACTER">Characters</option>
          <option value="CREATURE">Creatures</option>
          <option value="EVENT">Events</option>
          <option value="PLACE">Places</option>
          <option value="SPELL">Spells</option>
          <option value="POTION">Potions</option>
        </select>
        <button type="submit">Submit</button>
      </div>
    </form>
    <div class="loading-container">
    <div v-if="loading" v-cloak>
      <div class="loader"></div></div>
    </div>
    <div class="results" v-if="results">
      <p class="result" v-for="r of results" :key="r">{{ r }}</p>
    </div>

<!--     <div class="texts">
      <p class="text" v-for="(text, i) of texts" :key="i">{{ text.text }}</p>
    </div> -->
  </main>
</template>

<script>
export default {
  created() {
    this.$store.dispatch("initTexts");
    
  },
  computed: {
    texts() {
      this.loading = false;
      return this.$store.state.texts; 
    },
  },
  data() {
    return {
      text: "",
      selected: "CHARACTER",
      results: "",
      loading: false,
    };
  },
  methods: {
    async submitText() {
      this.loading = true;
      const textObject = {
        text: this.text,
        type: this.selected,
  
      };

      if (!this.text) return;

      let text = await fetch("/api/texts", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(textObject),
      });

      if (text.ok) {
        text = await text.json();
        this.results = text;
        this.$store.commit("appendText", textObject);
        this.loading = false;
      }
    },
  },
};
</script>

<style scoped>
.text-wrapper {
  display: flex;
  flex-direction: column;
  width: 50%;
  margin: 0 auto;
}

select,
button {
  margin: 15px 15px;
  width: 200px;
  background-color: #DDEFFD;
  color: #5474AA;
  border-radius: 4px;
  padding: 5px;
  border-block-color: rgba(11, 11, 75, 0.219);
  cursor: pointer;
  
}

.loading-container{
  display: flex;
  justify-content: center;
  align-items: center;
}

.loader {

    border: 16px solid #f3f3f3;
    border-top: 16px solid #092233;
    border-radius: 50%;
    width: 70px;
    height: 70px;
    animation: spin 2s linear infinite;
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

.Luca{
  width: 20%;
}

.results {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
}

.result {
  margin: 3px;
  border: 1px solid rgb(13, 41, 65);
  background: rgb(33, 54, 94);
  color: #DDEFFD;
  padding: 5px;
  border-radius: 5px;
}

.texts {
  width: 100%;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: center;
  margin-top: 100px;
}
.text {
  padding: 10px;
  border: 1px solid grey;
  width: 400px;
  max-height: 300px;
  overflow: auto;
  margin: 10px;
  border-radius: 8px;
  background-color: lightgray;
}

.text::-webkit-scrollbar {
  display: none;
}
</style>