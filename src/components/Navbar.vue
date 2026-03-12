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
        class="fixed inset-0 bg-[#0d0d0f]/98 backdrop-blur-3xl z-[100] md:hidden transition-all duration-500 ease-in-out flex flex-col items-center justify-center"
        :class="mobileMenuOpen ? 'opacity-100 visible' : 'opacity-0 invisible pointer-events-none'"
      >
        <div class="flex flex-col items-center gap-8" :class="{ 'translate-y-0': mobileMenuOpen, 'translate-y-10': !mobileMenuOpen }">
          <a 
            href="#perfil" 
            @click="closeMenu" 
            class="mobile-nav-link"
            :style="{ transitionDelay: '100ms' }"
          >
            <span class="text-[#e61919] mr-2 opacity-50 font-mono">01.</span> Perfil
          </a>
          <a 
            href="#experiencia" 
            @click="closeMenu" 
            class="mobile-nav-link"
            :style="{ transitionDelay: '200ms' }"
          >
            <span class="text-[#e61919] mr-2 opacity-50 font-mono">02.</span> Experiencia
          </a>
          <a 
            href="#habilidades" 
            @click="closeMenu" 
            class="mobile-nav-link"
            :style="{ transitionDelay: '300ms' }"
          >
            <span class="text-[#e61919] mr-2 opacity-50 font-mono">03.</span> Habilidades
          </a>
          <a 
            href="#contacto" 
            @click="closeMenu" 
            class="mobile-nav-link"
            :style="{ transitionDelay: '400ms' }"
          >
            <span class="text-[#e61919] mr-2 opacity-50 font-mono">04.</span> Contacto
          </a>
          
          <div class="mt-8 flex flex-col items-center gap-6" :style="{ transitionDelay: '500ms' }">
            <a href="mailto:srshipropro@gmail.com" class="px-8 py-3 bg-[#e61919] text-white rounded-full font-bold shadow-[0_10px_30px_rgba(230,25,25,0.3)] hover:scale-105 active:scale-95 transition-all">
              HOLA@LUIS.A
            </a>
            <div class="flex gap-6 mt-4">
              <a href="https://linkedin.com" target="_blank" class="text-white/40 text-2xl hover:text-white transition-colors"><i class="ph ph-linkedin-logo"></i></a>
              <a href="https://github.com" target="_blank" class="text-white/40 text-2xl hover:text-white transition-colors"><i class="ph ph-github-logo"></i></a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<style scoped>
.mobile-nav-link {
  @apply text-4xl font-['Outfit'] font-black uppercase tracking-tighter text-white/90 transition-all duration-500;
}
.mobile-nav-link:active {
  @apply text-[#e61919] scale-110;
}
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
