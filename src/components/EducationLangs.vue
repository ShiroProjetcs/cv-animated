<script setup>
</script>

<template>
  <section id="idiomas" class="py-24 max-w-6xl mx-auto px-6">
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-16">
      
      <!-- Columna Formación -->
      <div>
        <h3 class="text-4xl md:text-5xl font-['Outfit'] font-black mb-12 tracking-tight uppercase">
          Formación <span class="text-[#e61919]">Académica</span>
        </h3>
        
        <div class="flex flex-col gap-6">
          <div class="glass-card hover-red p-8 flex items-center gap-6 text-left">
            <i class="ph ph-graduation-cap text-5xl text-[#e61919] shrink-0"></i>
            <div>
              <h4 class="text-lg font-bold text-white mb-1">Desarrollo de Aplicaciones Web (GS)</h4>
              <p class="text-gray-400 text-sm">IES L'Estació, Ontinyent</p>
            </div>
          </div>
          
          <div class="glass-card hover-red p-8 flex items-center gap-6 text-left">
            <i class="ph ph-student text-5xl text-[#e61919] shrink-0"></i>
            <div>
              <h4 class="text-lg font-bold text-white mb-1">Sistemas Microinformáticos y Redes (GM)</h4>
              <p class="text-gray-400 text-sm">CIP FP Batoi, Alcoy</p>
            </div>
          </div>

          <div class="glass-card hover-red p-8 flex items-center gap-6 text-left">
            <i class="ph ph-books text-5xl text-[#e61919] shrink-0"></i>
            <div>
              <h4 class="text-lg font-bold text-white mb-1">Educación Secundaria Obligatoria</h4>
              <p class="text-gray-400 text-sm">Colegio José Arnauda</p>
            </div>
          </div>

          <div class="glass-card hover-red p-8 flex items-center gap-6 text-left">
            <i class="ph ph-barbell text-5xl text-[#e61919] shrink-0"></i>
            <div>
              <h4 class="text-lg font-bold text-white mb-1">Máster Nutrición Deportiva y Entrenador Personal</h4>
              <p class="text-gray-400 text-sm">Formación Especializada Complementaria</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Columna Idiomas -->
      <div>
        <h3 class="text-4xl md:text-5xl font-['Outfit'] font-black mb-12 tracking-tight uppercase">
          I<span class="text-[#e61919]">diomas</span>
        </h3>
        
        <div class="glass-card p-10 flex flex-col gap-8">
          
          <div class="w-full">
            <div class="flex justify-between mb-3">
              <span class="font-bold text-lg">Español</span>
              <span class="text-[#e61919] font-bold">Nativo</span>
            </div>
            <div class="w-full h-3 bg-red-900/20 rounded-full overflow-hidden">
              <div class="h-full bg-gradient-to-r from-[#e61919] to-[#a30000] w-full rounded-full"></div>
            </div>
          </div>

          <div class="w-full">
            <div class="flex justify-between mb-3">
              <span class="font-bold text-lg">Valenciano</span>
              <span class="text-[#e61919] font-bold">Nativo</span>
            </div>
            <div class="w-full h-3 bg-red-900/20 rounded-full overflow-hidden">
              <div class="h-full bg-gradient-to-r from-[#e61919] to-[#a30000] w-full rounded-full"></div>
            </div>
          </div>

          <div class="w-full">
            <div class="flex justify-between mb-3">
              <span class="font-bold text-lg">Inglés</span>
              <span class="text-[#e61919] font-bold">B2</span>
            </div>
            <div class="w-full h-3 bg-red-900/20 rounded-full overflow-hidden">
              <div class="h-full bg-gradient-to-r from-[#e61919] to-[#a30000] w-[75%] rounded-full relative overflow-hidden">
                <div class="absolute top-0 left-0 w-full h-full bg-white/10 w-[75%]"></div>
              </div>
            </div>
          </div>

        </div>
      </div>

    </div>
  </section>
</template>
