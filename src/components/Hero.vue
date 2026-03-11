<script setup>
// Hero Section
</script>

<template>
  <header class="min-h-screen flex items-center justify-center pt-24 relative z-10 px-6">
    <div class="max-w-6xl mx-auto flex flex-col-reverse lg:flex-row items-center gap-16 w-full">
      
      <!-- Text Content -->
      <div class="flex-1 text-center lg:text-left">
        <p class="inline-flex items-center gap-2 text-[#e61919] font-bold text-sm tracking-[0.2em] uppercase mb-4 bg-red-500/10 px-4 py-1.5 rounded-full border border-red-500/20">
          <i class="ph-fill ph-lightning"></i> Disponible para nuevos retos
        </p>
        
        <h1 class="text-6xl md:text-7xl lg:text-[5rem] font-['Outfit'] font-black leading-[1.1] tracking-tight mb-2">
          Luis Alberto <br />Jiménez
        </h1>
        
        <h2 class="text-3xl md:text-4xl text-[#94949b] font-['Outfit'] font-normal mb-6">
          Técnico IT & 
          <span class="bg-gradient-to-br from-[#e61919] to-[#a30000] bg-clip-text text-transparent">Productor Digital</span>
        </h2>
        
        <p class="text-[#94949b] text-lg max-w-xl mx-auto lg:mx-0 mb-10 leading-relaxed">
          Resolución técnica avanzada y producción creativa. Orientado a ofrecer soluciones ágiles y robustas en entornos dinámicos y de alta presión. De los sistemas a la pantalla.
        </p>

        <!-- Chips -->
        <div class="flex flex-wrapjustify-center lg:justify-start gap-4">
          <a href="mailto:srshipropro@gmail.com" class="chip">
            <i class="ph ph-envelope-simple text-xl text-[#e61919]"></i> srshipropro@gmail.com
          </a>
          <a href="tel:+34639401682" class="chip">
            <i class="ph ph-phone text-xl text-[#e61919]"></i> +34 639 40 16 82
          </a>
          <span class="chip">
            <i class="ph ph-map-pin text-xl text-[#e61919]"></i> Alcoy, España
          </span>
          <a href="https://www.linkedin.com/in/luisalbertojm/" target="_blank" class="chip hover-red">
            <i class="ph ph-linkedin-logo text-xl text-[#e61919]"></i> LinkedIn
          </a>
          <a href="https://github.com/ShiroProjects" target="_blank" class="chip hover-red">
            <i class="ph ph-github-logo text-xl text-[#e61919]"></i> GitHub
          </a>
          <a href="#contacto" class="chip-primary shadow-red-glow">
            <i class="ph ph-paper-plane-tilt text-xl text-white"></i> Contactar
          </a>
        </div>
      </div>

      <!-- Image & Badges -->
      <div class="relative w-[340px] h-[440px] perspective-1000 group mx-auto">
        <div class="absolute inset-0 rounded-[24px] p-[2px] bg-gradient-to-br from-red-500/60 to-transparent shadow-2xl overflow-hidden transform -rotate-y-3 rotate-x-1 transition-transform duration-700 ease-out group-hover:rotate-y-0 group-hover:rotate-x-0">
          <img 
            src="/avatar.jpg" 
            alt="Luis Alberto" 
            class="w-full h-full object-cover rounded-[22px] grayscale contrast-125 brightness-75 transition-all duration-700 group-hover:grayscale-0 group-hover:brightness-100"
            onerror="this.src='https://ui-avatars.com/api/?name=Luis+Alberto&background=b30000&color=fff&size=400'"
          >
          <div class="absolute -top-full left-0 w-full h-24 bg-gradient-to-b from-transparent via-red-500/30 to-transparent animate-scan-line"></div>
        </div>
        
        <!-- Badges -->
        <div class="absolute top-[8%] -left-[15%] floating-badge animation-delay-0">
          <i class="ph ph-hard-drives text-[#e61919] text-xl"></i> IT Support
        </div>
        <div class="absolute bottom-[25%] -right-[20%] floating-badge animation-delay-2000">
          <i class="ph ph-code text-[#e61919] text-xl"></i> Fullstack Web
        </div>
        <div class="absolute bottom-[2%] -left-[5%] floating-badge animation-delay-4000">
          <i class="ph ph-sparkle text-[#e61919] text-xl"></i> IA Integrator
        </div>
      </div>

    </div>
  </header>
</template>

<style scoped>
.perspective-1000 {
  perspective: 1000px;
}
.rotate-y-3 {
  transform: rotateY(-3deg) rotateX(1deg);
}

.chip {
  @apply inline-flex items-center gap-2 px-5 py-2.5 bg-white/5 border border-white/10 rounded-full text-sm font-medium transition-all duration-300;
}
.chip:hover {
  @apply bg-red-500/10 border-[#e61919] -translate-y-1 shadow-[0_10px_20px_rgba(230,25,25,0.15)];
}

.chip-primary {
  @apply inline-flex items-center gap-2 px-6 py-2.5 bg-gradient-to-br from-[#e61919] to-[#a30000] rounded-full text-sm font-bold text-white transition-all duration-300;
}
.chip-primary:hover {
  @apply shadow-[0_10px_25px_rgba(230,25,25,0.4)] -translate-y-1;
}

.floating-badge {
  @apply bg-black/85 backdrop-blur-xl border border-red-500/30 px-4 py-3 rounded-xl font-bold text-xs flex items-center gap-2 shadow-[0_10px_30px_rgba(0,0,0,0.6)] uppercase tracking-wide text-white;
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
