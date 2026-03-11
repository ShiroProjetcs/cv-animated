<script setup>
import { computed } from 'vue'

const age = computed(() => {
  const birthDate = new Date('1998-04-08')
  const today = new Date()
  let age = today.getFullYear() - birthDate.getFullYear()
  const m = today.getMonth() - birthDate.getMonth()
  if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) {
    age--
  }
  return age
})
</script>

<template>
  <section id="perfil" class="py-24 max-w-5xl mx-auto px-6">
    <div class="glass-card hover-red text-center relative px-8 py-16 lg:px-16 overflow-hidden group">
      <!-- Glow Decorativo -->
      <div class="absolute -top-24 -left-24 w-64 h-64 bg-red-500/10 rounded-full blur-3xl group-hover:bg-red-500/20 transition-all duration-700"></div>
      <div class="absolute -bottom-24 -right-24 w-64 h-64 bg-red-500/10 rounded-full blur-3xl group-hover:bg-red-500/20 transition-all duration-700"></div>

      <i class="ph-fill ph-quotes text-6xl text-[#e61919]/20 absolute top-6 left-1/2 -translate-x-1/2"></i>
      
      <h3 class="text-4xl md:text-5xl font-['Outfit'] font-black mb-10 tracking-tight uppercase relative z-10">
        Perfil <span class="text-[#e61919]">Profesional</span>
      </h3>
      
      <p class="text-[1.35rem] leading-relaxed text-[#94949b] font-light relative z-10">
        Técnico IT de <span class="text-white font-bold">{{ age }} años</span> con sólida experiencia en soporte avanzado, mantenimiento de equipos profesionales y desarrollo de proyectos digitales.
        Combino una alta capacidad de resolución de problemas técnicos en entornos corporativos con la integración de herramientas de Inteligencia Artificial para optimizar procesos.
      </p>
    </div>
  </section>
</template>
