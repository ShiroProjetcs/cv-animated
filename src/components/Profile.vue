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
  <section id="perfil" class="py-16 md:py-24 max-w-5xl mx-auto px-6">
    <div class="glass-card hover-red text-center relative px-6 py-12 md:px-16 md:py-16 overflow-hidden group">
      <!-- Glow Decorativo -->
      <div class="absolute -top-24 -left-24 w-64 h-64 bg-red-500/10 rounded-full blur-3xl group-hover:bg-red-500/20 transition-all duration-700"></div>
      <div class="absolute -bottom-24 -right-24 w-64 h-64 bg-red-500/10 rounded-full blur-3xl group-hover:bg-red-500/20 transition-all duration-700"></div>

      <i class="ph-fill ph-quotes text-5xl md:text-6xl text-[#e61919]/20 absolute top-6 left-1/2 -translate-x-1/2"></i>
      
      <h3 class="text-3xl md:text-5xl font-['Outfit'] font-black mb-6 md:mb-10 tracking-tight uppercase relative z-10">
        Perfil <span class="text-[#e61919]">Profesional</span>
      </h3>
      
      <p class="text-lg md:text-[1.35rem] leading-relaxed text-[#94949b] font-light relative z-10">
        Soy un apasionado de la tecnología con <span class="text-white font-bold">casi 10 años de experiencia</span> ayudando a empresas a que su informática no sea un problema. 
        Me especializo en dar soluciones reales: desde que una impresora o destructora vuelva a funcionar, hasta montar tiendas online atractivas integrando las últimas herramientas de <span class="text-[#e61919] font-bold">Inteligencia Artificial</span> para que todo sea más fácil.
      </p>
    </div>
  </section>
</template>
