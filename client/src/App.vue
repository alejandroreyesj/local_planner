<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import CalendarView from './components/CalendarView.vue'
</script>

<template>
  <div class="min-h-screen bg-gray-50">
    <header class="bg-white shadow">
      <div class="max-w-7xl mx-auto py-6 px-4">
        <h1 class="text-3xl font-bold text-gray-900">Digital Planner</h1>
      </div>
      <link href="/assets/main.css" rel="stylesheet" />
    </header>
    <main>
      <div class="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
        <CalendarView />
      </div>
    </main>
  </div>
</template>

<style scoped>
</style>
