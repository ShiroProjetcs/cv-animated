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
        
      <button 
        @click="toggleMenu"
        class="md:hidden w-10 h-10 flex flex-col justify-center items-center gap-1.5 z-[110]"
      >
        <span class="w-6 h-0.5 bg-white transition-all duration-300" :class="{ 'rotate-45 translate-y-2': mobileMenuOpen }"></span>
        <span class="w-6 h-0.5 bg-white transition-opacity duration-300" :class="{ 'opacity-0': mobileMenuOpen }"></span>
        <span class="w-6 h-0.5 bg-white transition-all duration-300" :class="{ '-rotate-45 -translate-y-2': mobileMenuOpen }"></span>
      </button>
    </div> <!-- Cierre del div secundario -->
  </div> <!-- Cierre del div principal de línea 27 que faltaba -->

    <!-- Mobile Menu Overlay - Minimalist Centered Design -->
    <transition 
      enter-active-class="transition-all duration-500 ease-out"
      enter-from-class="opacity-0 backdrop-blur-0"
      enter-to-class="opacity-100 backdrop-blur-2xl"
      leave-active-class="transition-all duration-300 ease-in"
      leave-from-class="opacity-100 backdrop-blur-2xl"
      leave-to-class="opacity-0 backdrop-blur-0"
    >
      <div 
        v-if="mobileMenuOpen"
        class="fixed inset-0 bg-black/95 z-[150] md:hidden flex flex-col items-center justify-center p-6"
      >
        <!-- Close Button -->
        <button 
          @click="closeMenu" 
          class="absolute top-6 right-6 w-12 h-12 flex items-center justify-center rounded-full bg-white/5 border border-white/10 text-white hover:bg-red-500/10 hover:border-red-500/50 transition-all"
        >
          <i class="ph ph-x text-2xl"></i>
        </button>

        <!-- Centered Navigation -->
        <nav class="flex flex-col items-center gap-10">
          <a href="#perfil" @click="closeMenu" class="group flex flex-col items-center">
            <span class="text-red-500 font-mono text-xs mb-2 tracking-[0.3em] opacity-0 group-hover:opacity-100 transition-all uppercase">Explorar</span>
            <span class="text-4xl sm:text-5xl font-['Outfit'] font-black text-white hover:text-red-500 transition-colors uppercase tracking-tight">Perfil</span>
          </a>
          <a href="#experiencia" @click="closeMenu" class="group flex flex-col items-center">
            <span class="text-red-500 font-mono text-xs mb-2 tracking-[0.3em] opacity-0 group-hover:opacity-100 transition-all uppercase">Trayectoria</span>
            <span class="text-4xl sm:text-5xl font-['Outfit'] font-black text-white hover:text-red-500 transition-colors uppercase tracking-tight">Experiencia</span>
          </a>
          <a href="#habilidades" @click="closeMenu" class="group flex flex-col items-center">
            <span class="text-red-500 font-mono text-xs mb-2 tracking-[0.3em] opacity-0 group-hover:opacity-100 transition-all uppercase">Arsenal</span>
            <span class="text-4xl sm:text-5xl font-['Outfit'] font-black text-white hover:text-red-500 transition-colors uppercase tracking-tight">Habilidades</span>
          </a>
          <a href="#contacto" @click="closeMenu" class="group flex flex-col items-center">
            <span class="text-red-500 font-mono text-xs mb-2 tracking-[0.3em] opacity-0 group-hover:opacity-100 transition-all uppercase">Contacto</span>
            <span class="text-4xl sm:text-5xl font-['Outfit'] font-black text-white hover:text-red-500 transition-colors uppercase tracking-tight">Contacto</span>
          </a>
        </nav>

        <!-- Social Footer -->
        <div class="absolute bottom-12 flex gap-8">
          <a href="https://linkedin.com/in/luisalbertojm/" target="_blank" class="text-white/40 hover:text-white transition-colors text-2xl"><i class="ph ph-linkedin-logo"></i></a>
          <a href="https://github.com/ShiroProjects" target="_blank" class="text-white/40 hover:text-white transition-colors text-2xl"><i class="ph ph-github-logo"></i></a>
          <a href="mailto:srshipropro@gmail.com" class="text-white/40 hover:text-white transition-colors text-2xl"><i class="ph ph-envelope-simple"></i></a>
        </div>
      </div>
    </transition>
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
