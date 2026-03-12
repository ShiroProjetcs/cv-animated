<script setup>
import { computed } from 'vue'

const currentYear = new Date().getFullYear()

const experiences = [
  {
    date: `2020 – Actualidad`,
    title: 'Desarrollador Web y Estratega Digital',
    company: 'Proyectos & E-commerce (Freelance)',
    bullets: [
      'Liderazgo técnico en Bushiro: Desarrollo integral de marca y plataforma e-commerce deportiva de alto rendimiento.',
      'Estratega E-commerce: Diseño y despliegue de soluciones escalables en Shopify y WooCommerce para diversas marcas del sector retail.',
      'Integrador de IA: Implementación de flujos de trabajo automatizados mediante LLMs (ChatGPT/Claude) para optimización de contenidos y procesos de negocio.',
      'Colaborador Estratégico en zbombilla.com: Ejecución técnica de modelos de negocio digitales y mantenimiento proactivo.'
    ]
  },
  {
    date: `2015 – Actualidad`,
    title: 'Técnico Especialista en Sistemas e Impresión',
    company: 'Ofimática 2000 S.L.U (Partner Olivetti)',
    bullets: [
      'Garantía de operatividad crítica: Soporte IT integral y mantenimiento avanzado de sistemas de impresión de alta producción.',
      'Especialista Multimarca: Experiencia certificada en entornos de producción Olivetti, Konica Minolta, Kyocera y Ricoh.',
      'Gestión de Infraestructura: Resolución de incidencias complejas tanto presenciales como remotas en entornos corporativos exigentes.',
      'Diagnóstico de Alto Nivel: Análisis preventivo y correctivo de hardware/software para asegurar flujos de trabajo eficientes.'
    ]
  },
  {
    date: 'Trayectoria Multimedia',
    title: 'Producción Técnica y Gestión Creativa',
    company: 'Creativo Independiente',
    bullets: [
      'Post-producción profesional: Gestión completa del flujo de edición de audio y video para contenido digital multiplataforma.',
      'Dirección Técnica de Eventos: Organización y control técnico en eventos de cultura urbana y freestyle.',
      'Consultoría Multimedia: Asesoramiento en branding y optimización de activos digitales para proyectos independientes.'
    ]
  },
  {
    date: '2017',
    title: 'Técnico en Sistemas (Prácticas)',
    company: 'Centre Estudis Nord - Alcoy',
    bullets: [
      'Despliegue de sitios web corporativos en WordPress y aseguramiento de políticas de backup robustas.',
      'Apoyo en la gestión diaria de infraestructura informática y creación de activos multimedia para redes sociales.'
    ],
    citation: '"Excepcional capacidad de resolución de incidencias técnicas complejas y actitud proactiva."'
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
