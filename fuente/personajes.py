# Personajes nuevos al estilo del faro y del bar (ta2/fa2)
SK='#c8a089';NK='#b38d77'
def P(d,fill,L,op=1,extra=''):  # forma con sombreado según el lado de la luz
    g='lgR' if L>0 else 'lgL'
    return f'<path d="{d}" fill="{fill}" opacity="{op}" {extra}/><path d="{d}" fill="url(#{g})"/>'
def S(d,col,w,L):  # brazo (trazo) con sombreado
    return f'<path d="{d}" stroke="{col}" stroke-width="{w}" stroke-linecap="round" fill="none"/>'
def head(cx,cy,r,L,op=.38,skin=SK):
    sw=0 if L>0 else 1
    return f'<rect x="{cx-6}" y="{cy+r-4}" width="12" height="12" fill="{NK}"/><circle cx="{cx}" cy="{cy}" r="{r}" fill="{skin}"/><path d="M{cx} {cy-r} A{r} {r} 0 0 {sw} {cx} {cy+r}Z" fill="#000" opacity="{op}"/>'
def legs(c='#15100c',a=-7,b=7,h=44):
    return f'<path d="M{a} 0 V-{h} M{b} 0 V-{h}" stroke="{c}" stroke-width="5"/><path d="M{a-5} 0h8M{b-3} 0h8" stroke="#080605" stroke-width="3"/>'
def shadow(): return '<ellipse rx="34" ry="6" fill="#000" opacity=".6"/>'
def eye(x,y): return f'<circle cx="{x}" cy="{y}" r="1.3" fill="#111"/>'

def candela(L):  # más estirada y fina: cuerpo más estrecho y largo, cabeza 10 más arriba
    s=shadow()+legs('#2a2420',-5,5,48)
    s+=P('M-19 -42 L-16 -114 Q0 -124 16 -114 L19 -42Z','#6e6248',L)
    s+='<path d="M-17 -76h34" stroke="#4e4434" stroke-width="3.5"/><path d="M0 -120 V-42" stroke="#4e4434" stroke-width="1.5"/><path d="M-8 -116 L0 -102 L8 -116" stroke="#4e4434" stroke-width="3" fill="none"/>'
    s+=S('M13 -110 Q23 -86 24 -62','#5e5440',8,L)+f'<circle cx="24" cy="-60" r="4.5" fill="{SK}"/>'
    s+='<rect x="15" y="-56" width="24" height="19" rx="2" fill="#4a2e1a"/><path d="M21 -56v-4h12v4" stroke="#2a1a0e" stroke-width="2" fill="none"/>'
    s+=S('M-13 -110 Q-21 -86 -19 -64','#5e5440',8,L)+f'<circle cx="-19" cy="-62" r="4.5" fill="{SK}"/>'
    s+='<g transform="translate(0 -10)">'
    s+='<path d="M-14 -134 Q-17 -108 -15 -92 Q-10 -90 -8 -96 L-8 -128Z M14 -134 Q17 -108 15 -92 Q10 -90 8 -96 L8 -128Z" fill="#2e1e14"/>'
    s+=head(0,-128,12,L)+eye(-4,-129)+eye(4,-129)+'<path d="M-3 -121 Q1 -119 4 -121" stroke="#8a4a3a" stroke-width="1.4" fill="none"/>'
    s+='<path d="M-12 -134 Q-11 -143 0 -143 Q11 -143 12 -134 Q2 -139 -12 -134Z" fill="#2e1e14"/>'
    s+='<ellipse cx="0" cy="-140" rx="19" ry="4.5" fill="#2a2420"/><path d="M-11 -141 Q-11 -155 0 -155 Q11 -155 11 -141Z" fill="#3a322b"/><path d="M-11 -145h22" stroke="#7a2018" stroke-width="3"/>'
    s+='</g>'
    return s
def aitor(L):
    s=shadow()+legs('#121418',-8,8,40)
    s+=P('M-30 0 Q-30 -60 -24 -104 Q0 -118 24 -104 Q30 -60 30 0Z','#232a33',L)
    s+='<g stroke="#14181d" stroke-width="1.4" fill="none"><path d="M-14 -92 Q-18 -40 -16 0M12 -92 Q16 -40 14 0"/></g><path d="M-27 -58h54" stroke="#1a130d" stroke-width="5"/>'
    s+='<circle cx="-2" cy="-96" r="2" fill="#c9a24a"/><circle cx="-2" cy="-82" r="2" fill="#c9a24a"/><circle cx="-2" cy="-70" r="2" fill="#c9a24a"/>'
    s+='<circle cx="16" cy="-50" r="5" fill="none" stroke="#c9a24a" stroke-width="1.6"/><path d="M14 -46l-2 8M18 -46l2 8" stroke="#c9a24a" stroke-width="1.6"/>'
    s+='<path d="M-38 -150 V0" stroke="#2a1d12" stroke-width="3.5"/><path d="M-41 -150l3 -14 3 14z" fill="#8d8a80"/>'
    s+=S('M-22 -98 Q-38 -84 -38 -64','#232a33',10,L)+f'<circle cx="-38" cy="-62" r="5.5" fill="{SK}"/>'
    s+=S('M22 -98 Q40 -82 44 -60','#232a33',10,L)+'<path d="M44 -60v8" stroke="#111" stroke-width="2"/><rect x="36" y="-52" width="16" height="22" rx="3" fill="#ffe3a0"/><path d="M36 -52h16M36 -30h16M44 -52v22" stroke="#111" stroke-width="2.5"/>'
    s+=head(0,-132,14,L)
    s+='<path d="M-14 -130 Q-14 -112 0 -110 Q14 -112 14 -130 Q8 -122 0 -123 Q-8 -122 -14 -130Z" fill="#7a736a"/><path d="M-6 -122 Q0 -119 6 -122" stroke="#4a423b" stroke-width="3" fill="none"/>'+eye(-5,-136)+eye(5,-136)
    s+='<path d="M-17 -140 Q-24 -134 -20 -126M17 -140 Q24 -134 20 -126" stroke="#4a3a2e" stroke-width="3" fill="none"/>'
    s+='<path d="M-16 -142 Q-16 -158 0 -158 Q16 -158 16 -142Z" fill="#1d2026"/><path d="M-19 -142 Q0 -137 22 -142 l-2 4 Q0 -133 -19 -138Z" fill="#0c0d10"/><rect x="-5" y="-154" width="10" height="5" fill="#c9a24a"/>'
    return s
def leonor(L):
    s=shadow()
    s+=P('M-26 0 Q-24 -60 -18 -104 Q0 -114 18 -104 Q24 -60 26 0Z','#141113',L)
    s+='<g stroke="#0a0809" stroke-width="1.2" fill="none"><path d="M-10 -80 Q-14 -40 -14 0M8 -80 Q12 -40 12 0"/></g>'
    s+=S('M-14 -100 Q-22 -80 -6 -66','#141113',9,L)+S('M14 -100 Q22 -80 6 -66','#141113',9,L)+f'<circle cx="0" cy="-64" r="5.5" fill="{SK}"/>'
    s+=head(0,-128,13,L,.45,'#c9b0a0')+eye(-4,-129)+eye(5,-129)+'<path d="M-4 -120h8" stroke="#5a3a34" stroke-width="1.4"/>'
    s+='<path d="M-13 -132 Q-14 -120 -10 -116 L-12 -136Z M13 -132 Q14 -120 10 -116 L12 -136Z" fill="#1a1414"/>'
    s+='<ellipse cx="0" cy="-139" rx="20" ry="4.5" fill="#0c0a0b"/><path d="M-11 -140 Q-11 -152 0 -152 Q11 -152 11 -140Z" fill="#141113"/>'
    s+='<path d="M-20 -139 Q-22 -126 -14 -118 L14 -118 Q22 -126 20 -139Z" fill="#000" opacity=".35"/>'
    return s
def salazar(L):
    s=shadow()+legs('#1a1b1e',-7,7,44)
    s+=P('M-24 -36 L-22 -104 Q0 -116 22 -104 L24 -36Z','#3a3c40',L)
    s+='<path d="M-6 -108 L0 -90 L6 -108Z" fill="#d8d4cc"/><path d="M-1 -104 v12" stroke="#1a1b1e" stroke-width="2"/><path d="M0 -90V-38" stroke="#26272a" stroke-width="1.4"/>'
    s+='<circle cx="-3" cy="-80" r="1.6" fill="#1a1b1e"/><circle cx="-3" cy="-64" r="1.6" fill="#1a1b1e"/>'
    s+=S('M-18 -100 Q-30 -76 -30 -56','#3a3c40',10,L)+f'<circle cx="-30" cy="-54" r="5" fill="{SK}"/>'
    s+='<path d="M-44 -50 h26 l2 20 h-30z" fill="#1e1410"/><path d="M-36 -50 q5 -8 10 0" stroke="#1e1410" stroke-width="2.5" fill="none"/><rect x="-33" y="-42" width="4" height="4" fill="#c9a24a"/>'
    s+=S('M18 -100 Q28 -78 24 -58','#3a3c40',10,L)+f'<circle cx="24" cy="-56" r="5" fill="{SK}"/>'
    s+=head(0,-128,13,L)+'<g fill="none" stroke="#1a1410" stroke-width="1.4"><circle cx="-5" cy="-129" r="3.6"/><circle cx="5" cy="-129" r="3.6"/><path d="M-1.5 -129h3"/></g>'
    s+='<path d="M-5 -119 Q0 -116 5 -119" stroke="#6a4a3a" stroke-width="1.4" fill="none"/><path d="M-13 -132 q-3 6 0 10M13 -132 q3 6 0 10" stroke="#b8b4ac" stroke-width="2.5" fill="none"/>'
    s+='<ellipse cx="0" cy="-138" rx="19" ry="4" fill="#0c0c0c"/><path d="M-12 -138 Q-12 -156 0 -156 Q12 -156 12 -138Z" fill="#151515"/><path d="M-12 -142h24" stroke="#2a2a2a" stroke-width="2"/>'
    return s
def inigo(L):
    s=shadow()+legs('#121216',-7,7,46)
    s+=P('M-24 -40 L-22 -106 Q0 -116 22 -106 L24 -40Z','#1e2130',L)
    s+='<path d="M-7 -110 L0 -84 L7 -110Z" fill="#e0dbd0"/><path d="M0 -104 l-2 14 2 4 2 -4z" fill="#7a1e18"/><path d="M-9 -108 L0 -80 M9 -108 L0 -80" stroke="#121420" stroke-width="2"/>'
    s+=S('M-18 -102 Q-28 -80 -26 -56','#1e2130',10,L)+f'<circle cx="-26" cy="-54" r="5" fill="{SK}"/><path d="M-26 -54 L-30 0" stroke="#3a2416" stroke-width="2.5"/><circle cx="-26" cy="-54" r="3" fill="#c9a24a"/>'
    s+=S('M18 -102 Q32 -90 26 -76 Q20 -84 14 -86','#1e2130',10,L)+f'<circle cx="16" cy="-86" r="5" fill="{SK}"/>'
    s+='<path d="M18 -88 l12 -4" stroke="#eee" stroke-width="1.8"/><circle cx="30" cy="-92" r="1.6" fill="#ff8a30"/><path class="a-humoP" d="M31 -95 q-4 -9 2 -15 q6 -6 0 -15 q-5 -7 2 -15 q8 -9 1 -19" stroke="#e8e0d0" stroke-width="3.2" fill="none" opacity=".35" filter="url(#humoB)"/>'
    s+=head(0,-130,13,L)+eye(-4,-131)+eye(5,-131)+'<path d="M-4 -122 Q1 -119 5 -123" stroke="#6a3a2a" stroke-width="1.4" fill="none"/>'
    s+='<path d="M-14 -132 Q-14 -146 0 -146 Q14 -146 14 -134 Q8 -142 -4 -140 Q-10 -138 -14 -132Z" fill="#0e0b09"/>'
    return s
def clara(L):
    s=shadow()+legs('#1a1416',-5,5,22)
    s+=P('M-20 -20 L-16 -102 Q0 -112 16 -102 L20 -20Z','#3a2434',L)
    s+='<path d="M-6 -104 Q0 -98 6 -104" stroke="#d8d0c4" stroke-width="2.5" fill="none"/>'
    s+=S('M-14 -100 Q-24 -78 -22 -58','#3a2434',9,L)+f'<circle cx="-22" cy="-56" r="5" fill="{SK}"/>'
    s+=S('M14 -100 Q24 -78 22 -58','#3a2434',9,L)+f'<circle cx="22" cy="-56" r="5" fill="{SK}"/>'
    s+='<g fill="#1e2a6a"><circle cx="20" cy="-58" r="1.5"/><circle cx="24" cy="-55" r="1.2"/><circle cx="22" cy="-52.5" r="1"/><ellipse cx="25.5" cy="-58" rx="1.3" ry=".8"/></g>'  # manchas de tinta
    s+='<rect x="16" y="-54" width="12" height="4" fill="#c9a24a"/><rect x="20" y="-72" width="4" height="18" fill="#efe6d0"/><path d="M22 -72 q-3 -5 0 -10 q3 5 0 10z" fill="#ffcf60"/>'
    s+=head(0,-126,12,L)+eye(-4,-127)+eye(4,-127)+'<path d="M-3 -119h6" stroke="#7a4a3a" stroke-width="1.3"/>'
    s+='<path d="M-14 -124 Q-16 -142 0 -142 Q16 -142 14 -124 L14 -114 L9 -114 L9 -130 Q0 -134 -9 -130 L-9 -114 L-14 -114Z" fill="#2a1a12"/>'
    return s
def mateo(L):
    s=shadow()+legs('#22262a',-8,8,46)
    s+=P('M-24 -42 L-22 -106 Q0 -116 22 -106 L24 -42Z','#bdb5a2',L)
    s+='<path d="M-12 -108 V-42 M12 -108 V-42" stroke="#3a2a1a" stroke-width="3"/>'
    s+=S('M-18 -98 Q-26 -80 8 -76','#a8a08e',11,L)+S('M18 -98 Q26 -80 -8 -72','#bdb5a2',11,L)+f'<circle cx="8" cy="-76" r="5" fill="{SK}"/><circle cx="-8" cy="-72" r="5" fill="{SK}"/>'
    s+=head(0,-130,14,L)+eye(-5,-131)+eye(5,-131)+'<path d="M-7 -122 Q0 -126 7 -122" stroke="#a88a40" stroke-width="3" fill="none"/>'
    s+='<path d="M-14 -134 Q-12 -148 0 -148 Q14 -148 14 -134 Q6 -140 -2 -138 Q-10 -138 -14 -134Z" fill="#d8b860"/>'
    return s

def lola(L):
    s=shadow()+'<path d="M-6 0 V-40 M6 0 V-40" stroke="#c8a089" stroke-width="3.5"/><path d="M-9 0h6M3 0h6" stroke="#3a0e0e" stroke-width="3"/>'
    s+=P('M-17 -34 L-14 -104 Q0 -112 14 -104 L17 -34Z','#6a1418',L)
    s+='<path d="M-17 -34 l3 8 3 -8 3 8 3 -8 3 8 3 -8 3 8 3 -8 3 8 3 -8" stroke="#8a2020" stroke-width="1.5" fill="none"/><g fill="#a83030" opacity=".6"><circle cx="-6" cy="-80" r="1"/><circle cx="4" cy="-70" r="1"/><circle cx="-4" cy="-56" r="1"/><circle cx="7" cy="-90" r="1"/><circle cx="6" cy="-48" r="1"/></g>'
    s+='<path d="M-20 -104 Q0 -94 20 -104 Q26 -96 18 -92 Q0 -86 -18 -92 Q-26 -96 -20 -104Z" fill="#e8dcd0" opacity=".85"/>'
    s+=S('M-14 -100 Q-22 -80 -20 -62','#c8a089',5,L)+S('M14 -100 Q24 -90 24 -76','#c8a089',5,L)
    s+='<path d="M24 -78 l14 -10" stroke="#111" stroke-width="1.6"/><circle cx="38" cy="-88" r="1.6" fill="#ff8a30"/><path class="a-humoP" d="M39 -91 q-4 -9 2 -15 q6 -6 0 -15 q-5 -7 2 -15 q8 -9 1 -19" stroke="#e8e0d0" stroke-width="3.2" fill="none" opacity=".35" filter="url(#humoB)"/>'
    s+=head(0,-124,12,L)+eye(-4,-125)+eye(4,-125)+'<path d="M-3 -117 Q0 -115 3 -117" stroke="#b01818" stroke-width="2.2" fill="none"/>'
    s+='<path d="M-14 -122 Q-16 -140 0 -140 Q16 -140 14 -122 L14 -116 Q12 -112 9 -116 L9 -128 Q0 -132 -9 -128 L-9 -116 Q-12 -112 -14 -116Z" fill="#0c0808"/>'
    s+='<path d="M10 -136 q8 -14 18 -14 q-8 6 -12 16z" fill="#c8505a"/><circle cx="10" cy="-134" r="2.5" fill="#c9a24a"/>'
    return s

def salazar_k(L):  # arrodillado junto al cuerpo
    s='<ellipse rx="44" ry="6" fill="#000" opacity=".6"/>'
    s+='<path d="M-6 -40 L-12 -4 L-40 -2" stroke="#1a1b1e" stroke-width="6" fill="none" stroke-linejoin="round"/><path d="M8 -40 L28 -40 L28 0" stroke="#1a1b1e" stroke-width="6" fill="none" stroke-linejoin="round"/><path d="M-46 -2h8M24 0h10" stroke="#080605" stroke-width="3"/>'
    s+=P('M-22 -36 L-26 -98 Q-6 -112 16 -100 L20 -36Z','#3a3c40',L)
    s+='<path d="M-10 -104 L-4 -88 L2 -104Z" fill="#d8d4cc"/><circle cx="-6" cy="-78" r="1.6" fill="#1a1b1e"/><circle cx="-6" cy="-62" r="1.6" fill="#1a1b1e"/>'
    s+=S('M-20 -96 Q-36 -70 -44 -40','#3a3c40',10,L)+f'<circle cx="-45" cy="-38" r="5" fill="{SK}"/>'
    s+=S('M14 -96 Q30 -74 26 -52','#3a3c40',10,L)+f'<circle cx="26" cy="-50" r="5" fill="{SK}"/>'
    s+='<path d="M40 -22 h34 l2 22 h-38z" fill="#2a1a10"/><path d="M48 -22 q9 -10 18 0" stroke="#2a1a10" stroke-width="3" fill="none"/><rect x="54" y="-14" width="5" height="5" fill="#c9a24a"/>'
    s+=head(-6,-126,13,L)+'<g fill="none" stroke="#1a1410" stroke-width="1.4"><circle cx="-11" cy="-127" r="3.6"/><circle cx="-1" cy="-127" r="3.6"/><path d="M-7.5 -127h3"/></g>'
    s+='<path d="M-11 -117 Q-6 -114 -1 -117" stroke="#6a4a3a" stroke-width="1.4" fill="none"/><path d="M-19 -130 q-3 6 0 10M7 -130 q3 6 0 10" stroke="#b8b4ac" stroke-width="2.5" fill="none"/>'
    s+='<ellipse cx="-6" cy="-136" rx="19" ry="4" fill="#0c0c0c"/><path d="M-18 -136 Q-18 -154 -6 -154 Q6 -154 6 -136Z" fill="#151515"/><path d="M-18 -140h24" stroke="#2a2a2a" stroke-width="2"/>'
    return s
def guardia(L):  # guardia civil con capa, tricornio y farol
    s='<ellipse rx="40" ry="7" fill="#000" opacity=".55"/>'
    s+=P('M-30 0 Q-30 -60 -24 -104 Q0 -118 24 -104 Q30 -60 30 0Z','#232c28',L)
    s+='<g stroke="#161c19" stroke-width="1.4" fill="none"><path d="M-14 -90 Q-18 -40 -16 0M10 -90 Q14 -40 12 0"/></g><path d="M-26 -60 h52" stroke="#3a2a1a" stroke-width="4"/><rect x="-4" y="-63" width="8" height="6" fill="#c9a24a"/>'
    s+='<path d="M-2 -110 V-62" stroke="#161c19" stroke-width="2"/><circle cx="-2" cy="-98" r="2" fill="#c9a24a"/><circle cx="-2" cy="-84" r="2" fill="#c9a24a"/><circle cx="-2" cy="-70" r="2" fill="#c9a24a"/>'
    s+=head(-1,-132,14,L,.4)+'<path d="M-8 -126 Q-1 -121 6 -126" stroke="#2a1c14" stroke-width="3" fill="none"/>'+eye(-6,-134)+eye(4,-134)
    s+='<path d="M-20 -140 Q-20 -160 -1 -160 Q16 -160 18 -146 L24 -150 L22 -138 Q-2 -136 -20 -140Z" fill="#0c0c0c"/><path d="M-20 -140 Q-2 -136 22 -138" stroke="#333" stroke-width="1" fill="none"/>'
    s+=S('M22 -96 Q40 -80 44 -58','#232c28',10,L)+'<path d="M44 -58 v8" stroke="#111" stroke-width="2"/><rect x="36" y="-50" width="16" height="22" rx="3" fill="#ffe3a0"/><path d="M36 -50h16M36 -28h16M44 -50v22" stroke="#111" stroke-width="2.5"/>'
    return s
def ibarra(L):  # comisario: gabán, bigote, prisa
    s=shadow()+legs('#1e1a16',-8,8,44)
    s+=P('M-28 -36 L-26 -106 Q0 -118 26 -106 L28 -36Z','#4a3a28',L)
    s+='<path d="M0 -112V-38" stroke="#2e2418" stroke-width="1.6"/><g fill="#c9a24a"><circle cx="-4" cy="-94" r="2"/><circle cx="-4" cy="-78" r="2"/><circle cx="-4" cy="-62" r="2"/></g><path d="M-12 -110 L0 -96 L12 -110" stroke="#2e2418" stroke-width="4" fill="none"/>'
    s+=S('M-22 -100 Q-32 -78 -30 -56','#4a3a28',11,L)+f'<circle cx="-30" cy="-54" r="5.5" fill="{SK}"/>'
    s+=S('M22 -100 Q34 -84 30 -64','#4a3a28',11,L)+f'<circle cx="30" cy="-62" r="5.5" fill="{SK}"/><rect x="28" y="-70" width="12" height="16" fill="#e9dfc7" transform="rotate(8 34 -62)"/>'
    s+=head(0,-132,15,L)+eye(-5,-135)+eye(6,-135)+'<path d="M-10 -125 Q0 -131 10 -125 Q5 -121 0 -123 Q-5 -121 -10 -125Z" fill="#3a3a3a"/>'
    s+='<path d="M-20 -140 Q-20 -162 -1 -162 Q16 -162 18 -148 L24 -152 L22 -140 Q-2 -138 -20 -140Z" fill="#0b0c0d"/><path d="M-20 -140 Q-2 -137 22 -140" stroke="#333" stroke-width="1" fill="none"/>'
    return s
def txomin(L):  # crío asomado: busto, en las unidades de la escena (pecho en y=60)
    s=P('M-34 60 Q-34 16 0 10 Q34 16 34 60Z','#3a2e22',L)
    s+='<path d="M-20 14 Q0 24 20 14 L24 26 Q0 36 -24 26Z" fill="#7a2018"/><path d="M14 20 l6 26 8 -4 -6 -22z" fill="#7a2018"/>'
    s+=head(0,-12,17,L,.38)+eye(-6,-13)+eye(7,-13)+'<path d="M-4 0 Q0 3 4 0" stroke="#7a3a2a" stroke-width="2" fill="none"/>'
    s+='<path d="M-20 -18 Q-18 -38 2 -38 Q22 -38 24 -20 Q10 -26 0 -25 Q-10 -24 -20 -18Z" fill="#1a1c20"/><circle cx="2" cy="-38" r="3" fill="#1a1c20"/>'
    return s
NF=lambda fn,L=1:f'<g transform="scale(1.6)">{fn(L)}</g>'

def clara_sv(L):  # Clara sin vela
    s=clara(L)
    i=s.index('<rect x="16" y="-54"');j=s.index('/>',s.index('<path d="M22 -72'))+2
    return s[:i]+s[j:]
def estibador(L):  # COL y COL2 se sustituyen en cada uno
    s=shadow()+legs('#1a1612',-7,7,42)+P('M-22 -36 L-20 -100 Q0 -112 20 -100 L22 -36Z','COL',L)
    s+=S('M-16 -96 Q-24 -76 10 -72','COL2',10,L)+S('M16 -96 Q24 -76 -10 -68','COL',10,L)+f'<circle cx="10" cy="-72" r="4.5" fill="{SK}"/><circle cx="-10" cy="-68" r="4.5" fill="{SK}"/>'
    s+=head(0,-124,13,L)+eye(-4,-125)+eye(5,-125)+'<path d="M-4 -116h8" stroke="#3a2a1a" stroke-width="1.6"/>'
    s+='<path d="M-14 -128 Q-14 -142 0 -142 Q14 -142 16 -130 L22 -128 L-14 -126Z" fill="#141414"/>'
    return s
def paco(L):  # tabernero: calvo, bigote, mandil
    s=shadow()+legs('#1a1410',-8,8,44)
    s+=P('M-28 -36 L-24 -108 Q0 -122 24 -108 L28 -36Z','#33302c',L)+'<path d="M-16 -86 L16 -86 L22 -36 L-22 -36Z" fill="#cfc8b6" opacity=".85"/>'
    s+=S('M-24 -100 Q-44 -70 -36 -44','#33302c',11,L)+f'<circle cx="-36" cy="-42" r="6" fill="{SK}"/>'+S('M24 -100 Q38 -76 30 -52','#33302c',11,L)+f'<circle cx="30" cy="-50" r="6" fill="{SK}"/>'
    s+=head(0,-138,15,L,.35)+eye(-5,-140)+eye(5,-140)
    s+='<path d="M-15 -142 Q0 -162 15 -142 Q0 -152 -15 -142Z" fill="#111"/><path d="M-14 -140 q-3 6 0 12M14 -140 q3 6 0 12" stroke="#2a2420" stroke-width="3" fill="none"/>'
    s+='<path d="M-11 -130 Q0 -124 11 -130 L9 -126 Q0 -121 -9 -126Z" fill="#2a1a10"/>'
    return s
def benigna_base(L):  # ama de llaves: vestido oscuro, delantal blanco, moño gris
    s=shadow()+'<path d="M-6 0 V-20 M6 0 V-20" stroke="#121014" stroke-width="5"/>'
    s+=P('M-24 -18 L-20 -102 Q0 -112 20 -102 L24 -18Z','#1e1e24',L)
    s+='<path d="M-14 -86 Q0 -90 14 -86 L18 -22 L-18 -22Z" fill="#d8d2c4" opacity=".9"/><path d="M-14 -86 Q0 -96 14 -86" stroke="#d8d2c4" stroke-width="3" fill="none"/>'
    s+=head(0,-126,13,L,.38,'#c4a08a')+eye(-4,-127)+eye(4,-127)+'<path d="M-4 -119h8" stroke="#5a3a2a" stroke-width="1.4"/>'
    s+='<path d="M-13 -128 Q-12 -142 0 -142 Q12 -142 13 -128 Q6 -134 0 -134 Q-6 -134 -13 -128Z" fill="#8a8680"/><circle cx="0" cy="-143" r="6" fill="#8a8680"/>'
    return s
def benigna(L):
    return benigna_base(L)+S('M-16 -98 Q-22 -78 -4 -66','#1e1e24',9,L)+S('M16 -98 Q22 -78 4 -66','#1e1e24',9,L)+f'<circle cx="0" cy="-64" r="5.5" fill="{SK}"/>'
def obrera(L):  # COL: vestido, PAN: pañuelo
    s=shadow()+'<path d="M-6 0 V-22 M6 0 V-22" stroke="#1a1612" stroke-width="5"/>'
    s+=P('M-20 -20 L-16 -100 Q0 -110 16 -100 L20 -20Z','COL',L)+'<path d="M-12 -84 L12 -84 L16 -24 L-16 -24Z" fill="#cfc8b6" opacity=".8"/>'
    s+=S('M-14 -96 Q-22 -76 -18 -58','COL',8,L)+f'<circle cx="-18" cy="-56" r="4.5" fill="{SK}"/>'+S('M14 -96 Q22 -76 18 -58','COL',8,L)+f'<circle cx="18" cy="-56" r="4.5" fill="{SK}"/>'
    s+=head(0,-124,12,L)+eye(-4,-125)+eye(4,-125)+'<path d="M-3 -117 Q0 -115 3 -117" stroke="#6a3a2a" stroke-width="1.3" fill="none"/>'
    s+='<path d="M-14 -124 Q-14 -142 0 -142 Q14 -142 14 -124 L16 -118 Q0 -130 -16 -118Z" fill="PAN"/>'
    return s
def remedios(L):  # encargada: seca, moño, llavero
    s=shadow()+'<path d="M-7 0 V-20 M7 0 V-20" stroke="#121214" stroke-width="5"/>'
    s+=P('M-24 -18 L-20 -104 Q0 -114 20 -104 L24 -18Z','#1a1a1e',L)
    s+=S('M-16 -100 Q-24 -76 -20 -56','#1a1a1e',9,L)+f'<circle cx="-20" cy="-54" r="5" fill="{SK}"/>'+S('M16 -100 Q24 -76 20 -56','#1a1a1e',9,L)+f'<circle cx="20" cy="-54" r="5" fill="{SK}"/>'
    s+='<path d="M20 -50v12" stroke="#8a7a5a" stroke-width="1.6"/><circle cx="20" cy="-34" r="4" fill="none" stroke="#c9a24a" stroke-width="1.5"/>'
    s+=head(0,-128,13,L)+eye(-4,-129)+eye(5,-129)+'<path d="M-9 -134l6 2M9 -134l-6 2" stroke="#2a2a2a" stroke-width="1.4"/><path d="M-5 -120h10" stroke="#5a3a2a" stroke-width="1.4"/>'
    s+='<path d="M-14 -130 Q-13 -144 0 -144 Q13 -144 14 -130 Q6 -136 0 -136 Q-6 -136 -14 -130Z" fill="#3a3a3a"/><circle cx="0" cy="-146" r="5.5" fill="#3a3a3a"/>'
    return s
def portero(L):
    s=shadow()+legs('#0a0a0c',-9,9,44)+P('M-30 -40 L-28 -106 Q0 -120 28 -106 L30 -40Z','#141418',L)
    s+=S('M-24 -100 Q-34 -76 -30 -50','#141418',13,L)+f'<circle cx="-30" cy="-48" r="7" fill="{SK}"/>'+S('M24 -100 Q34 -76 30 -50','#141418',13,L)+f'<circle cx="30" cy="-48" r="7" fill="{SK}"/>'
    s+=head(0,-132,14,L,.45)+eye(-5,-134)+eye(5,-134)+'<path d="M-9 -138l7 2M9 -138l-7 2" stroke="#111" stroke-width="2"/><path d="M-8 -124 h16" stroke="#2a1a14" stroke-width="2"/>'
    s+='<path d="M-15 -138 Q-15 -150 0 -150 Q15 -150 15 -138Z" fill="#0a0a0a"/>'
    return s
def mateo_cap(L): return mateo(L)
def candela_sin(L):  # sin sombrero ni maletín (en casa)
    s=candela(L)
    s=s[:s.index('<ellipse cx="0" cy="-140"')]+'</g>'
    i=s.index('<rect x="15" y="-56"');j=s.index('fill="none"/>',i)+13
    return s[:i]+s[j:]
def benigna_bandeja(L):  # con la bandeja de copas en las manos
    s=benigna_base(L)
    s+=S('M-16 -98 Q-24 -80 -16 -66','#1e1e24',9,L)+S('M16 -98 Q24 -80 16 -66','#1e1e24',9,L)
    s+=f'<circle cx="-16" cy="-65" r="5" fill="{SK}"/><circle cx="16" cy="-65" r="5" fill="{SK}"/>'
    s+='<ellipse cx="0" cy="-70" rx="27" ry="4.5" fill="#9a9a98"/><ellipse cx="0" cy="-71" rx="23" ry="3" fill="#c8c8c4"/>'
    s+='<path d="M-12 -72v-9h6v9M4 -72v-11h6v11" fill="#e8e2d4" opacity=".85"/><path d="M-11 -80h4M5 -82h4" stroke="#fff" stroke-width=".8" opacity=".6"/>'
    return s
def benigna_sorpresa(L):  # se le ha caído la bandeja: ojos como platos y boca abierta
    s=benigna_base(L)
    i=s.index('<circle cx="-4" cy="-127"');j=s.index('<path d="M-13 -128')
    s=s[:i]+'<circle cx="-4.5" cy="-127.5" r="2.6" fill="#f4efe6"/><circle cx="4.5" cy="-127.5" r="2.6" fill="#f4efe6"/><circle cx="-4.5" cy="-127.5" r="1.3" fill="#1a1410"/><circle cx="4.5" cy="-127.5" r="1.3" fill="#1a1410"/><path d="M-8 -132q3 -2 6 -1M2 -133q3 -1 6 1" stroke="#5e5a55" stroke-width="1.2" fill="none"/><ellipse cx="0" cy="-119" rx="2.2" ry="3" fill="#4a2620"/>'+s[j:]
    s+=S('M-16 -98 Q-28 -110 -24 -122','#1e1e24',9,L)+S('M16 -98 Q28 -110 24 -122','#1e1e24',9,L)
    s+=f'<circle cx="-24" cy="-124" r="5" fill="{SK}"/><circle cx="24" cy="-124" r="5" fill="{SK}"/>'
    return s
