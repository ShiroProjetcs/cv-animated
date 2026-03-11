<script setup>
import { ref, onMounted } from 'vue'

const hidden = ref(true)

onMounted(() => {
  setTimeout(() => {
    hidden.value = false
  }, 100)
})
</script>

<template>
  <nav 
    class="fixed top-0 left-0 w-full px-6 py-5 z-[100] backdrop-blur-xl border-b border-red-500/10 bg-black/80 transition-all duration-500 ease-out" 
    :class="{ '-translate-y-full opacity-0': hidden }"
  >
    <div class="max-w-6xl mx-auto flex justify-between items-center">
      <span class="font-['Outfit'] font-black text-2xl tracking-tighter">
        LUIS<span class="text-[#e61919]">_</span>A<span class="text-[#e61919]">.</span>
      </span>
      <ul class="hidden md:flex gap-8">
        <li><a href="#perfil" class="nav-link">Perfil</a></li>
        <li><a href="#experiencia" class="nav-link">Experiencia</a></li>
        <li><a href="#habilidades" class="nav-link">Habilidades</a></li>
        <li><a href="#contacto" class="nav-link">Contacto</a></li>
      </ul>
      <a href="mailto:srshipropro@gmail.com" class="px-5 py-2 bg-white/5 border border-white/10 rounded-full text-xs font-bold hover:bg-red-500/10 hover:border-[#e61919] transition-all duration-300">
        HOLA@LUIS.A
      </a>
    </div>
  </nav>
</template>

<style scoped>
.nav-link {
  @apply text-[#94949b] text-[0.95rem] font-semibold uppercase tracking-widest relative transition-colors duration-300;
}
.nav-link:hover {
  @apply text-white;
}
.nav-link::after {
  content: '';
  @apply absolute -bottom-1.5 left-0 w-0 h-0.5 bg-gradient-to-br from-[#e61919] to-[#a30000] transition-all duration-300;
}
.nav-link:hover::after {
  @apply w-full;
}
</style>
