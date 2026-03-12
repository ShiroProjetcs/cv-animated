<script setup>
import { computed } from 'vue'

const currentYear = new Date().getFullYear()

const experiences = [
  {
    date: 'Sept. 2018 – Actualidad',
    title: 'Técnico Informático Especialista',
    company: 'Ofimática 2000 S.L.U (Partner Olivetti)',
    bullets: [
      'Me encargo de que los equipos de nuestros clientes siempre estén a punto: reparación y mantenimiento de impresoras multifunción y sistemas de impresión de gran formato.',
      'Especialista en "solucionar marrones": arreglo desde destructoras de papel hasta equipos informáticos complejos de marcas como Olivetti o Konica Minolta.',
      'Soporte directo al cliente, tanto yendo a su oficina como de forma remota para que no pierdan ni un minuto de trabajo.',
      'Diagnóstico y puesta en marcha de todo tipo de hardware y software para empresas.'
    ]
  },
  {
    date: 'Sept. 2017 – Sept. 2018',
    title: 'Técnico de Soporte IT',
    company: 'AlbertNovias',
    bullets: [
      'Atención directa y resolución de cualquier problema informático que surgiera en el día a día.',
      'Mantenimiento de los ordenadores y equipos de la tienda para que todo funcionara sin fallos.',
      'Ayudar en cualquier necesidad digital para que el negocio pudiese centrarse en sus clientes.'
    ]
  },
  {
    date: 'Jun. 2017 – Ago. 2017',
    title: 'Informático (Prácticas)',
    company: 'Centre Estudis Nord',
    bullets: [
      'Creación de la página web de la academia para que fuesen más visibles en internet.',
      'Puesta a punto y reparación de los equipos de las aulas.',
      'Edición de vídeos para sus redes sociales y configuración de copias de seguridad para que sus datos estuviesen siempre a salvo.'
    ]
  },
  {
    date: '2020 – Actualidad',
    title: 'Desarrollador Web (Proyectos)',
    company: 'Independiente / Freelance',
    bullets: [
      'Proyecto Bushiro: Diseño y desarrollo de marca y tienda online para el sector deportivo.',
      'Integración de IA: Ayudo a optimizar el trabajo usando herramientas de Inteligencia Artificial.',
      'Apoyo Digital: Colaboraciones en proyectos como zbombilla.com y otras marcas retail.'
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
