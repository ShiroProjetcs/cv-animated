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
      <transition 
        enter-active-class="transition duration-300 ease-out"
        enter-from-class="opacity-0 translate-x-full"
        enter-to-class="opacity-100 translate-x-0"
        leave-active-class="transition duration-200 ease-in"
        leave-from-class="opacity-100 translate-x-0"
        leave-to-class="opacity-0 translate-x-full"
      >
        <div 
          v-if="mobileMenuOpen"
          class="fixed inset-0 bg-[#0a0a0c] z-[150] md:hidden flex flex-col p-8"
        >
          <!-- Menu Header -->
          <div class="flex justify-between items-center mb-16">
            <span class="font-['Outfit'] font-black text-2xl tracking-tighter">
              LUIS<span class="text-[#e61919]">_</span>A<span class="text-[#e61919]">.</span>
            </span>
            <button @click="closeMenu" class="w-12 h-12 flex items-center justify-center rounded-full bg-white/5 border border-white/10">
              <i class="ph ph-x text-2xl text-white"></i>
            </button>
          </div>

          <!-- Navigation Links -->
          <nav class="flex flex-col gap-6">
            <a href="#perfil" @click="closeMenu" class="group flex items-end gap-4 border-b border-white/5 pb-4">
              <span class="text-[#e61919] font-mono text-lg mb-1">01</span>
              <span class="text-4xl font-bold text-white group-hover:text-[#e61919] transition-colors">Perfil</span>
            </a>
            <a href="#experiencia" @click="closeMenu" class="group flex items-end gap-4 border-b border-white/5 pb-4">
              <span class="text-[#e61919] font-mono text-lg mb-1">02</span>
              <span class="text-4xl font-bold text-white group-hover:text-[#e61919] transition-colors">Experiencia</span>
            </a>
            <a href="#habilidades" @click="closeMenu" class="group flex items-end gap-4 border-b border-white/5 pb-4">
              <span class="text-[#e61919] font-mono text-lg mb-1">03</span>
              <span class="text-4xl font-bold text-white group-hover:text-[#e61919] transition-colors">Habilidades</span>
            </a>
            <a href="#contacto" @click="closeMenu" class="group flex items-end gap-4 border-b border-white/5 pb-4">
              <span class="text-[#e61919] font-mono text-lg mb-1">04</span>
              <span class="text-4xl font-bold text-white group-hover:text-[#e61919] transition-colors">Contacto</span>
            </a>
          </nav>

          <!-- Bottom Actions -->
          <div class="mt-auto pt-10 border-t border-white/5">
            <p class="text-gray-500 text-sm mb-6 uppercase tracking-widest font-bold">Inicia una conversación</p>
            <a href="mailto:srshipropro@gmail.com" class="flex items-center justify-between w-full p-5 bg-[#e61919] text-white rounded-2xl font-bold mb-8">
              <span>HOLA@LUIS.A</span>
              <i class="ph ph-arrow-right text-xl"></i>
            </a>
            
            <div class="flex gap-6">
              <a href="https://linkedin.com/in/luisalbertojm/" target="_blank" class="w-12 h-12 rounded-xl bg-white/5 flex items-center justify-center text-xl text-white/50 hover:text-[#e61919] transition-all border border-white/10">
                <i class="ph ph-linkedin-logo"></i>
              </a>
              <a href="https://github.com/ShiroProjects" target="_blank" class="w-12 h-12 rounded-xl bg-white/5 flex items-center justify-center text-xl text-white/50 hover:text-[#e61919] transition-all border border-white/10">
                <i class="ph ph-github-logo"></i>
              </a>
            </div>
          </div>
        </div>
      </transition>
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
