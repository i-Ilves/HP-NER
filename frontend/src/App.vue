<template>
  <main>
    <MainMenu />
    <router-view />
  </main>
</template>

<script setup>
import Home from './views/Home.vue';
import MainMenu from "./components/MainMenu.vue";

    
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
