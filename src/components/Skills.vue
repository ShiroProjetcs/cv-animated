<script setup>
const skillCategories = [
  {
    title: 'Soluciones Web',
    icon: 'ph-terminal-window',
    tags: ['Creación de Tiendas Online', 'Estructura Web', 'Despliegue y Hosting', 'Soluciones con IA']
  },
  {
    title: 'Sistemas & Soporte IT',
    icon: 'ph-cpu',
    tags: ['Mantenimiento Mutifunción', 'Diagnóstico Hardware', 'Soporte Remoto/Presencial', 'Redes e Informática']
  },
  {
    title: 'IA & Herramientas',
    icon: 'ph-sparkle',
    tags: ['Uso de LLMs', 'Automatización de Tareas', 'Contenido con IA', 'Mejora de Procesos']
  }
]

const marqueeSkills = [
  'Resolución Ágil de Problemas',
  'Adobe Creative Suite',
  'Premiere Pro & After Effects',
  'Photoshop & Illustrator',
  'DaVinci Resolve',
  'Producción de Eventos',
  'Atención al Cliente Directa',
  'Trabajo bajo Presión',
  'Liderazgo Técnico',
  'Visión de Negocio'
]
</script>

<template>
  <section id="habilidades" class="py-16 md:py-24 max-w-6xl mx-auto px-6 overflow-hidden">
    <h3 class="text-3xl md:text-5xl font-['Outfit'] font-black mb-12 md:mb-16 text-center tracking-tight uppercase">
      Arsenal <span class="text-[#e61919]">Técnico</span>
    </h3>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 md:gap-8">
      
      <!-- Categorías de Habilidades -->
      <div v-for="(category, index) in skillCategories" :key="index" class="glass-card hover-red p-6 md:p-8">
        <h4 class="flex items-center gap-3 text-lg md:text-xl font-bold mb-6 border-b border-white/10 pb-4">
          <i :class="['ph', category.icon, 'text-2xl md:text-3xl text-[#e61919]']"></i>
          {{ category.title }}
        </h4>
        <div class="flex flex-wrap gap-2 md:gap-3">
          <span v-for="tag in category.tags" :key="tag" class="skill-tag text-xs md:text-sm">
            {{ tag }}
          </span>
        </div>
      </div>

      <!-- Marquee de Soft Skills y Producción -->
      <div class="glass-card hover-red md:col-span-3 p-6 md:p-10 overflow-hidden relative">
        <h4 class="flex items-center justify-center gap-3 text-lg md:text-xl font-bold mb-8">
          <i class="ph ph-star text-2xl md:text-3xl text-[#e61919]"></i>
          Software & Soft Skills
        </h4>
        
        <div class="marquee-container flex overflow-hidden w-full relative">
          <!-- Fade edges -->
          <div class="absolute inset-y-0 left-0 w-10 md:w-20 bg-gradient-to-r from-[#0d0d0f] to-transparent z-10"></div>
          <div class="absolute inset-y-0 right-0 w-10 md:w-20 bg-gradient-to-l from-[#0d0d0f] to-transparent z-10"></div>
          
          <div class="marquee-content flex gap-4 md:gap-6 shrink-0 grow-0 animate-scroll hover:pause-animation px-6">
            <span v-for="(skill, i) in marqueeSkills" :key="`a-${i}`" class="marquee-tag text-sm md:text-[1.05rem]">{{ skill }}</span>
            <span v-for="(skill, i) in marqueeSkills" :key="`b-${i}`" class="marquee-tag text-sm md:text-[1.05rem]">{{ skill }}</span>
          </div>
        </div>
      </div>

    </div>
  </section>
</template>

<style scoped>
.skill-tag {
  @apply bg-red-500/5 border border-red-500/15 px-4 py-2.5 rounded-xl text-sm font-medium text-gray-400 transition-all duration-300 cursor-default;
}
.skill-tag:hover {
  @apply bg-gradient-to-br from-[#e61919] to-[#a30000] border-transparent text-white -translate-y-1 scale-[1.02] shadow-[0_5px_15px_rgba(230,25,25,0.3)];
}

.marquee-tag {
  @apply whitespace-nowrap text-[1.05rem] font-medium px-7 py-3 rounded-full bg-red-500/10 border border-red-500/20 text-white transition-all;
}

.animate-scroll {
  animation: scroll 25s linear infinite;
}

.hover\:pause-animation:hover {
  animation-play-state: paused;
}

@keyframes scroll {
  0% { transform: translateX(0); }
  100% { transform: translateX(calc(-50% - 1.5rem)); }
}
</style>
