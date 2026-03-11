<script setup>
import { onMounted, ref } from 'vue'
import Navbar from './components/Navbar.vue'
import Hero from './components/Hero.vue'
import Profile from './components/Profile.vue'
import Experience from './components/Experience.vue'
import Skills from './components/Skills.vue'
import EducationLangs from './components/EducationLangs.vue'
import ContactFooter from './components/ContactFooter.vue'

const glowPos = ref({ x: 0, y: 0 })

onMounted(() => {
  // Cursor Glow Mouse Tracking
  window.addEventListener('mousemove', (e) => {
    glowPos.value = { x: e.clientX, y: e.clientY }
  })

  // Scroll Reveal Observer
  const observerOptions = {
    threshold: 0.15,
    rootMargin: '0px 0px -50px 0px'
  }

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('active')
      }
    })
  }, observerOptions)

  document.querySelectorAll('.reveal').forEach(el => observer.observe(el))
})
</script>

<template>
  <!-- Dynamic Cursor Glow -->
  <div 
    class="cursor-glow" 
    :style="{ 
      transform: `translate(calc(${glowPos.x}px - 50%), calc(${glowPos.y}px - 50%))` 
    }"
  ></div>
  
  <Navbar />
  
  <main class="relative z-10">
    <Hero />
    <div class="reveal"><Profile /></div>
    <div class="reveal"><Experience /></div>
    <div class="reveal"><Skills /></div>
    <div class="reveal"><EducationLangs /></div>
    <div class="reveal"><ContactFooter /></div>
  </main>
</template>

<style>
/* Global scrollbar styling */
::-webkit-scrollbar {
  width: 10px;
}
::-webkit-scrollbar-track {
  background: #0d0d0f;
}
::-webkit-scrollbar-thumb {
  background: rgba(230, 25, 25, 0.3);
  border-radius: 10px;
}
::-webkit-scrollbar-thumb:hover {
  background: rgba(230, 25, 25, 0.6);
}
</style>
