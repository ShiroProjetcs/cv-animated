<script setup>
const experiences = [
  {
    date: '2018 – Actualidad',
    title: 'Técnico Informático y Equipos Multifunción',
    company: 'Ofimática 2000 S.L.U (Partner Olivetti)',
    bullets: [
      'Responsable del despliegue técnico, configuración y soporte de equipos profesionales.',
      'Diagnóstico de hardware/software y mantenimiento preventivo con altos estándares.',
      'Soporte remoto y presencial, garantizando la continuidad de negocio en empresas.',
      'Gestión logística y transporte de equipamiento técnico crítico.'
    ]
  },
  {
    date: '2020 – Actualidad',
    title: 'Desarrollador Web y Estratega Digital',
    company: 'Freelance & Colaboraciones',
    bullets: [
      'Proyecto Bushiro: Creación integral de marca y desarrollo de la plataforma e-commerce deportiva.',
      'E-commerce Avanzado: Diseño, despliegue y gestión de tiendas online usando Shopify y WordPress (WooCommerce) para marcas de moda y servicios.',
      'Integración IA: Uso de LLMs (ChatGPT, Claude) y herramientas generativas para automatización de workflows y creación de contenido dinámico.',
      'Colaborador zbombilla.com: Apoyo en desarrollo digital y ejecución de proyectos de negocio online.'
    ]
  },
  {
    date: 'Independiente',
    title: 'Producción Técnica y Creatividad',
    company: 'Home Studio & Eventos',
    bullets: [
      'Gestión integral del flujo de trabajo en grabación y edición de audio/video.',
      'Organización técnica en eventos de cultura urbana y freestyle (Batallas de Gallos).',
      'Creación de contenido digital multiplataforma centrado en comunidad y branding personal.'
    ]
  },
  {
    date: '2017',
    title: 'Técnico Informático en Prácticas',
    company: 'Centre Estudis Nord - Alcoy',
    bullets: [
      'Creación de páginas web corporativas con WordPress y mantenimiento de sistemas.',
      'Configuración de estrategias de backups y edición de vídeo para RRSS.'
    ],
    citation: '"Luis demostró una excepcional capacidad de aprendizaje y una actitud proactiva en la resolución de incidencias técnicas complejas."'
  }
]
</script>

<template>
  <section id="experiencia" class="py-24 max-w-4xl mx-auto px-6">
    <h3 class="text-4xl md:text-5xl font-['Outfit'] font-black mb-16 text-center tracking-tight uppercase">
      Experiencia <span class="text-[#e61919]">Destacada</span>
    </h3>
    
    <div class="relative before:content-[''] before:absolute before:top-2 before:left-[15px] md:before:left-[23px] before:w-[2px] before:h-[calc(100%-10px)] before:bg-gradient-to-b before:from-[#e61919] before:to-transparent">
      
      <div v-for="(exp, index) in experiences" :key="index" class="relative pl-12 md:pl-16 mb-12 last:mb-0 group">
        <!-- Dot -->
        <div class="absolute top-2 left-[10px] md:left-[18px] w-3 h-3 bg-[#0d0d0f] border-[3px] border-[#e61919] rounded-full shadow-[0_0_15px_#e61919] group-hover:scale-150 group-hover:bg-[#e61919] transition-all duration-300"></div>
        
        <!-- Content Card -->
        <div class="glass-card hover-red p-8">
          <span class="inline-block text-[#e61919] font-bold text-sm tracking-widest uppercase mb-4">
            {{ exp.date }}
          </span>
          <h4 class="text-2xl font-bold text-white mb-1">
            {{ exp.title }}
          </h4>
          <h5 class="text-lg text-gray-400 font-medium mb-6">
            {{ exp.company }}
          </h5>
          
          <ul class="space-y-3">
            <li v-for="(bullet, bIndex) in exp.bullets" :key="bIndex" class="text-gray-400 relative pl-6 leading-relaxed">
              <span class="absolute left-0 text-[#e61919] font-bold">→</span>
              {{ bullet }}
            </li>
          </ul>

          <!-- Citation Block (Opt) -->
          <blockquote v-if="exp.citation" class="mt-8 p-4 bg-white/5 border-l-4 border-[#e61919] text-gray-300 italic rounded-r-lg relative">
            <i class="ph-fill ph-quotes text-xl text-[#e61919] absolute -top-3 -left-3 bg-[#0d0d0f] rounded-full"></i>
            {{ exp.citation }}
          </blockquote>
        </div>
      </div>

    </div>
  </section>
</template>
