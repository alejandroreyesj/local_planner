<template>
  <div 
    class="day-view" 
    style="
      position: fixed;
      right: 0;
      top: 0;
      width: 300px;
      height: 100vh;
      border-left: 1px solid #e5e7eb;
      padding: 1rem;
      overflow-y: auto;
      background-color: white;
      z-index: 10;
    "
  >
    <div class="day-header" style="margin-bottom: 1rem;">
      <h3 style="font-size: 1.5rem; font-weight: bold;">{{ formattedDate }}</h3>
    </div>
    <div class="time-slots" style="display: flex; flex-direction: column; gap: 0.5rem;">
      <div 
        v-for="hour in 24" 
        :key="hour" 
        class="time-slot"
        style="
          border: 1px solid #e5e7eb;
          border-radius: 0.25rem;
          padding: 0.5rem;
          min-height: 60px;
          display: flex;
          align-items: flex-start;
          gap: 0.5rem;
        "
      >
        <span style="font-weight: 500; color: #4b5563;">
          {{ formatHour(hour - 1) }}
        </span>
        <div style="flex: 1; min-height: 100%;">
          <!-- Events will go here -->
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'

const props = defineProps<{
  date: Date
}>()

const formattedDate = computed(() => {
  return props.date.toLocaleDateString('default', { 
    weekday: 'long',
    month: 'long',
    day: 'numeric',
    year: 'numeric'
  })
})

const formatHour = (hour: number) => {
  const period = hour >= 12 ? 'PM' : 'AM'
  const displayHour = hour % 12 || 12
  return `${displayHour}:00 ${period}`
}
</script> 