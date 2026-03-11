<script setup>
import Navbar from './components/Navbar.vue'
import Hero from './components/Hero.vue'
import Profile from './components/Profile.vue'
import Experience from './components/Experience.vue'
import Skills from './components/Skills.vue'
import EducationLangs from './components/EducationLangs.vue'
import ContactFooter from './components/ContactFooter.vue'
</script>

<template>
  <div class="cursor-glow"></div>
  
  <Navbar />
  
  <main class="relative z-10">
    <Hero />
    <Profile />
    <Experience />
    <Skills />
    <EducationLangs />
    <ContactFooter />
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
