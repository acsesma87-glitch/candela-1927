# Genera los SVG de las escenas de Altamar (800x500). Devuelve dict nombre -> svg
import re

def defs(extra=''):
    return f'''<defs>
<linearGradient id="skyD" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3a4550"/><stop offset=".55" stop-color="#8d8f8a"/><stop offset="1" stop-color="#c9b48e"/></linearGradient>
<radialGradient id="warm"><stop offset="0" stop-color="#ffcf80" stop-opacity=".85"/><stop offset=".4" stop-color="#ffb757" stop-opacity=".28"/><stop offset="1" stop-color="#ff9a30" stop-opacity="0"/></radialGradient>
<radialGradient id="vig" cx=".5" cy=".5" r=".75"><stop offset=".55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".8"/></radialGradient>
<linearGradient id="coatA" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#3a3f48"/><stop offset=".5" stop-color="#2a2e35"/><stop offset="1" stop-color="#15171b"/></linearGradient>
<linearGradient id="coatC" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#9a8a6a"/><stop offset=".5" stop-color="#7a6c52"/><stop offset="1" stop-color="#3e362a"/></linearGradient>
<linearGradient id="skin" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#e3bea2"/><stop offset=".6" stop-color="#cfa588"/><stop offset="1" stop-color="#9c7660"/></linearGradient>
<linearGradient id="hairA" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#4a3a2e"/><stop offset=".5" stop-color="#33281f"/><stop offset="1" stop-color="#1e1712"/></linearGradient>
<linearGradient id="hairC" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#5a3e2c"/><stop offset=".5" stop-color="#3a281e"/><stop offset="1" stop-color="#22170f"/></linearGradient>
<filter id="fog" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".008 .03" numOctaves="4" seed="5"/><feColorMatrix values="0 0 0 0 .82 0 0 0 0 .83 0 0 0 0 .84 0 0 0 1.1 -.42"/></filter>
<filter id="b5"><feGaussianBlur stdDeviation="5"/></filter>
<filter id="paperT"><feTurbulence type="fractalNoise" baseFrequency=".8" numOctaves="2" seed="3"/><feColorMatrix values="0 0 0 0 .4 0 0 0 0 .33 0 0 0 0 .22 0 0 0 .22 0"/><feComposite in2="SourceGraphic" operator="in"/></filter>
<pattern id="cob" width="36" height="16" patternUnits="userSpaceOnUse"><rect width="36" height="16" fill="#3a3530"/><path d="M0 15.5H36M18 0V8M0 7.5H36M9 8V16M27 8V16" stroke="#22201c" stroke-width="1.5"/></pattern>
{extra}</defs>'''

def wrap(body, extra=''):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" preserveAspectRatio="none">{defs(extra)}{body}</svg>'

# ---------------- Aitor de sereno (figura de aitor.svg, coords 400x500) ----------------
src = open(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'aitor.svg')).read()
i = src.index('<!-- sereno -->'); j = src.index('<rect width="400" height="500" fill="url(#rain)"/>')
AITOR = src[i:j].replace('url(#coat)', 'url(#coatA)').replace('url(#hair)', 'url(#hairA)')
AITOR = AITOR.replace('<rect x="196" y="127" width="18" height="8" rx="1" fill="#c9a24a"/>',
  '<rect x="196" y="127" width="18" height="8" rx="1" fill="#c9a24a"/><text x="205" y="133.6" text-anchor="middle" font-size="4.2" fill="#3a2a10" font-family="Georgia">SERENO 7</text>')

def aitor(x, y, s=1):  # x,y = pies (centro)
    return f'<g transform="translate({x-205*s} {y-462*s}) scale({s})">{AITOR}</g>'

# ---------------- Candela de pie con maleta ----------------
CANDELA = '''<g>
 <ellipse cx="0" cy="0" rx="42" ry="7" fill="#000" opacity=".45"/>
 <rect x="-15" y="-80" width="11" height="78" fill="#2a2420"/><rect x="3" y="-80" width="11" height="78" fill="#241f1b"/>
 <path d="M-20 -2h16v5h-18zM3 -2h16l2 5h-18z" fill="#140f0c"/>
 <path d="M-24 -190q24-12 48 0l14 128h-76z" fill="url(#coatC)"/>
 <path d="M0 -188v126" stroke="#4e4434" stroke-width="1.5"/>
 <path d="M-26 -120h52" stroke="#5a4c38" stroke-width="5"/>
 <path d="M-12 -188l12 22 12-22" fill="none" stroke="#5a4c38" stroke-width="3"/>
 <!-- brazo con maleta -->
 <path d="M24 -184q12 30 12 78" stroke="#7a6c52" stroke-width="13" fill="none" stroke-linecap="round"/>
 <circle cx="36" cy="-102" r="6" fill="url(#skin)"/>
 <rect x="22" y="-96" width="44" height="34" rx="4" fill="#5a3a22" stroke="#2c1a10" stroke-width="2"/>
 <path d="M32 -96v-5h22v5" fill="none" stroke="#2c1a10" stroke-width="3"/><path d="M22 -80h44" stroke="#c9a24a" stroke-width="2"/>
 <path d="M-24 -184q-10 30-8 70" stroke="#8a7a5e" stroke-width="13" fill="none" stroke-linecap="round"/>
 <circle cx="-32" cy="-112" r="6" fill="url(#skin)"/>
 <!-- cuello y cabeza -->
 <rect x="-5" y="-206" width="10" height="18" fill="#c9a084"/>
 <path d="M-21 -226q-4 40 -6 70q10 6 14 -2l2-60z M21 -226q4 40 6 70q-10 6 -14 -2l-2-60z" fill="url(#hairC)"/>
 <ellipse cx="0" cy="-222" rx="15" ry="19" fill="url(#skin)"/>
 <path d="M-16 -224q2-20 16-20q14 0 16 20q-6-10-16-12q-10 2-16 12z" fill="#3a281e"/>
 <path d="M0 -242v10" stroke="#22170f" stroke-width="1"/>
 <circle cx="-6" cy="-222" r="1.8" fill="#3a2414"/><circle cx="6" cy="-222" r="1.8" fill="#3a2414"/>
 <path d="M-4 -212q4 3 8 0" stroke="#9a5a4a" stroke-width="1.4" fill="none"/>
 <!-- sombrero -->
 <ellipse cx="0" cy="-238" rx="26" ry="6" fill="#2a2420"/>
 <path d="M-15 -239q0-18 15-18t15 18z" fill="#3a322b"/>
 <path d="M-15 -243h30v4h-30z" fill="#8a2a20"/>
</g>'''
def candela(x, y, s=1):
    return f'<g transform="translate({x} {y}) scale({s})">{CANDELA}</g>'

SVG = {}

# ======================= PERIÓDICO =======================
def periodico():
    b = '<rect width="800" height="500" fill="#0b0908"/>'
    b += '<g transform="rotate(-1.2 400 250)">'
    b += '<rect x="96" y="14" width="608" height="476" fill="#e6dcc2"/><rect x="96" y="14" width="608" height="476" fill="#000" filter="url(#paperT)"/>'
    b += '<rect x="96" y="14" width="608" height="476" fill="none" stroke="#c9bb98" stroke-width="2"/>'
    ink = '#1f1a14'
    b += f'<text x="400" y="66" text-anchor="middle" font-family="Limelight,Georgia,serif" font-size="46" fill="{ink}" letter-spacing="3">EL FARO DE ALTAMAR</text>'
    b += f'<path d="M116 78H684M116 100H684" stroke="{ink}" stroke-width="1.5"/>'
    b += f'<text x="120" y="94" font-size="11" fill="{ink}" font-family="Georgia">Diario de la mañana</text>'
    b += f'<text x="400" y="94" text-anchor="middle" font-size="11" fill="{ink}" font-family="Georgia">Jueves, 1 de diciembre de 1927</text>'
    b += f'<text x="680" y="94" text-anchor="end" font-size="11" fill="{ink}" font-family="Georgia">10 céntimos</text>'
    # titular
    b += f'<text x="400" y="138" text-anchor="middle" font-size="25" textLength="560" lengthAdjust="spacingAndGlyphs" fill="{ink}" font-family="Georgia" font-weight="bold">LA HUELGA DEL PUERTO CUMPLE TRES SEMANAS</text>'
    b += f'<path d="M116 152H684" stroke="{ink}"/>'
    # columna izq: grabado estibadores
    b += '<g transform="translate(118 162)"><rect width="250" height="130" fill="#d3c7a8"/>'
    b += f'<path d="M150 20h70l10 70h-90z" fill="#5a5040"/><path d="M185 20v-14M160 30h50" stroke="{ink}" stroke-width="2"/>'
    for k in range(5):
        x = 20 + k*26
        b += f'<circle cx="{x}" cy="62" r="7" fill="{ink}"/><path d="M{x-10} 70h20l3 50h-26z" fill="{ink}"/><path d="M{x-9} 82h18" stroke="#d3c7a8" stroke-width="3"/>'
    b += f'<path d="M0 120H250" stroke="{ink}"/></g>'
    lines = ['Los estibadores de Altamar siguen con','los brazos cruzados. Mateo «el Rubio»,','capataz del muelle, no da su brazo a','torcer: «Sin seguridad en la conservera,','no hay descarga». Los barcos esperan.']
    for k,t in enumerate(lines):
        b += f'<text x="120" y="{310+k*14}" font-size="10.5" fill="{ink}" font-family="Georgia">{t}</text>'
    # columna centro: conservera
    b += f'<path d="M382 162V480" stroke="{ink}" stroke-width=".8"/>'
    b += f'<text x="396" y="178" font-size="15.5" fill="{ink}" font-family="Georgia" font-weight="bold">Conservas Arrieta suspende pagos</text>'
    b += '<g transform="translate(396 188)"><rect width="286" height="96" fill="#d3c7a8"/>'
    b += f'<path d="M20 90V40l40-20v20l40-20v20l40-20v70z" fill="{ink}"/><rect x="150" y="10" width="14" height="80" fill="{ink}"/><path d="M157 10q10-14 30-10q-14 4-20 14" fill="#8a8070"/>'
    b += f'<rect x="180" y="50" width="90" height="40" fill="{ink}"/><text x="225" y="74" text-anchor="middle" font-size="9" fill="#d3c7a8" font-family="Georgia">CONSERVAS ARRIETA</text></g>'
    lines = ['Don Julián Arrieta no hace declaraciones.','La conservera, la mayor de Altamar, no','paga a sus proveedores desde octubre.','Su hijo Íñigo fue visto anoche en el','Casino «de excelente humor».']
    for k,t in enumerate(lines):
        b += f'<text x="396" y="{304+k*14}" font-size="10.5" fill="{ink}" font-family="Georgia">{t}</text>'
    # anuncios (letra pequeña: se leen con lupa)
    b += f'<rect x="118" y="386" width="250" height="90" fill="none" stroke="{ink}"/>'
    b += f'<text x="243" y="402" text-anchor="middle" font-size="8" fill="{ink}" font-family="Georgia" font-weight="bold">JARABE DEL DR. SALAZAR</text>'
    b += f'<text x="243" y="414" text-anchor="middle" font-size="5.2" fill="{ink}" font-family="Georgia">Para la tos, los nervios y el insomnio.</text>'
    b += f'<text x="243" y="422" text-anchor="middle" font-size="5.2" fill="{ink}" font-family="Georgia">Dispensario del puerto. Se atiende de noche.</text>'
    b += f'<path d="M136 430H350" stroke="{ink}" stroke-width=".6"/>'
    b += f'<text x="243" y="446" text-anchor="middle" font-size="7.5" fill="{ink}" font-family="Georgia" font-weight="bold">SE BUSCA MOZO</text>'
    b += f'<text x="243" y="457" text-anchor="middle" font-size="5.2" fill="{ink}" font-family="Georgia">para la conservera. Abstenerse huelguistas.</text>'
    b += f'<text x="243" y="467" text-anchor="middle" font-size="5.2" fill="{ink}" font-family="Georgia">Razón: portería de Conservas Arrieta.</text>'
    # breve del sereno
    b += f'<rect x="396" y="386" width="286" height="90" fill="#ddd2b4" stroke="{ink}"/>'
    b += f'<text x="539" y="402" text-anchor="middle" font-size="8" fill="{ink}" font-family="Georgia" font-weight="bold">ECOS DEL BARRIO</text>'
    br = ['El sereno de Altamar espera hoy la visita de','una señorita argentina, llegada en el Topo.','Los vecinos, muy pendientes. Doña Puri ya ha','preguntado dos veces si la señorita es formal.']
    for k,t in enumerate(br):
        b += f'<text x="539" y="{418+k*10}" text-anchor="middle" font-size="5.6" fill="{ink}" font-family="Georgia" font-style="italic">{t}</text>'
    b += f'<text x="539" y="468" text-anchor="middle" font-size="5" fill="{ink}" font-family="Georgia">Mar en calma. Niebla al alba. Pleamar a la 1:30.</text>'
    b += '</g>'
    return wrap(b)
SVG['periodico'] = periodico()

# ======================= ESTACIÓN DEL TOPO =======================
def topo():
    b = '<rect width="800" height="500" fill="url(#skyD)"/>'
    # mar entre edificios
    b += '<rect x="330" y="150" width="140" height="120" fill="#5d6870"/><path d="M330 200h140M330 225h140" stroke="#7a868d" stroke-width="1" opacity=".6"/>'
    # fachadas con miradores
    def facade(x, w, h, col):
        s = f'<rect x="{x}" y="{330-h}" width="{w}" height="{h+40}" fill="{col}"/>'
        for r in range(int(h/60)):
            for c in range(int(w/44)):
                wx = x+12+c*44; wy = 330-h+20+r*60
                s += f'<rect x="{wx}" y="{wy}" width="22" height="34" fill="#2b2f33"/>'
                if (r+c) % 3 == 0: s += f'<rect x="{wx+2}" y="{wy+2}" width="18" height="30" fill="#e8c27a" opacity=".55"/>'
            s += f'<rect x="{x+w/2-30}" y="{330-h+16+r*60}" width="60" height="44" fill="#e8e2d6" opacity=".35"/>'
        return s
    b += facade(0, 330, 260, '#4a4642') + facade(470, 330, 280, '#433f3b')
    b += '<rect x="0" y="330" width="800" height="170" fill="url(#cob)"/>'
    b += '<path d="M0 420L800 420M0 452L800 452" stroke="#6f6a62" stroke-width="4"/>'
    # andén
    b += '<rect x="420" y="360" width="380" height="20" fill="#5c564e"/><rect x="420" y="380" width="380" height="8" fill="#2a2622"/>'
    # cable del trole
    b += '<path d="M0 118L800 104" stroke="#1a1a1a" stroke-width="2"/>'
    # el Topo (tranvía)
    b += '<g><rect x="20" y="230" width="300" height="160" rx="10" fill="#7a2a22"/><rect x="20" y="230" width="300" height="24" rx="8" fill="#5a1d18"/>'
    for k in range(5):
        b += f'<rect x="{40+k*56}" y="264" width="40" height="52" rx="4" fill="#2a2724"/><rect x="{42+k*56}" y="266" width="36" height="48" rx="3" fill="#e8c27a" opacity=".45"/>'
    b += '<rect x="20" y="330" width="300" height="10" fill="#c9a24a"/><text x="170" y="364" text-anchor="middle" font-family="Georgia" font-size="14" fill="#e8d6a8" letter-spacing="3">TOPO</text>'
    b += '<path d="M200 230L260 116" stroke="#111" stroke-width="4"/><circle cx="60" cy="398" r="14" fill="#111"/><circle cx="280" cy="398" r="14" fill="#111"/></g>'
    # vapor
    b += '<g filter="url(#b5)" opacity=".7"><ellipse cx="120" cy="400" rx="90" ry="26" fill="#d8d6d0"/><ellipse cx="240" cy="390" rx="70" ry="22" fill="#d8d6d0"/></g>'
    # letrero esmaltado sobre el andén
    b += '<rect x="540" y="150" width="3" height="40" fill="#222"/><rect x="606" y="150" width="3" height="40" fill="#222"/>'
    b += '<rect x="510" y="120" width="130" height="34" rx="4" fill="#1d3a5a" stroke="#e8e2d6" stroke-width="2"/>'
    b += '<text x="575" y="135" text-anchor="middle" font-family="Georgia" font-size="11" fill="#f0ead8" letter-spacing="2">TOPO</text>'
    b += '<text x="575" y="148" text-anchor="middle" font-family="Georgia" font-size="6.5" fill="#f0ead8">Frontera – San Sebastián</text>'
    # farola encendida
    b += '<rect x="726" y="150" width="6" height="214" fill="#1a1715"/><path d="M714 150h30l-5 26h-20z" fill="#2a2420"/><rect x="719" y="155" width="20" height="18" fill="#ffd28a"/>'
    b += '<circle cx="729" cy="165" r="90" fill="url(#warm)"/>'
    # niebla
    b += '<rect width="800" height="500" filter="url(#fog)" opacity=".55"/>'
    # personajes
    b += candela(470, 372, .95)
    b += aitor(690, 374, .74)
    b += '<rect width="800" height="500" fill="url(#vig)"/>'
    return wrap(b)
SVG['topo'] = topo()


# ---------------- variantes para casa ----------------
import re as _re
def _cut(t, a, b):
    i = t.index(a); j = t.index(b, i); return t[:i] + t[j:]
AITOR_CASA = AITOR
AITOR_CASA = _cut(AITOR_CASA, '<!-- chuzo -->', '<!-- piernas -->')
AITOR_CASA = _cut(AITOR_CASA, '<!-- farol -->', '<!-- cuello y cabeza -->')
AITOR_CASA = AITOR_CASA.replace('<!-- cuello y cabeza -->', '<circle cx="148" cy="305" r="8" fill="url(#skin)"/>\n <!-- cuello y cabeza -->', 1)  # mano derecha (sin farol)
AITOR_CASA = _cut(AITOR_CASA, '<!-- gorra de sereno -->', '<!-- mechones')
AITOR_CASA = AITOR_CASA.replace('<!-- mechones', '<path d="M175 150q0-30 30-33q30 3 31 33q-9-14-31-15q-21 1-30 15z" fill="url(#hairA)"/><path d="M190 126q8-3 14 0M212 124q8 0 12 5" stroke="#8a8680" stroke-width="1" fill="none"/>\n <!-- mechones')
def aitor_casa(x, y, s=1):
    return f'<g transform="translate({x-205*s} {y-462*s}) scale({s})">{AITOR_CASA}</g>'
CANDELA_CASA = _cut(CANDELA, '<!-- brazo con maleta -->', '<path d="M-24 -184q-10 30-8 70"')
CANDELA_CASA = CANDELA_CASA.replace('<path d="M-24 -184q-10 30-8 70"', '<path d="M24 -184q10 30 8 70" stroke="#7a6c52" stroke-width="13" fill="none" stroke-linecap="round"/><circle cx="32" cy="-112" r="6" fill="url(#skin)"/><path d="M-24 -184q-10 30-8 70"')
CANDELA_CASA = CANDELA_CASA[:CANDELA_CASA.index('<!-- sombrero -->')] + '<path d="M-16 -226q0-20 16-21q16 1 16 21q-6-9-16-10q-10 1-16 10z" fill="#3a281e"/><path d="M0 -247v12" stroke="#22170f" stroke-width="1.2"/></g>'
def candela_casa(x, y, s=1):
    return f'<g transform="translate({x} {y}) scale({s})">{CANDELA_CASA}</g>'

TXOMIN = """<g>
 <path d="M-34 60q0-46 34-50q34 4 34 50z" fill="#4a3a2a"/>
 <path d="M-20 14q20 10 40 0l4 12q-24 10-48 0z" fill="#8a2a20"/><path d="M14 20l6 26 8-4-6-22z" fill="#8a2a20"/>
 <ellipse cx="0" cy="-12" rx="17" ry="20" fill="url(#skin)"/>
 <path d="M-20 -20q2-18 20-18q22 0 24 16q-12-4-22-4q-12 0-22 6z" fill="#22252a"/><circle cx="2" cy="-38" r="3" fill="#22252a"/>
 <path d="M-13 -24q-2 6 0 10M13 -24q2 6 0 10" stroke="#5a3e2c" stroke-width="3" fill="none"/>
 <circle cx="-6" cy="-12" r="2.2" fill="#2a1d12"/><circle cx="7" cy="-12" r="2.2" fill="#2a1d12"/>
 <ellipse cx="0" cy="0" rx="4" ry="3" fill="#7a3a2a"/>
 <g fill="#b77a5a" opacity=".6"><circle cx="-9" cy="-5" r="1"/><circle cx="-6" cy="-3" r="1"/><circle cx="9" cy="-5" r="1"/><circle cx="6" cy="-3" r="1"/></g>
</g>"""

# ======================= COCINA DE AITOR =======================
def cocina(gente=True):
    b = '<rect width="800" height="500" fill="#3a2618"/>'
    b += '<rect width="800" height="300" fill="#4a3020"/><path d="M0 300H800" stroke="#2a1a10" stroke-width="4"/>'
    for k in range(0, 800, 40):
        b += f'<path d="M{k} 300V500" stroke="#2f1f14" stroke-width="1.2"/>'
    b += '<rect y="400" width="800" height="100" fill="#2a1a10" opacity=".55"/>'
    # ventana al puerto
    b += '<rect x="548" y="60" width="170" height="170" fill="#1a1410"/><rect x="556" y="68" width="154" height="154" fill="#7d8b93"/>'
    b += '<path d="M570 222V120M600 222V100M690 222V130" stroke="#3a4248" stroke-width="3"/><path d="M570 130l20 14M600 112l22 18" stroke="#3a4248" stroke-width="1.5"/>'
    b += '<rect x="556" y="68" width="154" height="154" filter="url(#fog)" opacity=".8"/>'
    b += '<path d="M633 68V222M556 145H710" stroke="#1a1410" stroke-width="6"/><rect x="540" y="228" width="186" height="10" fill="#5a3a22"/>'
    # tablón de corcho con las cartas
    b += '<rect x="214" y="70" width="170" height="118" rx="3" fill="#6b4a2a" stroke="#3a2414" stroke-width="5"/>'
    for (x, y, r) in [(232, 84, -6), (282, 80, 4), (334, 88, -3)]:
        b += f'<g transform="rotate({r} {x+20} {y+30})"><rect x="{x}" y="{y}" width="40" height="56" fill="#e9dfc7"/>'
        for l in range(6): b += f'<path d="M{x+5} {y+10+l*7}h{30-(l%3)*6}" stroke="#7a6c58" stroke-width="1.2"/>'
        b += f'<circle cx="{x+20}" cy="{y+4}" r="3" fill="#a3271c"/></g>'
    b += '<ellipse cx="248" cy="128" rx="9" ry="7" fill="#8a5a2a" opacity=".45"/>'
    b += '<text x="252" y="176" font-size="5" fill="#e9dfc7" font-family="Georgia" opacity=".9">La Plata</text>'
    # fogón de hierro
    b += '<circle cx="120" cy="300" r="190" fill="url(#warm)" opacity=".9"/>'
    b += '<rect x="40" y="220" width="160" height="190" rx="6" fill="#1c1a18"/><rect x="40" y="214" width="160" height="12" fill="#2c2926"/>'
    b += '<rect x="62" y="310" width="70" height="44" rx="4" fill="#ff9a30"/><path d="M70 350q10-30 20-6q6-24 16 0q8-20 18 4" fill="#ffd27a"/>'
    b += '<rect x="58" y="306" width="78" height="52" rx="4" fill="none" stroke="#3a3632" stroke-width="5"/>'
    b += '<rect x="150" y="250" width="34" height="140" fill="#2c2926"/><rect x="70" y="40" width="30" height="176" fill="#24211e"/>'
    # cafetera humeando
    b += '<path d="M90 214l6-34h28l6 34z" fill="#8d8a80"/><path d="M130 196q12 2 10 14" stroke="#8d8a80" stroke-width="4" fill="none"/>'
    b += '<g filter="url(#b5)" opacity=".7"><ellipse cx="110" cy="160" rx="12" ry="20" fill="#e8e2d6"/><ellipse cx="118" cy="128" rx="10" ry="16" fill="#e8e2d6"/></g>'
    # Aitor sentado (detrás de la mesa)
    if gente: b += '<clipPath id="tbl"><rect x="0" y="0" width="800" height="340"/></clipPath>'
    if gente: b += f'<g clip-path="url(#tbl)">{aitor_casa(380, 478, .8)}</g>'
    # mesa
    b += '<rect x="226" y="330" width="300" height="16" fill="#6b4426"/><rect x="226" y="346" width="300" height="12" fill="#4a2e18"/>'
    b += '<rect x="240" y="358" width="12" height="118" fill="#4a2e18"/><rect x="500" y="358" width="12" height="118" fill="#4a2e18"/>'
    # cosas de la mesa
    b += '<ellipse cx="268" cy="328" rx="26" ry="9" fill="#c9924a"/><path d="M250 324q18-8 36 0" stroke="#8a5a2a" stroke-width="1.5" fill="none"/>'
    b += '<path d="M314 316h20l-2 16h-16z" fill="#e8e2d6"/><path d="M334 320q6 2 0 8" stroke="#e8e2d6" stroke-width="2" fill="none"/>'
    b += '<path d="M448 316h20l-2 16h-16z" fill="#e8e2d6"/><path d="M448 320q-6 2 0 8" stroke="#e8e2d6" stroke-width="2" fill="none"/>'
    # cuaderno de ronda abierto
    b += '<g transform="rotate(-4 400 330)"><path d="M366 322h34v14h-34zM400 322h34v14h-34z" fill="#e9dfc7" stroke="#6a5a42" stroke-width=".8"/>'
    for l in range(4): b += f'<path d="M370 {325+l*3}h26M404 {325+l*3}h{24-l*3}" stroke="#4a3a2a" stroke-width=".7"/>'
    b += '</g>'
    # moneda de PortAventura
    b += '<circle cx="498" cy="331" r="5" fill="#c9a24a" stroke="#6e5320"/><path d="M495 331h6M498 328v6" stroke="#8a6a2a" stroke-width=".6"/>'
    b += '<text x="498" y="332.4" text-anchor="middle" font-size="1.6" fill="#3a2a10" font-family="Georgia">PortAventura</text>'
    # Candela de pie junto a la ventana
    if gente: b += candela_casa(628, 484, .9)
    # despensa (puerta entreabierta, a oscuras)
    b += '<rect x="716" y="246" width="84" height="232" fill="#120c08"/>'
    b += '<g class="ol"><path d="M724 280h76M724 330h76" stroke="#5a3a22" stroke-width="5"/><rect x="742" y="258" width="34" height="22" rx="2" fill="#a3271c"/><text x="759" y="272" text-anchor="middle" font-size="6" fill="#f0e0b0" font-family="Georgia">GALLETAS</text>'
    b += '<rect x="732" y="306" width="16" height="24" fill="#6a7a5a"/><rect x="756" y="300" width="14" height="30" fill="#8a6a3a"/></g>'
    b += '<path d="M716 246l-30 10v228l30-6z" fill="#5a3a22"/><circle cx="694" cy="370" r="3" fill="#c9a24a"/>'
    b += '<rect x="716" y="246" width="84" height="232" fill="#000" class="ob" opacity=".85"/>'
    b += '<rect width="800" height="500" fill="url(#vig)"/>'
    return wrap(b)
SVG['cocina'] = cocina()

# ======================= PORTAL =======================
def portal():
    b = '<rect width="800" height="500" fill="#2a2420"/>'
    # paredes encaladas viejas
    b += '<rect x="0" y="0" width="800" height="500" fill="#4a4038"/>'
    b += '<path d="M0 0h230v500H0z" fill="#3a322c"/>'
    # escalera de piedra que baja a la izquierda
    for k in range(7):
        y = 300 + k*28; x = 40 + k*18
        b += f'<rect x="0" y="{y}" width="{230-k*14}" height="28" fill="#5a524a"/><path d="M0 {y}h{230-k*14}" stroke="#7a7068" stroke-width="2"/>'
    b += '<path d="M232 0V500" stroke="#2a2420" stroke-width="6"/>'
    # Aitor bajando, de espaldas, poniéndose la gorra
    b += """<g transform="translate(120 360) scale(.62)">
 <path d="M-40 -150q40-16 80 0l12 170h-104z" fill="#2a2e35"/>
 <path d="M40 -146q20 -40 6 -86" stroke="#2a2e35" stroke-width="20" fill="none" stroke-linecap="round"/>
 <ellipse cx="0" cy="-185" rx="27" ry="31" fill="#33281f"/>
 <path d="M-26 -196q26-14 52 0l-2-16q-24-12-48 0z" fill="#1d2026"/><path d="M-30 -196q30 6 60 0l-2 6q-28 6-56 0z" fill="#0e0f12"/>
 <circle cx="44" cy="-232" r="9" fill="#c9a084"/>
</g>"""
    # puerta de madera con rendija de luz
    b += '<rect x="330" y="40" width="250" height="400" fill="#3a2414" stroke="#1a100a" stroke-width="8"/>'
    b += '<rect x="352" y="66" width="206" height="150" fill="none" stroke="#2a1a0e" stroke-width="5"/><rect x="352" y="246" width="206" height="170" fill="none" stroke="#2a1a0e" stroke-width="5"/>'
    b += '<circle cx="548" cy="250" r="7" fill="#c9a24a"/><rect x="460" y="180" width="30" height="8" rx="2" fill="#8a6a2a"/>'
    b += '<rect x="330" y="440" width="250" height="6" fill="#d8d0b8" opacity=".85"/>'
    b += '<rect x="330" y="446" width="250" height="40" fill="#d8d0b8" opacity=".08"/>'
    # suelo y felpudo
    b += '<rect y="446" width="800" height="54" fill="#2c2622"/>'
    b += '<g class="ol"><path d="M486 456l34-6 6 16-34 6z" fill="#e9dfc7"/><path d="M492 460l20-3M494 465l16-3" stroke="#6a5a42" stroke-width="1"/></g>'
    b += '<rect x="360" y="452" width="190" height="34" rx="3" fill="#8a6a3a"/>'
    for k in range(18): b += f'<path d="M{366+k*10} 455v28" stroke="#6a4e28" stroke-width="2"/>'
    b += '<rect width="800" height="500" fill="url(#vig)"/>'
    return wrap(b)
SVG['portal'] = portal()

# ======================= LA NOTA (primer plano) =======================
def nota():
    b = '<rect width="800" height="500" fill="#2a1d14"/>'
    for k in range(0, 500, 46): b += f'<path d="M0 {k}H800" stroke="#1e140d" stroke-width="3"/>'
    b += '<g transform="rotate(-4 400 250)">'
    # papel caro con la esquina de arriba a la derecha recortada
    b += '<path d="M190 70H590L620 100V430H190z" fill="#efe6d0"/><path d="M190 70H590L620 100V430H190z" fill="#000" filter="url(#paperT)"/>'
    b += '<path d="M590 70L620 100" stroke="#b8aa88" stroke-width="1.5"/>'
    b += '<text x="604" y="92" font-size="7" fill="#5a4a3a" font-family="Georgia" transform="rotate(45 604 92)">…ETA</text>'
    b += '<path d="M250 150q120-6 300 4M240 300q160 8 320-2" stroke="#d8cdb2" stroke-width="1" fill="none"/>'
    txt = ['NO FUE UN', 'SUICIDIO.', 'QUE LO MIRE', 'LA ARGENTINA.']
    for k, t in enumerate(txt):
        b += f'<text x="405" y="{170+k*62}" text-anchor="middle" font-size="40" fill="#3a3a3e" font-family="Special Elite,Courier New,monospace" letter-spacing="2">{t}</text>'
    b += '</g><rect width="800" height="500" fill="url(#vig)"/>'
    return wrap(b)
SVG['nota'] = nota()

# ======================= PERSONAJES DEL FARO =======================
GUARDIA = """<g>
 <ellipse cx="0" cy="0" rx="34" ry="6" fill="#000" opacity=".45"/>
 <rect x="-14" y="-70" width="11" height="68" fill="#1e2420"/><rect x="3" y="-70" width="11" height="68" fill="#1a201c"/>
 <path d="M-34 -60q-2-118 34-128q36 10 34 128z" fill="#2d3a33"/><path d="M-28 -70q0-100 28-110" fill="none" stroke="#1a221e" stroke-width="2"/>
 <rect x="-6" y="-196" width="12" height="14" fill="#b98f73"/>
 <ellipse cx="0" cy="-208" rx="14" ry="17" fill="url(#skin)"/>
 <path d="M-8 -200q8 4 16 0" stroke="#2a2018" stroke-width="3"/>
 <path d="M-14 -214q-2-22 14-24q16 2 14 24z" fill="#0b0c0d"/><path d="M6 -238q16-2 20 22l-10 2z" fill="#0b0c0d"/><path d="M-22 -213q22-9 46 0l-6 8q-17-6-34 0z" fill="#16181a"/><path d="M-10 -232q8-4 14 0" stroke="#3a3d40" stroke-width="1.5" fill="none"/>
 <path d="M28 -120v34" stroke="#2a2420" stroke-width="2"/><rect x="20" y="-90" width="16" height="22" rx="2" fill="#ffd28a" stroke="#2a2420" stroke-width="2"/>
</g>"""
SALAZAR = """<g>
 <ellipse cx="0" cy="0" rx="50" ry="7" fill="#000" opacity=".45"/>
 <path d="M-30 0v-40q0-14 14-14h40v54h-14v-38h-26v38z" fill="#2f3236"/>
 <path d="M-30 -6h16M10 0h14" stroke="#1a2a30" stroke-width="7"/>
 <path d="M-26 -50q26-80 52 0z" fill="#4a4c50"/>
 <path d="M22 -96q20 20 26 54" stroke="#4a4c50" stroke-width="12" fill="none" stroke-linecap="round"/><circle cx="48" cy="-40" r="5" fill="url(#skin)"/>
 <rect x="-5" y="-118" width="10" height="12" fill="#c9a084"/>
 <ellipse cx="0" cy="-128" rx="13" ry="15" fill="url(#skin)"/>
 <circle cx="-5" cy="-130" r="4" fill="none" stroke="#2a2a2a" stroke-width="1.4"/><circle cx="6" cy="-130" r="4" fill="none" stroke="#2a2a2a" stroke-width="1.4"/><path d="M-1 -130h3" stroke="#2a2a2a"/>
 <path d="M-6 -119q6 3 12 0" stroke="#7a4f3f" stroke-width="1.4" fill="none"/>
 <ellipse cx="0" cy="-140" rx="19" ry="4" fill="#151515"/><path d="M-11 -141q0-16 11-16t11 16z" fill="#1c1c1c"/>
 <g><rect x="52" y="-22" width="40" height="22" rx="3" fill="#3a2414"/><path d="M52 -22l6-10h28l6 10" fill="#2a180c"/><rect x="60" y="-30" width="4" height="8" fill="#c9c9c9"/></g>
</g>"""
IBARRA = """<g>
 <ellipse cx="0" cy="0" rx="44" ry="7" fill="#000" opacity=".45"/>
 <rect x="-18" y="-76" width="14" height="74" fill="#2a2420"/><rect x="4" y="-76" width="14" height="74" fill="#241f1b"/>
 <path d="M-40 -70q-6-110 40-118q46 8 40 118z" fill="#5a4630"/><path d="M0 -186v116" stroke="#3a2c1c" stroke-width="2"/>
 <g fill="#c9a24a"><circle cx="-6" cy="-150" r="2.5"/><circle cx="-6" cy="-125" r="2.5"/><circle cx="-6" cy="-100" r="2.5"/></g>
 <path d="M34 -170q16 30 10 66" stroke="#5a4630" stroke-width="15" fill="none" stroke-linecap="round"/>
 <rect x="34" y="-112" width="16" height="20" fill="#e9dfc7" stroke="#6a5a42"/>
 <rect x="-7" y="-200" width="14" height="14" fill="#c9a084"/>
 <ellipse cx="0" cy="-214" rx="18" ry="19" fill="url(#skin)"/>
 <circle cx="-7" cy="-216" r="2" fill="#2a2018"/><circle cx="7" cy="-216" r="2" fill="#2a2018"/>
 <path d="M-14 -204q14-8 28 0q-7 6-14 3q-7 3-14-3z" fill="#3a3a3a"/>
 <g transform="translate(0 -216) scale(1.25 1.15) translate(0 208)"><path d="M-14 -214q-2-22 14-24q16 2 14 24z" fill="#0b0c0d"/><path d="M6 -238q16-2 20 22l-10 2z" fill="#0b0c0d"/><path d="M-22 -213q22-9 46 0l-6 8q-17-6-34 0z" fill="#16181a"/><path d="M-10 -232q8-4 14 0" stroke="#3a3d40" stroke-width="1.5" fill="none"/></g>
</g>"""
LEONOR = """<g>
 <ellipse cx="0" cy="0" rx="38" ry="6" fill="#000" opacity=".45"/>
 <path d="M-30 0q4-120 30-170q26 50 30 170z" fill="#121014"/>
 <path d="M-26 -60q26-130 52 0" fill="none" stroke="#2a2630" stroke-width="2"/>
 <path d="M-28 -168q28-16 56 0q4 24-4 40q-24 10-48 0q-8-16-4-40z" fill="#3a2e26"/>
 <rect x="-5" y="-186" width="10" height="14" fill="#d8c0a8"/>
 <ellipse cx="0" cy="-198" rx="13" ry="16" fill="#e2cbb4"/>
 <circle cx="-5" cy="-200" r="1.6" fill="#2a2018"/><circle cx="5" cy="-200" r="1.6" fill="#2a2018"/><path d="M-4 -190h8" stroke="#7a4f3f" stroke-width="1.2"/>
 <path d="M-20 -206q20-20 40 0v4h-40z" fill="#0c0b0d"/><ellipse cx="0" cy="-205" rx="24" ry="5" fill="#0c0b0d"/>
 <path d="M-18 -204q-2 16 2 26h32q4-10 2-26" fill="#000" opacity=".35"/>
</g>"""
def fig(g, x, y, s=1, flip=False):
    return f'<g transform="translate({x} {y}) scale({-s if flip else s} {s})">{g}</g>'

def faro(leonor=False):
    b = '<linearGradient id="dawn" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2a3340"/><stop offset=".6" stop-color="#5a5e62"/><stop offset="1" stop-color="#7a7266"/></linearGradient>'
    b += '<rect width="800" height="500" fill="url(#dawn)"/>'
    # faro y casa del farero arriba a la derecha
    b += '<path d="M640 40h40v-8h-40z" fill="#2a2a2a"/><rect x="644" y="20" width="32" height="22" fill="#fff3c4"/><circle cx="660" cy="31" r="70" fill="url(#warm)"/>'
    b += '<path d="M676 30L800 6v50z" fill="#ffe9a8" opacity=".15"/>'
    b += '<path d="M636 42h48l8 150h-64z" fill="#d8d4cc"/><path d="M634 90h52M630 140h60" stroke="#8a2a20" stroke-width="14"/>'
    b += '<rect x="700" y="150" width="70" height="44" fill="#c8c0b0"/><path d="M694 152l41-22 41 22z" fill="#6a2a22"/><rect x="712" y="164" width="12" height="12" fill="#ffd28a"/>'
    # mar y olas a la izquierda
    b += '<path d="M0 230q100-10 200 0t260 6V500H0z" fill="#26323a"/>'
    for k in range(6):
        y = 250 + k*30
        b += f'<path d="M0 {y}q30-8 60 0t60 0t60 0t60 0" stroke="#4a5a64" stroke-width="2" fill="none" opacity=".6"/>'
    # barca sin luces en la niebla
    b += '<path d="M60 236h90l-12 14h-66z" fill="#1a1e22" opacity=".7"/><path d="M104 236v-40" stroke="#1a1e22" stroke-width="3" opacity=".7"/>'
    # camino y verja hacia el faro
    b += '<path d="M560 500L620 200h40l60 300z" fill="#2e2a27"/>'
    b += '<rect x="576" y="250" width="6" height="110" fill="#1a1a1a"/><rect x="686" y="250" width="6" height="110" fill="#1a1a1a"/>'
    b += '<g stroke="#1a1a1a" stroke-width="3">' + ''.join(f'<path d="M{x} 262v96"/>' for x in range(592, 640, 10)) + '<path d="M582 262h58M582 350h58"/></g>'
    b += '<path d="M640 262l26-10v96l-26 10" fill="none" stroke="#1a1a1a" stroke-width="3"/>'
    b += '<path d="M636 300a6 6 0 1 1 0 .1" fill="none" stroke="#8a6a2a" stroke-width="2.5"/><rect x="630" y="304" width="12" height="10" rx="1" fill="#8a6a2a"/>'
    # rocas planas y cuerpo
    b += '<path d="M120 500L170 360q120-30 300-10l90 150z" fill="#3a3632"/><path d="M200 380q100-14 220 0" stroke="#2a2622" stroke-width="3" fill="none"/>'
    # rocas del primer plano en sombra (huellas solo con luz)
    b += '<path d="M0 420q60-30 140-10l40 90H0z" fill="#1e1c1a"/>'
    b += '<g class="ol" fill="#0e0c0a" opacity=".8">' + ''.join(f'<ellipse cx="{30+i*26}" cy="{470-i*9}" rx="7" ry="11" transform="rotate(-60 {30+i*26} {470-i*9})"/>' for i in range(5)) + '</g>'
    b += '<rect x="0" y="420" width="180" height="80" fill="#000" class="ob" opacity=".55"/>'
    # el cuerpo bajo la sábana
    b += '<path d="M250 386q70-26 150-10l10 22q-80 14-162 6z" fill="#d6d2c6"/><path d="M262 392q60-12 130-4" stroke="#b8b2a4" stroke-width="2" fill="none"/>'
    b += '<path d="M404 380l18-6 4 12-18 4zM406 394l18-2 2 10-18 2z" fill="#1a1612"/>'
    # mano fuera de la sábana con ficha roja; las algas encima (se apartan)
    b += '<path d="M246 400q-14 4-22 16l6 4q8-6 18-10z" fill="#c9b0a0"/><rect x="216" y="412" width="12" height="9" rx="2" fill="#a3271c"/><text x="222" y="419.4" text-anchor="middle" font-size="5" fill="#f0d8a0" font-family="Georgia">C</text>'
    b += '<g id="algas"><path d="M200 420q20-24 50-14q-10 10-6 22q-20-8-44-8z" fill="#2e4a2a"/><path d="M206 424q16-14 40-10M212 430q14-6 30-4" stroke="#1e3a1a" stroke-width="3" fill="none"/><path d="M196 414q14-4 24 4" stroke="#3a5a34" stroke-width="5" fill="none"/></g>'
    # guardia civil con farol (izquierda del cuerpo)
    b += fig(GUARDIA, 190, 380, .9)
    b += '<circle cx="216" cy="309" r="60" fill="url(#warm)"/>'
    # doctor arrodillado y comisario
    b += fig(SALAZAR, 450, 404, .95)
    b += fig(IBARRA, 532, 404, .95)
    # Aitor junto a la verja
    b += aitor(715, 420, .62)
    if leonor:
        b += '<path d="M720 470h80v-40h-50l-14 18h-16z" fill="#0c0c0c"/><circle cx="738" cy="472" r="9" fill="#050505"/><rect x="756" y="434" width="30" height="14" fill="#3a4a5a" opacity=".6"/>'
        b += fig(LEONOR, 598, 470, .95)
    b += '<rect width="800" height="500" filter="url(#fog)" opacity=".45"/>'
    b += '<rect width="800" height="500" fill="url(#vig)"/>'
    return wrap(b)
SVG['faro'] = faro(); SVG['faroL'] = faro(True)

def trato():
    b = '<rect width="800" height="500" fill="#4a4c50"/>'
    b += '<g filter="url(#b5)" opacity=".7"><path d="M0 300q200-20 400 0t400 0V500H0z" fill="#2a2622"/><path d="M300 320q70-20 150-6l6 18q-80 10-160 2z" fill="#d6d2c6"/><rect x="620" y="60" width="40" height="160" fill="#d8d4cc"/></g>'
    b += '<rect width="800" height="500" filter="url(#fog)" opacity=".5"/>'
    b += fig(LEONOR, 180, 500, 1.9)
    b += f'<g transform="translate({400-205*1.2} {560-462*1.2}) scale(1.2)">{AITOR_CASA}</g>'
    b += '<path d="M330 420q-14 6-10 20q14 6 24-2z" fill="#1d2026"/>'
    b += fig(IBARRA, 630, 520, 1.85)
    b += '<rect width="800" height="500" fill="url(#vig)"/>'
    return wrap(b)
SVG['trato'] = trato()

def noche():
    c = cocina(False)
    c = c.replace('<rect width="800" height="500" fill="url(#vig)"/></svg>',
      '<rect width="800" height="500" fill="#05070c" opacity=".72"/>'
      '<rect x="62" y="310" width="70" height="44" fill="#ff7a20" opacity=".5"/>'
      '<circle class="verde" cx="572" cy="190" r="4" fill="#5dff8a" opacity="0"/>'
      '<rect width="800" height="500" fill="url(#vig)"/></svg>')
    return c
SVG['noche'] = noche()

# ======================= PERIÓDICO GENÉRICO =======================
def diario(fecha, titular, a_tit, a_grab, a_txt, b_tit, b_grab, b_txt, ads, breve_tit, breve, pie):
    ink = '#1f1a14'
    b = '<rect width="800" height="500" fill="#0b0908"/><g transform="rotate(1 400 250)">'
    b += '<rect x="96" y="14" width="608" height="476" fill="#e6dcc2"/><rect x="96" y="14" width="608" height="476" fill="#000" filter="url(#paperT)"/>'
    b += '<rect x="96" y="14" width="608" height="476" fill="none" stroke="#c9bb98" stroke-width="2"/>'
    b += f'<text x="400" y="66" text-anchor="middle" font-family="Limelight,Georgia,serif" font-size="46" fill="{ink}" letter-spacing="3">EL FARO DE ALTAMAR</text>'
    b += f'<path d="M116 78H684M116 100H684" stroke="{ink}" stroke-width="1.5"/>'
    b += f'<text x="120" y="94" font-size="11" fill="{ink}" font-family="Georgia">Diario de la mañana</text>'
    b += f'<text x="400" y="94" text-anchor="middle" font-size="11" fill="{ink}" font-family="Georgia">{fecha}</text>'
    b += f'<text x="680" y="94" text-anchor="end" font-size="11" fill="{ink}" font-family="Georgia">10 céntimos</text>'
    b += f'<text x="400" y="138" text-anchor="middle" font-size="25" textLength="560" lengthAdjust="spacingAndGlyphs" fill="{ink}" font-family="Georgia" font-weight="bold">{titular}</text>'
    b += f'<path d="M116 152H684" stroke="{ink}"/>'
    b += f'<text x="120" y="176" font-size="15.5" fill="{ink}" font-family="Georgia" font-weight="bold">{a_tit}</text>'
    b += f'<g transform="translate(118 186)"><rect width="250" height="104" fill="#d3c7a8"/>{a_grab}</g>'
    for k,t in enumerate(a_txt): b += f'<text x="120" y="{310+k*14}" font-size="10.5" fill="{ink}" font-family="Georgia">{t}</text>'
    b += f'<path d="M382 162V480" stroke="{ink}" stroke-width=".8"/>'
    b += f'<text x="396" y="178" font-size="15.5" fill="{ink}" font-family="Georgia" font-weight="bold">{b_tit}</text>'
    b += f'<g transform="translate(396 188)"><rect width="286" height="96" fill="#d3c7a8"/>{b_grab}</g>'
    for k,t in enumerate(b_txt): b += f'<text x="396" y="{304+k*14}" font-size="10.5" fill="{ink}" font-family="Georgia">{t}</text>'
    b += f'<rect x="118" y="386" width="250" height="90" fill="none" stroke="{ink}"/>'
    (t1, l1), (t2, l2) = ads
    b += f'<text x="243" y="402" text-anchor="middle" font-size="8" fill="{ink}" font-family="Georgia" font-weight="bold">{t1}</text>'
    for k,t in enumerate(l1): b += f'<text x="243" y="{414+k*8}" text-anchor="middle" font-size="5.2" fill="{ink}" font-family="Georgia">{t}</text>'
    b += f'<path d="M136 430H350" stroke="{ink}" stroke-width=".6"/>'
    b += f'<text x="243" y="446" text-anchor="middle" font-size="7.5" fill="{ink}" font-family="Georgia" font-weight="bold">{t2}</text>'
    for k,t in enumerate(l2): b += f'<text x="243" y="{457+k*10}" text-anchor="middle" font-size="5.2" fill="{ink}" font-family="Georgia">{t}</text>'
    b += f'<rect x="396" y="386" width="286" height="90" fill="#ddd2b4" stroke="{ink}"/>'
    b += f'<text x="539" y="402" text-anchor="middle" font-size="8" fill="{ink}" font-family="Georgia" font-weight="bold">{breve_tit}</text>'
    for k,t in enumerate(breve): b += f'<text x="539" y="{418+k*10}" text-anchor="middle" font-size="5.6" fill="{ink}" font-family="Georgia" font-style="italic">{t}</text>'
    b += f'<text x="539" y="468" text-anchor="middle" font-size="5" fill="{ink}" font-family="Georgia">{pie}</text>'
    b += '</g>'
    return wrap(b)

ink = '#1f1a14'
G_FARO = f'<path d="M20 100q60-20 120-6t110 6V104H20z" fill="{ink}"/><path d="M180 20h22l6 70h-34z" fill="{ink}"/><rect x="183" y="10" width="16" height="10" fill="{ink}"/><path d="M200 15l46-10v20z" fill="#8a8070"/><path d="M60 84q20-8 50-2l2 8q-28 4-52 0z" fill="#e6dcc2"/>'
G_PALACE = f'<rect x="40" y="30" width="200" height="66" fill="{ink}"/><path d="M30 32l110-26 110 26z" fill="{ink}"/>' + ''.join(f'<rect x="{56+i*36}" y="44" width="16" height="22" fill="#d3c7a8"/>' for i in range(6)) + '<rect x="128" y="70" width="28" height="26" fill="#d3c7a8"/>'
SVG['periodico2'] = diario('Viernes, 2 de diciembre de 1927', 'HALLADO MUERTO DON JULIÁN ARRIETA AL PIE DEL FARO',
  'La policía apunta a un suicidio', G_FARO,
  ['El comisario Ibarra da el caso por cerrado.','El doctor Salazar certificó la muerte «a las','tres de la madrugada, por la caída». La empresa','de Don Julián estaba en la ruina, y los','vecinos hablan de un hombre «hundido».'],
  'La viuda no recibe visitas', G_PALACE,
  ['Doña Leonor Arrieta guarda luto en el palacete.','Se comenta en el barrio que el seguro de vida','de Don Julián se subió hace apenas un mes.','Su hijo Íñigo no ha querido hablar con este','diario. Su hija Clara, tampoco.'],
  [('POMPAS FÚNEBRES OLAZABAL', ['Coches de caballos y de motor.','Discreción absoluta. Calle del Farol, 3.']),
   ('SIDRERÍA EL ANCLA', ['Esta noche, bertsolaris. Se fía a los huelguistas.'])],
  'ECOS DEL BARRIO',
  ['Una señorita argentina fue vista ayer en el faro,','tomando notas junto al cuerpo. Doña Puri insiste:','«formal, lo que se dice formal, no es». Los','estibadores, en asamblea hoy a mediodía en el muelle.'],
  'Mar de fondo. Niebla por la mañana. Pleamar a las 2:10.')

# ======================= EL MUELLE =======================
ESTIBADOR = """<g>
 <rect x="-12" y="-60" width="10" height="58" fill="#2a2622"/><rect x="2" y="-60" width="10" height="58" fill="#24201c"/>
 <path d="M-14 -2h12v4h-14zM2 -2h12l2 4h-14z" fill="#111"/>
 <path d="M-20 -130q20-10 40 0l6 72h-52z" fill="COL"/>
 <path d="M-22 -104q22 12 44 0" stroke="COL2" stroke-width="12" stroke-linecap="round" fill="none"/>
 <rect x="-5" y="-142" width="10" height="12" fill="#b98f73"/><ellipse cx="0" cy="-152" rx="11" ry="13" fill="url(#skin)"/>
 <path d="M-12 -158q12-12 24 0q2 4-2 4h-20q-4 0-2-4z" fill="#1d1d1d"/><path d="M8 -156l8 2" stroke="#1d1d1d" stroke-width="3"/>
</g>"""
MATEO = """<g>
 <ellipse cx="0" cy="0" rx="40" ry="6" fill="#000" opacity=".45"/>
 <rect x="-17" y="-80" width="14" height="76" fill="#3a3630"/><rect x="3" y="-80" width="14" height="76" fill="#34302a"/>
 <path d="M-20 -6h18v8h-20zM3 -6h18l3 8h-21z" fill="#1a1410"/><g fill="#9a9a9a"><circle cx="-16" cy="1" r="1"/><circle cx="-11" cy="1" r="1"/><circle cx="-6" cy="1" r="1"/><circle cx="7" cy="1" r="1"/><circle cx="12" cy="1" r="1"/><circle cx="17" cy="1" r="1"/></g>
 <path d="M-30 -170q30-12 60 0l8 92h-76z" fill="#d6cfc0"/>
 <path d="M-14 -170l-4 92M14 -170l4 92" stroke="#5a3a22" stroke-width="4"/>
 <path d="M-32 -132q32 16 64 0" stroke="#d6cfc0" stroke-width="18" stroke-linecap="round" fill="none"/><path d="M-30 -128q30 14 60 0" stroke="#c9b09a" stroke-width="6" stroke-linecap="round" fill="none"/>
 <rect x="-7" y="-186" width="14" height="16" fill="#c9a084"/>
 <ellipse cx="0" cy="-198" rx="16" ry="18" fill="url(#skin)"/>
 <path d="M-17 -204q2-20 17-20q16 0 17 20q-6-8-17-9q-11 1-17 9z" fill="#d8b860"/>
 <circle cx="-6" cy="-198" r="2" fill="#2a2018"/><circle cx="6" cy="-198" r="2" fill="#2a2018"/>
 <path d="M-6 -188q6 2 12 0" stroke="#7a4f3f" stroke-width="1.6" fill="none"/><path d="M-10 -192q10-3 20 0" stroke="#b89a50" stroke-width="2" fill="none"/>
</g>"""
def est(x, y, s, col, col2, flip=False):
    g = ESTIBADOR.replace('COL2', col2).replace('COL', col)
    return fig(g, x, y, s, flip)

def muelle():
    b = '<linearGradient id="fogsky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#6a7076"/><stop offset="1" stop-color="#a8a49a"/></linearGradient>'
    b += '<rect width="800" height="500" fill="url(#fogsky)"/>'
    # grúas al fondo
    b += '<g fill="none" stroke="#3a3c3e" stroke-width="6"><path d="M90 300V60l140 20M90 120l120 -40"/><path d="M620 300V40l-150 30M620 110l-130-30"/></g><path d="M226 80v80" stroke="#3a3c3e" stroke-width="2"/><path d="M474 70v70" stroke="#3a3c3e" stroke-width="2"/>'
    # agua
    b += '<rect y="250" width="800" height="90" fill="#3e4a50"/>'
    for k in range(4): b += f'<path d="M0 {262+k*20}q40-6 80 0t80 0t80 0t80 0t80 0t80 0t80 0t80 0t80 0t80 0" stroke="#5a6a72" stroke-width="1.5" fill="none"/>'
    # barcas amarradas (la Gaviota, sin farol)
    def barca(x, col, nombre, farol=True, w=120):
        s = f'<path d="M{x} 270h{w}l-14 22h-{w-28}z" fill="{col}"/><path d="M{x+w/2} 270v-60" stroke="#2a2622" stroke-width="3"/>'
        if farol: s += f'<rect x="{x+w/2-4}" y="206" width="8" height="10" fill="#e8e2d0" stroke="#2a2622"/>'
        else: s += f'<path d="M{x+w/2} 210h6v4" stroke="#2a2622" stroke-width="1.5" fill="none"/>'
        s += f'<text x="{x+w/2}" y="284" text-anchor="middle" font-size="5" fill="#e8e2d0" font-family="Georgia" letter-spacing="1">{nombre}</text>'
        return s
    b += barca(150, '#3a5a6a', 'SAN TELMO') + barca(300, '#f0ece0', 'GAVIOTA', False, 100) + barca(440, '#6a3a2a', 'ARANTZAZU')
    b += '<path d="M330 270q-10 20-24 30" stroke="#2a2622" stroke-width="1.5" fill="none"/>'
    # muelle
    b += '<rect y="320" width="800" height="180" fill="#57524a"/><path d="M0 320H800" stroke="#2a2622" stroke-width="5"/>'
    for k in range(0, 800, 60): b += f'<path d="M{k} 320v180" stroke="#4a463f" stroke-width="2"/>'
    b += '<rect x="250" y="310" width="16" height="18" rx="4" fill="#2a2622"/><rect x="540" y="310" width="16" height="18" rx="4" fill="#2a2622"/>'
    # cajas de conservas
    b += '<g><rect x="40" y="350" width="70" height="44" fill="#7a5a34"/><rect x="50" y="320" width="56" height="32" fill="#8a6a3e"/><text x="75" y="378" text-anchor="middle" font-size="7" fill="#2a1d10" font-family="Georgia">ARRIETA</text></g>'
    # caseta con la pizarra
    b += '<rect x="640" y="200" width="150" height="150" fill="#4a3424"/><path d="M630 204l85-34 85 34z" fill="#2a1d14"/>'
    b += '<rect x="660" y="228" width="80" height="58" fill="#1e2a24" stroke="#6a4a2a" stroke-width="4"/>'
    for k in range(5): b += f'<path d="M668 {242+k*9}h{30+(k*13)%34}" stroke="#d8d6cc" stroke-width="1.4" opacity=".7"/>'
    b += '<rect x="752" y="260" width="28" height="90" fill="#2a1d14"/>'
    # estibadores en huelga
    cols = [('#3a4652', '#34404a'), ('#5a4a3a', '#4e3f30'), ('#2e3a30', '#283228'), ('#4a3a40', '#40323a'), ('#36414a', '#30393f')]
    for i, (x, s) in enumerate([(120, .95), (175, 1.02), (228, .96), (455, 1.0), (510, .94)]):
        b += est(x, 440, s, *cols[i], flip=i % 2 == 1)
    # Mateo en primer plano
    b += fig(MATEO, 592, 470, 1.05)
    b += '<rect width="800" height="500" filter="url(#fog)" opacity=".55"/>'
    b += '<rect width="800" height="500" fill="url(#vig)"/>'
    return wrap(b)
SVG['muelle'] = muelle()

# ======================= LA PIZARRA DE TURNOS (puzle) =======================
def pizarra():
    b = '<rect width="800" height="500" fill="#3a2a1c"/>'
    for k in range(0, 500, 40): b += f'<path d="M0 {k}H800" stroke="#2e2014" stroke-width="2"/>'
    b += '<rect x="90" y="30" width="620" height="420" fill="#6a4a2a"/><rect x="104" y="44" width="592" height="392" fill="#1f2c26"/>'
    b += '<rect x="104" y="44" width="592" height="392" fill="#000" opacity=".15" filter="url(#paperT)"/>'
    ch = '#e2e0d6'
    b += f'<text x="400" y="88" text-anchor="middle" font-size="26" fill="{ch}" font-family="Special Elite,Courier New,monospace">GUARDIA DE AMARRAS</text>'
    b += f'<text x="400" y="114" text-anchor="middle" font-size="15" fill="{ch}" font-family="Special Elite,Courier New,monospace" opacity=".85">noche del 30 de noviembre</text>'
    slots = [('23:00 – 1:00', 160), ('1:00 – 3:00', 222), ('3:00 – 5:00', 284), ('5:00 – 7:00', 346)]
    frag = ['…teo', 'K…l…', '…ixen…', 'P…tx…']
    for i, (h, y) in enumerate(slots):
        b += f'<text x="150" y="{y+8}" font-size="20" fill="{ch}" font-family="Special Elite,Courier New,monospace">{h}</text>'
        b += f'<path d="M360 {y+12}h300" stroke="{ch}" stroke-width="1.5" opacity=".5"/>'
        # restos de tiza borrada (se leen con la lupa)
        b += f'<g opacity=".28"><path d="M372 {y-4}q60-14 140 4q60 10 120-6" stroke="{ch}" stroke-width="14" fill="none" opacity=".25"/></g>'
        b += f'<text x="392" y="{y+6}" font-size="9" fill="{ch}" font-family="Special Elite,Courier New,monospace" opacity=".45">{frag[i]}</text>'
        b += f'<text class="slot" data-i="{i}" x="520" y="{y+8}" font-size="22" fill="#f3dc9a" font-family="Special Elite,Courier New,monospace"></text>'
    b += f'<text x="150" y="410" font-size="11" fill="{ch}" font-family="Special Elite,Courier New,monospace" opacity=".7">Andoni: de baja (mano).   Firma: el capataz.</text>'
    b += f'<text x="604" y="418" font-size="6.5" fill="{ch}" font-family="Special Elite,Courier New,monospace" opacity=".55" transform="rotate(-8 604 418)">Mateo deja la guardia 0:00</text>'
    b += '<rect width="800" height="500" fill="url(#vig)"/>'
    return wrap(b)
SVG['pizarra'] = pizarra()

# ======================= DÍA 3 =======================
G_ASAMBLEA = f'<path d="M0 104V70h250v34z" fill="{ink}"/>' + ''.join(f'<circle cx="{20+i*24}" cy="60" r="8" fill="{ink}"/><path d="M{12+i*24} 70h16l2 34h-20z" fill="{ink}"/>' for i in range(10)) + f'<path d="M126 30l14-20 14 20z" fill="{ink}"/><rect x="120" y="30" width="40" height="20" fill="{ink}"/>'
G_FABRICA = f'<path d="M20 90V40l40-20v20l40-20v20l40-20v70z" fill="{ink}"/><rect x="150" y="10" width="14" height="80" fill="{ink}"/><rect x="180" y="40" width="90" height="50" fill="{ink}"/><text x="225" y="70" text-anchor="middle" font-size="8" fill="#d3c7a8" font-family="Georgia">LUTO · CERRADO</text>'
SVG['periodico3'] = diario('Sábado, 3 de diciembre de 1927', 'TENSIÓN EN EL MUELLE: «ARRIETA TUVO LO QUE SE MERECÍA»',
  'Asamblea de estibadores', G_ASAMBLEA,
  ['Mateo «el Rubio» no se mordió la lengua ante','sus hombres: «Arrieta tuvo lo que se merecía».','Después, ya más calmado, pidió que «nadie','haga tonterías». La huelga sigue. Los barcos','de la conservera no se descargan.'],
  'La conservera, en manos de la viuda', G_FABRICA,
  ['Doña Leonor Arrieta tomará las riendas de','Conservas Arrieta hasta que se lea el','testamento. El notario, Sr. Etxeberria, no','confirma la fecha. La fábrica cierra tres','días por luto.'],
  [('CASINO DE ALTAMAR', ['Esta noche, ruleta y orquesta.','Se ruega etiqueta. Socios y señoritas.']),
   ('DISPENSARIO DEL PUERTO', ['Vacunas gratis los martes. Dr. R. Salazar.'])],
  'ECOS DEL BARRIO',
  ['La señorita argentina interrogó ayer a los estibadores','en pleno muelle. Doña Puri, escandalizada, ha','comprado otra libreta para apuntarlo todo. En El Ancla','dicen que el tabernero ya le guarda sitio.'],
  'Mar rizada. Lluvia por la tarde. Pleamar a las 2:50.')

PACO = """<g>
 <path d="M-46 0q-4-120 46-130q50 10 46 130z" fill="#3a2c24"/>
 <path d="M-30 -110h60l6 110h-72z" fill="#e8e2d4"/><path d="M-30 -110q30 10 60 0" stroke="#bfb7a6" stroke-width="2" fill="none"/>
 <path d="M44 -100q18 20 14 54" stroke="#3a2c24" stroke-width="18" fill="none" stroke-linecap="round"/><circle cx="58" cy="-44" r="9" fill="url(#skin)"/>
 <rect x="-9" y="-146" width="18" height="18" fill="#c9a084"/>
 <ellipse cx="0" cy="-162" rx="22" ry="24" fill="url(#skin)"/>
 <path d="M-22 -168q2 -18 22-18q20 0 22 18q-4-8-22-9q-18 1-22 9z" fill="#d8b89a" opacity=".6"/>
 <path d="M-24 -160q-4 8 0 16M24 -160q4 8 0 16" stroke="#5a4a3a" stroke-width="4" fill="none"/>
 <circle cx="-8" cy="-164" r="2.4" fill="#2a2018"/><circle cx="8" cy="-164" r="2.4" fill="#2a2018"/>
 <path d="M-18 -152q18-12 36 0q-9 8-18 4q-9 4-18-4z" fill="#3a2e26"/>
 <path d="M-8 -142q8 3 16 0" stroke="#7a4f3f" stroke-width="1.6" fill="none"/>
</g>"""
def taberna():
    b = '<rect width="800" height="500" fill="#2a1a10"/>'
    b += '<rect width="800" height="300" fill="#3a2416"/>'
    for k in range(0, 800, 46): b += f'<path d="M{k} 0V300" stroke="#2e1c10" stroke-width="2"/>'
    b += '<path d="M0 40H800M0 44H800" stroke="#1e120a" stroke-width="6"/>'
    # vigas y faroles
    for x in (180, 480): b += f'<path d="M{x} 44v40" stroke="#1e120a" stroke-width="2"/><rect x="{x-9}" y="84" width="18" height="22" fill="#ffd28a"/><circle cx="{x}" cy="96" r="130" fill="url(#warm)"/>'
    # barriles de sidra al fondo
    for i in range(4):
        x = 30 + i*72; b += f'<ellipse cx="{x+30}" cy="200" rx="30" ry="40" fill="#5a3a22"/><path d="M{x+2} 186h56M{x+2} 214h56" stroke="#2a1a10" stroke-width="4"/><circle cx="{x+30}" cy="200" r="5" fill="#2a1a10"/>'
    # diana de dardos en la pared
    b += '<g id="dianaPared"><circle cx="650" cy="150" r="40" fill="#1a1a1a"/><circle cx="650" cy="150" r="32" fill="#e8dcc0"/><circle cx="650" cy="150" r="22" fill="#2a2a2a"/><circle cx="650" cy="150" r="12" fill="#a3271c"/><circle cx="650" cy="150" r="4" fill="#2a7a3a"/>'
    b += '<path d="M640 132l-14-10M664 160l14 6M650 140l2-16" stroke="#c9a24a" stroke-width="2"/></g>'
    # puerta de la trastienda
    b += '<rect x="720" y="120" width="70" height="180" fill="#1e140c" stroke="#120a06" stroke-width="5"/><circle cx="732" cy="214" r="3" fill="#8a6a2a"/><text x="755" y="140" text-anchor="middle" font-size="7" fill="#8a7a5a" font-family="Georgia">PRIVADO</text>'
    # pizarra de fiados
    b += '<rect x="330" y="90" width="110" height="80" fill="#1f2c26" stroke="#5a3a22" stroke-width="4"/>'
    b += '<text x="385" y="104" text-anchor="middle" font-size="8" fill="#e2e0d6" font-family="Special Elite,Courier New">FIADOS</text>'
    for k, t in enumerate(['Koldo ... 4 sidras', 'Mateo ... 2 sidras (30-XI)', 'Patxi ... 1 txakoli', 'Bixente ... 6 sidras (!)']):
        b += f'<text x="338" y="{118+k*12}" font-size="5.6" fill="#e2e0d6" font-family="Special Elite,Courier New">{t}</text>'
    # barra
    b += '<rect y="300" width="800" height="200" fill="#24160c"/>'
    b += '<path d="M120 300h460v34H120z" fill="#6b4426"/><rect x="120" y="334" width="460" height="130" fill="#4a2e18"/>'
    for k in range(5): b += f'<path d="M{150+k*90} 340v120" stroke="#3a2412" stroke-width="3"/>'
    b += '<path d="M200 300h16v-22h-16zM470 300h12v-26h-12z" fill="#6a8a5a" opacity=".8"/><path d="M300 296h20l-2 6h-16z" fill="#e8e2d0"/>'
    # Paco detrás de la barra
    b += '<clipPath id="barra"><rect width="800" height="300"/></clipPath>'
    b += f'<g clip-path="url(#barra)">{fig(PACO, 400, 360, 1.05)}</g>'
    # marineros en la barra (de espaldas y de lado)
    cols = [('#3a4652', '#34404a'), ('#4a3a2e', '#40322a')]
    b += est(110, 470, 1.08, *cols[0]) + est(640, 470, 1.05, *cols[1], flip=True)
    # rincón oscuro bajo la escalera (sangre y silla rota, solo con luz)
    b += '<path d="M0 500V360l90-60v200z" fill="#140c06"/>'
    b += '<g class="ol"><path d="M20 470l26-30M30 480l10-34" stroke="#5a3a22" stroke-width="5"/><g fill="#5a1410">' + ''.join(f'<ellipse cx="{50+i*9}" cy="{462+(i%2)*6}" rx="{3+i%2}" ry="2"/>' for i in range(5)) + '</g></g>'
    b += '<path d="M0 500V360l90-60v200z" fill="#000" class="ob" opacity=".7"/>'
    # humo
    b += '<rect width="800" height="500" filter="url(#fog)" opacity=".35"/>'
    b += '<rect width="800" height="500" fill="url(#vig)"/>'
    return wrap(b)
SVG['taberna'] = taberna()

def diana():
    b = '<rect width="800" height="500" fill="#3a2416"/>'
    for k in range(0, 800, 46): b += f'<path d="M{k} 0V500" stroke="#2e1c10" stroke-width="2"/>'
    # hueco en la pared con el papel (debajo de la diana)
    b += '<rect x="330" y="180" width="140" height="140" fill="#160c06"/><g transform="rotate(-6 400 250)"><rect x="362" y="214" width="76" height="62" fill="#e9dfc7"/><path d="M362 245h76M400 214v62" stroke="#c9bb98"/></g>'
    b += '<g id="diana"><circle cx="400" cy="250" r="170" fill="#121212"/>'
    cols = ['#e8dcc0', '#1a1a1a']
    for i in range(20):
        a0 = i*18-9; a1 = a0+18
        import math
        def pt(r, a): return f'{400+r*math.cos(math.radians(a)):.1f} {250+r*math.sin(math.radians(a)):.1f}'
        b += f'<path d="M400 250L{pt(150,a0)}A150 150 0 0 1 {pt(150,a1)}z" fill="{cols[i%2]}"/>'
        b += f'<path d="M{pt(150,a0)}A150 150 0 0 1 {pt(150,a1)}L{pt(140,a1)}A140 140 0 0 0 {pt(140,a0)}z" fill="{["#a3271c","#2a7a3a"][i%2]}"/>'
        b += f'<path d="M{pt(95,a0)}A95 95 0 0 1 {pt(95,a1)}L{pt(86,a1)}A86 86 0 0 0 {pt(86,a0)}z" fill="{["#a3271c","#2a7a3a"][i%2]}"/>'
    b += '<circle cx="400" cy="250" r="16" fill="#2a7a3a"/><circle cx="400" cy="250" r="7" fill="#a3271c"/>'
    for (x, y, a) in [(360, 210, -30), (452, 280, 20), (410, 160, -5)]:
        b += f'<g transform="rotate({a} {x} {y})"><rect x="{x-2}" y="{y-40}" width="4" height="40" fill="#c9a24a"/><path d="M{x} {y-40}l-8-14h16z" fill="#a3271c"/></g>'
    b += '</g><rect width="800" height="500" fill="url(#vig)"/>'
    return wrap(b)
SVG['diana'] = diana()

def notaC():
    b = '<rect width="800" height="500" fill="#2a1d14"/>'
    b += '<g transform="rotate(3 400 250)"><rect x="230" y="110" width="340" height="270" fill="#efe6d0"/><rect x="230" y="110" width="340" height="270" fill="#000" filter="url(#paperT)"/>'
    b += '<path d="M230 245h340M400 110v270" stroke="#d8cdb2" stroke-width="1.5"/>'
    for k, t in enumerate(['A las doce,', 'donde siempre.', 'Trae los papeles.']):
        b += f'<text x="400" y="{190+k*44}" text-anchor="middle" font-size="30" fill="#2a3a5a" font-family="Georgia" font-style="italic">{t}</text>'
    b += '<text x="520" y="350" text-anchor="middle" font-size="26" fill="#2a3a5a" font-family="Georgia" font-style="italic">— C.</text>'
    b += '<text x="300" y="368" font-size="6" fill="#8a7a5a" font-family="Georgia">Papelería · Imprenta Ugalde</text>'
    b += '</g><rect width="800" height="500" fill="url(#vig)"/>'
    return wrap(b)
SVG['notaC'] = notaC()

# ======================= DÍA 4 =======================
G_VELA = f'<rect x="80" y="40" width="90" height="40" fill="{ink}"/><path d="M70 40h110l-10-8h-90z" fill="{ink}"/>' + ''.join(f'<rect x="{x}" y="20" width="4" height="20" fill="{ink}"/><path d="M{x+2} 12q4 4 0 8q-4-4 0-8z" fill="{ink}"/>' for x in (60, 190)) + f'<path d="M20 100q105-14 210 0" stroke="{ink}" stroke-width="3" fill="none"/>'
G_NOTARIO = f'<rect x="90" y="16" width="100" height="70" fill="{ink}"/><rect x="104" y="28" width="72" height="8" fill="#d3c7a8"/><rect x="104" y="44" width="60" height="4" fill="#d3c7a8"/><rect x="104" y="54" width="66" height="4" fill="#d3c7a8"/><circle cx="160" cy="74" r="8" fill="#a3271c"/>'
SVG['periodico4'] = diario('Domingo, 4 de diciembre de 1927', 'VELATORIO DE DON JULIÁN, HOY EN EL PALACETE',
  'El barrio despide a Arrieta', G_VELA,
  ['La capilla ardiente se abre hoy de diez a','dos en el palacete de la familia. El entierro,','mañana a las once. Se espera a medio Altamar:','unos por respeto, otros por curiosidad, y','algunos, dicen, para asegurarse.'],
  '¿Quién heredará la conservera?', G_NOTARIO,
  ['El notario Etxeberria guarda silencio. Se','rumorea que Don Julián cambió el testamento','días antes de morir. La familia lo niega.','Íñigo Arrieta, el heredero, fue visto anoche','otra vez en el Casino.'],
  [('JOYERÍA ZUBELDIA', ['Compramos oro y alhajas al mejor precio.','Discreción. Pago en el acto.']),
   ('FLORISTERÍA LAS DALIAS', ['Coronas y ramos para todo momento. Servicio nocturno.'])],
  'ECOS DEL BARRIO',
  ['Doña Puri irá al velatorio «a dar el pésame».','Lleva la libreta nueva en el bolso. La señorita','argentina, nos dicen, también irá, del brazo','del sereno. Habrá que verlo.'],
  'Mar en calma. Niebla al alba. Pleamar a las 3:30.')

INIGO = """<g>
 <ellipse cx="0" cy="0" rx="34" ry="6" fill="#000" opacity=".45"/>
 <rect x="-14" y="-80" width="11" height="78" fill="#1c1c22"/><rect x="3" y="-80" width="11" height="78" fill="#18181e"/>
 <path d="M-16 -2h14v5h-16zM3 -2h14l2 5h-16z" fill="#0a0a0a"/>
 <path d="M-26 -176q26-12 52 0l6 98h-64z" fill="#2a2a34"/><path d="M-8 -176l8 30 8-30" fill="#e8e2d4"/><path d="M-2 -158h4l2 14h-8z" fill="#5a1a1a"/>
 <path d="M-26 -170q-12 40-6 82" stroke="#2a2a34" stroke-width="13" fill="none" stroke-linecap="round"/><circle cx="-31" cy="-86" r="6" fill="url(#skin)"/>
 <path d="M-32 -86l-6 86" stroke="#4a2a14" stroke-width="4"/><circle cx="-31" cy="-88" r="5" fill="#c9a24a"/>
 <path d="M26 -170q14 20 6 42" stroke="#2a2a34" stroke-width="13" fill="none" stroke-linecap="round"/><circle cx="30" cy="-126" r="6" fill="url(#skin)"/>
 <path d="M34 -128l16-4" stroke="#e8e2d4" stroke-width="2.5"/><circle cx="50" cy="-132" r="1.6" fill="#ff8a3a"/>
 <rect x="-6" y="-192" width="12" height="16" fill="#c9a084"/>
 <ellipse cx="0" cy="-206" rx="15" ry="18" fill="url(#skin)"/>
 <path d="M-16 -210q0-18 16-20q18 2 17 18q-8-12-18-10q-8 2-15 12z" fill="#1a120c"/>
 <circle cx="-5" cy="-206" r="1.8" fill="#2a2018"/><circle cx="6" cy="-206" r="1.8" fill="#2a2018"/>
 <path d="M-5 -196q6 4 11 0" stroke="#7a4f3f" stroke-width="1.4" fill="none"/>
</g>"""
CLARA = """<g>
 <ellipse cx="0" cy="0" rx="30" ry="6" fill="#000" opacity=".45"/>
 <path d="M-24 0q2-110 24-160q22 50 24 160z" fill="#2a1c24"/>
 <path d="M-22 -150q22-16 44 0l2 40h-48z" fill="#2a1c24"/>
 <path d="M22 -146q12 30 6 64" stroke="#2a1c24" stroke-width="11" fill="none" stroke-linecap="round"/><circle cx="28" cy="-82" r="5" fill="url(#skin)"/><circle cx="30" cy="-80" r="1.6" fill="#1a2a5a"/><circle cx="26" cy="-79" r="1.2" fill="#1a2a5a"/>
 <path d="M-22 -146q-10 30-4 60" stroke="#2a1c24" stroke-width="11" fill="none" stroke-linecap="round"/><circle cx="-26" cy="-86" r="5" fill="url(#skin)"/>
 <rect x="-5" y="-166" width="10" height="14" fill="#d8b49a"/>
 <ellipse cx="0" cy="-180" rx="13" ry="16" fill="url(#skin)"/>
 <path d="M-15 -176q-2-22 15-22q17 0 15 22q-2 8-4 10v-14q-11-6-22 0v14q-2-2-4-10z" fill="#3a2414"/>
 <circle cx="-5" cy="-180" r="1.7" fill="#2a2018"/><circle cx="5" cy="-180" r="1.7" fill="#2a2018"/>
 <path d="M-4 -170h8" stroke="#8a4a3a" stroke-width="1.4"/>
</g>"""
BENIGNA = """<g>
 <ellipse cx="0" cy="0" rx="32" ry="6" fill="#000" opacity=".45"/>
 <path d="M-28 0q0-100 28-150q28 50 28 150z" fill="#1e1e24"/>
 <path d="M-18 -120h36l6 120h-48z" fill="#e8e2d4"/>
 <path d="M-24 -136q-6 20 10 34h34q8-10 4-34" fill="#1e1e24"/>
 <path d="M-16 -104h56" stroke="#8a8a8a" stroke-width="4"/><ellipse cx="22" cy="-106" rx="26" ry="4" fill="#b8b8b8"/><path d="M8 -110v-8h6v8M28 -110v-10h5v10" fill="#e8e2d4"/>
 <rect x="-5" y="-158" width="10" height="12" fill="#c9a084"/>
 <ellipse cx="0" cy="-170" rx="13" ry="15" fill="url(#skin)"/>
 <path d="M-14 -174q2-16 14-16q12 0 14 16q-6-8-14-8t-14 8z" fill="#8a8680"/><circle cx="0" cy="-190" r="7" fill="#8a8680"/>
 <circle cx="-5" cy="-171" r="1.6" fill="#2a2018"/><circle cx="5" cy="-171" r="1.6" fill="#2a2018"/><path d="M-5 -161q5-2 10 0" stroke="#7a4f3f" stroke-width="1.3" fill="none"/>
</g>"""

def salon():
    b = '<rect width="800" height="500" fill="#2a1418"/>'
    b += '<rect width="800" height="330" fill="#3a1c22"/>'
    for k in range(0, 800, 60): b += f'<path d="M{k} 0V330" stroke="#30161c" stroke-width="18" opacity=".5"/>'
    b += '<path d="M0 330H800" stroke="#1a0c0e" stroke-width="6"/>'
    # retratos
    for (x, w) in [(60, 70), (560, 60)]:
        b += f'<rect x="{x}" y="60" width="{w}" height="{w*1.3}" fill="#2a1a0e" stroke="#8a6a2a" stroke-width="5"/><ellipse cx="{x+w/2}" cy="{60+w*.55}" rx="{w*.25}" ry="{w*.32}" fill="#4a3a2a"/>'
    # ventana con cortinas
    b += '<rect x="640" y="50" width="120" height="200" fill="#5a6a72"/><rect x="640" y="50" width="120" height="200" filter="url(#fog)" opacity=".7"/><path d="M630 40q30 120 10 220h-14V40zM770 40q-30 120-10 220h14V40z" fill="#5a1a22"/>'
    # puerta del despacho (izquierda, entreabierta)
    b += '<rect x="170" y="110" width="80" height="220" fill="#1a0e08" stroke="#4a2a14" stroke-width="5"/><circle cx="240" cy="230" r="3" fill="#c9a24a"/><text x="210" y="102" text-anchor="middle" font-size="7" fill="#8a7a5a" font-family="Georgia">DESPACHO</text>'
    # ataúd y velas
    b += '<path d="M300 300h220l20 30h-260z" fill="#2a1a10"/><path d="M296 290h228v14H296z" fill="#4a2e18"/><path d="M300 290h220l-10-14H310z" fill="#3a2414"/><path d="M410 278v10M402 283h16" stroke="#c9a24a" stroke-width="2"/>'
    for x in (280, 540):
        b += f'<rect x="{x-3}" y="230" width="6" height="66" fill="#c9a24a"/><rect x="{x-4}" y="212" width="8" height="18" fill="#efe6d0"/><path d="M{x} 202q5 6 0 10q-5-4 0-10z" fill="#ffd27a"/><circle cx="{x}" cy="208" r="70" fill="url(#warm)"/>'
    # alfombra y suelo
    b += '<rect y="330" width="800" height="170" fill="#2a1a12"/><path d="M120 360h560l40 140H80z" fill="#4a1a1e"/><path d="M140 372h520l34 120H106z" fill="none" stroke="#8a6a2a" stroke-width="2"/>'
    # personajes
    b += fig(LEONOR, 420, 470, 1.05)
    b += fig(INIGO, 680, 470, 1.0)
    b += fig(CLARA, 120, 470, .98)
    b += fig(BENIGNA, 300, 480, .95)
    b += f'<g transform="translate({560-205*.78} {478-462*.78}) scale(.78)">{AITOR_CASA}</g>'
    b += '<path d="M548 380q-8 6-4 14l10-2z" fill="#1d2026"/>'
    # platito con horquillas en el velador
    b += '<rect x="752" y="380" width="40" height="6" fill="#4a2e18"/><rect x="768" y="386" width="6" height="90" fill="#4a2e18"/><ellipse cx="772" cy="379" rx="14" ry="4" fill="#d8d0c0"/><path d="M764 377l6-2M770 378l6-3M772 376l4 3" stroke="#3a3a3a" stroke-width="1.2"/>'
    b += '<rect width="800" height="500" fill="url(#vig)"/>'
    return wrap(b)
SVG['salon'] = salon()

def despacho(leonor=False):
    b = '<rect width="800" height="500" fill="#20140c"/>'
    b += '<rect width="800" height="320" fill="#2e1e12"/>'
    for k in range(0, 800, 50): b += f'<path d="M{k} 40V320" stroke="#26180e" stroke-width="3"/>'
    # librería
    b += '<rect x="20" y="40" width="200" height="280" fill="#1a0e08"/>'
    for r in range(5):
        for c in range(9):
            h = 30 + (r*7+c*13) % 14
            b += f'<rect x="{30+c*21}" y="{88+r*52-h}" width="16" height="{h}" fill="{["#5a2a1a","#2a3a4a","#4a4a2a","#3a2a3a"][(r+c)%4]}"/>'
        b += f'<rect x="24" y="{88+r*52}" width="192" height="5" fill="#3a2414"/>'
    # retrato de Don Julián (tapa la caja fuerte)
    b += '<rect x="330" y="60" width="120" height="150" fill="#2a1a0e" stroke="#8a6a2a" stroke-width="6"/><ellipse cx="390" cy="125" rx="32" ry="40" fill="#5a4a3a"/><path d="M360 200q30-40 60 0" fill="#2a2a2a"/><path d="M372 140q18 8 36 0" stroke="#3a2a1a" stroke-width="5"/>'
    # secreter de Leonor (derecha)
    b += '<rect x="560" y="150" width="160" height="200" fill="#4a2a18"/><path d="M560 230h160" stroke="#2a180c" stroke-width="3"/><rect x="574" y="164" width="132" height="56" fill="#3a2014"/><circle cx="640" cy="196" r="7" fill="#c9a24a"/><rect x="637" y="194" width="6" height="10" fill="#1a0e08"/>'
    b += '<rect x="560" y="350" width="10" height="40" fill="#3a2014"/><rect x="710" y="350" width="10" height="40" fill="#3a2014"/>'
    # escritorio de Julián con el bloc, el lápiz y la póliza
    b += '<rect x="180" y="320" width="360" height="22" fill="#5a3a22"/><rect x="190" y="342" width="60" height="140" fill="#3a2414"/><rect x="470" y="342" width="60" height="140" fill="#3a2414"/>'
    b += '<rect x="260" y="300" width="70" height="20" fill="#efe6d0"/><path d="M262 304h66M262 309h50" stroke="#cfc4a8" stroke-width=".8"/><path d="M336 316l40-8" stroke="#c9a24a" stroke-width="3"/>'
    b += '<rect x="400" y="302" width="64" height="18" fill="#e8dcc0" transform="rotate(4 432 311)"/><text x="432" y="313" text-anchor="middle" font-size="4" fill="#2a1d10" font-family="Georgia" transform="rotate(4 432 311)">LA PREVISORA</text>'
    b += '<path d="M490 300v20h14v-20z" fill="#2a2a2a"/><circle cx="497" cy="296" r="70" fill="url(#warm)" opacity=".7"/><path d="M486 300l11-24 11 24z" fill="#6a4a2a"/>'
    # suelo
    b += '<rect y="482" width="800" height="18" fill="#1a0e08"/>'
    if leonor:
        b += '<rect x="740" y="100" width="60" height="390" fill="#c9b48e" opacity=".25"/>'
        b += fig(LEONOR, 760, 488, 1.15)
    b += '<rect width="800" height="500" fill="url(#vig)"/>'
    return wrap(b)
SVG['despacho'] = despacho(); SVG['despachoL'] = despacho(True)

def escritorio():
    b = '<rect width="800" height="500" fill="#4a2e18"/>'
    for k in range(0, 500, 22): b += f'<path d="M0 {k}q400 8 800 0" stroke="#3e2614" stroke-width="2" fill="none"/>'
    b += '<mask id="rubMask"><rect width="800" height="500" fill="#000"/><g id="rubPts"></g></mask>'
    b += '<g transform="rotate(-3 360 250)"><rect x="200" y="60" width="320" height="380" fill="#efe6d0"/><rect x="200" y="60" width="320" height="380" fill="#000" filter="url(#paperT)"/>'
    for k in range(14): b += f'<path d="M214 {100+k*24}H506" stroke="#cfd8e0" stroke-width="1"/>'
    b += '<path d="M236 60V440" stroke="#e0a0a0" stroke-width="1.2"/>'
    b += '<g mask="url(#rubMask)"><rect x="200" y="60" width="320" height="380" fill="#4a4a50"/>'
    for k, t in enumerate(['Esta noche', 'se acaba todo.', 'Que Dios', 'me perdone.']):
        b += f'<text x="360" y="{170+k*58}" text-anchor="middle" font-size="34" fill="#efe6d0" font-family="Georgia" font-style="italic">{t}</text>'
    b += '<text x="440" y="410" text-anchor="middle" font-size="22" fill="#efe6d0" font-family="Georgia" font-style="italic">J.</text></g>'
    b += '<g id="rubFull" opacity="0"><rect x="200" y="60" width="320" height="380" fill="#4a4a50"/>'
    for k, t in enumerate(['Esta noche', 'se acaba todo.', 'Que Dios', 'me perdone.']):
        b += f'<text x="360" y="{170+k*58}" text-anchor="middle" font-size="34" fill="#efe6d0" font-family="Georgia" font-style="italic">{t}</text>'
    b += '<text x="440" y="410" text-anchor="middle" font-size="22" fill="#efe6d0" font-family="Georgia" font-style="italic">J.</text></g></g>'
    # lápiz (se arrastra)
    b += '<g id="lapiz"><g transform="translate(640 330) rotate(-35)"><rect x="-6" y="-110" width="12" height="100" fill="#c9a24a"/><rect x="-6" y="-120" width="12" height="12" fill="#e8a0a0"/><path d="M-6 -10l6 18 6-18z" fill="#e8d0a8"/><path d="M-2 2l2 6 2-6z" fill="#2a2a2a"/></g></g>'
    b += '<rect width="800" height="500" fill="url(#vig)"/>'
    return wrap(b)
SVG['escritorio'] = escritorio()

def secreter(abierto=False):
    b = '<rect width="800" height="500" fill="#2a180c"/>'
    b += '<rect x="120" y="40" width="560" height="420" fill="#4a2a18"/><rect x="150" y="70" width="500" height="360" fill="#3a2014" stroke="#2a180c" stroke-width="6"/>'
    if abierto:
        b += '<rect x="170" y="90" width="460" height="320" fill="#1a0e08"/>'
        b += '<path d="M220 380q0-50 30-60h40q10 30 0 60z" fill="#1a1a1a"/><path d="M300 380q0-50 30-60h40q10 30 0 60z" fill="#1a1a1a"/><path d="M220 372h80M300 372h80" stroke="#6a5a3a" stroke-width="6"/><g fill="#6a5a3a" opacity=".8"><ellipse cx="240" cy="378" rx="10" ry="3"/><ellipse cx="330" cy="379" rx="12" ry="3"/></g>'
        b += '<g transform="rotate(-8 520 250)"><rect x="450" y="200" width="150" height="100" fill="#efe6d0"/>'
        for k, t in enumerate(['FLORISTERÍA LAS DALIAS', 'Servicio nocturno', '30 de noviembre', 'Entrega: 23:00', '1 ramo blanco', 'Cobrado. Gracias.']):
            b += f'<text x="525" y="{218+k*14}" text-anchor="middle" font-size="{8 if k==0 else 6.5}" fill="#2a1d10" font-family="Georgia">{t}</text>'
        b += '</g>'
    else:
        b += '<circle cx="400" cy="250" r="90" fill="url(#warm)" opacity=".5"/>'
    b += '<rect width="800" height="500" fill="url(#vig)"/>'
    return wrap(b)
SVG['secreter'] = secreter(); SVG['secreterA'] = secreter(True)

# ======================= DÍA 5 =======================
G_CRUZ = f'<path d="M0 104q125-30 250 0z" fill="{ink}"/>' + ''.join(f'<rect x="{x-3}" y="{y}" width="6" height="{90-y}" fill="{ink}"/><rect x="{x-12}" y="{y+10}" width="24" height="5" fill="{ink}"/>' for x, y in ((60, 40), (125, 20), (190, 46))) + f'<path d="M100 96q25-10 50 0" stroke="{ink}" stroke-width="4" fill="none"/>'
SVG['periodico5'] = diario('Lunes, 5 de diciembre de 1927', 'ALTAMAR DA HOY SEPULTURA A DON JULIÁN ARRIETA',
  'Entierro a las once en el alto', G_CRUZ,
  ['Toda la familia acompañará al féretro desde','el palacete hasta el cementerio del alto. La','casa quedará cerrada a las visitas hasta la','tarde. El comisario Ibarra asistirá «a título','personal».'],
  'La conservera, todavía parada', G_FABRICA,
  ['Tercera semana de huelga. Los obreros piden','el pago de octubre y noviembre. Nadie de la','familia ha querido decir si la fábrica volverá','a abrir. En el muelle se habla de cerrarla','«para siempre».'],
  [('DISPENSARIO DEL PUERTO', ['Dr. R. Salazar. Consultas de 10 a 13.','Urgencias, a cualquier hora del día o de la noche.']),
   ('CASA DE EMPEÑOS EL MONTE', ['Se presta sobre alhajas, relojes y papeles. Reserva total.'])],
  'ECOS DEL BARRIO',
  ['Doña Puri ha pedido sitio en primera fila para el','entierro. Dice que es «por cercanía». Del sereno y','de la señorita argentina no se sabe si irán.','En el palacete, solo se quedará el servicio.'],
  'Lluvia fina. Viento del noroeste. Pleamar a las 4:10.')

def cocinaP():
    b = '<rect width="800" height="500" fill="#2a2118"/>'
    b += '<rect width="800" height="340" fill="#4a3a2a"/>'
    for y in range(0, 340, 26):
        o = 0 if (y//26) % 2 else 30
        for x in range(-30, 800, 60): b += f'<rect x="{x+o}" y="{y}" width="58" height="24" fill="#54432f" opacity=".55"/>'
    # puerta de servicio (izquierda) y cajas
    b += '<rect x="30" y="110" width="90" height="230" fill="#2a1c10" stroke="#1a1008" stroke-width="5"/><rect x="44" y="126" width="62" height="70" fill="#6a7a82" opacity=".5"/><circle cx="110" cy="230" r="4" fill="#8a7a5a"/>'
    for (x, y) in ((130, 290), (178, 290), (150, 246)):
        b += f'<rect x="{x}" y="{y}" width="46" height="44" fill="#7a5a32" stroke="#4a3418" stroke-width="2"/><text x="{x+23}" y="{y+20}" text-anchor="middle" font-size="5" fill="#2a1c0c" font-family="Georgia">CONSERVAS</text><text x="{x+23}" y="{y+28}" text-anchor="middle" font-size="5" fill="#2a1c0c" font-family="Georgia">ARRIETA</text><text x="{x+23}" y="{y+36}" text-anchor="middle" font-size="3.4" fill="#2a1c0c" font-family="Georgia">envases vacíos</text>'
    # cobres colgados
    b += '<path d="M260 60H520" stroke="#2a1c10" stroke-width="4"/>'
    for k, x in enumerate((280, 330, 385, 440, 495)):
        r = 18 + (k % 3) * 5
        b += f'<path d="M{x} 60v14" stroke="#2a1c10" stroke-width="2"/><circle cx="{x}" cy="{74+r}" r="{r}" fill="#b0643a"/><path d="M{x-r+4} {74+r}a{r-4} {r-4} 0 0 1 {2*r-8} 0" fill="#d4885a" opacity=".6"/>'
    # fogón
    b += '<rect x="250" y="200" width="250" height="140" fill="#1c1c1e"/><rect x="250" y="190" width="250" height="14" fill="#2c2c30"/><rect x="270" y="250" width="70" height="50" fill="#2c2c30"/><rect x="282" y="262" width="46" height="26" fill="#ff8a30" opacity=".85"/><rect x="400" y="250" width="80" height="70" fill="#2c2c30"/>'
    b += '<path d="M300 160h50v32h-50z" fill="#8a8a8a"/><path d="M304 160q21-12 42 0" fill="#9a9a9a"/><path d="M325 150q-8-20 4-40M318 140q-6-14 2-26" stroke="#d8d0c0" stroke-width="5" fill="none" opacity=".35"/>'
    b += '<circle cx="305" cy="275" r="90" fill="url(#warm)" opacity=".7"/>'
    # mesa
    b += '<rect x="420" y="360" width="260" height="16" fill="#6a4a2a"/><rect x="430" y="376" width="14" height="110" fill="#4a3018"/><rect x="656" y="376" width="14" height="110" fill="#4a3018"/>'
    b += '<ellipse cx="480" cy="356" rx="26" ry="6" fill="#d8d0c0"/><path d="M560 356l40-10l6 8l-40 8z" fill="#c9b48e"/><path d="M610 352h30v6h-30z" fill="#8a8680"/>'
    # despensa (derecha, oscura)
    b += '<rect x="620" y="80" width="150" height="260" fill="#0c0906" stroke="#2a1c10" stroke-width="6"/>'
    for k in range(4): b += f'<rect x="628" y="{130+k*52}" width="134" height="5" fill="#1a120a"/>'
    for k in range(4):
        for j in range(5):
            if (k, j) == (3, 3): continue
            b += f'<rect x="{634+j*26}" y="{100+k*52}" width="16" height="30" rx="3" fill="#2a2418"/>'
    # frasquito del dispensario (escondido detrás de los tarros)
    b += '<g><rect x="714" y="270" width="12" height="22" rx="2" fill="#2a3a4a"/><rect x="716" y="264" width="8" height="7" fill="#1a1a1a"/><rect x="715" y="276" width="10" height="9" fill="#d8d0c0"/></g>'
    b += '<rect x="620" y="80" width="150" height="260" fill="#000" opacity=".55"/>'
    # suelo
    b += '<rect y="340" width="800" height="160" fill="#3a2c1e"/>'
    for x in range(0, 800, 50): b += f'<path d="M{x} 340l{(x-400)*.25} 160" stroke="#2a2016" stroke-width="2"/>'
    # Benigna junto al fogón, con la escoba
    b += '<path d="M590 470l-40-200" stroke="#8a6a3a" stroke-width="4"/><path d="M590 470l-14 8 30-4z" fill="#b89a5a"/>'
    b += fig(BENIGNA.replace('<path d="M-16 -104h56" stroke="#8a8a8a" stroke-width="4"/><ellipse cx="22" cy="-106" rx="26" ry="4" fill="#b8b8b8"/><path d="M8 -110v-8h6v8M28 -110v-10h5v10" fill="#e8e2d4"/>', '<path d="M-24 -134q-12 30 -6 60M24 -134q12 30 6 60" stroke="#1e1e24" stroke-width="11" fill="none" stroke-linecap="round"/><circle cx="-30" cy="-74" r="5" fill="url(#skin)"/><circle cx="30" cy="-74" r="5" fill="url(#skin)"/>'), 545, 470, 1.25)
    b += '<rect width="800" height="500" fill="url(#vig)"/>'
    return wrap(b)
SVG['cocinaP'] = cocinaP()

SALAZAR_D = SALAZAR.replace('<ellipse cx="0" cy="-140" rx="19" ry="4" fill="#151515"/>',
  '<path d="M-13 -132q0-6 2-8M13 -132q0-6-2-8" stroke="#b8b4ac" stroke-width="3" fill="none"/><ellipse cx="0" cy="-140" rx="19" ry="4" fill="#151515"/>')  # siempre con su bombín
SALAZAR_D = SALAZAR_D.replace('<rect x="-5" y="-118"', '<path d="M-22 -96q-20 20 -26 54" stroke="#4a4c50" stroke-width="12" fill="none" stroke-linecap="round"/><circle cx="-48" cy="-40" r="5" fill="url(#skin)"/><rect x="-5" y="-118"', 1)
SALAZAR_D = re.sub(r'<g><rect x="52" y="-22".*?</g>', '', SALAZAR_D, flags=re.S)

def dispensario(doctor=True):
    b = '<defs><pattern id="tile" width="24" height="24" patternUnits="userSpaceOnUse"><rect width="24" height="24" fill="#d8d6cc"/><path d="M0 23.5H24M23.5 0V24" stroke="#b8b6aa" stroke-width="1"/></pattern></defs>'
    b += '<rect width="800" height="500" fill="#2a2a28"/><rect width="800" height="350" fill="url(#tile)"/><rect y="330" width="800" height="20" fill="#2a4a4a"/>'
    # diploma
    b += '<rect x="360" y="50" width="90" height="66" fill="#efe6d0" stroke="#4a3a1a" stroke-width="5"/><text x="405" y="72" text-anchor="middle" font-size="6.5" fill="#2a1d10" font-family="Georgia">LICENCIADO EN MEDICINA</text><text x="405" y="86" text-anchor="middle" font-size="5" fill="#2a1d10" font-family="Georgia">Ramón Salazar Ortiz</text><text x="405" y="98" text-anchor="middle" font-size="4.5" fill="#2a1d10" font-family="Georgia">Valladolid, 1901</text><circle cx="430" cy="106" r="5" fill="#a3271c"/>'
    # estantería detrás del mostrador
    for k in range(2):
        y = 150 + k * 60
        b += f'<rect x="300" y="{y+40}" width="250" height="5" fill="#5a4a3a"/>'
        for j in range(9):
            col = ['#7a3a2a', '#2a4a6a', '#5a6a3a', '#8a7a5a'][(j + k) % 4]
            b += f'<rect x="{308+j*27}" y="{y+12}" width="16" height="28" rx="3" fill="{col}" opacity=".85"/><rect x="{310+j*27}" y="{y+22}" width="12" height="8" fill="#efe6d0"/>'
    # armario de cristal (izquierda)
    b += '<rect x="40" y="90" width="170" height="320" fill="#4a3a2a"/><rect x="52" y="102" width="146" height="230" fill="#9aa8a8" opacity=".35"/>'
    for k in range(3): b += f'<rect x="52" y="{170+k*70}" width="146" height="5" fill="#4a3a2a"/>'
    for j in range(6): b += f'<rect x="{60+j*23}" y="{140+(j%2)*4}" width="15" height="28" rx="3" fill="{["#7a3a2a","#2a4a6a","#5a6a3a"][j%3]}"/>'
    b += '<path d="M125 102V332" stroke="#4a3a2a" stroke-width="4"/><circle cx="118" cy="230" r="3" fill="#c9a24a"/><circle cx="132" cy="230" r="3" fill="#c9a24a"/>'
    b += '<rect x="52" y="345" width="146" height="50" fill="#3a2c1e"/><circle cx="125" cy="370" r="3" fill="#c9a24a"/>'
    b += '<path d="M70 110l40 200" stroke="#fff" stroke-width="6" opacity=".15"/>'
    # perchero con el impermeable de mar (derecha)
    b += '<path d="M700 470V110" stroke="#3a2a1a" stroke-width="7"/><path d="M670 120h60" stroke="#3a2a1a" stroke-width="5"/><path d="M680 470h40" stroke="#3a2a1a" stroke-width="8"/>'
    b += '<path d="M686 124q-30 10-34 60l-10 170h104l-10-170q-4-50-34-60z" fill="#3a4a2a"/><path d="M700 126v228" stroke="#2a3820" stroke-width="2"/><path d="M660 200q8 40 2 120M740 200q-8 40-2 120" stroke="#4a5a38" stroke-width="3" fill="none" opacity=".7"/>'
    b += '<g fill="#e8e6e0" opacity=".55"><circle cx="664" cy="240" r="1.6"/><circle cx="676" cy="300" r="1.4"/><circle cx="722" cy="260" r="1.6"/><circle cx="732" cy="320" r="1.3"/><circle cx="690" cy="340" r="1.5"/></g>'
    b += '<g fill="#9ab8c8" opacity=".7"><path d="M660 356q2 6 0 8q-2-2 0-8z"/><path d="M700 356q2 6 0 8q-2-2 0-8z"/><path d="M736 356q2 6 0 8q-2-2 0-8z"/></g><ellipse cx="700" cy="470" rx="34" ry="4" fill="#5a6a72" opacity=".5"/>'
    # suelo
    b += '<rect y="350" width="800" height="150" fill="#3a3a36"/>'
    for x in range(0, 900, 60): b += f'<path d="M{x} 350l-60 150" stroke="#2e2e2a" stroke-width="2"/>'
    # doctor
    if doctor: b += fig(SALAZAR_D, 430, 545, 1.9)
    # mostrador
    b += '<rect x="250" y="440" width="340" height="14" fill="#5a4a3a"/><rect x="260" y="454" width="320" height="46" fill="#4a3a2a"/><path d="M260 480h320" stroke="#3a2c1e" stroke-width="3"/>'
    b += '<path d="M300 440v-26h4v26M290 414h24M292 414l-6 12h16zM312 414l-6 12h16z" stroke="#c9a24a" stroke-width="2" fill="#c9a24a" opacity=".85"/>'
    b += '<rect x="500" y="424" width="60" height="16" fill="#2a3a2a"/><rect x="504" y="427" width="52" height="10" fill="#efe6d0"/>'
    b += '<rect width="800" height="500" fill="url(#vig)" opacity=".7"/>'
    return wrap(b)
SVG['dispensario'] = dispensario(); SVG['dispensarioV'] = dispensario(False)

# frascos del armario: (etiqueta, dosis)
FRASCOS = [('Bromuro potásico', '℈ 1'), ('Tint. de valeriana', 'gr. 30'), ('Polvo de quina', 'ʒ 1'),
           ('Bicarbonato', '℈ 4'), ('Ruibarbo', 'ʒ 2'), ('Sal de Epsom', '℥ ½')]
FR_COL = ['#7a3a2a', '#2a4a6a', '#5a6a3a', '#6a4a7a', '#8a6a2a', '#3a6a6a']
def armario():
    b = '<rect width="800" height="500" fill="#1e1a16"/>'
    b += '<rect x="60" y="20" width="620" height="470" fill="#4a3a2a"/><rect x="80" y="40" width="580" height="430" fill="#cfd6d2"/><rect x="80" y="40" width="580" height="430" fill="#000" opacity=".18"/>'
    b += '<rect x="80" y="360" width="580" height="12" fill="#4a3a2a"/><rect x="80" y="150" width="580" height="10" fill="#4a3a2a"/>'
    # tarjeta del doctor
    b += '<g transform="rotate(-2 370 98)"><rect x="240" y="58" width="260" height="78" fill="#efe6d0"/><text x="370" y="82" text-anchor="middle" font-size="15" fill="#2a1d10" font-family="Georgia" font-style="italic">Cada cosa en su sitio:</text><text x="370" y="102" text-anchor="middle" font-size="15" fill="#2a1d10" font-family="Georgia" font-style="italic">de más a menos,</text><text x="370" y="122" text-anchor="middle" font-size="15" fill="#2a1d10" font-family="Georgia" font-style="italic">empezando por la derecha. R. S.</text></g>'
    # selección
    b += '<ellipse class="frSel" cx="0" cy="356" rx="44" ry="10" fill="#ffd27a" opacity="0"/>'
    for k, (nom, dosis) in enumerate(FRASCOS):
        c = FR_COL[k]
        b += f'<g class="fr" data-k="{k}" transform="translate({140+k*92} 0)">'
        b += f'<rect x="-30" y="232" width="60" height="124" rx="10" fill="{c}" opacity=".92"/><rect x="-14" y="212" width="28" height="22" fill="{c}"/><rect x="-17" y="200" width="34" height="14" rx="3" fill="#2a2018"/>'
        b += f'<path d="M-22 244v100" stroke="#fff" stroke-width="5" opacity=".2"/>'
        b += f'<rect x="-27" y="262" width="54" height="66" fill="#efe6d0"/><rect x="-27" y="262" width="54" height="66" fill="none" stroke="#8a6a2a" stroke-width="1.2"/>'
        b += f'<text x="0" y="276" text-anchor="middle" font-size="6.2" fill="#2a1d10" font-family="Georgia">{nom}</text>'
        b += f'<text x="0" y="306" text-anchor="middle" font-size="19" fill="#2a1d10" font-family="Georgia,\'Noto Serif\',serif" font-weight="bold">{dosis}</text>'
        b += f'<text x="0" y="322" text-anchor="middle" font-size="4.2" fill="#2a1d10" font-family="Georgia">Dispensario del Puerto</text></g>'
    # cajón (cerrado / abierto)
    b += '<rect x="80" y="380" width="580" height="80" fill="#3a2c1e"/><rect class="cajonC" x="300" y="396" width="140" height="48" fill="#4a3a2a" stroke="#2a1c10" stroke-width="3"/>'
    b += '<g class="cajonA" opacity="0"><rect x="280" y="400" width="180" height="70" fill="#2a1c10"/><rect x="296" y="404" width="148" height="56" fill="#efe6d0" transform="rotate(-3 370 432)"/><text x="370" y="424" text-anchor="middle" font-size="9" fill="#2a1d10" font-family="Georgia" transform="rotate(-3 370 432)">FICHA CLÍNICA</text><text x="370" y="440" text-anchor="middle" font-size="8" fill="#2a1d10" font-family="Georgia" font-style="italic" transform="rotate(-3 370 432)">Arrieta, Julián</text></g>'
    # receta del doctor (letra pequeña, en el lateral): la clave de las medidas
    b += '<g transform="rotate(2 738 200)"><rect x="688" y="112" width="104" height="176" fill="#efe8d6"/><rect x="688" y="112" width="104" height="176" fill="#000" filter="url(#paperT)"/>'
    b += '<text x="694" y="130" font-size="10" fill="#2a1d10" font-family="Georgia" font-style="italic">Rp/</text><text x="714" y="129" font-size="5.4" fill="#2a1d10" font-family="Georgia" font-style="italic">Jarabe para la tos</text>'
    b += '<path d="M694 136H786" stroke="#8a7a5a" stroke-width=".5"/>'
    for k, (n, m, g) in enumerate([('Regaliz', '℈ 4', '96 gr.'), ('Azúcar', '℥ ½', '288 gr.'), ('Canela', '℈ 1', '24 gr.'), ('Anís', 'ʒ 2', '144 gr.'), ('Limón', 'gr. 30', '30 gr.'), ('Miel', 'ʒ 1', '72 gr.')]):
        y = 152 + k*19
        b += f'<text x="694" y="{y}" font-size="5.6" fill="#2a1d10" font-family="Georgia" font-style="italic">{n}</text><text x="748" y="{y}" text-anchor="middle" font-size="6.4" fill="#2a1d10" font-family="Georgia,\'Noto Serif\',serif">{m}</text><text x="786" y="{y}" text-anchor="end" font-size="5.2" fill="#2a1d10" font-family="Georgia">{g}</text>'
    b += '<text x="786" y="278" text-anchor="end" font-size="6" fill="#2a1d10" font-family="Georgia" font-style="italic">R. S.</text><circle cx="740" cy="116" r="3" fill="#8a1a1a"/></g>'
    b += '<rect width="800" height="500" fill="url(#vig)" opacity=".6"/>'
    return wrap(b)
SVG['armario'] = armario()

if __name__ == '__main__':
    for k, v in SVG.items():
        open(__import__('os').path.join('/tmp', f'{k}.svg'), 'w').write(v)
    print({k: len(v) for k, v in SVG.items()})
