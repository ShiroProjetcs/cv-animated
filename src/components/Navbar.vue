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

    <!-- Mobile Menu Overlay - Teleported to body for absolute control -->
    <Teleport to="body">
      <transition 
        enter-active-class="transition-opacity duration-500 ease-out"
        enter-from-class="opacity-0"
        enter-to-class="opacity-100"
        leave-active-class="transition-opacity duration-300 ease-in"
        leave-from-class="opacity-100"
        leave-to-class="opacity-0"
      >
        <div 
          v-if="mobileMenuOpen"
          class="fixed inset-0 bg-[#070708] z-[9999] flex flex-col items-center justify-center p-6 overflow-hidden md:hidden"
        >
          <!-- Background Decoration (Subtle) -->
          <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[150%] h-[150%] bg-[radial-gradient(circle_at_center,rgba(230,25,25,0.05)_0%,transparent_70%)] pointer-events-none"></div>

          <!-- Close Button -->
          <button 
            @click="closeMenu" 
            class="absolute top-8 right-8 w-14 h-14 flex items-center justify-center rounded-full bg-white/5 border border-white/10 text-white hover:bg-red-500/10 hover:border-red-500/50 transition-all active:scale-90"
          >
            <i class="ph ph-x text-3xl"></i>
          </button>

          <!-- Navigation Links -->
          <nav class="flex flex-col items-center gap-12 relative z-10">
            <a 
              v-for="(link, i) in [
                { id: '#perfil', label: 'Perfil', sub: '01. Perfil Profesional' },
                { id: '#experiencia', label: 'Experiencia', sub: '02. Trayectoria Laboral' },
                { id: '#habilidades', label: 'Habilidades', sub: '03. Arsenal Técnico' },
                { id: '#contacto', label: 'Contacto', sub: '04. Disponibilidad' }
              ]" 
              :key="link.id"
              :href="link.id" 
              @click="closeMenu" 
              class="group flex flex-col items-center"
            >
              <span class="text-xs font-mono text-red-500/60 mb-2 tracking-[0.4em] uppercase opacity-0 group-hover:opacity-100 transition-all duration-300 transform translate-y-2 group-hover:translate-y-0">
                {{ link.sub }}
              </span>
              <span class="text-5xl sm:text-6xl font-['Outfit'] font-black text-white group-hover:text-red-500 transition-all duration-300 uppercase tracking-tighter">
                {{ link.label }}
              </span>
            </a>
          </nav>

          <!-- Professional Footer -->
          <div class="absolute bottom-16 flex flex-col items-center gap-8 w-full px-8">
            <div class="w-12 h-[1px] bg-red-500/30"></div>
            <div class="flex gap-10">
              <a href="https://linkedin.com/in/luisalbertojm/" target="_blank" class="text-white/30 hover:text-red-500 transition-all text-3xl"><i class="ph ph-linkedin-logo"></i></a>
              <a href="https://github.com/ShiroProjects" target="_blank" class="text-white/30 hover:text-red-500 transition-all text-3xl"><i class="ph ph-github-logo"></i></a>
              <a href="mailto:srshipropro@gmail.com" class="text-white/30 hover:text-red-500 transition-all text-3xl"><i class="ph ph-envelope-simple"></i></a>
            </div>
          </div>
        </div>
      </transition>
    </Teleport>
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
