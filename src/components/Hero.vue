<script setup>
// Hero Section
</script>

<template>
  <header class="min-h-screen flex items-center justify-center pt-24 lg:pt-32 relative z-10 px-6 overflow-hidden">
    <div class="max-w-6xl mx-auto flex flex-col-reverse lg:flex-row items-center gap-12 lg:gap-16 w-full">
      
      <!-- Text Content -->
      <div class="flex-1 text-center lg:text-left">
        <p class="inline-flex items-center gap-2 text-[#e61919] font-bold text-xs md:text-sm tracking-[0.2em] uppercase mb-4 bg-red-500/10 px-4 py-1.5 rounded-full border border-red-500/20">
          <i class="ph-fill ph-lightning"></i> Disponible para nuevos retos
        </p>
        
        <h1 class="text-4xl sm:text-5xl md:text-7xl lg:text-[5rem] font-['Outfit'] font-black leading-[1.1] tracking-tight mb-2">
          Luis Alberto <br class="hidden sm:block" />Jiménez
        </h1>
        
        <h2 class="text-xl sm:text-2xl md:text-4xl text-[#94949b] font-['Outfit'] font-normal mb-6">
          Técnico IT & 
          <span class="bg-gradient-to-br from-[#e61919] to-[#a30000] bg-clip-text text-transparent">Productor Digital</span>
        </h2>
        
        <p class="text-[#94949b] text-base md:text-lg max-w-xl mx-auto lg:mx-0 mb-10 leading-relaxed">
          Especialista en producción rápida y resolución tecnológica. Utilizo herramientas de vanguardia e <span class="text-white font-bold">IA</span> para desplegar soluciones digitales en tiempo récord. De la idea al directo, sin bloqueos.
        </p>

        <!-- Chips -->
        <div class="flex flex-wrap justify-center lg:justify-start gap-2 md:gap-3">
          <a href="mailto:srshipropro@gmail.com" class="chip text-xs md:text-sm">
            <i class="ph ph-envelope-simple text-lg md:text-xl text-[#e61919]"></i> <span class="hidden sm:inline">srshipropro@gmail.com</span><span class="sm:hidden">Email</span>
          </a>
          <a href="tel:+34639401682" class="chip text-xs md:text-sm">
            <i class="ph ph-phone text-lg md:text-xl text-[#e61919]"></i> <span class="hidden sm:inline">+34 639 40 16 82</span><span class="sm:hidden">Llamar</span>
          </a>
          <span class="chip text-xs md:text-sm">
            <i class="ph ph-map-pin text-lg md:text-xl text-[#e61919]"></i> Alcoy
          </span>
          <a href="https://www.linkedin.com/in/luisalbertojm/" target="_blank" class="chip text-xs md:text-sm">
            <i class="ph ph-linkedin-logo text-lg md:text-xl text-[#e61919]"></i>
          </a>
          <a href="https://github.com/ShiroProjetcs" target="_blank" class="chip text-xs md:text-sm">
            <i class="ph ph-github-logo text-lg md:text-xl text-[#e61919]"></i>
          </a>
          <a href="#contacto" class="chip-primary text-xs md:text-sm">
            <i class="ph ph-paper-plane-tilt text-lg md:text-xl text-white"></i> Contactar
          </a>
        </div>
      </div>

      <!-- Image & Badges -->
      <div class="relative w-full max-w-[280px] sm:max-w-[340px] aspect-[3/4] perspective-1000 group mx-auto lg:mx-0">
        <div class="absolute inset-0 rounded-[24px] p-[2px] bg-gradient-to-br from-red-500/60 to-transparent shadow-2xl overflow-hidden transform lg:-rotate-y-3 lg:rotate-x-1 transition-transform duration-700 ease-out group-hover:rotate-y-0 group-hover:rotate-x-0">
          <img 
            src="/avatar.jpg" 
            alt="Luis Alberto" 
            class="w-full h-full object-cover rounded-[22px] grayscale contrast-125 brightness-75 transition-all duration-700 group-hover:grayscale-0 group-hover:brightness-100"
            onerror="this.src='https://ui-avatars.com/api/?name=Luis+Alberto&background=b30000&color=fff&size=400'"
          >
          <div class="absolute -top-full left-0 w-full h-24 bg-gradient-to-b from-transparent via-red-500/30 to-transparent animate-scan-line"></div>
        </div>
        
        <!-- Badges - Adjust positions for responsive -->
        <div class="absolute top-[8%] -left-[10%] sm:-left-[15%] floating-badge animation-delay-0 text-[10px] sm:text-xs">
          <i class="ph ph-hard-drives text-[#e61919] text-sm sm:text-xl"></i> IT Support
        </div>
        <div class="absolute bottom-[25%] -right-[15%] sm:-right-[20%] floating-badge animation-delay-2000 text-[10px] sm:text-xs">
          <i class="ph ph-globe text-[#e61919] text-sm sm:text-xl"></i> Web Solutions
        </div>
        <div class="absolute bottom-[2%] -left-[5%] floating-badge animation-delay-4000 text-[10px] sm:text-xs">
          <i class="ph ph-cpu text-[#e61919] text-sm sm:text-xl"></i> IT Support
        </div>
      </div>

    </div>
  </header>
</template>

<style scoped>
.perspective-1000 {
  perspective: 1000px;
}

.floating-badge {
  @apply bg-black/85 backdrop-blur-xl border border-red-500/30 px-3 py-2 sm:px-4 sm:py-3 rounded-xl font-bold flex items-center gap-2 shadow-[0_10px_30px_rgba(0,0,0,0.6)] uppercase tracking-wide text-white whitespace-nowrap z-20;
  animation: float 6s ease-in-out infinite;
}

.animation-delay-2000 {
  animation-delay: 2s;
}
.animation-delay-4000 {
  animation-delay: 4s;
}

@keyframes float {
  0%, 100% { transform: translateY(0px) }
  50% { transform: translateY(-12px) }
}

@keyframes scanLine {
  0% { top: -100px; }
  100% { top: 100%; }
}
.animate-scan-line {
  animation: scanLine 4s linear infinite;
  pointer-events: none;
}
</style>
