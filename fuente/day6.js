// ---------- Día 6 ----------
const d6=()=>D(6).flags;
const CAJA_OK=[7,9,19],CAJA_BODA=[12,4,98];
// el otro sereno va y viene por la calle
const otroX=()=>400+330*Math.sin(performance.now()/1500);
function rondaOtro(){const svg=SVG.calle;const f=()=>{if(!SC||SC.svg!==svg)return;const x=otroX(),dir=Math.cos(performance.now()/1500)>0?1:-1;
  allSel('.otroS',e=>e.style.transform=`translate(${x}px,0px) scaleX(${dir})`);requestAnimationFrame(f)};requestAnimationFrame(f)}
function cajaPinta(){const f=d6();if(!f.cifras){f.cifras=[0,0,0];save()}f.cifras.forEach((n,i)=>setText(`.cifra[data-i="${i}"]`,String(n)))}
function cifra(i,paso){const f=d6();if(f.abierta)return;const c=f.cifras;c[i]=(c[i]+paso+100)%100;save();cajaPinta();
  AU.sfx('tic')}
async function manija(){const f=d6();if(f.abierta)return;const c=f.cifras;AU.sfx('cerradura');
  if(c.every((n,i)=>n===CAJA_OK[i])){f.abierta=1;$('#acts').innerHTML='';save();await sleep(300);swapSvg(SVG.cajaA);await shake();
    await bubble('¡Clac! La puerta de la caja se abre. Dentro, unos billetes… y un sobre lacrado: «Testamento».',4600);
    nar('Un testamento. Y el lacre está roto: alguien ya lo ha abierto antes que yo.');return}
  if(c.every((n,i)=>n===CAJA_BODA[i])){f.boda=1;save();await bubble('Un clic sordo. Nada. La fecha de su boda no es.',3600);return}
  if(c[0]===4&&c[1]===45){await bubble('Un clic sordo. Las 4:45 tampoco. Esa hora no es la clave.',3800);return}
  await bubble('La manija no cede. No es esa combinación.',3000)}
async function susto(){const f=d6();f.susto=1;save();await sleep(400);AU.sfx('toc');await shake();
  await bubble('¡La puerta de la calle! Clara apaga la vela de un soplo y me empuja detrás de la cortina.',4400);
  swapSvg(SVG.despachoI);anima('.luzI',[{opacity:0},{opacity:.22}],{duration:700});
  if(ANIM2)anima('.borracho',[{transform:'translateX(0) rotate(0)'},{transform:'translateX(-6px) rotate(-2deg)'},{transform:'translateX(3px) rotate(1.5deg)'},{transform:'translateX(0) rotate(0)'}],{duration:1600,iterations:Infinity,fill:'none'});
  await talk('Íñigo Arrieta','(Arrastrando las palabras.) ¿Clara? ¿Estás despierta? … Nadie. Como siempre en esta casa.');
  await talk('Íñigo Arrieta','(Se sirve una copa del mueble de su padre.) A tu salud, viejo. Mañana el notario lee el papel y todo esto es mío. Todo.');
  await talk('Íñigo Arrieta','(Se queda mirando el retrato. Se ríe, sin ganas.) No me mires así. Tú tampoco eras un santo.');
  await talk('Candela','(Detrás de la cortina, no respiro. Si mira hacia aquí, me ve.)');
  await talk('Íñigo Arrieta','(Bosteza, deja la copa a medias y se va dando tumbos escaleras arriba.)');endTalk();
  persona('Íñigo Arrieta','Volvió borracho del Casino: «Mañana el notario lee el papel y todo esto es mío». No sabe nada del testamento nuevo… ¿o sí?');
  swapSvg(SVG.despachoNA);
  await talk('Clara Arrieta','(Vuelve a encender la vela. Le tiemblan las manos.) Ya está, se ha ido a dormir. En diez minutos ronca como un oso.');endTalk();
  nar('Íñigo se ha dejado el abrigo en el sillón, empapado. Un minuto más… solo uno.')}
async function despedida6(){const f=d6();f.despedida=1;save();
  await talk('Clara Arrieta','Váyase. Ya. Lo que ha visto, guárdeselo en la cabeza: el papel se queda donde estaba.');
  await talk('Candela','Gracias, Clara. Le prometo que voy a averiguar qué le pasó a su padre.');
  await talk('Clara Arrieta','No me prometa nada. Averígüelo.');endTalk();
  nar('Fuera, Aitor me espera con el farol apagado. No le digo nada hasta que doblamos la esquina.');
  narBtn('Volver a casa',()=>{narSigue=true;goScene(5)})}
DAYS[6]=[
// ===== Periódico =====
{svg:SVG.periodico6,dark:0,tools:['mano','linterna','lupa'],cartel:'MARTES<br>6 DE DICIEMBRE DE 1927',
 spots:[
  {id:'p6casino',tool:'lupa',x:243,y:410,w:240,h:34,act:async()=>{await bubble('«Casino de Altamar. Esta noche, baile de invierno, hasta el amanecer.» Íñigo no se lo pierde, seguro.',4400)}},
  {id:'p6reloj',tool:'lupa',x:243,y:455,w:240,h:30,act:async()=>{await bubble('«Relojería Etxeberria. Se arreglan relojes de pie y de bolsillo.» Qué cosas anuncian.',4000)}},
  {id:'p6breve',tool:'lupa',x:539,y:432,w:280,h:44,act:async()=>{persona('Doña Leonor','Esta noche duerme fuera, en casa de su hermana, en Hondarribia.');
    await bubble('La viuda duerme esta noche en Hondarribia. El palacete, solo con el servicio… y con el heredero. Es ahora o nunca.',4800)}},
  {id:'p6marea',tool:'lupa',x:539,y:467,w:200,h:10,act:async()=>{await bubble('«Noche cerrada, sin luna. Pleamar a las 4:50.»',3200)}},
 ],
 enter:async()=>{persona('Íñigo Arrieta','La noche del entierro de su padre se fue al Casino «hasta el amanecer».');
   nar('Martes. Llueve sobre el entierro de ayer. Aitor lee el periódico en voz alta, despacio, como si le pesara.<br><br><i>Léelo bien: la letra pequeña también cuenta.</i>');
   narBtn('Ir al palacete, de noche',async()=>{narPaso('A las once de la noche, Aitor llama con los nudillos en la puerta de servicio: tres golpes cortos. No sé a quién espero encontrar.');await sleep(5000);goScene(1)})}},

// ===== La calle del palacete: esquivar al otro sereno =====
{svg:SVG.calle,dark:.15,tools:['mano','linterna','lupa'],cartel:'ALTAMAR<br>LA CALLE DEL PALACETE',
 spots:[
  {id:'puertaS',tool:'mano',x:675,y:330,r:75,once:false,act:async()=>{const f=d6();if(f.calle)return;
    if(otroX()<260){f.calle=1;save();await bubble('Ahora. Cruzamos pegados a la tapia mientras el farol se aleja calle abajo. Aitor da tres golpes cortos en la puerta de servicio.',4600);goScene(2);return}
    f.fallos=(f.fallos||0)+1;save();await shake();
    await bubble('«¿Quién anda ahí?» El farol se vuelve hacia nosotros. Aitor me tira del brazo de vuelta a la sombra. Por los pelos.',4400);
    if(f.fallos>=2)nar('Hay que esperar a que su farol esté bien lejos, al otro lado de la farola.<br><br><i>Entonces, toca la puerta de servicio.</i>')}},
  {id:'aitorC',tool:'mano',x:70,y:330,r:70,once:false,act:async()=>{await talk('Aitor','(En un susurro.) Es Patxi, el sereno de esta calle. Buen hombre, pero tiene la lengua muy larga: si nos ve, mañana lo sabe todo Altamar.');endTalk()}},
 ],
 enter:async()=>{const f=d6();if(f.calle){goScene(2);return}rondaOtro();
   nar('La calle del palacete, a oscuras. Patxi, el sereno de esta calle, hace la ronda con su farol de punta a punta. Si nos ve cruzar, adiós.<br><br><i>Cuando sea el momento, toca la puerta de servicio.</i>')}},

// ===== La cocina, de noche =====
{svg:SVG.cocinaN,dark:.2,tools:['mano','linterna','lupa'],cartel:'ALTAMAR<br>EL PALACETE, DE NOCHE',
 ekiSpots:[
  {who:'Clara Arrieta',x:190,y:330,act:async()=>{await bubble('Eki se acerca a Clara moviendo el rabo. Clara se agacha y le rasca detrás de las orejas. Por primera vez la veo sonreír.',4600);
    ekiLog('Clara Arrieta','le cae muy bien: le rasca detrás de las orejas.')}},
 ],
 spots:[
  {id:'claraN',tool:'mano',x:190,y:320,r:95,once:false,act:async()=>{const f=d6();
    if(!f.clara){await talk('Clara Arrieta','(En voz muy baja, con una vela en la mano.) ¿Usted? Benigna me dijo que vendría alguien. No pensé que fuera usted.');
      await talk('Candela','En el despacho de su padre hay una caja fuerte. Necesito ver qué hay dentro.');
      await talk('Clara Arrieta','(Se queda callada un momento.) Mi madre en Hondarribia, mi hermano en el Casino… Si alguna vez hay una noche, es esta. Venga. Y no haga ruido.');
      endTalk();f.clara=1;save();persona('Clara Arrieta','Me abre el palacete de noche: quiere saber la verdad sobre su padre tanto como yo.');
      nar('Clara me guía por la casa a oscuras, con la vela tapada con la mano.');narBtn('Subir al despacho',()=>goScene(3));return}
    await talk('Clara Arrieta','Rápido, por favor.');endTalk()}},
 ],
 enter:async()=>{const f=d6();
   if(f.clara){nar('La cocina, a oscuras. Clara me espera en la escalera.');narBtn('Subir al despacho',()=>goScene(3));return}
   nar('La puerta de servicio se abre una rendija. Al otro lado no está Benigna: es Clara, la hija, con una vela. Aitor se queda fuera, vigilando la calle.')}},

// ===== El despacho, de noche =====
{svg:SVG.despachoN,dark:.55,tools:['mano','linterna','lupa'],
 ekiSpots:[
  {who:'Clara Arrieta',x:735,y:330,act:async()=>{await bubble('Eki se pega a las piernas de Clara. Clara, sin dejar de vigilar la puerta, le acaricia la cabeza.',4200);ekiLog('Clara Arrieta','le cae muy bien.')}},
 ],
 spots:[
  {id:'bodaR',tool:'lupa',x:400,y:203,w:110,h:20,act:async()=>{await bubble('En el marco, en letras doradas muy pequeñas: «Julián y Leonor · 12 · IV · 1898». El día de su boda.',4600);
    await pista('bodaRetrato','El retrato de la boda','En el marco del retrato de Don Julián: «Julián y Leonor · 12 · IV · 1898». La fecha de su boda.')}},
  {id:'cajaVer',tool:'mano',x:390,y:135,r:70,once:false,act:async()=>{if(d6().testamento){await bubble('La caja, cerrada otra vez. Como si nadie la hubiera tocado.',3000);return}goScene(4)}},
  {id:'horaR',tool:'lupa',x:514,y:104,w:46,h:46,act:async()=>{await bubble('Las agujas del reloj de pie, paradas: marcan las 4:45. Las cinco menos cuarto.',4200);
    await pista('horaReloj','El reloj parado','El reloj de pie del despacho está parado a las 4:45.')}},
  {id:'tarjeta',tool:'linterna',x:514,y:205,w:34,h:40,act:async()=>{await bubble('El reloj de pie está parado. Dentro, pegada en la caja del péndulo, una tarjetita con la letra de Don Julián: «No es la boda. Es lo único bueno que he hecho. J.»',5200);
    await pista('tarjetaReloj','La tarjeta del reloj','Escondida dentro del reloj de pie: «No es la boda. Es lo único bueno que he hecho. J.»')}},
  {id:'biblia',tool:'mano',x:222,y:308,r:40,once:false,act:async()=>{
    await docShow('<div style="text-align:left;font-size:15px;line-height:1.75"><b style="color:#8a2a20">Santa Biblia · Familia Arrieta</b><br>Julián Arrieta Goñi y Leonor Uriarte, casados el 12 de abril de 1898.<br>Íñigo, nacido el 3 de marzo de 1900.<br>Clara, nacida el 19 de mayo de 1905.<br><span style="font-family:Georgia,serif;font-style:italic;color:#2a3a6a">La niña — 7 · IX · 1919</span> <span style="font-size:12px;opacity:.7">(otra tinta, sin apellido)</span></div>');
    await pista('bibliaNina','La Biblia de la familia','En la primera página, los nacimientos de la familia. Al final, con otra tinta y sin apellido: «La niña — 7 · IX · 1919».')}},
  {id:'lacre',tool:'linterna',x:392,y:470,w:44,h:26,act:async()=>{await bubble('En la alfombra, debajo del retrato, una gota de lacre rojo. Seca: no es de esta noche. Y otra más allá… y otra. Van hacia la puerta del pasillo.',5000);
    await talk('Clara Arrieta','(Sigue el rastro con la vela, muy despacio.) Esa puerta… es la del dormitorio de mi madre.');endTalk();
    await pista('lacre','El rastro de lacre','Gotas de lacre rojo, secas, desde la caja fuerte hasta la puerta del dormitorio de Doña Leonor. Alguien abrió el testamento antes que yo… y se lo llevó a leer a su cuarto.')}},
  {id:'resguardo',tool:'lupa',x:580,y:425,w:110,h:80,when:()=>d6().susto,act:async()=>{await bubble('En el bolsillo del abrigo de Íñigo asoma un papel roto: un resguardo de la casa de empeños El Monte. Le falta la esquina de la fecha y la hora.',5000);
    await talk('Clara Arrieta','¿El Monte? ¿Mi hermano empeña cosas? … ¿Qué cosas?');endTalk();
    await pista('resguardo','El resguardo de Íñigo','En el bolsillo de Íñigo, un resguardo roto de la casa de empeños El Monte. Le falta la esquina de la fecha y la hora.');
    persona('Íñigo Arrieta','Lleva en el bolsillo un resguardo de la casa de empeños El Monte. Clara no sabía que empeñaba cosas.')}},
  {id:'claraD',tool:'mano',x:735,y:340,r:80,once:false,act:async()=>{const f=d6();
    if(f.testamento){await talk('Clara Arrieta','(Mira la puerta.) Váyase antes de que…');endTalk();return}
    if(!f.claraD){f.claraD=1;save();await talk('Clara Arrieta','Mi padre era un hombre de costumbres. Cada noche, antes de acostarse, le daba cuerda a ese reloj. Hasta hace un mes: un día lo dejó parar y ya no lo volvió a tocar.');endTalk();return}
    await talk('Clara Arrieta','No sé la combinación, de verdad. Nunca me dejó acercarme a esa caja.');endTalk()}},
 ],
 check:()=>{const f=d6();if(f.testamento&&!f.susto){run(susto);return}
   if(f.susto&&!f.despedida&&found('resguardo')&&found('lacre'))run(despedida6)},
 enter:async()=>{const f=d6();
   if(f.susto){swapSvg(SVG.despachoNA);if(f.despedida){nar('El despacho, otra vez en silencio. Toca irse.');narBtn('Volver a casa',()=>{narSigue=true;goScene(5)});return}
     nar('Íñigo duerme arriba. Su abrigo, empapado en el sillón.');return}
   if(f.testamento)return;
   nar(f.desp?'El despacho de Don Julián. Clara vigila la puerta.':'El despacho de Don Julián, solo con la vela de Clara. Huele a tabaco frío y a cera.<br><br><i>La caja fuerte, detrás del retrato. Sin la combinación, no hay nada que hacer.</i>');f.desp=1;save()}},

// ===== La caja fuerte =====
{svg:SVG.cajaF,dark:0,tools:['mano','linterna','lupa'],
 spots:[
  ...[0,1,2].flatMap(i=>[
    {id:'arriba'+i,tool:'mano',x:300+i*100,y:165,r:30,once:false,when:()=>!d6().abierta,act:async()=>cifra(i,1)},
    {id:'abajo'+i,tool:'mano',x:300+i*100,y:283,r:30,once:false,when:()=>!d6().abierta,act:async()=>cifra(i,-1)}]),
  {id:'manija',tool:'mano',x:410,y:350,r:42,once:false,when:()=>!d6().abierta,act:manija},
  {id:'testamento',tool:'mano',x:450,y:240,r:80,when:()=>d6().abierta,act:async()=>{const f=d6();
    await docShow('<div style="text-align:left;font-size:15px;line-height:1.7"><b style="color:#8a2a20">Testamento de Julián Arrieta Goñi</b><br><i>Altamar, 29 de noviembre de 1927</i><br>Revoco todo testamento anterior.<br>A mi hijo Íñigo, <u>nada</u>: ya se ha llevado bastante.<br>A mi esposa Leonor y a mi hija Clara, el palacete y la conservera.<br>Y una renta de por vida <b>a L. y a la niña</b>, que no tienen la culpa de nada.<br><span style="float:right">J. A.</span></div>');
    await pista('testamento','El testamento nuevo','Firmado el 29 de noviembre, un día antes de morir: deshereda a Íñigo y deja una renta «a L. y a la niña». El lacre ya estaba roto.');
    persona('Don Julián Arrieta','Tenía otra mujer, «L.», y una hija secreta nacida el 7 de septiembre de 1919. Les dejó una renta en su testamento nuevo.');
    persona('Íñigo Arrieta','Desheredado en el testamento nuevo del 29 de noviembre, un día antes de morir su padre.');
    await talk('Clara Arrieta','(Lee por encima de mi hombro. Se queda blanca.) «A L. y a la niña»… ¿La niña? ¿Mi padre tenía… otra hija?');
    await talk('Candela','La fecha de la Biblia. «Lo único bueno que he hecho.» Lo siento, Clara.');
    await talk('Clara Arrieta','(Cierra la caja despacio.) Déjelo todo como estaba. Por favor.');endTalk();
    f.testamento=1;save();nar('Dejamos el testamento donde estaba y cerramos la caja.');narBtn('Volver al despacho',()=>goScene(3))}},
 ],
 enter:async()=>{const f=d6();
   if(f.abierta){swapSvg(SVG.cajaA);if(hasP('testamento')){nar('El testamento, otra vez en su sitio.');narBtn('Volver al despacho',()=>goScene(3));return}
     nar('Un testamento. Y el lacre está roto: alguien ya lo ha abierto antes que yo.');return}
   cajaPinta();
   nar('La caja fuerte de Don Julián: tres ruedas de números y una manija.<br><br><i>Toca las flechas para cambiar cada número y gira la manija para probar.</i>');
   narBtn('Volver al despacho',()=>goScene(3))}},

// ===== Esa noche =====
{svg:SVG.noche,dark:.35,tools:['mano','linterna','lupa'],sleep:1,laikaHome:120,ekiHome:215,cartel:'ALTAMAR<br>ESA NOCHE',
 enter:async()=>{const f=d6();
   if(!f.cabos){await talk('Aitor','(Pone agua a calentar y se sienta enfrente.) A ver, detective. Despacio. Ese testamento nuevo: ¿quién sale perdiendo?');
     for(;;){const c=await choose(null,null,['Doña Leonor','Íñigo','Clara','«L.» y la niña']);
       if(c===1){await talk('Aitor','Íñigo. Desheredado. Y su padre lo firma un día antes de morir…');break}
       await talk('Aitor',['Leonor se queda el palacete y la conservera. Perder, lo que se dice perder… no.','Clara se queda con la mitad de todo. Esa no pierde.','Al revés: a esas dos les deja una renta. Ganan.'][c===0?0:c===2?1:2]);
       await talk('Aitor','Piénsalo otra vez. ¿Quién se queda sin nada?')}
     await talk('Aitor','Ahora lo difícil. ¿Quién sabía ya lo del testamento nuevo, antes que tú?');
     for(;;){const c=await choose(null,null,['Íñigo','Doña Leonor','Clara']);
       if(c===1){await talk('Aitor','El lacre roto y el rastro hasta su dormitorio. La viuda lo sabía: que su marido le dejaba una renta a otra mujer y a otra hija… Y en el faro, ni una lágrima.');break}
       await talk('Aitor',c===0?'¿Íñigo? Si lo oíste tú: «mañana el notario lee el papel y todo esto es mío». No tiene ni idea.':'¿Clara? Se quedó blanca al leerlo. Eso no se finge.');
       await talk('Aitor','Acuérdate de lo que viste en el suelo del despacho.')}
     await talk('Aitor','Mañana voy contigo a la conservera. Allí todo el mundo sabe algo de todo el mundo… y alguien sabrá quién es «L.».');endTalk();
     f.cabos=1;save();await pista('cabos6','Atando cabos con Aitor','Íñigo pierde con el testamento nuevo, pero no sabe que existe. Doña Leonor sí lo sabía: el lacre roto llevaba a su dormitorio.');
     persona('Doña Leonor','Sabía lo del testamento nuevo antes que nadie: el rastro de lacre llevaba a su dormitorio.')}
   nar(`Aitor pone agua a calentar sin preguntar nada. Laika y Eki duermen junto al fogón.<br><br>Pistas de hoy: ${S.pistas.filter(p=>p.day===6).length}.<br>Don Julián tenía otra mujer, «L.», y una hija de ocho años.`);
   await sleep(5000);narAdd('Íñigo, desheredado un día antes de la muerte de su padre… sin saberlo. Y Doña Leonor, que lo sabía todo y no dijo nada.<br><br>¿Quién es «L.»? Mañana, a la conservera.');
   narBtn('Cerrar el día',()=>{endDay();SC=null;drawCal();show('cal');bubCal('Día 6 resuelto. Mañana, la conservera.')})}},
];
