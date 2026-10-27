"""Generate the downloadable CV: python -m pip install PyMuPDF==1.26.7

Run python scripts/generate_cv.py from any directory. Content is an editorial
summary of src/components; update it here when the professional history changes.
The website serves the committed PDF, so Python is not required by Vercel.
"""

from pathlib import Path
import fitz

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "public" / "CV_LuisAlbertoJimenez.pdf"
RED = (0.72, 0.08, 0.10)
INK = (0.12, 0.14, 0.18)
GRAY = (0.35, 0.38, 0.42)
doc = fitz.open()


LEFT = 36
WIDTH = 299


def text(page, value, y, size=10, bold=False, color=INK):
    """Measure wrapping first; reject overflow instead of clipping or shrinking."""
    font = "hebo" if bold else "helv"
    words = value.split()
    lines, line = [], ""
    for word in words:
        candidate = f"{line} {word}".strip()
        if fitz.get_text_length(candidate, fontname=font, fontsize=size) > WIDTH:
            lines.append(line)
            line = word
        else:
            line = candidate
    lines.append(line)
    for line in lines:
        if y + size > 777:
            raise ValueError(f"CV content exceeds page: {value}")
        page.insert_text((LEFT, y + size), line, fontsize=size, fontname=font, color=color)
        y += size * 1.35
    return y


def section(page, title, y):
    y = text(page, title.upper(), y + 9, 11, True, RED)
    page.draw_line((LEFT, y + 3), (LEFT + WIDTH, y + 3), color=(0.85, 0.86, 0.88), width=0.6)
    return y + 13


def entry(page, title, subtitle, bullets, y):
    y = text(page, title, y, 10.5, True)
    y = text(page, subtitle, y + 2, 9, color=GRAY) + 5
    for bullet in bullets:
        y = text(page, bullet, y, 10) + 3
    return y + 6


def new_page(number):
    page = doc.new_page(width=595.276, height=841.89)
    page.draw_rect(fitz.Rect(0, 0, page.rect.width, 8), color=None, fill=RED)
    page.draw_line((48, 794), (547, 794), color=(0.85, 0.86, 0.88), width=0.6)
    page.insert_text((48, 812), "Luis Alberto Jiménez Mohedano · cv-animated.vercel.app", fontsize=9, color=GRAY)
    return page


page = new_page(1)
with fitz.open(ROOT / "public" / "avatar.jpg") as image:
    portrait = image.convert_to_pdf()
with fitz.open("pdf", portrait) as image:
    r = image[0].rect
    image[0].set_cropbox(fitz.Rect(r.width * .22, r.height * .08, r.width * .78, r.height * .53))
    pix = image[0].get_pixmap()
    page.insert_image(fitz.Rect(451, 32, 559, 140), stream=pix.tobytes("jpeg"))
WIDTH = 395
y = text(page, "Luis Alberto", 32, 26, True)
y = text(page, "Jiménez Mohedano", y, 26, True)
y = text(page, "Técnico IT & Productor Digital", y + 4, 14, color=RED)
y = text(page, "Alcoy  |  +34 639 40 16 82  |  srshipropro@gmail.com", y + 9, 9)
y = text(page, "linkedin.com/in/luisalbertojm  |  github.com/ShiroProjetcs", y + 3, 9)
y = text(page, "Disponible para nuevas oportunidades laborales", y + 5, 10, True, RED)
WIDTH = 523
y = section(page, "Perfil profesional", y + 4)
y = text(page, "Especialista en soporte IT, mantenimiento de equipos y resolución tecnológica. Combino soluciones web, automatización e IA para poner en marcha proyectos digitales, con experiencia en diagnóstico de hardware y software y atención directa al cliente.", y)
column_top = y + 8
WIDTH = 299
page.draw_line((347, column_top + 12), (347, 777), color=(.88, .89, .90), width=.6)
y = section(page, "Experiencia profesional", column_top)
y = entry(page, "Técnico Informático Especialista", "Ofimática 2000 S.L.U · Partner Olivetti | Sept. 2018 - Ago. 2026", [
    "Mantenimiento de equipos multifunción y gran formato (Olivetti y Konica Minolta). Diagnóstico de hardware y software. Soporte presencial y remoto a empresas."
], y)
y = entry(page, "Productor Digital & Integrador", "Emprendimiento personal | 2020 - Actualidad", [
    "Creación de marcas y sitios web con IA. Integración de redes, automatización de procesos y consultoría para desplegar soluciones digitales."
], y)
y = entry(page, "Técnico de Soporte IT", "AlbertNovias | Sept. 2017 - Sept. 2018", [
    "Resolución de incidencias, mantenimiento de ordenadores y soporte digital al equipo comercial."
], y)
y = entry(page, "Informático · Prácticas", "Centre Estudis Nord | Jun. 2017 - Ago. 2017", [
    "Creación de la web de la academia, reparación de equipos, edición de vídeos y copias de seguridad."
], y)

y = entry(page, "Asesoramiento Físico & Nutricional", "Freelance | 2023 - Actualidad", [
    "Entrenamiento personalizado, seguimiento de dietas y control del progreso con herramientas digitales."
], y)
LEFT = 359
WIDTH = 200
y = section(page, "Formación", column_top)
for title, subtitle in [
    ("Desarrollo de Aplicaciones Web (GS)", "IES L'Estació · Ontinyent"),
    ("Sistemas Microinformáticos y Redes (GM)", "CIP FP Batoi · Alcoy | 2016 - 2018"),
    ("Educación Secundaria Obligatoria", "Colegio José Arnauda"),
    ("MPlus: IT Basics (Hardware & Software)", "Konica Minolta Academy | 2023"),
    ("Máster en Personal Trainer & Nutrición Deportiva", "Instituto Internacional de Ciencias Deportivas | 2023"),
]:
    y = entry(page, title, subtitle, [], y)
y = section(page, "Competencias", y - 5)
for title, content in [
    ("Sistemas y web", "Hardware, redes, soporte IT, tiendas online, despliegue y hosting."),
    ("IA y automatización", "LLMs, contenido digital y mejora de procesos."),
    ("Producción digital", "Premiere Pro, After Effects, Photoshop, Illustrator, DaVinci Resolve y producción de eventos."),
]:
    y = text(page, title, y, 10, True)
    y = text(page, content, y + 2, 9.5) + 8
y = section(page, "Idiomas", y - 5)
y = text(page, "Español y valenciano: nativos. Inglés: B2.", y, 10)

doc.set_metadata({"title": "CV - Luis Alberto Jiménez Mohedano", "author": "Luis Alberto Jiménez Mohedano", "subject": "Técnico IT & Productor Digital"})
assert len(doc) == 1
doc.save(OUTPUT, garbage=4, deflate=True)
print(f"Generated {OUTPUT}: {len(doc)} A4 pages, {OUTPUT.stat().st_size:,} bytes")
