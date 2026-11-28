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
{extra}<linearGradient id="lgR" x1="0" x2="1"><stop offset="0" stop-color="#000" stop-opacity=".5"/><stop offset=".55" stop-color="#000" stop-opacity=".05"/><stop offset=".85" stop-color="#ffcf80" stop-opacity=".08"/><stop offset="1" stop-color="#ffcf80" stop-opacity=".28"/></linearGradient>
<linearGradient id="lgL" x1="1" x2="0"><stop offset="0" stop-color="#000" stop-opacity=".5"/><stop offset=".55" stop-color="#000" stop-opacity=".05"/><stop offset=".85" stop-color="#ffcf80" stop-opacity=".08"/><stop offset="1" stop-color="#ffcf80" stop-opacity=".28"/></linearGradient>
<radialGradient id="hole"><stop offset="0" stop-color="#000"/><stop offset=".55" stop-color="#000" stop-opacity=".85"/><stop offset="1" stop-color="#000" stop-opacity="0"/></radialGradient>
<radialGradient id="fire"><stop offset="0" stop-color="#ffb060" stop-opacity=".95"/><stop offset=".4" stop-color="#ff7a20" stop-opacity=".35"/><stop offset="1" stop-color="#c04000" stop-opacity="0"/></radialGradient>
<radialGradient id="pale"><stop offset="0" stop-color="#fff2c8" stop-opacity=".9"/><stop offset="1" stop-color="#fff2c8" stop-opacity="0"/></radialGradient>
<radialGradient id="cold"><stop offset="0" stop-color="#d8f0e0" stop-opacity=".85"/><stop offset=".4" stop-color="#a8d0c0" stop-opacity=".25"/><stop offset="1" stop-color="#80b0a0" stop-opacity="0"/></radialGradient>
<radialGradient id="redL"><stop offset="0" stop-color="#ff7a68" stop-opacity=".95"/><stop offset=".35" stop-color="#e03a2a" stop-opacity=".35"/><stop offset="1" stop-color="#a01010" stop-opacity="0"/></radialGradient>
<filter id="smoke" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".012 .022" numOctaves="3" seed="11"/><feColorMatrix values="0 0 0 0 .86 0 0 0 0 .8 0 0 0 0 .7 0 0 0 1.4 -.45"/></filter>
<pattern id="rain" width="46" height="70" patternUnits="userSpaceOnUse"><path d="M6 0l-5 16M28 26l-5 16M17 48l-5 16M40 10l-5 16" stroke="#cfdbe0" stroke-width="1" opacity=".22"/></pattern>
<pattern id="plkC" width="52" height="500" patternUnits="userSpaceOnUse"><rect width="52" height="500" fill="#2c1c12"/><rect width="3" height="500" fill="#170e08"/><path d="M16 0q5 120 -2 240q-4 120 2 260" stroke="#22150c" stroke-width="1.3" fill="none"/><circle cx="34" cy="170" r="2.6" fill="#170e08"/></pattern><pattern id="tarC" width="70" height="18" patternUnits="userSpaceOnUse"><rect width="70" height="18" fill="#1e130b"/><path d="M0 17.5H70M35 0V18" stroke="#100a05" stroke-width="1.5"/></pattern><filter id="desA"><feColorMatrix type="saturate" values=".8"/></filter><filter id="blkF"><feColorMatrix values="0 0 0 0 .02 0 0 0 0 .02 0 0 0 0 .03 0 0 0 1 0"/></filter>
<linearGradient id="aitG" gradientUnits="userSpaceOnUse" x1="180" x2="260" y1="0" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#fff" stop-opacity=".5"/></linearGradient><mask id="aitM"><rect x="0" y="0" width="400" height="500" fill="url(#aitG)"/></mask>
</defs>'''

def resp(inner, who=None, x=0):
    d = f' data-who="{who}"' if who else ''
    return f'<g class="resp"{d} style="animation-delay:-{int(x*37)%3000}ms">{inner}</g>'

QUIEN = {'LEONOR':'Doña Leonor','SALAZAR':'Dr. Salazar','SALAZAR_D':'Dr. Salazar','IBARRA':'Comisario Ibarra','GUARDIA':'El guardia','PACO':'Paco',
         'INIGO':'Íñigo Arrieta','CLARA':'Clara Arrieta','BENIGNA':'Benigna','MATEO':'Mateo «el Rubio»','TXOMIN':'Txomin'}
def fig(g, x, y, s=1, flip=False, who=None, cls=''):
    who = who or next((v for k, v in QUIEN.items() if globals().get(k) == g), None)
    g2 = f'<g transform="translate({x} {y}) scale({-s if flip else s} {s})">{resp(g, who, x)}</g>'
    return f'<g class="{cls}">{g2}</g>' if cls else g2

def luz(dk, holes, glows=(), humo=0, lluvia=False, tono=.28):
    """Claroscuro: oscuridad con huecos en las fuentes de luz (la linterna la quita) y halos encima."""
    m=''.join(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="url(#hole)" opacity="{o}"/>' for x,y,rx,ry,o in holes)
    g=''
    if humo: g+=f'<rect width="800" height="330" filter="url(#smoke)" opacity="{humo}" class="ob"/>'
    if lluvia: g+='<rect width="800" height="500" fill="url(#rain)"/>'
    g+=f'<rect width="800" height="500" fill="#0a0705" opacity="{tono}" class="ob"/>'
    g+=f'<mask id="oscuro"><rect width="800" height="500" fill="#fff"/>{m}</mask><rect width="800" height="500" fill="#030201" opacity="{dk}" mask="url(#oscuro)" class="ob"/>'
    for x,y,r,gr,o,core in glows:
        g+=f'<circle cx="{x}" cy="{y}" r="{r}" fill="url(#{gr})" opacity="{o}"/>'+(f'<circle cx="{x}" cy="{y}" r="{core}" fill="url(#{gr})"/>' if core else '')
    return g
VIG='<rect width="800" height="500" fill="url(#vig)"/>'
def conluz(b, *a, **k):
    """Mete la capa de luz justo antes de la viñeta final de la escena."""
    L=luz(*a, **k)
    i=b.rfind(VIG)
    return b[:i]+L+b[i:] if i>=0 else b+L
def wrap(body, extra=''):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" preserveAspectRatio="none">{defs(extra)}{body}</svg>'

# ---------------- Aitor de sereno (figura de aitor.svg, coords 400x500) ----------------
src = open(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'aitor.svg')).read()
i = src.index('<!-- sereno -->'); j = src.index('<rect width="400" height="500" fill="url(#rain)"/>')
AITOR = src[i:j].replace('url(#coat)', 'url(#coatA)').replace('url(#hair)', 'url(#hairA)')
AITOR = AITOR.replace('<rect x="196" y="127" width="18" height="8" rx="1" fill="#c9a24a"/>',
  '<rect x="196" y="127" width="18" height="8" rx="1" fill="#c9a24a"/><text x="205" y="133.6" text-anchor="middle" font-size="4.2" fill="#3a2a10" font-family="Georgia">SERENO 7</text>')

def aitor(x, y, s=1):  # x,y = pies (centro)
    return f'<g transform="translate({x-205*s} {y-462*s}) scale({s})">{resp(AITOR_T, "Aitor", x)}</g>'

# Aitor con los toques del estilo nuevo (color apagado, lado en sombra y media cara)
AITOR_T = f'<g><g filter="url(#desA)">{AITOR}</g><g mask="url(#aitM)"><g filter="url(#blkF)">{AITOR}</g></g><path d="M205 138 A25 30 0 0 1 205 198Z" fill="#000" opacity=".33"/></g>'
import personajes as PJ
def tAit(g): return f'<g><g filter="url(#desA)">{g}</g><g mask="url(#aitM)"><g filter="url(#blkF)">{g}</g></g><path d="M205 138 A25 30 0 0 1 205 198Z" fill="#000" opacity=".33"/></g>'
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
CANDELA_OLD = CANDELA
CANDELA = PJ.NF(PJ.candela)
def candela(x, y, s=1):
    return f'<g transform="translate({x} {y}) scale({s})">{resp(CANDELA, "Candela", x)}</g>'

SVG = {}

# ======================= PERIÓDICO =======================
def periodico():
    b = '<rect width="800" height="500" fill="#0b0908"/>'
    b += '<g class="diarioG"><g transform="rotate(-1.2 400 250)">'
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
    b += '</g></g>'
    return wrap(b)
SVG['periodico'] = periodico()

# ======================= ESTACIÓN DEL TOPO =======================
def topo():
    b = '<linearGradient id="skyT" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#06090c"/><stop offset=".7" stop-color="#1e2428"/><stop offset="1" stop-color="#2c3236"/></linearGradient>'
    b += '<rect width="800" height="500" fill="url(#skyT)"/>'
    # edificios de fondo, con ventanas encendidas sueltas
    for x, w, h in [(0, 150, 270), (140, 120, 310), (470, 130, 290), (590, 210, 250)]:
        b += f'<rect x="{x}" y="{370-h}" width="{w}" height="{h}" fill="#14171a"/><rect x="{x}" y="{370-h}" width="{w}" height="6" fill="#0b0d0f"/>'
        for yy in range(390-h, 340, 34):
            for xx in range(x+14, x+w-14, 26):
                on = (xx*7+yy*3) % 11 < 2 and not (600 < xx < 790)  # nada encendido detrás de Aitor
                b += f'<rect x="{xx}" y="{yy}" width="11" height="16" fill="{"#e8b860" if on else "#0a0c0e"}" opacity="{.75 if on else 1}"/>'
    b += '<rect width="800" height="320" filter="url(#fog)" opacity=".45"/>'
    # cable del trole
    b += '<path d="M0 118L800 104" stroke="#0c0c0c" stroke-width="2"/>'
    # marquesina de hierro del andén
    b += '<path d="M380 92 L800 76 V96 L380 114Z" fill="#191b1d"/><path d="M380 114 L800 96" stroke="#2c2f32" stroke-width="3"/>'
    for x in (430, 600, 770):
        t = 112 - (x-380)*.042
        b += f'<rect x="{x-4}" y="{t}" width="8" height="{372-t}" fill="#111315"/><path d="M{x} {t+24} l-24 -20 M{x} {t+24} l24 -20" stroke="#111315" stroke-width="4"/>'
    # vías y andén (adoquín mojado)
    b += '<rect y="372" width="800" height="128" fill="#121110"/>'
    b += '<rect x="0" y="390" width="800" height="110" fill="url(#cob)" opacity=".55"/>'
    b += '<path d="M0 420H800M0 452H800" stroke="#4a4640" stroke-width="4"/>' + ''.join(f'<rect x="{x}" y="414" width="30" height="44" fill="#1a1612" opacity=".7"/>' for x in range(0, 800, 52))
    b += '<rect x="420" y="360" width="380" height="16" fill="#3a3530"/><path d="M420 360H800" stroke="#6a6258" stroke-width="3"/><rect x="420" y="376" width="380" height="8" fill="#0c0b0a"/>'
    b += '<path d="M440 384h340" stroke="#e8c27a" stroke-width="1.5" opacity=".18"/>'
    # el Topo: tren eléctrico de verdad, a escala de la gente, saliendo del cuadro por la izquierda
    b += '<linearGradient id="carro" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#4a1712"/><stop offset=".5" stop-color="#3a110d"/><stop offset="1" stop-color="#1c0806"/></linearGradient>'
    b += '<g class="a-ralenti">'
    b += '<path d="M150 112 L250 30 M190 112 L250 30" stroke="#0a0a0a" stroke-width="3"/><path d="M236 30h30" stroke="#0a0a0a" stroke-width="4"/>'
    b += '<path d="M-40 128 Q-40 112 -24 110 L360 110 Q384 112 386 136 L392 384 L-40 384Z" fill="url(#carro)"/>'
    b += '<path d="M-40 128 Q-40 112 -24 110 L360 110 Q384 112 386 136" fill="none" stroke="#5a2018" stroke-width="3"/>'
    b += '<rect x="-40" y="110" width="430" height="16" fill="#260a07"/>'
    for k in range(4):
        x = -20 + k*92
        b += f'<rect x="{x}" y="150" width="70" height="96" rx="5" fill="#0c0605"/><rect x="{x+4}" y="154" width="62" height="88" rx="3" fill="#e8b868" opacity=".72"/>'
        b += f'<path d="M{x+4} 196h62" stroke="#3a1a10" stroke-width="3"/>'
        if k in (1, 2): b += f'<path d="M{x+20} 242 q0 -30 14 -34 q14 4 14 34z" fill="#1a0e08" opacity=".75"/><circle cx="{x+34}" cy="200" r="8" fill="#1a0e08" opacity=".75"/>'
    b += '<rect x="352" y="140" width="30" height="210" rx="3" fill="#2a0c08"/><rect x="356" y="150" width="22" height="70" rx="2" fill="#e8b868" opacity=".45"/>'
    b += '<rect x="-40" y="262" width="430" height="7" fill="#7a5a28"/><rect x="-40" y="300" width="430" height="3" fill="#5a4020"/>'
    b += ''.join(f'<circle cx="{x}" cy="282" r="1.6" fill="#140504"/>' for x in range(-30, 386, 18))
    b += '<text x="170" y="292" text-anchor="middle" font-family="Georgia" font-size="16" fill="#b89860" letter-spacing="5" opacity=".85">TOPO</text>'
    b += '<rect x="-40" y="340" width="430" height="44" fill="#120504"/><circle cx="40" cy="388" r="18" fill="#050505"/><circle cx="96" cy="388" r="18" fill="#050505"/><circle cx="250" cy="388" r="18" fill="#050505"/><circle cx="306" cy="388" r="18" fill="#050505"/>'
    b += '<circle cx="372" cy="330" r="7" fill="#ffe0a0"/></g>'
    b += '<rect x="-20" y="392" width="400" height="60" fill="#e8b868" opacity=".08" filter="url(#b5)"/>'
    b += '<g class="a-vapor"><g filter="url(#b5)" opacity=".45"><ellipse cx="120" cy="400" rx="110" ry="24" fill="#a8a6a0"/><ellipse cx="290" cy="394" rx="80" ry="20" fill="#a8a6a0"/></g></g>'
    # letrero esmaltado
    b += '<rect x="540" y="150" width="3" height="40" fill="#111"/><rect x="606" y="150" width="3" height="40" fill="#111"/>'
    b += '<rect x="510" y="120" width="130" height="34" rx="4" fill="#142a40" stroke="#c8c0a8" stroke-width="2"/>'
    b += '<text x="575" y="135" text-anchor="middle" font-family="Georgia" font-size="11" fill="#d8d0b8" letter-spacing="2">TOPO</text>'
    b += '<text x="575" y="148" text-anchor="middle" font-family="Georgia" font-size="6.5" fill="#d8d0b8">Frontera – San Sebastián</text>'
    # farola
    b += '<rect x="780" y="150" width="6" height="214" fill="#0e0c0a"/><path d="M768 150h30l-5 26h-20z" fill="#1c1814"/><rect x="773" y="155" width="20" height="18" fill="#ffd88a"/>'
    # charcos con reflejos
    b += '<ellipse cx="783" cy="440" rx="40" ry="6" fill="#ffd88a" opacity=".16"/><ellipse cx="560" cy="470" rx="70" ry="7" fill="#2a3a44" opacity=".6"/><ellipse cx="560" cy="470" rx="30" ry="3" fill="#ffd88a" opacity=".12"/>'
    b += candela(470, 372, .95)
    b += aitor(690, 374, .74)
    b += '<g class="a-brillo"><circle cx="783" cy="165" r="60" fill="url(#warm)" opacity=".8"/></g>'
    b += '<rect y="380" width="800" height="120" filter="url(#fog)" opacity=".35"/>'
    b += '<rect width="800" height="500" fill="url(#vig)"/>'
    b = conluz(b, .62, [(783,200,130,240,1),(646,290,130,130,1),(180,250,230,190,1),(470,300,120,150,.7)], [(160,200,200,'warm',.25,0),(783,165,110,'warm',.4,0),(646,273,90,'warm',.55,12)], lluvia=True, tono=.15)
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
    return f'<g transform="translate({x-205*s} {y-462*s}) scale({s})">{resp(tAit(AITOR_CASA), "Aitor", x)}</g>'
CANDELA_CASA = _cut(CANDELA_OLD, '<!-- brazo con maleta -->', '<path d="M-24 -184q-10 30-8 70"')
CANDELA_CASA = CANDELA_CASA.replace('<path d="M-24 -184q-10 30-8 70"', '<path d="M24 -184q10 30 8 70" stroke="#7a6c52" stroke-width="13" fill="none" stroke-linecap="round"/><circle cx="32" cy="-112" r="6" fill="url(#skin)"/><path d="M-24 -184q-10 30-8 70"')
CANDELA_CASA = CANDELA_CASA[:CANDELA_CASA.index('<!-- sombrero -->')] + '<path d="M-16 -226q0-20 16-21q16 1 16 21q-6-9-16-10q-10 1-16 10z" fill="#3a281e"/><path d="M0 -247v12" stroke="#22170f" stroke-width="1.2"/></g>'
def candela_casa(x, y, s=1):
    return f'<g transform="translate({x} {y}) scale({s})">{resp(CANDELA_CASA, "Candela", x)}</g>'

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
TXOMIN = PJ.txomin(1)

# ======================= COCINA DE AITOR =======================
def cocina(gente=True, mesa=False):
    # pared de tablones con veta, zócalo y suelo de tarima
    b = '<pattern id="plk" width="52" height="500" patternUnits="userSpaceOnUse"><rect width="52" height="500" fill="#2c1c12"/><rect width="3" height="500" fill="#170e08"/><path d="M16 0q5 120 -2 240q-4 120 2 260" stroke="#22150c" stroke-width="1.3" fill="none"/><circle cx="34" cy="170" r="2.6" fill="#170e08"/><circle cx="26" cy="390" r="2" fill="#170e08"/></pattern>'
    b += '<pattern id="tar" width="70" height="18" patternUnits="userSpaceOnUse"><rect width="70" height="18" fill="#1e130b"/><path d="M0 17.5H70M35 0V18" stroke="#100a05" stroke-width="1.5"/></pattern>'
    b += '<rect width="800" height="500" fill="url(#plk)"/>'
    b += '<rect y="292" width="800" height="48" fill="#22160d"/><path d="M0 292H800" stroke="#120b06" stroke-width="5"/><path d="M0 340H800" stroke="#120b06" stroke-width="3"/>'
    b += '<rect y="340" width="800" height="160" fill="url(#tar)"/>'
    # viga del techo
    b += '<rect y="0" width="800" height="22" fill="#170e08"/><rect y="22" width="800" height="4" fill="#0c0704"/>'
    # ventana al puerto, con lluvia y niebla
    b += '<rect x="548" y="60" width="170" height="170" fill="#0e0907"/><rect x="556" y="68" width="154" height="154" fill="#16222a"/>'
    b += '<path d="M570 222V120M600 222V100M690 222V130" stroke="#0c1216" stroke-width="3"/><path d="M570 130l20 14M600 112l22 18" stroke="#0c1216" stroke-width="1.5"/>'
    b += '<rect x="556" y="68" width="154" height="154" filter="url(#fog)" opacity=".6"/><rect x="556" y="68" width="154" height="154" fill="url(#rain)"/>'
    b += '<path d="M633 68V222M556 145H710" stroke="#0e0907" stroke-width="6"/><rect x="540" y="228" width="186" height="10" fill="#2e1c10"/>'
    b += '<path d="M548 238 q85 30 170 0" fill="#9ab0b8" opacity=".05"/>'
    # tablón de corcho con las cartas
    b += '<rect x="214" y="70" width="170" height="118" rx="3" fill="#5a3e22" stroke="#24160a" stroke-width="5"/>'
    for (x, y, r) in [(232, 84, -6), (282, 80, 4), (334, 88, -3)]:
        b += f'<g transform="rotate({r} {x+20} {y+30})"><rect x="{x}" y="{y}" width="40" height="56" fill="#d8cdb0"/>'
        for l in range(6): b += f'<path d="M{x+5} {y+10+l*7}h{30-(l%3)*6}" stroke="#6a5c48" stroke-width="1.2"/>'
        b += f'<circle cx="{x+20}" cy="{y+4}" r="3" fill="#8a1d14"/></g>'
    b += '<ellipse cx="248" cy="128" rx="9" ry="7" fill="#6a4a2a" opacity=".45"/>'
    b += '<text x="252" y="176" font-size="5" fill="#d8cdb0" font-family="Georgia" opacity=".9">La Plata</text>'
    # estufa de hierro con su tubo
    b += '<rect x="70" y="26" width="30" height="190" fill="#0c0a09"/><rect x="66" y="120" width="38" height="6" fill="#1a1816"/>'
    b += '<rect x="40" y="220" width="160" height="190" rx="6" fill="#121110"/><rect x="40" y="214" width="160" height="12" fill="#22201e"/><path d="M48 230v170" stroke="#1e1c1a" stroke-width="3"/>'
    b += '<rect x="62" y="310" width="70" height="44" rx="4" fill="#ff8a20"/><path class="a-llama" d="M70 350q10-30 20-6q6-24 16 0q8-20 18 4" fill="#ffd27a"/>'
    b += '<rect x="58" y="306" width="78" height="52" rx="4" fill="none" stroke="#2a2622" stroke-width="5"/><path d="M70 306v52M86 306v52M102 306v52M118 306v52" stroke="#2a2622" stroke-width="2" opacity=".7"/>'
    b += '<rect x="150" y="250" width="34" height="140" fill="#1a1816"/>'
    b += '<path d="M40 410 q80 26 160 0" fill="#ff9a30" opacity=".12" filter="url(#b5)"/>'
    # cafetera humeando
    b += '<path d="M90 214l6-34h28l6 34z" fill="#5a5850"/><path d="M130 196q12 2 10 14" stroke="#5a5850" stroke-width="4" fill="none"/>'
    b += '<g class="a-humo"><g filter="url(#b5)" opacity=".55"><ellipse cx="110" cy="160" rx="12" ry="20" fill="#d8d2c6"/><ellipse cx="118" cy="128" rx="10" ry="16" fill="#d8d2c6"/></g></g>'
    # estante con tarros
    b += '<rect x="400" y="96" width="110" height="6" fill="#2e1c10"/>' + ''.join(f'<rect x="{x}" y="{78 if i%2 else 82}" width="14" height="{18 if i%2 else 14}" rx="2" fill="{c}"/>' for i,(x,c) in enumerate(zip(range(408,500,20),['#3a4a3a','#5a3a22','#4a3a2a','#2a3a44','#5a4a2a'])))
    # lámpara colgante sobre la mesa
    b += '<path d="M376 0V150" stroke="#000" stroke-width="2"/><path d="M356 150H396L406 172H346Z" fill="#0e0e0e"/><path d="M356 150H396L398 156H354Z" fill="#5a4a3a"/>'
    # Aitor sentado (detrás de la mesa)
    if gente: b += '<clipPath id="tbl"><rect x="0" y="0" width="800" height="340"/></clipPath>'
    if gente and not mesa: b += f'<g clip-path="url(#tbl)">{aitor_casa(380, 478, .8)}</g>'
    if mesa: b += f'<g clip-path="url(#tbl)">{aitor_casa(318, 478, .8)}<g transform="translate(470 420)">{resp(PJ.NF(PJ.candela_sin), "Candela", 470)}</g></g>'
    # mesa
    b += '<rect x="226" y="330" width="300" height="16" fill="#4a2e18"/><rect x="226" y="346" width="300" height="12" fill="#2a1a0e"/>'
    b += '<rect x="240" y="358" width="12" height="118" fill="#2a1a0e"/><rect x="500" y="358" width="12" height="118" fill="#2a1a0e"/>'
    b += '<ellipse cx="376" cy="476" rx="170" ry="12" fill="#000" opacity=".45"/>'
    # cosas de la mesa
    b += '<ellipse cx="268" cy="328" rx="26" ry="9" fill="#a8763a"/><path d="M250 324q18-8 36 0" stroke="#6a4a2a" stroke-width="1.5" fill="none"/>'
    b += '<path d="M314 316h20l-2 16h-16z" fill="#d8d2c6"/><path d="M334 320q6 2 0 8" stroke="#d8d2c6" stroke-width="2" fill="none"/>'
    b += '<path d="M448 316h20l-2 16h-16z" fill="#d8d2c6"/><path d="M448 320q-6 2 0 8" stroke="#d8d2c6" stroke-width="2" fill="none"/>'
    b += '<g transform="rotate(-4 400 330)"><path d="M366 322h34v14h-34zM400 322h34v14h-34z" fill="#e0d6be" stroke="#6a5a42" stroke-width=".8"/>'
    for l in range(4): b += f'<path d="M370 {325+l*3}h26M404 {325+l*3}h{24-l*3}" stroke="#4a3a2a" stroke-width=".7"/>'
    b += '</g>'
    b += '<circle cx="498" cy="331" r="5" fill="#c9a24a" stroke="#6e5320"/><path d="M495 331h6M498 328v6" stroke="#8a6a2a" stroke-width=".6"/>'
    b += '<text x="498" y="332.4" text-anchor="middle" font-size="1.6" fill="#3a2a10" font-family="Georgia">PortAventura</text>'
    # Candela de pie junto a la ventana
    if gente and not mesa: b += candela(628, 484, .9)
    if mesa: b += '<rect x="556" y="68" width="154" height="154" fill="#0a0e14" opacity=".7"/>'
    # despensa (puerta entreabierta, a oscuras)
    b += '<rect x="716" y="246" width="84" height="232" fill="#0c0806"/>'
    b += '<g class="ol"><path d="M724 280h76M724 330h76" stroke="#5a3a22" stroke-width="5"/><rect x="742" y="258" width="34" height="22" rx="2" fill="#a3271c"/><text x="759" y="272" text-anchor="middle" font-size="6" fill="#f0e0b0" font-family="Georgia">GALLETAS</text>'
    b += '<rect x="732" y="306" width="16" height="24" fill="#6a7a5a"/><rect x="756" y="300" width="14" height="30" fill="#8a6a3a"/></g>'
    b += '<path d="M716 246l-30 10v228l30-6z" fill="#3a2414"/><circle cx="694" cy="370" r="3" fill="#c9a24a"/>'
    b += '<rect x="716" y="246" width="84" height="232" fill="#000" class="ob" opacity=".85"/>'
    if gente: b += f'<g class="txoP" opacity="0"><path d="M800 250L700 500H800z" fill="#ffd28a" opacity=".18"/>{fig(TXOMIN, 760, 430, 1.7)}</g>'
    b += '<rect width="800" height="500" fill="url(#vig)"/>'
    b = conluz(b, .62, [(110,320,230,210,1),(376,250,250,200,1),(633,150,110,110,.5)], [(97,332,170,'fire',.5,0),(376,165,190,'warm',.45,26)], humo=.16, tono=.12)
    return wrap(b)
SVG['cocina'] = cocina(); SVG['cocinaMesa'] = cocina(mesa=True)

# ======================= PORTAL =======================
def portal():
    # escalera de vecinos: pared de cal sucia, desconchones, bombilla pelada
    b = '<rect width="800" height="500" fill="#2a2520"/>'
    b += '<rect x="232" y="0" width="568" height="446" fill="#3a332c"/>'
    b += ''.join(f'<path d="M{x} {y}q{w*.4} -6 {w} 2q-4 {h*.6} -{w*.3} {h}q-{w*.5} 4 -{w*.7} -{h*.4}z" fill="#2c2620" opacity=".35"/>' for x,y,w,h in [(640,90,60,40),(260,300,50,60),(700,330,40,50),(600,40,30,22)])
    b += '<path d="M232 380H800" stroke="#2a241e" stroke-width="2"/><rect x="232" y="380" width="568" height="66" fill="#2e2822"/>'
    b += '<path d="M0 0h230v500H0z" fill="#26201b"/>'
    for k in range(7):
        y = 300 + k*28
        b += f'<rect x="0" y="{y}" width="{230-k*14}" height="28" fill="#3e3832"/><path d="M0 {y}h{230-k*14}" stroke="#5a524a" stroke-width="2"/>'
    b += '<path d="M10 300 L200 250" stroke="#1a1612" stroke-width="5"/>' + ''.join(f'<path d="M{20+i*36} {297-i*9.5}v28" stroke="#1a1612" stroke-width="2"/>' for i in range(5))
    b += '<path d="M232 0V500" stroke="#16120e" stroke-width="6"/>'
    # Aitor bajando, de espaldas, poniéndose la gorra
    b += """<g transform="translate(120 360) scale(.62)">
 <path d="M-40 -150q40-16 80 0l12 170h-104z" fill="#1e2228"/>
 <path d="M40 -146q20 -40 6 -86" stroke="#1e2228" stroke-width="20" fill="none" stroke-linecap="round"/>
 <ellipse cx="0" cy="-185" rx="27" ry="31" fill="#2a2018"/>
 <path d="M-26 -196q26-14 52 0l-2-16q-24-12-48 0z" fill="#14161a"/><path d="M-30 -196q30 6 60 0l-2 6q-28 6-56 0z" fill="#0a0b0d"/>
 <circle cx="44" cy="-232" r="9" fill="#a88470"/>
</g>"""
    # bombilla pelada colgando
    b += '<path d="M455 0V40" stroke="#0a0a0a" stroke-width="2"/><rect x="450" y="40" width="10" height="8" fill="#2a2a2a"/><ellipse cx="455" cy="54" rx="7" ry="9" fill="#ffe8b0"/>'
    # puerta de madera con rendija de luz
    b += '<rect x="330" y="80" width="250" height="360" fill="#2a1a0e" stroke="#120a05" stroke-width="8"/>'
    b += '<rect x="352" y="102" width="206" height="130" fill="none" stroke="#1a1008" stroke-width="5"/><rect x="352" y="256" width="206" height="160" fill="none" stroke="#1a1008" stroke-width="5"/>'
    b += '<path d="M360 110l40 120M500 270l40 130" stroke="#3a2614" stroke-width="2" opacity=".6"/>'
    b += '<circle cx="548" cy="260" r="7" fill="#a88a3a"/><rect x="460" y="196" width="30" height="8" rx="2" fill="#6a5222"/>'
    b += '<rect x="440" y="110" width="30" height="18" fill="#c8bca0"/><text x="455" y="122" text-anchor="middle" font-size="6" fill="#2a2018" font-family="Georgia">2º</text>'
    b += '<rect x="330" y="440" width="250" height="6" fill="#e8d8b0" opacity=".85"/>'
    b += '<rect x="330" y="446" width="250" height="40" fill="#e8d8b0" opacity=".08"/>'
    # suelo de baldosa y felpudo
    b += '<rect y="446" width="800" height="54" fill="#1e1a16"/>' + ''.join(f'<path d="M{x} 446 L{x*1.3-120} 500" stroke="#141210" stroke-width="1.5"/>' for x in range(240,800,40))
    b += '<g class="ol"><path d="M486 456l34-6 6 16-34 6z" fill="#e9dfc7"/><path d="M492 460l20-3M494 465l16-3" stroke="#6a5a42" stroke-width="1"/></g>'
    b += '<rect x="360" y="452" width="190" height="34" rx="3" fill="#6a5030"/>'
    for k in range(18): b += f'<path d="M{366+k*10} 455v28" stroke="#4e3a20" stroke-width="2"/>'
    b += '<rect width="800" height="500" fill="url(#vig)"/>'
    b = conluz(b, .6, [(455,120,260,260,1),(110,330,130,180,.6)], [(455,54,230,'warm',.4,20)], tono=.12)
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
GUARDIA = PJ.NF(PJ.guardia)
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
SALAZAR_OLD = SALAZAR
SALAZAR = PJ.NF(PJ.salazar_k)
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
IBARRA = PJ.NF(PJ.ibarra)
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
LEONOR = PJ.NF(PJ.leonor)
import re as _re
def _muestra(fich, pre):
    t=open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), fich)).read()
    t=t[t.index('>',t.index('<svg'))+1:t.rindex('</svg>')]
    ids=set(_re.findall(r'id="([^"]+)"',t))
    for i in ids:
        t=t.replace(f'id="{i}"',f'id="{pre}{i}"').replace(f'url(#{i})',f'url(#{pre}{i})').replace(f'href="#{i}"',f'href="#{pre}{i}"')
    return t
import os as _os
def faro(leonor=False):
    t=_muestra('muestra_faro.svg','f2')
    # la oscuridad la quita la linterna; huecos para el comisario y Aitor
    t=t.replace('<polygon points="650,62 0,0 0,150"','<ellipse cx="640" cy="410" rx="100" ry="130" fill="url(#f2hole)"/><ellipse cx="150" cy="420" rx="90" ry="110" fill="url(#f2hole)"/><ellipse cx="720" cy="410" rx="90" ry="120" fill="url(#f2hole)"/><polygon points="650,62 0,0 0,150"')
    t=t.replace('opacity=".78" mask="url(#f2dark)"/>','opacity=".78" mask="url(#f2dark)" class="ob"/>')
    # la ficha del Casino en la mano, tapada por las algas (se apartan con el dedo)
    alg='<path d="M300 440 q-8 6 -18 4 q6 6 18 0 q-4 8 -14 10" stroke="#3e5a34" stroke-width="2.5" fill="none"/>'
    assert alg in t
    t=t.replace(alg,'<rect x="290" y="432" width="12" height="9" rx="2" fill="#a3271c"/><text x="296" y="439.4" text-anchor="middle" font-size="5" fill="#f0d8a0" font-family="Georgia">C</text>'
      '<g id="algas"><path d="M276 444q14-22 40-12q-8 8-4 18q-18-6-36-6z" fill="#22381f"/><path d="M280 446q14-12 32-8M286 450q12-5 24-3" stroke="#142a12" stroke-width="3" fill="none"/><path d="M272 438q12-4 22 4" stroke="#2e4a28" stroke-width="5" fill="none"/></g>')
    # huellas de bota en las rocas del primer plano (solo con luz)
    extra='<g class="ol" fill="#0e0c0a" opacity=".85">' + ''.join(f'<ellipse cx="{50+i*26}" cy="{488-i*7}" rx="7" ry="11" transform="rotate(-60 {50+i*26} {488-i*7})"/>' for i in range(5)) + '</g>'
    extra+='<rect x="20" y="440" width="180" height="60" fill="#000" class="ob" opacity=".55"/>'
    # verja con candado, el comisario y Aitor
    extra+='<g stroke="#0a0a0a" stroke-width="3"><path d="M738 352v96M790 352v96"/>' + ''.join(f'<path d="M{x} 362v84"/>' for x in range(748, 790, 9)) + '<path d="M738 364h52M738 440h52"/></g>'
    extra+='<path d="M752 392a6 6 0 1 1 0 .1" fill="none" stroke="#8a6a2a" stroke-width="2.5"/><rect x="746" y="396" width="12" height="10" rx="1" fill="#8a6a2a"/>'
    extra+=fig(IBARRA, 620, 470, .64)
    extra+=aitor(700, 476, .5)
    if leonor:
        # Leonor llega por la izquierda, lejos del doctor (si no, al tocarla se toca a él)
        extra+='<g class="cocheL"><g transform="translate(800 -36) scale(-1 1)"><path d="M720 490h80v-40h-50l-14 18h-16z" fill="#0a0a0a"/><circle cx="738" cy="492" r="9" fill="#030303"/><rect x="756" y="454" width="30" height="14" fill="#2a3a4a" opacity=".6"/><g class="farosL"><path d="M722 476L600 450v50z" fill="#fff3c4" opacity=".22"/><circle cx="723" cy="477" r="4" fill="#fff3c4"/></g></g></g>'
        extra+=fig(LEONOR, 150, 484, .64, cls='leoF')
    t=t.replace('<!-- niebla baja delante -->',extra+'<!-- niebla baja delante -->')
    t=t.replace('<rect width="800" height="500" fill="url(#f2vig)"/>','<circle cx="670" cy="408" r="60" fill="url(#f2warm)" opacity=".6"/><rect width="800" height="500" fill="url(#f2vig)"/>')
    return wrap(t)
SVG['faro'] = faro(); SVG['faroL'] = faro(True)

def trato():
    b = '<rect width="800" height="500" fill="#4a4c50"/>'
    b += '<g filter="url(#b5)" opacity=".7"><path d="M0 300q200-20 400 0t400 0V500H0z" fill="#2a2622"/><path d="M300 320q70-20 150-6l6 18q-80 10-160 2z" fill="#d6d2c6"/><rect x="620" y="60" width="40" height="160" fill="#d8d4cc"/></g>'
    b += '<rect width="800" height="500" filter="url(#fog)" opacity=".5"/>'
    b += fig(LEONOR, 180, 500, 1.9)
    b += f'<g transform="translate({400-205*1.2} {560-462*1.2}) scale(1.2)">{resp(tAit(AITOR_CASA), "Aitor", 400)}</g>'
    b += '<path d="M330 420q-14 6-10 20q14 6 24-2z" fill="#1d2026"/>'
    b += fig(IBARRA, 630, 520, 1.85)
    b += '<rect width="800" height="500" fill="url(#vig)"/>'
    b = conluz(b, .5, [(400,300,380,300,1)])
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
    b = '<rect width="800" height="500" fill="#0b0908"/><g class="diarioG"><g transform="rotate(1 400 250)">'
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
    b += '</g></g>'
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
ESTIBADOR = PJ.NF(PJ.estibador)
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
MATEO = PJ.NF(PJ.mateo)
def est(x, y, s, col, col2, flip=False):
    g = ESTIBADOR.replace('COL2', col2).replace('COL', col)
    return fig(g, x, y, s, flip)

def muelle():
    b = '<linearGradient id="fogsky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1e2428"/><stop offset="1" stop-color="#4a4c4a"/></linearGradient>'
    b += '<rect width="800" height="500" fill="url(#fogsky)"/>'
    # grúas al fondo
    b += '<g fill="none" stroke="#3a3c3e" stroke-width="6"><path d="M90 300V60l140 20M90 120l120 -40"/><path d="M620 300V40l-150 30M620 110l-130-30"/></g><path d="M226 80v80" stroke="#3a3c3e" stroke-width="2"/><path d="M474 70v70" stroke="#3a3c3e" stroke-width="2"/>'
    b += '<path d="M0 236 L110 196 L170 212 L260 176 L340 204 L460 190 L560 172 L680 198 L800 186 V252 H0Z" fill="#141a1e" opacity=".9"/>'
    # agua
    b += '<rect y="250" width="800" height="90" fill="#1a262c"/>'
    b += '<g class="a-agua">'
    for k in range(4): b += f'<path d="M-160 {262+k*20}q40-6 80 0' + 't80 0'*11 + '" stroke="#5a6a72" stroke-width="1.5" fill="none"/>'
    b += '</g>'
    # barcas amarradas (la Gaviota, sin farol)
    def barca(x, col, nombre, farol=True, w=120):
        s = f'<path d="M{x} 270h{w}l-14 22h-{w-28}z" fill="{col}"/><path d="M{x+w/2} 270v-60" stroke="#2a2622" stroke-width="3"/>'
        if farol: s += f'<rect x="{x+w/2-4}" y="206" width="8" height="10" fill="#e8e2d0" stroke="#2a2622"/>'
        else: s += f'<path d="M{x+w/2} 210h6v4" stroke="#2a2622" stroke-width="1.5" fill="none"/>'
        s += f'<text x="{x+w/2}" y="284" text-anchor="middle" font-size="5" fill="#e8e2d0" font-family="Georgia" letter-spacing="1">{nombre}</text>'
        return s
    for k, bc in enumerate([barca(150, '#3a5a6a', 'SAN TELMO'), barca(300, '#f0ece0', 'GAVIOTA', False, 100), barca(440, '#6a3a2a', 'ARANTZAZU')]):
        b += f'<g class="a-barca" style="animation-delay:-{k*1.3}s">{bc}</g>'
    b += '<g class="a-gaviota"><path d="M0 0q7-7 14 0q7-7 14 0" stroke="#2a2a2a" stroke-width="2.2" fill="none"/></g>'
    b += '<path d="M330 270q-10 20-24 30" stroke="#2a2622" stroke-width="1.5" fill="none"/>'
    # muelle
    b += '<rect y="320" width="800" height="180" fill="#2a2724"/><rect y="330" width="800" height="170" fill="url(#cob)" opacity=".35"/><path d="M0 320H800" stroke="#2a2622" stroke-width="5"/>'
    for k in range(0, 800, 60): b += f'<path d="M{k} 320v180" stroke="#4a463f" stroke-width="2"/>'
    b += '<rect x="250" y="310" width="16" height="18" rx="4" fill="#2a2622"/><rect x="540" y="310" width="16" height="18" rx="4" fill="#2a2622"/>'
    b += ''.join(f'<path d="M{x} 320 L{x*1.4-160} 500" stroke="#1a1816" stroke-width="2"/>' for x in range(0,800,70))
    b += '<path d="M258 318 q30 30 80 26 M548 318 q-20 40 -70 30" stroke="#4a3a24" stroke-width="3" fill="none"/>'
    b += '<ellipse cx="330" cy="470" rx="70" ry="6" fill="#3a4a52" opacity=".5"/><ellipse cx="690" cy="440" rx="50" ry="5" fill="#3a4a52" opacity=".5"/><rect width="800" height="500" fill="url(#rain)" opacity=".5"/>'
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
    b += '<rect width="800" height="300" filter="url(#fog)" opacity=".35"/>'
    b += '<rect width="800" height="500" fill="url(#vig)"/>'
    b = conluz(b, .42, [(400,390,460,200,1),(700,270,120,120,.6)], tono=.1)
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
 <path d="M44 -100q18 20 14 54" stroke="#3a2c24" stroke-width="18" fill="none" stroke-linecap="round"/><g class="a-vaso"><path d="M50 -66h18l-2 22h-14z" fill="#d8e4e0" opacity=".75"/><path d="M46 -52q12-10 26 -2l-4 10q-10-6-20 2z" fill="#e8e2d4"/></g><circle cx="58" cy="-44" r="9" fill="url(#skin)"/>
 <rect x="-9" y="-146" width="18" height="18" fill="#c9a084"/>
 <ellipse cx="0" cy="-162" rx="22" ry="24" fill="url(#skin)"/>
 <path d="M-22 -168q2 -18 22-18q20 0 22 18q-4-8-22-9q-18 1-22 9z" fill="#d8b89a" opacity=".6"/>
 <path d="M-24 -160q-4 8 0 16M24 -160q4 8 0 16" stroke="#5a4a3a" stroke-width="4" fill="none"/>
 <circle cx="-8" cy="-164" r="2.4" fill="#2a2018"/><circle cx="8" cy="-164" r="2.4" fill="#2a2018"/>
 <path d="M-18 -152q18-12 36 0q-9 8-18 4q-9 4-18-4z" fill="#3a2e26"/>
 <path d="M-8 -142q8 3 16 0" stroke="#7a4f3f" stroke-width="1.6" fill="none"/>
</g>"""
PACO = PJ.NF(PJ.paco)
def taberna():
    t=_muestra('muestra_bar.svg','t2')
    # pizarra de fiados en lugar del menú
    i=t.index('<g fill="#d6d6cc" font-family="Georgia,serif" font-size="11">');j=t.index('</g>',i)+4
    fi='<text x="245" y="128" text-anchor="middle" font-size="9" fill="#e2e0d6" font-family="Special Elite,Courier New">FIADOS</text>'
    for k,x in enumerate(['Koldo ... 4 sidras','Mateo ... 2 sidras (30-XI)','Patxi ... 1 txakoli','Bixente ... 6 sidras (!)']):
        fi+=f'<text x="200" y="{142+k*11}" font-size="6.4" fill="#e2e0d6" font-family="Special Elite,Courier New">{x}</text>'
    t=t[:i]+fi+t[j:]
    # diana en la pared, puerta de la trastienda y la sangre bajo los barriles
    add='<g id="dianaPared" transform="translate(372 108) scale(.72) translate(-650 -150)"><circle cx="650" cy="150" r="40" fill="#141414"/><circle cx="650" cy="150" r="32" fill="#cfc4a8"/><circle cx="650" cy="150" r="22" fill="#222"/><circle cx="650" cy="150" r="12" fill="#8a1d14"/><circle cx="650" cy="150" r="4" fill="#2a6a3a"/><path d="M640 132l-14-10M664 160l14 6M650 140l2-16" stroke="#c9a24a" stroke-width="2"/></g>'
    add+='<rect x="764" y="96" width="40" height="182" fill="#160d07" stroke="#0c0703" stroke-width="5"/><circle cx="772" cy="196" r="3" fill="#6a5222"/><text x="783" y="112" text-anchor="middle" font-size="5.5" fill="#8a7a5a" font-family="Georgia">PRIVADO</text>'
    t=t.replace('<!-- maqueta de barco -->',add+'<!-- maqueta de barco -->')
    sangre='<g class="ol"><path d="M20 470l26-30M30 480l10-34" stroke="#5a3a22" stroke-width="5"/><g fill="#5a1410">'+''.join(f'<ellipse cx="{50+i*9}" cy="{462+(i%2)*6}" rx="{3+i%2}" ry="2"/>' for i in range(5))+'</g></g><path d="M0 500V420l110-10v90z" fill="#000" class="ob" opacity=".6"/>'
    t=t.replace('<!-- marinero A (gorra) -->',sangre+'<!-- marinero A (gorra) -->')
    t=t.replace('opacity=".8" mask="url(#t2dark)"/>','opacity=".8" mask="url(#t2dark)" class="ob"/>')
    t=t.replace('<ellipse cx="702" cy="150" rx="90" ry="90" fill="url(#t2hole)" opacity=".7"/>','<ellipse cx="702" cy="150" rx="90" ry="90" fill="url(#t2hole)" opacity=".7"/><ellipse cx="380" cy="120" rx="60" ry="60" fill="url(#t2hole)" opacity=".6"/>')
    return wrap(t)
SVG['taberna'] = taberna()

def diana():
    b = '<rect width="800" height="500" fill="#3a2416"/>'
    for k in range(0, 800, 46): b += f'<path d="M{k} 0V500" stroke="#2e1c10" stroke-width="2"/>'
    # hueco en la pared con el papel (debajo de la diana)
    b += '<rect x="330" y="180" width="140" height="140" fill="#160c06"/><g transform="rotate(-6 400 250)"><rect x="362" y="214" width="76" height="62" fill="#e9dfc7"/><path d="M362 245h76M400 214v62" stroke="#c9bb98"/></g>'
    b += '<g id="diana"><g class="dianaG"><circle cx="400" cy="250" r="170" fill="#121212"/>'
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
    b += '</g></g><path d="M400 76v8" stroke="#8a8a8a" stroke-width="4"/><rect width="800" height="500" fill="url(#vig)"/>'
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
 <path d="M34 -128l16-4" stroke="#e8e2d4" stroke-width="2.5"/><circle class="a-brasa" cx="50" cy="-132" r="1.6" fill="#ff8a3a"/><g class="a-humoC"><path d="M51 -135q-5 -7 1 -14q6 -7 0 -14" stroke="#d8d8d8" stroke-width="1.6" fill="none" opacity=".45"/></g>
 <rect x="-6" y="-192" width="12" height="16" fill="#c9a084"/>
 <ellipse cx="0" cy="-206" rx="15" ry="18" fill="url(#skin)"/>
 <path d="M-16 -210q0-18 16-20q18 2 17 18q-8-12-18-10q-8 2-15 12z" fill="#1a120c"/>
 <circle cx="-5" cy="-206" r="1.8" fill="#2a2018"/><circle cx="6" cy="-206" r="1.8" fill="#2a2018"/>
 <path d="M-5 -196q6 4 11 0" stroke="#7a4f3f" stroke-width="1.4" fill="none"/>
</g>"""
INIGO = PJ.NF(PJ.inigo)
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
CLARA = PJ.NF(PJ.clara_sv)
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
BENIGNA = PJ.NF(PJ.benigna)

def salon():
    b = '<rect width="800" height="500" fill="#2a1418"/>'
    b += '<rect width="800" height="330" fill="#2a1218"/>'
    for k in range(0, 800, 60): b += f'<path d="M{k} 0V330" stroke="#30161c" stroke-width="18" opacity=".5"/>'
    b += '<path d="M0 330H800" stroke="#1a0c0e" stroke-width="6"/>'
    # retratos
    for (x, w) in [(60, 70), (560, 60)]:
        b += f'<rect x="{x}" y="60" width="{w}" height="{w*1.3}" fill="#2a1a0e" stroke="#8a6a2a" stroke-width="5"/><ellipse cx="{x+w/2}" cy="{60+w*.55}" rx="{w*.25}" ry="{w*.32}" fill="#4a3a2a"/>'
    # ventana con cortinas
    b += '<rect x="640" y="50" width="120" height="200" fill="#5a6a72"/><rect x="640" y="50" width="120" height="200" filter="url(#fog)" opacity=".7"/><path d="M630 40q30 120 10 220h-14V40zM770 40q-30 120-10 220h14V40z" fill="#5a1a22"/>'
    # puerta del despacho (izquierda, entreabierta)
    b += '<rect x="170" y="110" width="80" height="220" fill="#1a0e08" stroke="#4a2a14" stroke-width="5"/><circle cx="240" cy="230" r="3" fill="#c9a24a"/><text x="210" y="102" text-anchor="middle" font-size="7" fill="#8a7a5a" font-family="Georgia">DESPACHO</text>'
    b += ''.join(f'<rect x="{x}" y="0" width="14" height="330" fill="#1e0c10" opacity=".6"/>' for x in range(0,800,40))
    b += '<rect y="290" width="800" height="40" fill="#1a0c0a"/><path d="M0 290H800" stroke="#3a2014" stroke-width="3"/>'
    b += '<path d="M420 0V40" stroke="#0a0a0a" stroke-width="2"/><path d="M380 40h80l-10 16h-60z" fill="#3a2a10"/>' + ''.join(f'<path d="M{x} 56 q0 14 -6 18" stroke="#3a2a10" stroke-width="2" fill="none"/><rect x="{x-9}" y="70" width="6" height="10" fill="#cfc4a8" opacity=".6"/>' for x in (396,420,444))
    b += '<g fill="#d8d2c4" opacity=".85">' + ''.join(f'<circle cx="{x}" cy="{y}" r="6"/>' for x,y in [(296,286),(306,280),(316,288),(524,286),(534,280),(544,288)]) + '</g>'
    # ataúd y velas
    b += '<path d="M300 300h220l20 30h-260z" fill="#2a1a10"/><path d="M296 290h228v14H296z" fill="#4a2e18"/><path d="M300 290h220l-10-14H310z" fill="#3a2414"/><path d="M410 278v10M402 283h16" stroke="#c9a24a" stroke-width="2"/>'
    for x in (280, 540):
        b += f'<rect x="{x-3}" y="230" width="6" height="66" fill="#c9a24a"/><rect x="{x-4}" y="212" width="8" height="18" fill="#efe6d0"/><path class="a-llama" d="M{x} 202q5 6 0 10q-5-4 0-10z" fill="#ffd27a"/><g class="a-brillo"><circle cx="{x}" cy="208" r="70" fill="url(#warm)"/></g>'
    # alfombra y suelo
    b += '<rect y="330" width="800" height="170" fill="#2a1a12"/><path d="M120 360h560l40 140H80z" fill="#4a1a1e"/><path d="M140 372h520l34 120H106z" fill="none" stroke="#8a6a2a" stroke-width="2"/>'
    # personajes
    b += fig(LEONOR, 420, 470, 1.05)
    b += fig(INIGO, 680, 470, 1.0)
    b += fig(CLARA, 120, 470, .98)
    b += fig(BENIGNA, 300, 480, .95)
    b += f'<g transform="translate({560-205*.78} {478-462*.78}) scale(.78)">{resp(tAit(AITOR_CASA), "Aitor", 560)}</g>'
    b += '<path d="M548 380q-8 6-4 14l10-2z" fill="#1d2026"/>'
    # platito con horquillas en el velador
    b += '<rect x="752" y="380" width="40" height="6" fill="#4a2e18"/><rect x="768" y="386" width="6" height="90" fill="#4a2e18"/><ellipse cx="772" cy="379" rx="14" ry="4" fill="#d8d0c0"/><path d="M764 377l6-2M770 378l6-3M772 376l4 3" stroke="#3a3a3a" stroke-width="1.2"/>'
    b += '<rect width="800" height="500" fill="url(#vig)"/>'
    b = conluz(b, .6, [(280,240,170,240,1),(540,240,170,240,1),(700,150,100,140,.5)], [(280,215,160,'warm',.5,0),(540,215,160,'warm',.5,0)], humo=.12, tono=.1)
    return wrap(b)
SVG['salon'] = salon()

def despacho(leonor=False, noche=False, inigo=False, abrigo=False):
    b = '<rect width="800" height="500" fill="#20140c"/>'
    b += '<rect width="800" height="320" fill="url(#plkC)"/>'
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
    b += '<rect y="0" width="800" height="18" fill="#120a05"/><path d="M110 500 L170 360 L640 360 L700 500Z" fill="#2a0e10" opacity=".85"/><path d="M130 490 L182 372 L628 372 L682 490Z" fill="none" stroke="#6a4a20" stroke-width="2" opacity=".5"/>'
    b += '<rect x="180" y="320" width="360" height="22" fill="#5a3a22"/><rect x="190" y="342" width="60" height="140" fill="#3a2414"/><rect x="470" y="342" width="60" height="140" fill="#3a2414"/>'
    b += '<rect x="260" y="300" width="70" height="20" fill="#efe6d0"/><path d="M262 304h66M262 309h50" stroke="#cfc4a8" stroke-width=".8"/><path d="M336 316l40-8" stroke="#c9a24a" stroke-width="3"/>'
    b += '<rect x="400" y="302" width="64" height="18" fill="#e8dcc0" transform="rotate(4 432 311)"/><text x="432" y="313" text-anchor="middle" font-size="4" fill="#2a1d10" font-family="Georgia" transform="rotate(4 432 311)">LA PREVISORA</text>'
    b += '<path d="M490 300v20h14v-20z" fill="#2a2a2a"/><g class="a-brillo"><circle cx="497" cy="296" r="70" fill="url(#warm)" opacity=".7"/></g><path d="M486 300l11-24 11 24z" fill="#6a4a2a"/>'
    # suelo
    b += '<rect y="482" width="800" height="18" fill="#1a0e08"/>'
    if noche:
        # inscripción del retrato (letra pequeña)
        b += '<text x="444" y="204" text-anchor="end" font-size="4.6" fill="#c9a24a" font-family="Georgia" font-style="italic">Julián y Leonor · 12 · IV · 1898</text>'
        # reloj de pie, parado
        b += '<rect x="486" y="66" width="56" height="266" fill="#3a2010" stroke="#1e1008" stroke-width="3"/><path d="M482 66h64l-6-12h-52z" fill="#2a160a"/>'
        b += '<circle cx="514" cy="104" r="21" fill="#e8dcc0" stroke="#8a6a2a" stroke-width="3"/><path d="M514 104H499" stroke="#1a1a1a" stroke-width="1.6"/><path d="M514 104L519.5 111.1" stroke="#1a1a1a" stroke-width="2.6"/>'
        b += '<rect x="498" y="142" width="32" height="150" fill="#140a04" stroke="#8a6a2a" stroke-width="2"/><path d="M514 146v104" stroke="#c9a24a" stroke-width="2"/><circle cx="514" cy="258" r="9" fill="#c9a24a"/>'
        b += '<g class="ol"><rect x="501" y="196" width="26" height="18" fill="#efe6d0" transform="rotate(-4 514 205)"/><path d="M504 201h20M504 205h16M504 209h18" stroke="#3a2a1a" stroke-width=".8" transform="rotate(-4 514 205)"/></g>'
        # la Biblia familiar, sobre el escritorio
        b += '<rect x="194" y="300" width="56" height="20" rx="2" fill="#2a1408"/><rect x="196" y="300" width="52" height="6" fill="#e8dcc0"/><path d="M222 307v10M217 311h10" stroke="#c9a24a" stroke-width="2"/>'
        # gotas de lacre rojo, secas, del retrato hacia la puerta del pasillo (solo con la linterna)
        b += '<g class="ol" fill="#8a1a1a">' + ''.join(f'<ellipse cx="{x}" cy="{y}" rx="{r}" ry="{r*.55}"/>' for x, y, r in ((392, 470, 3.2), (468, 474, 2.4), (560, 477, 2.8), (650, 474, 2.2), (722, 478, 2.6))) + '</g>'
        if abrigo:
            # el abrigo de Íñigo, empapado, en el sillón
            b += '<g transform="translate(-75 0)"><path d="M600 400h110v70h-110z" fill="#3a2018"/><path d="M594 380h16v90h-16zM700 380h16v90h-16z" fill="#2a160e"/>'
            b += '<path d="M610 384q40-14 84 2l6 70q-48 8-96-2z" fill="#2c2c36"/><path d="M640 392l14 50M664 392l-8 52" stroke="#16161c" stroke-width="3"/><path d="M676 420h16v12h-16z" fill="#1a1a20"/><g class="ol"><path d="M679 422l12-14 8 6-10 12z" fill="#e8dcc0"/><path d="M683 418l8-8" stroke="#8a7a5a" stroke-width=".8"/></g>'
            b += '<g fill="#7a9ab0" opacity=".7"><circle cx="630" cy="458" r="1.6"/><circle cx="672" cy="461" r="1.4"/></g></g>'
        if not inigo:
            # Clara con una vela
            b += fig(CLARA, 735, 488, 1.12)
            b += '<rect x="764" y="380" width="5" height="16" fill="#efe6d0"/><path class="a-llama" d="M766 372q4 5 0 8q-4-3 0-8z" fill="#ffd27a"/><g class="a-brillo"><circle cx="766" cy="378" r="90" fill="url(#warm)" opacity=".8"/></g>'
        else:
            b += '<rect class="luzI" x="740" y="100" width="60" height="390" fill="#c9b48e" opacity=".22"/>'
            b += fig(INIGO, 752, 488, 1.12, cls='borracho')
            b += '<path d="M0 0h70q-20 140 0 500H0z" fill="#3a0e12"/><path d="M60 0q-16 140 4 500" stroke="#2a080c" stroke-width="6" fill="none"/>'
        b += '<rect width="800" height="500" fill="#05070c" opacity=".45"/>'
    if leonor:
        b += '<rect class="luzL" x="740" y="100" width="60" height="390" fill="#c9b48e" opacity=".25"/>'
        b += fig(LEONOR, 760, 488, 1.15, cls='leoD')
    b += '<rect width="800" height="500" fill="url(#vig)"/>'
    b = conluz(b, (.4 if noche else .55), [(497,296,210,190,1),(390,130,150,160,.5)], [(497,296,150,'warm',.45,0)], tono=.1)
    return wrap(b)
SVG['despacho'] = despacho(); SVG['despachoL'] = despacho(True)
SVG['despachoN'] = despacho(noche=True); SVG['despachoI'] = despacho(noche=True, inigo=True); SVG['despachoNA'] = despacho(noche=True, abrigo=True)

def escritorio():
    b = '<rect width="800" height="500" fill="#4a2e18"/>'
    for k in range(0, 500, 22): b += f'<path d="M0 {k}q400 8 800 0" stroke="#3e2614" stroke-width="2" fill="none"/>'
    b += '<mask id="rubMask"><rect width="800" height="500" fill="#000"/><g id="rubPts"></g></mask>'
    b += '<g transform="rotate(-3 360 250)"><rect x="200" y="60" width="320" height="380" fill="#efe6d0"/><rect x="200" y="60" width="320" height="380" fill="#000" filter="url(#paperT)"/>'
    for k in range(14): b += f'<path d="M214 {100+k*24}H506" stroke="#cfd8e0" stroke-width="1"/>'
    b += '<path d="M236 60V440" stroke="#e0a0a0" stroke-width="1.2"/>'
    b += '<g mask="url(#rubMask)"><rect x="200" y="60" width="320" height="380" fill="#4a4a50"/>'
    b += '<g transform="rotate(-28 435 362)">' + ''.join(f'<text x="435" y="{334+k*20}" text-anchor="middle" font-size="15" fill="#efe6d0" font-family="Georgia" font-style="italic">{t}</text>' for k, t in enumerate(['Esta noche se acaba todo.', 'Que Dios me perdone.', 'J.'])) + '</g></g>'
    b += '<g id="rubFull" opacity="0"><rect x="200" y="60" width="320" height="380" fill="#4a4a50"/>'
    b += '<g transform="rotate(-28 435 362)">' + ''.join(f'<text x="435" y="{334+k*20}" text-anchor="middle" font-size="15" fill="#efe6d0" font-family="Georgia" font-style="italic">{t}</text>' for k, t in enumerate(['Esta noche se acaba todo.', 'Que Dios me perdone.', 'J.'])) + '</g></g></g>'
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
        tapa = '<rect class="tapaS" x="150" y="70" width="500" height="360" fill="#3a2014" stroke="#2a180c" stroke-width="6" opacity="0"/>'
        b += '<path d="M220 380q0-50 30-60h40q10 30 0 60z" fill="#1a1a1a"/><path d="M300 380q0-50 30-60h40q10 30 0 60z" fill="#1a1a1a"/><path d="M220 372h80M300 372h80" stroke="#6a5a3a" stroke-width="6"/><g fill="#6a5a3a" opacity=".8"><ellipse cx="240" cy="378" rx="10" ry="3"/><ellipse cx="330" cy="379" rx="12" ry="3"/></g>'
        b += '<g transform="rotate(-8 520 250)"><rect x="450" y="200" width="150" height="100" fill="#efe6d0"/>'
        for k, t in enumerate(['FLORISTERÍA LAS DALIAS', 'Servicio nocturno', '30 de noviembre', 'Entrega: 23:00', '1 ramo blanco', 'Cobrado. Gracias.']):
            b += f'<text x="525" y="{218+k*14}" text-anchor="middle" font-size="{8 if k==0 else 6.5}" fill="#2a1d10" font-family="Georgia">{t}</text>'
        b += '</g>' + tapa
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
    b += '<rect width="800" height="340" fill="#2e2418"/>'
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
    b += '<rect x="250" y="200" width="250" height="140" fill="#1c1c1e"/><rect x="250" y="190" width="250" height="14" fill="#2c2c30"/><rect x="270" y="250" width="70" height="50" fill="#2c2c30"/><rect class="a-llama" x="282" y="262" width="46" height="26" fill="#ff8a30" opacity=".85"/><rect x="400" y="250" width="80" height="70" fill="#2c2c30"/>'
    b += '<path d="M300 160h50v32h-50z" fill="#8a8a8a"/><path d="M304 160q21-12 42 0" fill="#9a9a9a"/><g class="a-humo"><path d="M325 150q-8-20 4-40M318 140q-6-14 2-26" stroke="#d8d0c0" stroke-width="5" fill="none" opacity=".35"/></g>'
    b += '<g class="a-brillo"><circle cx="305" cy="275" r="90" fill="url(#warm)" opacity=".7"/></g>'
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
    b += fig(who='Benigna', g=PJ.NF(PJ.benigna_base), x=545, y=470, s=1.25)
    # la escoba, delante, en su mano derecha
    # la escoba, delante, agarrada con las dos manos
    b += ('<g class="a-escoba"><path d="M566 300L600 452" stroke="#8a6a3a" stroke-width="5" stroke-linecap="round"/><path d="M588 448h26l10 30h-46z" fill="#b89a5a"/><path d="M584 462h34M582 470h38" stroke="#8a6a3a" stroke-width="1.5"/>'
          '<path d="M515 268Q528 330 571 336M575 268Q600 340 586 394" stroke="#1e1e24" stroke-width="14" fill="none" stroke-linecap="round"/>'
          '<circle cx="574" cy="335" r="7" fill="url(#skin)"/><circle cx="587" cy="395" r="7" fill="url(#skin)"/></g>')
    b += '<rect width="800" height="500" fill="url(#vig)"/>'
    b = conluz(b, .55, [(305,275,230,210,1),(545,330,170,230,1),(75,160,90,120,.6)], [(305,275,170,'fire',.5,0)], humo=.15, tono=.1)
    return wrap(b)
SVG['cocinaP'] = cocinaP()

SALAZAR_D = SALAZAR_OLD.replace('<ellipse cx="0" cy="-140" rx="19" ry="4" fill="#151515"/>',
  '<path d="M-13 -132q0-6 2-8M13 -132q0-6-2-8" stroke="#b8b4ac" stroke-width="3" fill="none"/><ellipse cx="0" cy="-140" rx="19" ry="4" fill="#151515"/>')  # siempre con su bombín
SALAZAR_D = SALAZAR_D.replace('<rect x="-5" y="-118"', '<path d="M-22 -96q-20 20 -26 54" stroke="#4a4c50" stroke-width="12" fill="none" stroke-linecap="round"/><circle cx="-48" cy="-40" r="5" fill="url(#skin)"/><rect x="-5" y="-118"', 1)
SALAZAR_D = re.sub(r'<g><rect x="52" y="-22".*?</g>', '', SALAZAR_D, flags=re.S)
SALAZAR_D = PJ.NF(PJ.salazar)

def dispensario(doctor=True):
    b = '<defs><pattern id="tile" width="24" height="24" patternUnits="userSpaceOnUse"><rect width="24" height="24" fill="#8e948c"/><path d="M0 23.5H24M23.5 0V24" stroke="#b8b6aa" stroke-width="1"/></pattern></defs>'
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
    b += ''.join(f'<g class="a-gota" style="animation-delay:-{d}s"><path d="M{x} 356q2 6 0 8q-2-2 0-8z" fill="#9ab8c8" opacity=".8"/></g>' for x, d in ((660, 0), (700, 1.1), (736, 2.0)))
    b += '<ellipse cx="700" cy="470" rx="34" ry="4" fill="#5a6a72" opacity=".5"/>'
    # suelo
    b += '<rect y="350" width="800" height="150" fill="#1e1e1c"/><path d="M430 0V96" stroke="#000" stroke-width="2"/><path d="M406 96H454L466 118H394Z" fill="#1c2a22"/><path d="M406 96H454L456 102H404Z" fill="#3a5a48"/>'
    for x in range(0, 900, 60): b += f'<path d="M{x} 350l-60 150" stroke="#2e2e2a" stroke-width="2"/>'
    # doctor
    if doctor: b += fig(SALAZAR_D, 430, 545, 1.18, cls='docG')
    b += f'<g class="chaval" opacity="0">{fig(TXOMIN, 770, 330, 1.5)}</g>'
    # mostrador
    b += '<rect x="250" y="440" width="340" height="14" fill="#5a4a3a"/><rect x="260" y="454" width="320" height="46" fill="#4a3a2a"/><path d="M260 480h320" stroke="#3a2c1e" stroke-width="3"/>'
    b += '<path d="M300 440v-26h4v26M290 414h24M292 414l-6 12h16zM312 414l-6 12h16z" stroke="#c9a24a" stroke-width="2" fill="#c9a24a" opacity=".85"/>'
    b += '<rect x="500" y="424" width="60" height="16" fill="#2a3a2a"/><rect x="504" y="427" width="52" height="10" fill="#efe6d0"/>'
    b += '<rect width="800" height="500" fill="url(#vig)" opacity=".7"/>'
    b = conluz(b, .55, [(430,260,310,270,1)], [(430,118,250,'cold',.45,26)], tono=.14)
    return wrap(b)
SVG['dispensario'] = dispensario(); SVG['dispensarioV'] = dispensario(False)

# frascos del armario: (etiqueta, dosis)
# ordenados de menos a más granos (la solución): 36 · 44 · 48 · 57,6 · 96 · 108
FRASCOS = [('Bicarbonato', 'ʒ ½'), ('Ruibarbo', 'gr. 44'), ('Bromuro potásico', '℈ 2'),
           ('Sal de Epsom', '℥ 1/10'), ('Tint. de valeriana', '℈ 4'), ('Polvo de quina', 'ʒ 1½')]
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
        b += f'<g class="fr" data-k="{k}" style="transform:translate({140+k*92}px,0px)">'
        b += f'<rect x="-30" y="232" width="60" height="124" rx="10" fill="{c}" opacity=".92"/><rect x="-14" y="212" width="28" height="22" fill="{c}"/><rect x="-17" y="200" width="34" height="14" rx="3" fill="#2a2018"/>'
        b += f'<path d="M-22 244v100" stroke="#fff" stroke-width="5" opacity=".2"/>'
        b += f'<rect x="-27" y="262" width="54" height="66" fill="#efe6d0"/><rect x="-27" y="262" width="54" height="66" fill="none" stroke="#8a6a2a" stroke-width="1.2"/>'
        b += f'<text x="0" y="276" text-anchor="middle" font-size="6.2" fill="#2a1d10" font-family="Georgia">{nom}</text>'
        b += f'<text x="0" y="306" text-anchor="middle" font-size="{16 if len(dosis)>5 else 19}" fill="#2a1d10" font-family="Georgia,\'Noto Serif\',serif" font-weight="bold">{dosis}</text>'
        b += f'<text x="0" y="322" text-anchor="middle" font-size="4.2" fill="#2a1d10" font-family="Georgia">Dispensario del Puerto</text></g>'
    # cajón (cerrado / abierto)
    b += '<rect x="80" y="380" width="580" height="80" fill="#3a2c1e"/><rect class="cajonC" x="300" y="396" width="140" height="48" fill="#4a3a2a" stroke="#2a1c10" stroke-width="3"/>'
    b += '<g class="cajonA" opacity="0"><rect x="280" y="400" width="180" height="70" fill="#2a1c10"/><rect x="296" y="404" width="148" height="56" fill="#efe6d0" transform="rotate(-3 370 432)"/><text x="370" y="424" text-anchor="middle" font-size="9" fill="#2a1d10" font-family="Georgia" transform="rotate(-3 370 432)">FICHA CLÍNICA</text><text x="370" y="440" text-anchor="middle" font-size="8" fill="#2a1d10" font-family="Georgia" font-style="italic" transform="rotate(-3 370 432)">Arrieta, Julián</text></g>'
    # receta del doctor (letra pequeña, en el lateral): cuánto vale cada medida en granos
    b += '<g transform="rotate(2 738 200)"><rect x="688" y="112" width="104" height="176" fill="#efe8d6"/><rect x="688" y="112" width="104" height="176" fill="#000" filter="url(#paperT)"/>'
    b += '<text x="694" y="130" font-size="10" fill="#2a1d10" font-family="Georgia" font-style="italic">Rp/</text><text x="714" y="129" font-size="5.6" fill="#2a1d10" font-family="Georgia" font-style="italic">Pesas de botica</text>'
    b += '<path d="M694 136H786" stroke="#8a7a5a" stroke-width=".5"/>'
    for k, (m, n, g) in enumerate([('gr.', 'grano', '1 gr.'), ('℈', 'escrúpulo', '24 gr.'), ('ʒ', 'dracma', '72 gr.'), ('℥', 'onza', '576 gr.')]):
        y = 154 + k*22
        b += f'<text x="702" y="{y}" text-anchor="middle" font-size="8" fill="#2a1d10" font-family="Georgia,\'Noto Serif\',serif">{m}</text><text x="716" y="{y}" font-size="5.8" fill="#2a1d10" font-family="Georgia" font-style="italic">1 {n}</text><text x="786" y="{y}" text-anchor="end" font-size="5.6" fill="#2a1d10" font-family="Georgia">= {g}</text>'
    b += '<path d="M694 236H786" stroke="#8a7a5a" stroke-width=".5"/><text x="740" y="250" text-anchor="middle" font-size="5.4" fill="#2a1d10" font-family="Georgia" font-style="italic">½ = media · 1/10 = una décima</text>'
    b += '<text x="786" y="278" text-anchor="end" font-size="6" fill="#2a1d10" font-family="Georgia" font-style="italic">R. S.</text><circle cx="740" cy="116" r="3" fill="#8a1a1a"/></g>'
    b += '<rect width="800" height="500" fill="url(#vig)" opacity=".6"/>'
    return wrap(b)
SVG['armario'] = armario()

# ======================= DÍA 6 =======================
SVG['periodico6'] = diario('Martes, 6 de diciembre de 1927', 'ALTAMAR DESPIDE A DON JULIÁN; EL TESTAMENTO, EN EL AIRE',
  'Medio barrio subió al alto', G_CRUZ,
  ['Medio Altamar subió ayer al cementerio del alto.','Doña Leonor, del brazo de su hijo, no derramó','una lágrima. El comisario Ibarra asistió «a','título personal». Benigna, el ama de llaves,','lloró por todos.'],
  '¿Dónde está el papel nuevo?', G_NOTARIO,
  ['El notario Etxeberria se niega a hablar. En el','muelle se dice que Don Julián dejó un papel','nuevo, guardado «donde nadie mira». Íñigo','Arrieta celebró anoche el duelo en el Casino.','Hasta el amanecer.'],
  [('CASINO DE ALTAMAR', ['Esta noche, baile de invierno.','Ruleta y orquesta hasta el amanecer.']),
   ('RELOJERÍA ETXEBERRIA', ['Se arreglan relojes de pie y de bolsillo. A domicilio.'])],
  'ECOS DEL BARRIO',
  ['La viuda de Arrieta pasará esta noche en casa de','su hermana, en Hondarribia. El palacete queda en','manos del servicio. Doña Puri pregunta: ¿y quién','vigila al heredero?'],
  'Noche cerrada, sin luna. Pleamar a las 4:50.')

def cocinaN():
    b = '<rect width="800" height="500" fill="#14100c"/>'
    b += '<rect width="800" height="340" fill="#241c14"/>'
    for y in range(0, 340, 26):
        o = 0 if (y//26) % 2 else 30
        for x in range(-30, 800, 60): b += f'<rect x="{x+o}" y="{y}" width="58" height="24" fill="#2a2118" opacity=".55"/>'
    b += '<rect x="30" y="110" width="90" height="230" fill="#120c06" stroke="#0a0604" stroke-width="5"/><rect x="44" y="126" width="62" height="70" fill="#1e2a34" opacity=".8"/>'
    b += '<path d="M260 60H520" stroke="#0e0a06" stroke-width="4"/>'
    for k, x in enumerate((280, 330, 385, 440, 495)):
        r = 18 + (k % 3) * 5
        b += f'<path d="M{x} 60v14" stroke="#0e0a06" stroke-width="2"/><circle cx="{x}" cy="{74+r}" r="{r}" fill="#4a2a18"/>'
    b += '<rect x="250" y="200" width="250" height="140" fill="#0e0e10"/><rect x="282" y="262" width="46" height="26" fill="#ff5a20" opacity=".35"/>'
    b += '<rect x="420" y="360" width="260" height="16" fill="#2a1c10"/><rect x="430" y="376" width="14" height="110" fill="#1e140a"/><rect x="656" y="376" width="14" height="110" fill="#1e140a"/>'
    b += '<rect x="620" y="80" width="150" height="260" fill="#060403" stroke="#120c06" stroke-width="6"/>'
    b += '<rect y="340" width="800" height="160" fill="#181209"/>'
    # Clara con una vela, junto a la puerta de servicio
    b += fig(CLARA, 190, 470, 1.15)
    b += '<rect x="219" y="362" width="5" height="16" fill="#efe6d0"/><path class="a-llama" d="M221 354q4 5 0 8q-4-3 0-8z" fill="#ffd27a"/><g class="a-brillo"><circle cx="221" cy="360" r="150" fill="url(#warm)" opacity=".9"/></g>'
    b += '<rect width="800" height="500" fill="url(#vig)"/>'
    b = conluz(b, .6, [(221,360,190,210,1)], [(221,358,150,'warm',.5,0)], tono=.08)
    return wrap(b)
SVG['cocinaN'] = cocinaN()

def cajaF(abierta=False):
    b = '<rect width="800" height="500" fill="#2e1e12"/>'
    for k in range(0, 800, 50): b += f'<path d="M{k} 0V500" stroke="#26180e" stroke-width="3"/>'
    # el retrato apartado a un lado
    b += '<g transform="rotate(-14 120 250)"><rect x="40" y="110" width="150" height="190" fill="#2a1a0e" stroke="#8a6a2a" stroke-width="8"/><ellipse cx="115" cy="190" rx="40" ry="50" fill="#5a4a3a"/></g>'
    b += '<rect x="230" y="70" width="340" height="360" rx="8" fill="#3a3e44" stroke="#1a1c20" stroke-width="8"/>'
    if not abierta:
        b += '<rect x="250" y="90" width="300" height="320" rx="6" fill="#4a5058"/><text x="400" y="124" text-anchor="middle" font-size="11" fill="#c9a24a" font-family="Georgia" letter-spacing="3">CAJAS FUERTES · BILBAO</text>'
        for i in range(3):
            x = 300 + i*100
            b += f'<path d="M{x-18} 176l18-22 18 22z" fill="#c9a24a"/>'
            b += f'<rect x="{x-34}" y="196" width="68" height="56" rx="4" fill="#14161a" stroke="#c9a24a" stroke-width="2"/><text class="cifra" data-i="{i}" x="{x}" y="236" text-anchor="middle" font-size="32" fill="#efe6d0" font-family="Georgia">0</text>'
            b += f'<path d="M{x-18} 272l18 22 18-22z" fill="#c9a24a"/>'
        b += '<circle cx="400" cy="350" r="28" fill="#2a2c30" stroke="#c9a24a" stroke-width="3"/><path d="M400 350h38" stroke="#c9a24a" stroke-width="8" stroke-linecap="round"/>'
    else:
        b += '<rect x="250" y="90" width="300" height="320" fill="#0e0c0a"/><path d="M250 90l-120 30v320l120-30z" fill="#4a5058" stroke="#1a1c20" stroke-width="4"/>'
        b += '<rect x="270" y="300" width="260" height="8" fill="#2a2a2a"/><rect x="290" y="270" width="70" height="30" fill="#6a8a5a"/><rect x="296" y="264" width="70" height="30" fill="#7a9a6a"/>'
        b += '<g transform="rotate(-4 450 250)"><rect x="380" y="190" width="140" height="100" fill="#efe6d0"/><text x="450" y="226" text-anchor="middle" font-size="13" fill="#2a1d10" font-family="Georgia" font-style="italic">Testamento</text><text x="450" y="246" text-anchor="middle" font-size="8" fill="#2a1d10" font-family="Georgia">Julián Arrieta Goñi</text><circle cx="490" cy="272" r="9" fill="#8a1a1a"/></g>'
    b += '<rect width="800" height="500" fill="url(#vig)"/>'
    return wrap(b)
SVG['cajaF'] = cajaF(); SVG['cajaA'] = cajaF(True)

def calle():
    b = '<rect width="800" height="500" fill="#0a0c12"/>'
    # tapia y fachada del palacete
    b += '<rect y="120" width="800" height="300" fill="#1e1c1a"/>'
    for y in range(120, 420, 22):
        o = 0 if (y//22) % 2 else 24
        for x in range(-24, 800, 48): b += f'<rect x="{x+o}" y="{y}" width="46" height="20" fill="#24221f" opacity=".7"/>'
    b += '<path d="M0 120h800" stroke="#121110" stroke-width="8"/>'
    for x in (160, 470): b += f'<rect x="{x}" y="150" width="40" height="60" fill="#14181e"/><rect x="{x+4}" y="154" width="32" height="52" fill="#1e2a36" opacity=".6"/>'
    # puerta de servicio
    b += '<rect x="640" y="250" width="70" height="170" fill="#140c06" stroke="#0a0604" stroke-width="5"/><circle cx="700" cy="340" r="3" fill="#6a5a3a"/><text x="675" y="244" text-anchor="middle" font-size="7" fill="#5a4a3a" font-family="Georgia">SERVICIO</text>'
    # farola de gas
    b += '<rect x="317" y="200" width="6" height="220" fill="#111"/><path d="M308 196h24l-4 22h-16z" fill="#1e1a14"/><rect x="313" y="200" width="14" height="14" fill="#ffd28a"/><g class="a-brillo"><circle cx="320" cy="210" r="120" fill="url(#warm)" opacity=".75"/></g>'
    # calle mojada
    b += '<rect y="420" width="800" height="80" fill="#14161a"/><path d="M0 420h800" stroke="#2a2c30" stroke-width="3"/>'
    b += '<ellipse cx="320" cy="460" rx="70" ry="6" fill="#ffd28a" opacity=".12"/>'
    # el otro sereno, con su farol (lo mueve el guion)
    est_ = ESTIBADOR.replace('COL2', '#2a2e36').replace('COL', '#30343c')
    b += f'<g class="otroS" style="transform:translate(200px,0px)">{fig(est_, 0, 470, 1.4, who="El otro sereno")}<path d="M20 340v14" stroke="#111" stroke-width="2"/><rect x="13" y="354" width="14" height="18" fill="#ffd28a"/><circle cx="20" cy="363" r="80" fill="url(#warm)"/></g>'
    # Aitor esperando en la sombra
    b += '<rect x="0" y="120" width="120" height="380" fill="#000" opacity=".45"/>'
    b += aitor(70, 478, .72)
    b += '<rect width="800" height="500" fill="#05070c" opacity=".35"/><rect width="800" height="500" fill="url(#vig)"/>'
    return wrap(b)
SVG['calle'] = calle()

# ======================= DÍA 7 =======================
OBRERA = """<g>
 <ellipse cx="0" cy="0" rx="28" ry="5" fill="#000" opacity=".4"/>
 <path d="M-24 0q2-96 24-136q22 40 24 136z" fill="COL"/>
 <path d="M-16 -110h32l5 106h-42z" fill="#d8d2c2"/>
 <path d="M-20 -124q-12 26 -2 52M20 -124q12 26 2 52" stroke="COL" stroke-width="10" fill="none" stroke-linecap="round"/><circle cx="-22" cy="-70" r="4.5" fill="url(#skin)"/><circle cx="22" cy="-70" r="4.5" fill="url(#skin)"/>
 <rect x="-4" y="-146" width="8" height="10" fill="#c9a084"/>
 <ellipse cx="0" cy="-156" rx="11" ry="13" fill="url(#skin)"/>
 <path d="M-13 -158q0-16 13-16q13 0 13 16l2 8q-15-8-30 0z" fill="PAN"/>
 <circle cx="-4" cy="-156" r="1.4" fill="#2a2018"/><circle cx="4" cy="-156" r="1.4" fill="#2a2018"/><path d="M-4 -148q4 2 8 0" stroke="#7a4f3f" stroke-width="1.2" fill="none"/>
</g>"""
OBRERA = PJ.NF(PJ.obrera)
def obrera(x, y, s, col, pan, flip=False, who=None):
    return fig(OBRERA.replace('COL', col).replace('PAN', pan), x, y, s, flip, who=who)
REMEDIOS = """<g>
 <ellipse cx="0" cy="0" rx="32" ry="6" fill="#000" opacity=".45"/>
 <path d="M-28 0q0-110 28-160q28 50 28 160z" fill="#1a1a1e"/>
 <path d="M-22 -140q22-12 44 0" stroke="#2a2a30" stroke-width="12" fill="none"/>
 <path d="M-24 -134q-10 30 -2 62M24 -134q10 30 2 62" stroke="#1a1a1e" stroke-width="11" fill="none" stroke-linecap="round"/><circle cx="-26" cy="-72" r="5" fill="url(#skin)"/><circle cx="26" cy="-72" r="5" fill="url(#skin)"/>
 <path d="M26 -70v18" stroke="#8a7a5a" stroke-width="2"/><circle cx="26" cy="-50" r="4" fill="none" stroke="#c9a24a" stroke-width="1.6"/>
 <rect x="-5" y="-170" width="10" height="12" fill="#c9a084"/>
 <ellipse cx="0" cy="-182" rx="13" ry="15" fill="url(#skin)"/>
 <path d="M-14 -186q2-16 14-16q12 0 14 16q-6-8-14-8t-14 8z" fill="#3a3a3a"/><circle cx="0" cy="-200" r="6" fill="#3a3a3a"/>
 <circle cx="-5" cy="-183" r="1.6" fill="#2a2018"/><circle cx="5" cy="-183" r="1.6" fill="#2a2018"/><path d="M-6 -173h12" stroke="#6a3f2f" stroke-width="1.4"/>
 <path d="M-9 -189l6 2M9 -189l-6 2" stroke="#2a2a2a" stroke-width="1.6"/>
</g>"""
REMEDIOS = PJ.NF(PJ.remedios)
G_LATAS = f'<g fill="{ink}">' + ''.join(f'<rect x="{60+c*30+r*15}" y="{76-r*18}" width="26" height="15" rx="3"/>' for r in range(4) for c in range(6) if c < 6-r) + '</g>'
SVG['periodico7'] = diario('Miércoles, 7 de diciembre de 1927', 'LA VIUDA REABRE LA CONSERVERA; EL MUELLE SIGUE PARADO',
  'Las mujeres vuelven a las latas', G_FABRICA,
  ['Doña Leonor Arrieta reabrió ayer la conservera','con las mujeres del barrio. Los estibadores','siguen en huelga y no cargan ni una caja.','La máquina del accidente sigue parada','«hasta nueva orden».'],
  'Latas que nadie carga', G_LATAS,
  ['En el almacén se amontonan las cajas sin','embarcar. «Si no salen esta semana, se','pierde la campaña», dice la encargada,','Doña Remedios. Mateo «el Rubio» responde:','«Antes, que arreglen la máquina».'],
  [('CAFÉ ROYAL', ['Calle del Farol. Esta noche, LOLA y sus «artistas».','Reservados discretos. Hasta el amanecer.']),
   ('ULTRAMARINOS ZABALETA', ['Bacalao, aceite y velas. Se fía a las conserveras.'])],
  'ECOS DEL BARRIO',
  ['A la señorita argentina se la vio ayer de noche','cerca del palacete. Doña Puri no da crédito:','«¿A esas horas? ¿Y sola?». No iba sola: iba','con el sereno. Doña Puri, menos todavía.'],
  'Viento sur. Cielo despejado. Pleamar a las 5:30.')

def conservera():
    b = '<rect width="800" height="500" fill="#1e1e1c"/>'
    b += '<rect width="800" height="330" fill="#2e2e2a"/>'
    for x in range(0, 800, 100): b += f'<path d="M{x} 0V330" stroke="#4a4a44" stroke-width="10"/>'
    b += '<path d="M0 40h800" stroke="#3a3a34" stroke-width="12"/>'
    for x in (120, 360, 600): b += f'<rect x="{x}" y="70" width="90" height="120" fill="#8a9a9a" opacity=".6"/><path d="M{x+45} 70v120M{x} 130h90" stroke="#4a4a44" stroke-width="4"/>'
    # vapor de las calderas
    b += '<g class="a-humo"><g filter="url(#b5)" opacity=".5"><ellipse cx="700" cy="220" rx="60" ry="40" fill="#e8e6e0"/><ellipse cx="660" cy="170" rx="40" ry="30" fill="#e8e6e0"/></g></g>'
    b += '<rect x="650" y="230" width="110" height="110" fill="#2a2a2a"/><rect x="664" y="250" width="80" height="30" fill="#ff8a30" opacity=".6"/>'
    b += '<path d="M0 52H800M0 60H800" stroke="#141412" stroke-width="5"/><path d="M600 60V230" stroke="#141412" stroke-width="8"/>'
    b += ''.join(f'<path d="M{x} 60V214" stroke="#000" stroke-width="2"/><path d="M{x-22} 214H{x+22}L{x+30} 232H{x-30}Z" fill="#1a1c1a"/><ellipse cx="{x}" cy="234" rx="14" ry="5" fill="#ffd98a"/>' for x in (230,440))
    # mesa larga de enlatar
    b += '<rect y="330" width="800" height="170" fill="#262622"/>'
    b += '<rect x="120" y="360" width="460" height="16" fill="#7a6a52"/><rect x="130" y="376" width="12" height="100" fill="#5a4a36"/><rect x="560" y="376" width="12" height="100" fill="#5a4a36"/>'
    for k in range(12): b += f'<rect x="{140+k*36}" y="{348-(k%3)*2}" width="18" height="12" rx="3" fill="#b8bcc0"/>'
    b += '<ellipse cx="230" cy="358" rx="22" ry="5" fill="#9aa8b0"/><path d="M215 356l12-4l8 3" stroke="#6a7a82" stroke-width="2"/>'
    # obreras y la encargada
    b += obrera(210, 470, 1.15, '#4a3a44', '#a3271c')
    b += obrera(330, 472, 1.12, '#2e3a46', '#d8c070', flip=True, who='La obrera charlatana')
    b += obrera(470, 470, 1.15, '#3a4436', '#e8e2d4')
    b += fig(REMEDIOS, 640, 482, 1.12, who='Doña Remedios')
    # Aitor en la puerta
    b += aitor(90, 480, .62)
    b += '<rect width="800" height="500" fill="url(#vig)"/>'
    b = conluz(b, .5, [(705,265,180,180,1),(165,130,110,110,.7),(405,130,110,110,.7),(645,130,110,110,.7),(230,330,170,180,1),(440,330,170,180,1),(400,420,340,120,.7)], [(704,265,150,'fire',.45,0),(230,236,170,'warm',.45,24),(440,236,170,'warm',.45,24)], humo=.2, tono=.1)
    return wrap(b)
SVG['conservera'] = conservera()

# las cajas de latas (puzle): tablero 6x5, casillas de 66
CAJAS = [(2, 0, 2, False), (4, 4, 2, False), (5, 1, 2, False), (0, 5, 2, True), (1, 0, 3, False), (1, 3, 2, True), (0, 2, 2, False), (4, 0, 2, True), (4, 2, 2, False), (2, 2, 2, True), (2, 5, 2, True), (3, 0, 2, False)]
def cajas():
    b = '<rect width="800" height="500" fill="#2e2e2a"/>'
    for x in range(0, 800, 40): b += f'<path d="M{x} 0V500" stroke="#262622" stroke-width="2"/>'
    # la máquina, al fondo a la derecha
    b += '<rect x="600" y="120" width="190" height="200" fill="#3a3e42"/><circle cx="690" cy="200" r="50" fill="#2a2c30" stroke="#5a5e62" stroke-width="6"/><path d="M640 270h100" stroke="#5a5e62" stroke-width="8"/>'
    b += '<text x="695" y="110" text-anchor="middle" font-size="10" fill="#c9a24a" font-family="Georgia" letter-spacing="2">LA MÁQUINA</text>'
    # suelo del tablero y salida
    b += '<rect x="196" y="48" width="404" height="404" fill="#24241f" stroke="#5a4a36" stroke-width="4"/>'
    for r in range(6):
        for c in range(6): b += f'<rect x="{200+c*66}" y="{52+r*66}" width="64" height="64" fill="#2c2c27"/>'
    b += '<path d="M600 184v66" stroke="#2c2c27" stroke-width="8"/><path d="M604 217h-14l8-8M590 217l8 8" stroke="#c9a24a" stroke-width="2" fill="none"/>'
    for i, (r, c, l, v) in enumerate(CAJAS):
        w, h = (64, l*66-2) if v else (l*66-2, 64)
        if i == 0:
            g = f'<rect width="{w}" height="{h}" rx="6" fill="#8a2a20" stroke="#4a1410" stroke-width="3"/><circle cx="20" cy="{h-6}" r="7" fill="#1a1a1a"/><circle cx="{w-20}" cy="{h-6}" r="7" fill="#1a1a1a"/><text x="{w/2}" y="{h/2+4}" text-anchor="middle" font-size="11" fill="#f0e0c0" font-family="Georgia">CARRETILLA</text>'
        else:
            g = f'<rect width="{w}" height="{h}" fill="#8a6a3e" stroke="#4a3418" stroke-width="3"/><path d="M4 4L{w-4} {h-4}M{w-4} 4L4 {h-4}" stroke="#6a4e2a" stroke-width="2"/>'
            g += f'<rect x="{w/2-26}" y="{h/2-9}" width="52" height="18" fill="#c9b48e"/><text x="{w/2}" y="{h/2+4}" text-anchor="middle" font-size="7" fill="#2a1c0c" font-family="Georgia">ARRIETA</text>'
        b += f'<g class="caja" data-i="{i}" style="transform:translate({200+c*66}px,{52+r*66}px)">{g}</g>'
    b += '<rect width="800" height="500" fill="url(#vig)" opacity=".7"/>'
    return wrap(b)
SVG['cajas'] = cajas()

def maquina():
    b = '<rect width="800" height="500" fill="#262624"/>'
    b += '<rect x="160" y="60" width="480" height="330" fill="#3a3e42" stroke="#1a1c1e" stroke-width="6"/>'
    b += '<circle cx="330" cy="200" r="100" fill="#2a2c30" stroke="#5a5e62" stroke-width="10"/>'
    for k in range(12):
        import math
        a = k*30
        b += f'<path d="M{330+70*math.cos(math.radians(a)):.0f} {200+70*math.sin(math.radians(a)):.0f}L{330+100*math.cos(math.radians(a)):.0f} {200+100*math.sin(math.radians(a)):.0f}" stroke="#6a6e72" stroke-width="12"/>'
    b += '<circle cx="330" cy="200" r="20" fill="#5a5e62"/>'
    # donde iba la reja: agujeros de los tornillos, limpios
    b += '<rect x="214" y="84" width="232" height="232" fill="none" stroke="#4a4e52" stroke-width="2" stroke-dasharray="6 6"/>'
    for x, y in ((214, 84), (446, 84), (214, 316), (446, 316)): b += f'<circle cx="{x}" cy="{y}" r="6" fill="#141414"/><circle cx="{x}" cy="{y}" r="9" fill="none" stroke="#c9a24a" stroke-width="1.2" opacity=".6"/>'
    b += '<rect x="500" y="110" width="100" height="160" fill="#2e3236"/><circle cx="550" cy="150" r="16" fill="#8a2a20"/><text x="550" y="200" text-anchor="middle" font-size="9" fill="#c9c4b8" font-family="Georgia">PARADA</text>'
    b += '<rect x="160" y="390" width="480" height="110" fill="#121210"/>'
    # la orden, debajo de la máquina (solo con la linterna)
    b += '<g class="ol"><rect x="450" y="430" width="70" height="40" fill="#e8dcc0" transform="rotate(-6 485 450)"/><path d="M458 440h50M458 448h40M458 456h46" stroke="#3a2a1a" stroke-width="1" transform="rotate(-6 485 450)"/></g>'
    b += '<rect x="160" y="390" width="480" height="110" fill="#000" class="ob" opacity=".6"/>'
    b += '<rect width="800" height="500" fill="url(#vig)"/>'
    b = conluz(b, .45, [(330,200,270,250,1)], tono=.1)
    return wrap(b)
SVG['maquina'] = maquina()

def oficina():
    b = '<rect width="800" height="500" fill="#1e160e"/>'
    b += '<rect width="800" height="320" fill="url(#plkC)"/>'
    b += '<rect x="560" y="60" width="180" height="150" fill="#8a9a9a" opacity=".5"/><path d="M650 60v150M560 135h180" stroke="#3a2e22" stroke-width="6"/>'
    # estante con frascos de matarratas
    b += '<rect x="60" y="80" width="200" height="8" fill="#2a1e14"/>'
    for k in range(5): b += f'<rect x="{74+k*36}" y="44" width="22" height="36" rx="3" fill="#3a5a3a"/><rect x="{76+k*36}" y="56" width="18" height="12" fill="#e8dcc0"/><path d="M{80+k*36} 60h10M{80+k*36} 64h8" stroke="#8a1a1a" stroke-width="1.2"/>'
    b += '<text x="160" y="104" text-anchor="middle" font-size="8" fill="#e8dcc0" font-family="Georgia">VENENO · MATARRATAS</text>'
    b += '<rect y="0" width="800" height="18" fill="#120a05"/><rect x="680" y="230" width="90" height="250" fill="#24180e"/>' + ''.join(f'<rect x="690" y="{y}" width="70" height="48" fill="#2e2012" stroke="#140c06" stroke-width="2"/><rect x="716" y="{y+20}" width="18" height="5" fill="#8a6a2a"/>' for y in (240,296,352,408))
    # mesa con el registro y el libro de envíos
    b += '<rect x="120" y="300" width="520" height="20" fill="#6a4a2a"/><rect x="130" y="320" width="16" height="160" fill="#4a3018"/><rect x="614" y="320" width="16" height="160" fill="#4a3018"/>'
    b += '<g transform="rotate(-3 250 288)"><rect x="180" y="268" width="140" height="36" fill="#e8dcc0"/><path d="M250 268v36" stroke="#a89a7a"/>'
    for k in range(4): b += f'<path d="M186 {276+k*7}h58M256 {276+k*7}h{56-k*8}" stroke="#4a3a2a" stroke-width=".8"/>'
    b += '<text x="215" y="264" text-anchor="middle" font-size="6" fill="#e8dcc0" font-family="Georgia">REGISTRO</text></g>'
    b += '<g transform="rotate(4 470 286)"><rect x="410" y="266" width="120" height="38" fill="#1e2a3a"/><rect x="414" y="270" width="112" height="30" fill="#e8dcc0"/>'
    for k in range(4): b += f'<text x="420" y="{278+k*7}" font-size="5.6" fill="#2a1d10" font-family="Georgia,\'Noto Serif\',serif">{["12-XI ✶◆✶ 40","19-XI ◆◆✶ 38","26-XI ✶✶◆ 44","30-XI ◆✶◆ —"][k]}</text>'
    b += '</g>'
    b += '<path d="M560 300v-30h4v30M548 270h28l-6-10h-16z" fill="#2a2a2a"/><circle cx="562" cy="270" r="60" fill="url(#warm)" opacity=".6"/>'
    b += '<rect y="482" width="800" height="18" fill="#22180e"/>'
    b += '<rect width="800" height="500" fill="url(#vig)"/>'
    b = conluz(b, .6, [(562,280,250,210,1),(650,135,110,90,.5)], [(562,268,190,'warm',.45,0)], tono=.12)
    return wrap(b)
SVG['oficina'] = oficina()

# ======================= DÍA 8 =======================
LOLA = """<g>
 <ellipse cx="0" cy="0" rx="30" ry="6" fill="#000" opacity=".45"/>
 <path d="M-8 0l-4-60h10zM8 0l4-60h-10z" fill="url(#skin)"/>
 <path d="M-26 -50q0-60 12-96h28q12 36 12 96q-26 10-52 0z" fill="#6a1424"/>
 <g fill="#e8c060" opacity=".55">""" + ''.join(f'<circle cx="{x}" cy="{y}" r="1.4"/>' for x in range(-20, 22, 7) for y in range(-140, -56, 9)) + """</g>
 <path d="M-14 -146q14 8 28 0l-2 -10h-24z" fill="#5a1020"/>
 <path d="M-30 -150q30 22 60 0q4 10-4 16q-26 14-52 0q-8-6-4-16z" fill="#f0e8e0" opacity=".9"/>
 <path d="M-16 -150q-14 30 -8 60M16 -150q14 30 8 60" stroke="url(#skin)" stroke-width="8" fill="none" stroke-linecap="round"/>
 <rect x="-4" y="-166" width="8" height="12" fill="#e0b494"/>
 <ellipse cx="0" cy="-180" rx="13" ry="15" fill="url(#skin)"/>
 <path d="M-17 -182q-4-22 17-22q21 0 17 22q-2 12-6 16q2-18-11-22q-13 4-11 22q-4-4-6-16z" fill="#1a0e0a"/>
 <circle cx="-14" cy="-170" r="5" fill="#1a0e0a"/><circle cx="14" cy="-170" r="5" fill="#1a0e0a"/>
 <path d="M8 -200q14-12 20 4q-10-2-16 6z" fill="#d84a6a"/>
 <circle cx="-5" cy="-181" r="1.6" fill="#1a1010"/><circle cx="5" cy="-181" r="1.6" fill="#1a1010"/><path d="M-8 -186l5 1M8 -186l-5 1" stroke="#1a1010" stroke-width="1.2"/>
 <path d="M-4 -172q4 3 8 0" stroke="#b02030" stroke-width="2.4" fill="none" stroke-linecap="round"/><circle cx="-8" cy="-176" r="2.5" fill="#e0707a" opacity=".5"/><circle cx="8" cy="-176" r="2.5" fill="#e0707a" opacity=".5"/>
</g>"""
LOLA = PJ.NF(PJ.lola)
PORTERO = """<g>
 <ellipse cx="0" cy="0" rx="38" ry="7" fill="#000" opacity=".45"/>
 <rect x="-22" y="-80" width="18" height="80" fill="#1a1a1a"/><rect x="4" y="-80" width="18" height="80" fill="#1a1a1a"/>
 <path d="M-40 -80q-4-70 40-90q44 20 40 90z" fill="#2a2a30"/>
 <path d="M-40 -150q-14 40 -6 76M40 -150q14 40 6 76" stroke="#2a2a30" stroke-width="18" fill="none" stroke-linecap="round"/><circle cx="-46" cy="-72" r="9" fill="url(#skin)"/><circle cx="46" cy="-72" r="9" fill="url(#skin)"/>
 <rect x="-8" y="-180" width="16" height="12" fill="#c9a084"/>
 <ellipse cx="0" cy="-194" rx="17" ry="18" fill="url(#skin)"/>
 <path d="M-18 -196q0-20 18-20q18 0 18 20q-4-8-18-8t-18 8z" fill="#1a1a1a"/>
 <circle cx="-6" cy="-194" r="1.8" fill="#1a1010"/><circle cx="6" cy="-194" r="1.8" fill="#1a1010"/><path d="M-11 -200l8 2M11 -200l-8 2" stroke="#1a1010" stroke-width="2.2"/>
 <path d="M-8 -182h16" stroke="#6a3f2f" stroke-width="1.8"/><path d="M-14 -186q14 10 28 0" stroke="#2a1a14" stroke-width="3" fill="none"/>
</g>"""
PORTERO = PJ.NF(PJ.portero)
SVG['periodico8'] = diario('Jueves, 8 de diciembre de 1927', 'INMACULADA: PROCESIÓN SIN HUELGUISTAS Y CON MUCHO FRÍO',
  'Altamar sale a la calle', G_CRUZ,
  ['La procesión de la Inmaculada recorrió ayer','el muelle con más paraguas que velas. Los','estibadores no la siguieron: «La Virgen','no carga cajas, pero nosotros tampoco»,','dijo uno, entre risas.'],
  'El puerto, en un puño', G_LATAS,
  ['El capitán del puerto, Don Fermín Olaso, pide','que se cierre «de una vez» el caso Arrieta:','«Aquí se cayó un hombre, y punto. Lo demás','son ganas de hablar». Ni el comisario Ibarra','le lleva la contraria.'],
  [('CAFÉ ROYAL', ['Calle del Farol. Esta noche y todas las noches,','LOLA canta para usted. Entrada discreta.']),
   ('SASTRERÍA LARRAÑAGA', ['Lutos en veinticuatro horas. Se arreglan gabardinas.'])],
  'ECOS DEL BARRIO',
  ['Un comisario de esta ciudad, cuyo nombre no','diremos, frecuenta últimamente la calle del Farol.','Doña Puri asegura que «por razones de servicio».','Nadie se lo cree, ni ella.'],
  'Frío seco. Luna menguante. Pleamar a las 6:10.')

def calleFarol():
    b = '<defs><radialGradient id="rojo"><stop offset="0" stop-color="#ff3a2a" stop-opacity=".42"/><stop offset=".5" stop-color="#ff3a2a" stop-opacity=".12"/><stop offset="1" stop-color="#ff3a2a" stop-opacity="0"/></radialGradient></defs>'
    b += '<rect width="800" height="500" fill="#0c0a10"/>'
    for x, w, h in ((0, 220, 380), (220, 190, 420), (410, 200, 400), (610, 190, 370)):
        b += f'<rect x="{x}" y="{500-h-80}" width="{w}" height="{h}" fill="#1a1418"/>'
        for k in range(2): b += f'<rect x="{x+30+k*90}" y="{500-h-40}" width="44" height="60" fill="#3a1418" opacity=".8"/><rect x="{x+34+k*90}" y="{500-h-36}" width="36" height="52" fill="#a83a2a" opacity=".35"/>'
    # farolas rojas
    for x in (120, 560):
        b += f'<rect x="{x-3}" y="230" width="6" height="190" fill="#111"/><path d="M{x-12} 222h24l-4 20h-16z" fill="#1e0e0e"/><rect x="{x-7}" y="226" width="14" height="14" fill="#ff5a4a"/>'
        b += f'<g class="a-brillo"><circle cx="{x}" cy="236" r="150" fill="url(#rojo)"/></g>'
    # puerta del Café Royal
    b += '<rect x="300" y="250" width="110" height="170" fill="#ffd28a" opacity=".85"/><rect x="306" y="256" width="98" height="164" fill="#e8a85a" opacity=".5"/>'
    b += '<path d="M290 236h130v14h-130z" fill="#2a0e14"/><text x="355" y="247" text-anchor="middle" font-size="10" fill="#ffd28a" font-family="Georgia" letter-spacing="3">CAFÉ ROYAL</text>'
    b += '<path d="M410 420L520 500H300L300 420z" fill="#ffd28a" opacity=".12"/>'
    # señoritas en el portal (siluetas, fumando)
    for x, f in ((470, False), (520, True)):
        b += f'<g transform="translate({x} 420) scale({-1 if f else 1} 1)"><path d="M-12 0q-2-60 12-96q14 36 12 96z" fill="#2a0e1a"/><circle cx="0" cy="-104" r="9" fill="#1a0e10"/><path d="M6 -98l12-4" stroke="#e8e2d4" stroke-width="1.6"/><circle class="a-brasa" cx="18" cy="-102" r="1.4" fill="#ff8a3a"/></g>'
    b += '<rect y="420" width="800" height="80" fill="#0c0a0e"/><rect y="424" width="800" height="76" fill="url(#cob)" opacity=".3"/><rect x="110" y="424" width="20" height="76" fill="#ff3a2a" opacity=".16" filter="url(#b5)"/><rect x="550" y="424" width="20" height="76" fill="#ff3a2a" opacity=".16" filter="url(#b5)"/><ellipse cx="120" cy="450" rx="60" ry="5" fill="#ff3a2a" opacity=".15"/><ellipse cx="560" cy="452" rx="60" ry="5" fill="#ff3a2a" opacity=".15"/>'
    b += fig(PORTERO, 270, 440, 1.0, who='El portero')
    b += aitor(80, 480, .7)
    b += '<rect width="800" height="500" fill="url(#vig)"/>'
    b = conluz(b, .45, [(120,236,170,230,1),(560,236,170,230,1),(355,330,150,170,1)], lluvia=True, tono=.08)
    return wrap(b)
SVG['calleFarol'] = calleFarol()

def camerino():
    b = '<rect width="800" height="500" fill="#2a1418"/>'
    b += '<rect width="800" height="330" fill="#2a1218"/>'
    for x in range(0, 800, 40): b += f'<path d="M{x} 0V330" stroke="#42202a" stroke-width="14"/>'
    # biombo con vestidos
    b += '<path d="M600 90l60-10v300l-60 10zM660 80l60 10v300l-60-10zM720 90l60-10v300l-60 10z" fill="#4a2a2a" stroke="#2a1416" stroke-width="3"/>'
    b += '<path d="M640 100q20 40 0 160h40q-20-120 0-160z" fill="#b8a040" opacity=".8"/><path d="M730 110q-30 60 10 170" stroke="#f0e8e0" stroke-width="14" fill="none" opacity=".7"/>'
    # espejo con bombillas
    b += '<rect x="250" y="40" width="240" height="190" rx="10" fill="#1a1012" stroke="#c9a24a" stroke-width="6"/><rect x="262" y="52" width="216" height="166" fill="#5a4a52" opacity=".6"/><path d="M280 60l60 150" stroke="#fff" stroke-width="10" opacity=".08"/>'
    for k in range(7): b += f'<circle cx="{262+k*36}" cy="34" r="7" fill="#ffe6a8"/>'
    for k in range(5): b += f'<circle cx="244" cy="{62+k*38}" r="7" fill="#ffe6a8"/><circle cx="496" cy="{62+k*38}" r="7" fill="#ffe6a8"/>'
    b += '<g class="a-brillo"><circle cx="370" cy="140" r="200" fill="url(#warm)" opacity=".55"/></g>'
    # la foto metida en el marco del espejo
    b += '<g transform="rotate(8 455 75)"><rect x="432" y="52" width="46" height="56" fill="#e8dcc0"/><rect x="436" y="56" width="38" height="38" fill="#8a7a6a"/><circle cx="450" cy="70" r="6" fill="#4a3a2a"/><path d="M442 94q8-18 16 0z" fill="#3a2a1a"/><circle cx="462" cy="80" r="4" fill="#4a3a2a"/><path d="M457 94q5-10 10 0z" fill="#5a4a3a"/></g>'
    # el dibujo de la niña
    b += '<g transform="rotate(-4 130 110)"><rect x="80" y="60" width="104" height="96" fill="#f4efe2"/><circle cx="104" cy="82" r="10" fill="#e8c040"/><path d="M120 140v-26l20-16 20 16v26z" fill="none" stroke="#c03030" stroke-width="3"/><path d="M96 150v-18M96 136l-6 6M96 136l6 6M168 150v-24M168 132l-7 7M168 132l7 7M132 150v-12" stroke="#3050a0" stroke-width="2.4"/><circle cx="96" cy="128" r="5" fill="none" stroke="#3050a0" stroke-width="2"/><circle cx="168" cy="122" r="5" fill="none" stroke="#3050a0" stroke-width="2"/><circle cx="132" cy="134" r="4" fill="none" stroke="#3050a0" stroke-width="2"/><circle cx="120" cy="64" r="3" fill="#8a1a1a"/></g>'
    # tocador
    b += '<rect x="220" y="260" width="300" height="20" fill="#5a3020"/><rect x="230" y="280" width="16" height="150" fill="#3a1e14"/><rect x="494" y="280" width="16" height="150" fill="#3a1e14"/>'
    for k, c in enumerate(('#c9a24a', '#d84a6a', '#8ab0c0', '#e8dcc0')): b += f'<rect x="{260+k*28}" y="{240+(k%2)*4}" width="14" height="{20-(k%2)*4}" rx="3" fill="{c}"/>'
    b += '<ellipse cx="420" cy="256" rx="24" ry="6" fill="#e8dcc0"/><circle cx="420" cy="250" r="9" fill="#f4e8d8"/>'
    # papelera debajo del tocador
    b += '<path d="M440 400l8 70h48l8-70z" fill="#2a1812"/><ellipse cx="472" cy="400" rx="32" ry="7" fill="#1a0e0a"/>'
    b += '<g class="ol"><path d="M452 396l10-8 6 6-8 6zM470 392l12-4 2 8-10 2zM486 398l8-6 4 6-8 4z" fill="#e8dcc0"/></g>'
    b += '<rect x="420" y="380" width="110" height="100" fill="#000" class="ob" opacity=".55"/>'
    b += '<rect y="430" width="800" height="70" fill="#1e0e10"/>'
    b += fig(LOLA, 340, 480, 1.45, who='Lola')
    b += '<rect width="800" height="500" fill="url(#vig)"/>'
    b = conluz(b, .55, [(370,160,270,240,1)], [(370,140,200,'warm',.35,0)], tono=.1)
    return wrap(b)
SVG['camerino'] = camerino()

# la carta rota: 8 trozos (4x2) de 90x100; el texto completo va en <defs>
CARTA_TXT = ['Lola:', 'Esta noche se acaba todo. Ya no puedo', 'seguir con esta mentira. Te espero en el', 'faro a la una, para despedirme como Dios', 'manda. Lo de la niña está arreglado: pase', 'lo que pase, no os faltará de nada.', 'J. · 30 de noviembre']
# 15 trozos de la carta (5x3, de 72x66) + 4 trozos de otro papel (la cuenta del café) que no encajan
TROZOS0 = [(10, 10, 1), (600, 10, 2), (240, 290, 3), (90, 22, 0), (700, 120, 1), (520, 335, 2), (10, 104, 3), (430, 296, 1),
           (690, 30, 3), (140, 330, 2), (620, 200, 0), (100, 112, 2), (330, 330, 1), (40, 300, 3), (610, 110, 2),
           (20, 196, 0), (706, 214, 2), (620, 300, 1), (240, 400, 3)]
def carta():
    b = '<rect width="800" height="500" fill="#24141a"/>'
    for x in range(0, 800, 40): b += f'<path d="M{x} 0V500" stroke="#2c1820" stroke-width="10"/>'
    t = '<g id="cartaTxt"><rect width="360" height="198" fill="#efe6d0"/>' + ''.join(f'<path d="M8 {32+k*25}H352" stroke="#c8bca0" stroke-width=".7"/>' for k in range(7)) + '<rect x="6" y="6" width="348" height="186" fill="none" stroke="#a8987a" stroke-width="1"/>'
    for k, l in enumerate(CARTA_TXT):
        fit = '' if k in (0, 6) else ' textLength="334" lengthAdjust="spacingAndGlyphs"'
        t += f'<text x="{14 if k < 6 else 190}" y="{28+k*25}" font-size="{15 if k in (0, 6) else 14}" fill="#1e2a4a" font-family="Georgia" font-style="italic"{fit}>{l}</text>'
    t += '</g>'
    c = '<g id="cuentaTxt"><rect width="288" height="132" fill="#f0e2da"/>'
    for k, l in enumerate(['Café Royal · cuenta n.º 212', '2 copas de anís ........ 1,50', '1 botella de champán .. 12,00', 'Reservado nº 3 · Total 13,50 pts']):
        c += f'<text x="10" y="{26+k*28}" font-size="13" fill="#5a5a5a" font-family="Georgia" textLength="266" lengthAdjust="spacingAndGlyphs">{l}</text>'
    c += '</g>'
    b += f'<defs>{t}{c}<clipPath id="ctz"><rect width="72" height="66"/></clipPath></defs>'
    b += '<rect x="216" y="46" width="368" height="206" fill="none" stroke="#c9a24a" stroke-width="2" stroke-dasharray="8 6" opacity=".6"/>'
    for i, (x, y, r) in enumerate(TROZOS0):
        if i < 15: src, cx, cy, edge = '#cartaTxt', (i % 5)*72, (i//5)*66, '#b8a88a'
        else: src, cx, cy, edge = '#cuentaTxt', ((i-15) % 4)*72, (i % 2)*66, '#c0a8a0'
        b += f'<g class="trozo" data-i="{i}" style="transform:translate({x}px,{y}px) rotate({r*90}deg);transform-origin:36px 33px"><g clip-path="url(#ctz)"><use href="{src}" x="{-cx}" y="{-cy}"/></g><rect width="72" height="66" fill="none" stroke="{edge}" stroke-width="1.5"/></g>'
    b += '<rect width="800" height="500" fill="url(#vig)" opacity=".6"/>'
    return wrap(b)
SVG['carta'] = carta()

if __name__ == '__main__':
    for k, v in SVG.items():
        open(__import__('os').path.join('/tmp', f'{k}.svg'), 'w').write(v)
    print({k: len(v) for k, v in SVG.items()})
