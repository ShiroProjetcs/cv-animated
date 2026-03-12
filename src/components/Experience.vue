<script setup>
import { computed } from 'vue'

const currentYear = new Date().getFullYear()

const getDuration = (startYear, startMonth = 0) => {
  const startDate = new Date(startYear, startMonth)
  const today = new Date()
  
  let years = today.getFullYear() - startDate.getFullYear()
  let months = today.getMonth() - startDate.getMonth()
  
  if (months < 0) {
    years--
    months += 12
  }
  
  let text = ''
  if (years > 0) text += `${years} ${years === 1 ? 'año' : 'años'}`
  if (months > 0) text += `${years > 0 ? ' y ' : ''}${months} ${months === 1 ? 'mes' : 'meses'}`
  
  return text || 'Reciente'
}

const experiences = [
  {
    date: '2023 – Actualidad',
    duration: getDuration(2023, 0),
    title: 'Asesoramiento Físico & Nutricional (Freelance)',
    company: 'Bienestar y Rendimiento',
    bullets: [
      'Ayudo a personas a alcanzar sus objetivos de salud mediante planes de entrenamiento personalizados.',
      'Elaboración y seguimiento de dietas adaptadas a las necesidades reales de cada persona.',
      'Uso de mis conocimientos técnicos para llevar un control detallado del progreso de cada asesorado.',
      'Compaginando mi pasión por el deporte con mi capacidad de organización y motivación.'
    ]
  },
  {
    date: '2020 – Actualidad',
    duration: getDuration(2020, 0),
    title: 'Desarrollador Web (Proyectos & Freelance)',
    company: 'Emprendimiento Personal',
    bullets: [
      'Proyecto Bushiro: Diseño y desarrollo de marca y tienda online para el sector deportivo.',
      'Integración de IA: Ayudo a optimizar el trabajo y los resultados usando herramientas de Inteligencia Artificial.',
      'Apoyo Digital: Colaboraciones en proyectos como zbombilla.com y otras marcas retail, trabajando por mi cuenta.'
    ]
  },
  {
    date: 'Sept. 2018 – Actualidad',
    duration: getDuration(2018, 8), // Septiembre es mes 8 (0-indexed)
    title: 'Técnico Informático Especialista',
    company: 'Ofimática 2000 S.L.U (Partner Olivetti)',
    bullets: [
      'Me encargo de que los equipos de nuestros clientes siempre estén a punto: reparación y mantenimiento de impresoras multifunción y sistemas de gran formato.',
      'Especialista en "solucionar marrones": arreglo desde destructoras de papel hasta equipos informáticos complejos (Olivetti, Konica Minolta).',
      'Soporte directo al cliente, tanto presencial como remoto, para asegurar que su negocio nunca se detenga.',
      'Diagnóstico y puesta en marcha de hardware y software para empresas.'
    ]
  },
  {
    date: 'Sept. 2017 – Sept. 2018',
    duration: '1 año',
    title: 'Técnico de Soporte IT',
    company: 'AlbertNovias',
    bullets: [
      'Atención directa y resolución de cualquier tipo de problema informático en el día a día.',
      'Mantenimiento de los ordenadores y equipos para que todo funcionase sin fallos.',
      'Soporte digital integral para que el equipo pudiese centrarse en sus ventas y clientes.'
    ]
  },
  {
    date: 'Jun. 2017 – Ago. 2017',
    duration: '3 meses',
    title: 'Informático (Prácticas)',
    company: 'Centre Estudis Nord',
    bullets: [
      'Creación de la web de la academia para mejorar su presencia digital.',
      'Puesta a punto y reparación de los equipos informáticos de las aulas.',
      'Edición de vídeos para redes sociales y gestión de sistemas de copias de seguridad.'
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
          <div class="flex flex-wrap items-center justify-between gap-2 mb-4">
            <span class="text-[#e61919] font-bold text-xs md:text-sm tracking-widest uppercase">
              {{ exp.date }}
            </span>
            <span v-if="exp.duration" class="bg-red-500/10 text-red-500 text-[10px] md:text-xs font-mono px-3 py-1 rounded-full border border-red-500/20">
              {{ exp.duration }}
            </span>
          </div>
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
