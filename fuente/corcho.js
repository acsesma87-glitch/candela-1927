// ---------- El corcho: 6 huecos; Candela elige a quién clava y salen solos sus motivos, oportunidades y coartadas ----------
// Reglas: solo aparece lo que ella ha descubierto (pista o línea de «Personas»); son hechos, nunca conclusiones;
// el juego no opina de quién pone ni de cómo lo marca.
const cP=id=>S.pistas.some(p=>p.id===id);
const cL=(who,trozo)=>(S.personas[who]||[]).some(l=>l.includes(trozo));
const CARA_X='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 60 60"><rect width="60" height="60" fill="#2a2520"/><circle cx="30" cy="24" r="11" fill="#4a4038"/><path d="M10 60 Q12 38 30 38 Q48 38 50 60Z" fill="#4a4038"/></svg>';
const CORCHO={
 'Doña Leonor':{f:FACE_LEONOR,n:[
  ['m','El seguro de vida de su marido, subido a 200.000 pesetas, es para ella.',()=>cP('poliza')],
  ['m','Sabía lo del testamento nuevo: el rastro de lacre llevaba a su dormitorio.',()=>cP('lacre')],
  ['o','La noche del 30 salió de casa: un ramo blanco a las 23:00 y botines con barro.',()=>cP('floristeria')],
  ['c','Dice que esa noche no salió de casa: «estuve dormida».',()=>cL('Doña Leonor','estuve dormida')],
  ['c','Al enseñarle el recibo: «es asunto mío y de Dios».',()=>cL('Doña Leonor','asunto mío')]]},
 'Íñigo Arrieta':{f:FACE_INIGO,n:[
  ['m','El testamento nuevo lo deja sin nada.',()=>cP('testamento')],
  ['m','Empeñó un reloj de oro del abuelo en El Monte.',()=>cP('resguardo')],
  ['o','Discutió con su padre en el Casino esa noche.',()=>cL('Íñigo Arrieta','discutió')],
  ['o','El muerto apretaba en la mano una ficha del Casino.',()=>cP('ficha')],
  ['c','Dice que volvió a casa a medianoche.',()=>cL('Íñigo Arrieta','discutió')],
  ['c','Arrancó la fecha y la hora del resguardo de El Monte.',()=>cP('resguardo')]]},
 'Clara Arrieta':{f:FACE_CLARA,n:[
  ['m','«En esta casa todos mienten. Yo la que más.»',()=>cL('Clara Arrieta','todos mienten')],
  ['m','El testamento nuevo deja una renta «a L. y a la niña».',()=>cP('testamento')],
  ['o','El 28 de noviembre firmó por un frasco de matarratas: «C. Arrieta».',()=>cP('matarratas')],
  ['o','Tiene los dedos manchados de tinta azul.',()=>cP('tintaClara')]]},
 'Mateo «el Rubio»':{f:FACE_MATEO,n:[
  ['m','Amenazó a Don Julián en público por el chaval muerto en la conservera.',()=>cL('Mateo «el Rubio»','Amenazó')],
  ['m','En la asamblea: «Arrieta tuvo lo que se merecía».',()=>cL('Mateo «el Rubio»','merecía')],
  ['o','Dejó la guardia de amarras a medianoche.',()=>cP('guardia')||cP('mateoMiente')],
  ['o','Sus botas claveteadas son como las huellas de las rocas.',()=>cP('botas')],
  ['c','Dice que estuvo en El Ancla hasta el cierre.',()=>cL('Mateo «el Rubio»','hasta el cierre')],
  ['c','Paco: se fue de El Ancla a medianoche «por un asunto».',()=>cP('paco')]]},
 'Lola':{f:FACE_LOLA,n:[
  ['m','Don Julián le escribió para despedirse: «esta noche se acaba todo».',()=>cP('cartaLola')],
  ['m','Tienen una hija, Julia, de ocho años.',()=>cP('dibujo8')],
  ['o','Él la citó en el faro a la una de la madrugada.',()=>cP('cartaLola')||cL('Lola','faro')],
  ['c','Primero dijo que esa noche ni lo vio.',()=>cL('Lola','ni lo vio')],
  ['c','Luego: lo esperó en el faro y «no vino».',()=>cL('Lola','Confiesa')]]},
 'Dr. Salazar':{f:FACE_SALAZAR,n:[
  ['m','«Julián estaba hundido.» Le daba tónicos para el estómago y los nervios.',()=>cL('Dr. Salazar','hundido')],
  ['o','Tenía los bajos del pantalón mojados de mar: «bajé a las rocas».',()=>cP('bajos')],
  ['o','El frasquito escondido en la despensa es de su dispensario.',()=>cP('frasquito')],
  ['c','Su impermeable estaba empapado: dice que lo llamaron a una urgencia en una trainera.',()=>cL('Dr. Salazar','trainera')]]},
 'Aitor':{f:FACE_AITOR,n:[
  ['o','Tiene la llave de la verja del faro, y el candado estaba abierto.',()=>cP('verja')],
  ['c','Hacía la ronda: a la 1:10 oyó una barca ir hacia el faro sin luces.',()=>cP('ronda')]]},
 'Comisario Ibarra':{f:FACE_IBARRA,n:[
  ['m','Quiere cerrar el caso como suicidio «antes del almuerzo».',()=>cL('Comisario Ibarra','almuerzo')],
  ['o','Según los «Ecos del barrio», un comisario frecuenta la calle del Farol.',()=>cL('Comisario Ibarra','Ecos')]]},
 'Don Fermín Olaso':{f:CARA_X,n:[
  ['m','Presiona para que el caso se cierre «de una vez» como un accidente.',()=>cL('Don Fermín Olaso','Presiona')]]},
 'Benigna':{f:FACE_BENIGNA,n:[
  ['o','Es el ama de llaves del palacete.',()=>cL('Benigna','ama de llaves')],
  ['c','De la nota anónima: «Yo no he visto nada». Pero se quedó quieta un segundo.',()=>cL('Benigna','no he visto nada')]]},
 'Paco, el tabernero':{f:FACE_PACO,n:[
  ['o','Mateo recibía notas escondidas detrás de la diana de su taberna.',()=>cP('notaC')],
  ['c','La sangre de la escalera: una pelea «de gente de fuera».',()=>cP('sangreAncla')]]},
 'Doña Remedios':{f:FACE_REMEDIOS,n:[
  ['o','La encargada de la conservera.',()=>cL('Doña Remedios','encargada')]]},
 'Txomin':{f:FACE_TXOMIN,n:[
  ['o','Fue él quien vino corriendo a avisar a Aitor del muerto.',()=>cL('Txomin','avisar')]]},
 'El guardia civil':{f:FACE_GUARDIA,n:[
  ['o','Estaba en las rocas cuando encontraron el cuerpo.',()=>cL('El guardia civil','6:40')]]},
};
const CAT=[['m','Motivo'],['o','Oportunidad'],['c','Coartada']];
let corPick=-1;
function corchoHTML(){
  const C=S.corcho=S.corcho||[null,null,null,null,null,null];
  if(corPick>=0){const ya=C.filter(Boolean),gente=Object.keys(S.personas).filter(k=>CORCHO[k]&&!ya.includes(k));
    let h='<h2>¿A quién clavo?</h2><div class="fich">';
    if(!gente.length)h+='<div class="it no">No conozco a nadie más.</div>';
    gente.forEach(k=>h+=`<button data-p="${k}"><span class="cara">${CORCHO[k].f}</span>${k}</button>`);
    return h+'</div><button class="corV">← Volver al corcho</button>'}
  let h='<h2>El corcho</h2><div class="corcho">';
  C.forEach((k,i)=>{
    if(!k){h+=`<div class="ficha vacia" data-i="${i}"><span class="chin"></span><div class="hueco">+</div></div>`;return}
    const m=S.sus[k]||0,ns=CORCHO[k].n.filter(n=>n[2]());
    h+=`<div class="ficha"><span class="chin"></span><div class="cab"><span class="cara">${CORCHO[k].f}${m===1?'<i class="tache"></i>':''}${m===2?'<i class="duda">?</i>':''}</span><b>${k}</b>
      <span class="bt"><button data-mk="${i}" data-v="2" class="${m===2?'on':''}">?</button><button data-mk="${i}" data-v="1" class="${m===1?'on':''}">✗</button><button data-q="${i}">Quitar</button></span></div>`;
    CAT.forEach(([c,t])=>{const xs=ns.filter(n=>n[0]===c);h+=`<div class="cat">${t}</div>`+(xs.length?xs.map(n=>`<div class="pap p${c}">${n[1]}</div>`).join(''):'<div class="pap nada">Nada todavía.</div>')});
    h+='</div>'});
  return h+'</div>'}
function corchoWire(){const P=$('#pages');
  P.querySelectorAll('.ficha.vacia').forEach(e=>e.onclick=()=>{corPick=+e.dataset.i;libDraw()});
  P.querySelectorAll('.fich button').forEach(e=>e.onclick=()=>{S.corcho[corPick]=e.dataset.p;corPick=-1;AU.sfx('papel');save();libDraw()});
  P.querySelectorAll('.corV').forEach(e=>e.onclick=()=>{corPick=-1;libDraw()});
  P.querySelectorAll('[data-mk]').forEach(e=>e.onclick=()=>{const k=S.corcho[+e.dataset.mk],v=+e.dataset.v;S.sus[k]=(S.sus[k]===v)?0:v;save();libDraw()});
  P.querySelectorAll('[data-q]').forEach(e=>e.onclick=()=>{S.corcho[+e.dataset.q]=null;save();libDraw()})}
