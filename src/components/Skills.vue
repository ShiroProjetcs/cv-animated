<script setup>
const skillCategories = [
  {
    title: 'Desarrollo & E-Commerce',
    icon: 'ph-terminal-window',
    tags: ['Shopify', 'WordPress / WooCommerce', 'Desarrollo Web Fullstack', 'Gestión CMS']
  },
  {
    title: 'IT & Sistemas',
    icon: 'ph-cpu',
    tags: ['Soporte Técnico Especializado', 'Redes y Configuración', 'Diagnóstico Hardware', 'Mantenimiento Preventivo']
  },
  {
    title: 'IA & Automatización',
    icon: 'ph-sparkle',
    tags: ['Prompt Engineering', 'LLM Workflows', 'Generación de Assets IA', 'Análisis de Datos con IA']
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
  <section id="habilidades" class="py-24 max-w-6xl mx-auto px-6 overflow-hidden">
    <h3 class="text-4xl md:text-5xl font-['Outfit'] font-black mb-16 text-center tracking-tight uppercase">
      Arsenal <span class="text-[#e61919]">Técnico</span>
    </h3>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
      
      <!-- Categorías de Habilidades -->
      <div v-for="(category, index) in skillCategories" :key="index" class="glass-card hover-red p-8">
        <h4 class="flex items-center gap-3 text-xl font-bold mb-6 border-b border-white/10 pb-4">
          <i :class="['ph', category.icon, 'text-3xl text-[#e61919]']"></i>
          {{ category.title }}
        </h4>
        <div class="flex flex-wrap gap-3">
          <span v-for="tag in category.tags" :key="tag" class="skill-tag">
            {{ tag }}
          </span>
        </div>
      </div>

      <!-- Marquee de Soft Skills y Producción -->
      <div class="glass-card hover-red md:col-span-3 p-10 overflow-hidden relative">
        <h4 class="flex items-center justify-center gap-3 text-xl font-bold mb-8">
          <i class="ph ph-star text-3xl text-[#e61919]"></i>
          Software de Producción y Soft Skills
        </h4>
        
        <div class="marquee-container flex overflow-hidden w-full relative">
          <!-- Fade edges -->
          <div class="absolute inset-y-0 left-0 w-20 bg-gradient-to-r from-[#0d0d0f] to-transparent z-10"></div>
          <div class="absolute inset-y-0 right-0 w-20 bg-gradient-to-l from-[#0d0d0f] to-transparent z-10"></div>
          
          <div class="marquee-content flex gap-6 shrink-0 grow-0 animate-scroll hover:pause-animation px-6">
            <span v-for="(skill, i) in marqueeSkills" :key="`a-${i}`" class="marquee-tag">{{ skill }}</span>
            <!-- Doble render para el efecto infinito -->
            <span v-for="(skill, i) in marqueeSkills" :key="`b-${i}`" class="marquee-tag">{{ skill }}</span>
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
