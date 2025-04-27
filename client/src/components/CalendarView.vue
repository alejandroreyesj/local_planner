<template>
  <div style="display: flex; min-height: 100vh;">
    <div class="calendar-container" style="width: 1200px; padding: 2rem; margin: 0 auto;">
      <div class="calendar-header" style="margin-bottom: 2rem; text-align: center;">
        <h2 style="font-size: 2rem; font-weight: bold;">{{ currentMonthName }} {{ currentYear }}</h2>
      </div>
      <div class="calendar-grid" style="display: grid; grid-template-columns: repeat(7, 1fr); gap: 0.5rem;">
        <div 
          v-for="day in weekDays" 
          :key="day" 
          class="weekday" 
          style="text-align: center; font-weight: 600; color: #4b5563; font-size: 1.25rem; padding: 0.5rem;"
        >
          {{ day }}
        </div>
        <div
          v-for="day in calendarDays"
          :key="day.date"
          class="calendar-day"
          :style="{
            'aspect-ratio': '1/1',
            'min-height': '120px',
            'padding': '0.75rem',
            'border': '1px solid #e5e7eb',
            'border-radius': '0.5rem',
            'background-color': day.isCurrentMonth ? '#ffffff' : '#f9fafb',
            'color': day.isCurrentMonth ? 'inherit' : '#9ca3af',
            'border-color': day.isToday ? '#93c5fd' : '#e5e7eb',
            'background-color': day.isToday ? '#dbeafe' : (day.isCurrentMonth ? '#ffffff' : '#f9fafb'),
            'display': 'flex',
            'flex-direction': 'column',
            'position': 'relative',
            'cursor': 'pointer',
            'transition': 'all 0.2s ease',
            '&:hover': {
              'background-color': '#f3f4f6'
            }
          }"
          @click="selectDay(day)"
        >
          <span class="day-number" style="font-size: 1.25rem; font-weight: 500; position: absolute; top: 0.5rem; right: 0.5rem;">{{ day.day }}</span>
        </div>
      </div>
    </div>
    <WeekView v-if="selectedDay" :date="selectedDay" />
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import WeekView from './WeekView.vue'

const currentDate = ref(new Date())
const selectedDay = ref<Date | null>(null)
const currentMonth = computed(() => currentDate.value.getMonth())
const currentYear = computed(() => currentDate.value.getFullYear())
const currentMonthName = computed(() => {
  return currentDate.value.toLocaleString('default', { month: 'long' })
})

const weekDays = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

const calendarDays = computed(() => {
  const year = currentYear.value
  const month = currentMonth.value
  
  // Get first day of the month
  const firstDay = new Date(year, month, 1)
  // Get last day of the month
  const lastDay = new Date(year, month + 1, 0)
  
  // Get the day of week of the first day (0-6)
  const firstDayOfWeek = firstDay.getDay()
  
  // Get the number of days in the month
  const daysInMonth = lastDay.getDate()
  
  // Get the number of days in the previous month
  const prevMonthLastDay = new Date(year, month, 0)
  const daysInPrevMonth = prevMonthLastDay.getDate()
  
  const days = []
  
  // Add days from previous month
  for (let i = firstDayOfWeek - 1; i >= 0; i--) {
    days.push({
      day: daysInPrevMonth - i,
      date: new Date(year, month - 1, daysInPrevMonth - i),
      isCurrentMonth: false,
      isToday: false
    })
  }
  
  // Add days from current month
  for (let i = 1; i <= daysInMonth; i++) {
    const date = new Date(year, month, i)
    days.push({
      day: i,
      date,
      isCurrentMonth: true,
      isToday: date.toDateString() === new Date().toDateString()
    })
  }
  
  // Add days from next month to complete the grid
  const remainingDays = 42 - days.length // 6 rows * 7 days
  for (let i = 1; i <= remainingDays; i++) {
    days.push({
      day: i,
      date: new Date(year, month + 1, i),
      isCurrentMonth: false,
      isToday: false
    })
  }
  
  return days
})

const selectDay = (day: { date: Date }) => {
  selectedDay.value = day.date
}
</script> 