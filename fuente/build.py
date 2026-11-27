import json, sys, os
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, D)
import scenes
from scenes import SVG, defs, AITOR, CANDELA

eng = open(os.path.join(D, 'engine.html')).read()
laika = open(os.path.join(D, 'laika.svgfrag')).read()
eki = open(os.path.join(D, 'eki.svgfrag')).read()
day1 = open(os.path.join(D, 'day1.js')).read() + '\n' + open(os.path.join(D, 'day2.js')).read() + '\n' + open(os.path.join(D, 'day3.js')).read() + '\n' + open(os.path.join(D, 'day4.js')).read() + '\n' + open(os.path.join(D, 'day5.js')).read() + '\n' + open(os.path.join(D, 'day6.js')).read() + '\n' + open(os.path.join(D, 'day7.js')).read() + '\n' + open(os.path.join(D, 'day8.js')).read()

def face(vb, body, bg='#2a2520'):
    x, y, w, h = vb
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x} {y} {w} {h}">{defs()}<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{bg}"/><circle cx="{x+w*.3}" cy="{y+h*.3}" r="{w*.7}" fill="url(#warm)" opacity=".5"/>{body}</svg>'

faces = {
  'FACE_AITOR': face((150, 106, 110, 110), AITOR),
  'FACE_CANDELA': face((-42, -266, 84, 84), CANDELA),
  'FACE_TXOMIN': face((-40, -50, 80, 80), scenes.TXOMIN),
  'FACE_IBARRA': face((-34, -250, 68, 68), scenes.IBARRA),
  'FACE_SALAZAR': face((-26, -158, 52, 52), scenes.SALAZAR),
  'FACE_GUARDIA': face((-30, -240, 60, 60), scenes.GUARDIA),
  'FACE_LEONOR': face((-30, -228, 60, 60), scenes.LEONOR),
  'FACE_PACO': face((-30, -194, 60, 60), scenes.PACO),
  'FACE_INIGO': face((-26, -232, 52, 52), scenes.INIGO),
  'FACE_CLARA': face((-24, -204, 48, 48), scenes.CLARA),
  'FACE_BENIGNA': face((-24, -196, 48, 48), scenes.BENIGNA),
  'FACE_MATEO': face((-30, -228, 60, 60), scenes.MATEO),
  'FACE_REMEDIOS': face((-26, -210, 52, 52), scenes.REMEDIOS),
  'FACE_OBRERA': face((-22, -176, 44, 44), scenes.OBRERA.replace('COL','#2e3a46').replace('PAN','#d8c070')),
  'FACE_LOLA': face((-24, -206, 48, 48), scenes.LOLA),
  'FACE_PORTERO': face((-28, -220, 56, 56), scenes.PORTERO),
  'FACE_EST': face((-22, -174, 44, 44), scenes.ESTIBADOR.replace('COL2','#34404a').replace('COL','#3a4652')),
}
consts = ''.join(f'const {k}={json.dumps(v)};\n' for k, v in faces.items())

out = eng.replace('{{LAIKA}}', laika).replace('{{EKI}}', eki)
out = out.replace('{{SCENES}}', json.dumps(SVG, ensure_ascii=False))
out = out.replace('{{DAY1}}', consts + day1)
open(os.path.join(D, '..', 'prueba', 'altamar.html'), 'w').write(out)
print(len(out))
