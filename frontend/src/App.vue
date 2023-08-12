<script setup lang="ts">
import CutBlock from './components/CutBlock.vue'
import ScissorsLogo from './components/icons/ScissorsLogo.vue';
</script>

<template>
  <header class="text-blue-950">
    <ScissorsLogo />
    <span>Cut URL</span>
  </header>

  <main>
    <CutBlock />
  </main>
</template>

<style scoped>
header {
  display: flex;
  gap: 16px;
  font-size: 56px;
  font-family: 'Charnego Nation', sans-serif;
}

@media (max-width: 360px) {
  header {
    font-size: 46px;
  }
}
</style>
