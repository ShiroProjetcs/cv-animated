<template>
  <footer class="pt-24 pb-12 relative overflow-hidden">
    <!-- CTA -->
    <section id="contacto" class="max-w-4xl mx-auto px-6 mb-24 relative z-10">
      <div class="glass-card text-center p-12 md:p-16 border-[#e61919]/30 shadow-[0_20px_60px_rgba(230,25,25,0.1)]">
        <h2 class="text-3xl md:text-4xl font-black font-['Outfit'] mb-6">
          ¿Hablamos de tu próximo proyecto?
        </h2>
        <p class="text-lg text-gray-400 mb-10 max-w-2xl mx-auto">
          Estoy disponible para aportar soluciones técnicas, creativas y enfocarme en los resultados de tu empresa.
        </p>

        <div class="flex flex-wrap justify-center gap-4">
          <a href="mailto:srshipropro@gmail.com" class="btn-primary">
            <i class="ph ph-envelope-simple text-xl"></i> Enviar Correo
          </a>
          <a href="tel:+34639401682" class="btn-secondary">
            <i class="ph ph-phone text-xl text-[#e61919]"></i> Llamar Ahora
          </a>
          <a href="/CV_LuisAlbertoJimenez.pdf" download class="btn-secondary">
            <i class="ph ph-download-simple text-xl text-[#e61919]"></i> Descargar CV (PDF)
          </a>
        </div>
      </div>
    </section>

    <!-- Footer base -->
    <div class="max-w-6xl mx-auto px-6 flex flex-col items-center border-t border-white/10 pt-12 relative z-10">
      <div class="flex flex-col items-center gap-4 mb-8">
        <img 
          src="https://api.qrserver.com/v1/create-qr-code/?size=120x120&data=https://cv-luis-alberto.vercel.app&color=ffffff&bgcolor=0d0d0f&margin=2" 
          alt="QR CV Web" 
          class="w-24 h-24 border border-white/20 rounded-lg shadow-xl"
        >
        <span class="text-sm text-gray-400 font-medium">Escanea para ver la versión interactiva</span>
      </div>
      
      <p class="text-center text-gray-500 font-medium leading-relaxed">
        © 2026 Luis Alberto Jiménez Mohedano. <br />
        <span class="text-xs opacity-50 block mt-1">Ingeniería, Creatividad y Resolución.</span>
      </p>
    </div>
  </footer>
</template>

