<script setup>
import { ref, onMounted } from 'vue'

const hidden = ref(true)
const mobileMenuOpen = ref(false)

const toggleMenu = () => {
  mobileMenuOpen.value = !mobileMenuOpen.value
}

const closeMenu = () => {
  mobileMenuOpen.value = false
}

onMounted(() => {
  setTimeout(() => {
    hidden.value = false
  }, 100)
})
</script>

<template>
  <nav 
    class="fixed top-0 left-0 w-full px-6 py-4 md:py-5 z-[100] backdrop-blur-xl border-b border-red-500/10 bg-black/80 transition-all duration-500 ease-out" 
    :class="{ '-translate-y-full opacity-0': hidden }"
  >
    <div class="max-w-6xl mx-auto flex justify-between items-center relative">
      <span class="font-['Outfit'] font-black text-2xl tracking-tighter z-[110]">
        LUIS<span class="text-[#e61919]">_</span>A<span class="text-[#e61919]">.</span>
      </span>
      
      <!-- Desktop Links -->
      <ul class="hidden md:flex gap-8">
        <li><a href="#perfil" class="nav-link">Perfil</a></li>
        <li><a href="#experiencia" class="nav-link">Experiencia</a></li>
        <li><a href="#habilidades" class="nav-link">Habilidades</a></li>
        <li><a href="#contacto" class="nav-link">Contacto</a></li>
      </ul>

      <div class="flex items-center gap-4">
        <a href="mailto:srshipropro@gmail.com" class="hidden sm:block px-5 py-2 bg-white/5 border border-white/10 rounded-full text-xs font-bold hover:bg-red-500/10 hover:border-[#e61919] transition-all duration-300">
          HOLA@LUIS.A
        </a>
        
        <!-- Mobile Toggle -->
        <button 
          @click="toggleMenu"
          class="md:hidden w-10 h-10 flex flex-col justify-center items-center gap-1.5 z-[110]"
        >
          <span class="w-6 h-0.5 bg-white transition-all duration-300" :class="{ 'rotate-45 translate-y-2': mobileMenuOpen }"></span>
          <span class="w-6 h-0.5 bg-white transition-opacity duration-300" :class="{ 'opacity-0': mobileMenuOpen }"></span>
          <span class="w-6 h-0.5 bg-white transition-all duration-300" :class="{ '-rotate-45 -translate-y-2': mobileMenuOpen }"></span>
        </button>
      </div>

      <!-- Mobile Menu Overlay -->
      <div 
        class="fixed inset-0 bg-black/95 backdrop-blur-2xl z-[100] md:hidden transition-all duration-500 flex flex-col items-center justify-center gap-8"
        :class="mobileMenuOpen ? 'opacity-100 visible' : 'opacity-0 invisible pointer-events-none'"
      >
        <a href="#perfil" @click="closeMenu" class="text-3xl font-bold uppercase tracking-widest text-white/60 hover:text-[#e61919]">Perfil</a>
        <a href="#experiencia" @click="closeMenu" class="text-3xl font-bold uppercase tracking-widest text-white/60 hover:text-[#e61919]">Experiencia</a>
        <a href="#habilidades" @click="closeMenu" class="text-3xl font-bold uppercase tracking-widest text-white/60 hover:text-[#e61919]">Habilidades</a>
        <a href="#contacto" @click="closeMenu" class="text-3xl font-bold uppercase tracking-widest text-white/60 hover:text-[#e61919]">Contacto</a>
        <a href="mailto:srshipropro@gmail.com" class="mt-4 px-8 py-3 bg-[#e61919] text-white rounded-full font-bold">HOLA@LUIS.A</a>
      </div>
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
