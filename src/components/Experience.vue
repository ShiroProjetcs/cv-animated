<script setup>
import { computed } from 'vue'

const currentYear = new Date().getFullYear()

const experiences = [
  {
    date: 'Sept. 2018 – Actualidad',
    title: 'Técnico Informático Specialist',
    company: 'Ofimática 2000 S.L.U (Partner Olivetti)',
    bullets: [
      'Soporte IT integral y mantenimiento avanzado de sistemas de impresión digital de alta producción.',
      'Gestión de infraestructura tecnológica para más de 40 años de experiencia del partner líder en el sector.',
      'Especialista en diagnóstico y resolución en entornos corporativos de alta demanda.',
      'Garantía de calidad y servicio técnico especializado en equipos multifunción (Olivetti, Konica Minolta).'
    ]
  },
  {
    date: 'Sept. 2017 – Sept. 2018',
    title: 'Técnico de Soporte IT',
    company: 'AlbertNovias',
    bullets: [
      'Responsable de soporte técnico informático y atención al cliente.',
      'Mantenimiento de sistemas locales y optimización operativa de flujos de trabajo.',
      'Gestión de infraestructura digital para asegurar la continuidad del negocio.'
    ]
  },
  {
    date: 'Jun. 2017 – Ago. 2017',
    title: 'Técnico en Sistemas (Prácticas)',
    company: 'Centre Estudis Nord',
    bullets: [
      'Desarrollo y lanzamiento de sitio web corporativo optimizado para la academia de idiomas.',
      'Reparación de hardware y gestión proactiva de sistemas de backups críticos.',
      'Producción multimedia y edición de video para estrategias de redes sociales.',
      'Mención especial por resolución de incidencias técnicas con carta de recomendación.'
    ]
  },
  {
    date: '2020 – Actualidad',
    title: 'Desarrollador Web (Proyectos)',
    company: 'Independiente / Freelance',
    bullets: [
      'Proyecto Bushiro: Liderazgo en branding y desarrollo integral de plataforma e-commerce deportiva.',
      'Integración de IA: Automatización de flujos de trabajo mediante LLMs para optimización de procesos digitales.',
      'Colaboración Estratégica: Soporte técnico y creativo para zbombilla.com y marcas retail.'
    ]
  }
]
</script>

<template>
  <section id="experiencia" class="py-16 md:py-24 max-w-4xl mx-auto px-6">
    <h3 class="text-3xl md:text-5xl font-['Outfit'] font-black mb-12 md:mb-16 text-center tracking-tight uppercase">
      Experiencia <span class="text-[#e61919]">Destacada</span>
    </h3>
    
    <div class="relative before:content-[''] before:absolute before:top-2 before:left-[15px] md:before:left-[23px] before:w-[2px] before:h-[calc(100%-10px)] before:bg-gradient-to-b before:from-[#e61919] before:to-transparent">
      
      <div v-for="(exp, index) in experiences" :key="index" class="relative pl-10 md:pl-16 mb-10 md:mb-12 last:mb-0 group">
        <!-- Dot -->
        <div class="absolute top-2 left-[10px] md:left-[18px] w-3 h-3 bg-[#0d0d0f] border-[3px] border-[#e61919] rounded-full shadow-[0_0_15px_#e61919] group-hover:scale-150 group-hover:bg-[#e61919] transition-all duration-300"></div>
        
        <!-- Content Card -->
        <div class="glass-card hover-red p-6 md:p-8">
          <span class="inline-block text-[#e61919] font-bold text-xs md:text-sm tracking-widest uppercase mb-4">
            {{ exp.date }}
          </span>
          <h4 class="text-xl md:text-2xl font-bold text-white mb-1">
            {{ exp.title }}
          </h4>
          <h5 class="text-base md:text-lg text-gray-400 font-medium mb-4 md:mb-6">
            {{ exp.company }}
          </h5>
          
          <ul class="space-y-3">
            <li v-for="(bullet, bIndex) in exp.bullets" :key="bIndex" class="text-sm md:text-base text-gray-400 relative pl-6 leading-relaxed">
              <span class="absolute left-0 text-[#e61919] font-bold">→</span>
              {{ bullet }}
            </li>
          </ul>

          <!-- Citation Block (Opt) -->
          <blockquote v-if="exp.citation" class="mt-8 p-4 bg-white/5 border-l-4 border-[#e61919] text-gray-300 text-sm md:text-base italic rounded-r-lg relative">
            <i class="ph-fill ph-quotes text-xl text-[#e61919] absolute -top-3 -left-3 bg-[#0d0d0f] rounded-full"></i>
            {{ exp.citation }}
          </blockquote>
        </div>
      </div>

    </div>
  </section>
</template>
