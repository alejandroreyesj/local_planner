<template>
  <div class="fixed right-0 top-0 w-[min(1000px,calc(100vw-1200px))] h-screen border-l border-gray-200 p-4 overflow-y-auto bg-white z-10">
    <div class="mb-4 flex gap-2 pl-[60px]">
      <div 
        v-for="(day, index) in weekDays" 
        :key="day.date"
        class="flex-1 text-center"
        :class="{'border-r border-gray-200 pr-2': index < weekDays.length - 1}"
      >
        <div class="font-semibold text-gray-600">{{ day.name }}</div>
        <div class="text-2xl font-bold">{{ day.number }}</div>
      </div>
    </div>
    <div class="relative">
      <div 
        v-for="hour in 24" 
        :key="hour"
        class="absolute left-0 right-0 h-[60px] border-b border-gray-200 flex items-start"
        :style="{ top: `${hour * 60}px` }"
      >
        <div class="w-[60px] pr-2 text-right text-gray-600 sticky top-0">
          {{ formatHour(hour - 1) }}
        </div>
        <div class="flex-1 flex gap-2">
          <div 
            v-for="(day, index) in weekDays" 
            :key="day.date"
            class="flex-1 min-h-[60px] relative"
            :class="{'border-r border-gray-200 pr-2': index < weekDays.length - 1}"
          >
            <!-- Events will go here -->
          </div>
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

const weekDays = computed(() => {
  const startOfWeek = new Date(props.date)
  startOfWeek.setDate(props.date.getDate() - props.date.getDay())
  
  const days = []
  for (let i = 0; i < 7; i++) {
    const date = new Date(startOfWeek)
    date.setDate(startOfWeek.getDate() + i)
    days.push({
      date,
      name: date.toLocaleDateString('default', { weekday: 'short' }),
      number: date.getDate()
    })
  }
  return days
})

const formatHour = (hour: number) => {
  const period = hour >= 12 ? 'PM' : 'AM'
  const displayHour = hour % 12 || 12
  return `${displayHour}:00 ${period}`
}
</script> 