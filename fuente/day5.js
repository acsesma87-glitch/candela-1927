// ---------- Día 5 ----------
const d5=()=>D(5).flags,hasP=id=>S.pistas.some(p=>p.id===id);
const FR_OK=[0,1,2,3,4,5],FR_X=i=>140+i*92;
function armarioPinta(ya){const f=d5();if(!f.orden){f.orden=[4,0,5,1,3,2];save()}if(ya)allSel('.fr',e=>e.style.transition='none');
  f.orden.forEach((k,i)=>allSel(`.fr[data-k="${k}"]`,e=>e.style.transform=`translate(${FR_X(i)}px,0px)`));
  allSel('.frSel',e=>{e.setAttribute('opacity',f.sel!=null&&!f.cajon?'.8':'0');if(f.sel!=null)e.setAttribute('cx',FR_X(f.sel))});
  allSel('.cajonA',e=>e.setAttribute('opacity',f.cajon?'1':'0'));allSel('.cajonC',e=>e.setAttribute('opacity',f.cajon?'0':'1'));
  if(ya){void base.offsetWidth;requestAnimationFrame(()=>allSel('.fr',e=>e.style.transition=''))}}
async function frasco(i){const f=d5();if(f.cajon)return;
  if(f.sel==null){f.sel=i;save();AU.sfx('tic');armarioPinta();return}
  if(f.sel===i){f.sel=null;save();armarioPinta();return}
  const o=f.orden;[o[f.sel],o[i]]=[o[i],o[f.sel]];f.sel=null;f.cambios=(f.cambios||0)+1;save();AU.sfx('clic');armarioPinta();
  if(o.every((k,j)=>k===FR_OK[j])){f.cajon=1;save();$('#acts').innerHTML='';await sleep(500);AU.sfx('cerradura');armarioPinta();anima('.cajonA',[{transform:'translateY(-34px)',opacity:0},{transform:'none',opacity:1}],{duration:700,easing:'ease-out'});
    await bubble('¡Clic! Con los frascos en su sitio, se abre un cajón escondido en la base del armario.',4000);
    nar('Dentro del cajón hay un papel doblado.');return}
  if(f.cambios===10&&!f.pistaTabla){f.pistaTabla=1;save();await bubble('Esos símbolos raros de los frascos… Para compararlos habría que pasarlos todos a la misma medida. ¿Habrá algún papel por aquí que lo explique?',4600)}}
async function vuelta5(){const f=d5();f.vuelta=1;save();await sleep(500);AU.sfx('clic');swapSvg(SVG.dispensario);
  if(ANIM2)await anima('.docG',[{transform:'translate(-380px,0)',opacity:0},{transform:'translate(-285px,-6px)',opacity:1},{transform:'translate(-190px,0)'},{transform:'translate(-95px,-6px)'},{transform:'translate(0,0)'}],{duration:1600,easing:'linear'});
  await talk('Dr. Salazar','(Entra sacudiéndose la lluvia.) Ya estoy. Un corte feo en la frente, pero nada que no arregle un poco de hilo.');
  const c=await choose('Candela','(Me aparto del perchero, como si nada.)',['«¿Sale usted a la mar, doctor? Ese impermeable está empapado.»','No decir nada.']);
  if(c===1)await talk('Dr. Salazar','(Ve que miro el perchero y sonríe.) ¿Le llama la atención mi impermeable? Está empapado, ya lo sé.');
  await talk('Dr. Salazar','Anoche me llamaron a una urgencia en una trainera: un pescador con la mano abierta. Hasta el muelle con este tiempo… Y en este puerto no se seca nada.');
  persona('Dr. Salazar','Tiene un impermeable de mar empapado y con sal. Dice que anoche lo llamaron a una urgencia en una trainera.');
  await talk('Dr. Salazar','(Abre un cajón del mostrador y le tiende una libretita.) Tome. Una agenda del dispensario, con las mareas de todo el año. A una detective que vive en un puerto le hará falta.');
  objeto({id:'agenda',i:'📒',t:'Agenda del dispensario',d:'Regalo del doctor Salazar. Trae la tabla de mareas de todo el año.'});
  await talk('Candela','Gracias, doctor.');await talk('Dr. Salazar','Y cuídese, Candela. Las preguntas, en este puerto, también mojan.');endTalk();
  nar('Salgo del dispensario con una agenda nueva… y una ficha que no debería haber visto.');narBtn('Volver a casa',()=>{narSigue=true;goScene(4)})}
DAYS[5]=[
// ===== Periódico =====
{svg:SVG.periodico5,dark:0,tools:['mano','linterna','lupa'],cartel:'LUNES<br>5 DE DICIEMBRE DE 1927',
 spots:[
  {id:'p5disp',tool:'lupa',x:243,y:410,w:240,h:34,act:async()=>{persona('Dr. Salazar','Tiene el dispensario del puerto: consultas de 10 a 13 y urgencias a cualquier hora.');
    await bubble('«Urgencias, a cualquier hora del día o de la noche.» El doctor Salazar no duerme nunca, por lo visto.',4400)}},
  {id:'p5monte',tool:'lupa',x:243,y:455,w:240,h:30,act:async()=>{await bubble('«Se presta sobre alhajas, relojes y papeles.» ¿Papeles? ¿Quién empeña papeles?',4000)}},
  {id:'p5breve',tool:'lupa',x:539,y:432,w:280,h:44,act:async()=>{await bubble('Doña Puri, en primera fila «por cercanía». Si ella no se entera de algo, es que no ha pasado.',4200)}},
  {id:'p5marea',tool:'lupa',x:539,y:467,w:200,h:10,act:async()=>{await bubble('«Pleamar a las 4:10.»',3000)}},
 ],
 enter:async()=>{nar('Lunes. Llovizna. Aitor ha subido el periódico al volver de la ronda y se ha quedado dormido con la gorra puesta.<br><br><i>Léelo bien: la letra pequeña también cuenta.</i>');
   narBtn('Ir al palacete',async()=>{narPaso('A las once, la familia Arrieta sale detrás del coche fúnebre hacia el cementerio. Aitor y yo esperamos en la esquina hasta que se pierden de vista.');await sleep(5000);goScene(1)})}},

// ===== La cocina del palacete =====
{svg:SVG.cocinaP,dark:.1,tools:['mano','linterna','lupa'],cartel:'ALTAMAR<br>LA COCINA DEL PALACETE',
 laika:()=>d5().cajas?null:(d5().cajas=1,save(),{x:175,t:'Laika olfatea las cajas de Conservas Arrieta y gruñe bajito. «Envases vacíos», dicen. Pues pesan.'}),
 ekiSpots:[
  {who:'Benigna',x:545,y:330,act:async()=>{await bubble('Eki va derecha hacia Benigna… y Benigna la espanta con la escoba: «¡Fuera de mi cocina!». Eki vuelve con las orejas gachas.',4600);
    ekiLog('Benigna','no la deja acercarse: la espanta con la escoba («¡Fuera de mi cocina!»).')}},
 ],
 spots:[
  {id:'benigna',tool:'mano',x:545,y:330,r:100,once:false,act:async()=>{const f=d5();
    if(!f.carta){await talk('Benigna','(Sin dejar de barrer.) Puntual. Bien. Están todos en el cementerio; tenemos hasta la una.');
      await talk('Candela','Su hermana Maite me dio esto para usted, en Buenos Aires.');if(ANIM2)allSel('.a-escoba',e=>e.classList.add('quieta'));
      await talk('Benigna','(Apoya la escoba en el fogón y lee la carta despacio. Se le escapa una sonrisa, la primera.) «A ver si te cuidas, Beni, que en esa casa te matan a trabajar»… La misma de siempre.');
      await talk('Benigna','De crías, en Rentería, nos escapábamos al río a coger cangrejos con la saya remangada. A ella siempre la pillaban. A mí, nunca.');
      await talk('Candela','(Rentería… No sé muy bien por qué, pero sonrío.)');
      allSel('.a-escoba',e=>e.classList.remove('quieta'));await talk('Benigna','(Se seca los ojos con el delantal y se endereza.) Bueno. Pregunte lo que tenga que preguntar, que tengo el caldo al fuego.');endTalk();
      f.carta=1;save();persona('Benigna','De Rentería, como su hermana Maite, que vive en Buenos Aires. Con la carta se ha ablandado… un poco.');return}
    const P=[['comia','¿Cómo estaba Don Julián estos días?'],['salia','¿Salía mucho de casa?'],['nota','¿Fue usted quien me dejó una nota bajo la puerta?']],f2=f.preg||{},q=P.filter(p=>!f2[p[0]]);
    if(!q.length){await talk('Benigna','Váyase ya, que vuelven del cementerio y si la señora la ve aquí, a la que echan es a mí.');endTalk();return}
    const c=await choose('Candela','(¿Qué le pregunto?)',[...q.map(p=>p[1]),'Nada más, de momento.']);
    if(c===q.length){endTalk();return}
    const k=q[c][0];f2[k]=1;f.preg=f2;save();
    if(k==='comia'){await talk('Benigna','Ni comía ni dormía. Se apretaba aquí (se toca el estómago) cuando creía que nadie lo veía. Un hombre así no está para nada.');
      persona('Don Julián Arrieta','Según Benigna, estos días no comía ni dormía, y le dolía el estómago.')}
    if(k==='salia'){await talk('Benigna','Al dispensario, todos los jueves. Y el doctor venía aquí a traerle sus medicinas. En frasquitos, como si fueran perfume.');
      persona('Don Julián Arrieta','Iba al dispensario todos los jueves; el doctor le traía medicinas en frasquitos.')}
    if(k==='nota'){await talk('Benigna','(Se queda quieta un segundo. Luego barre con más fuerza.) No sé de qué nota me habla. Yo no he visto nada. Ni en esta casa, ni en la despensa, ni en ningún sitio.');
      persona('Benigna','Le pregunté por la nota anónima: «Yo no he visto nada». Pero se quedó quieta un segundo.')}
    endTalk()}},
  {id:'cajasP',tool:'lupa',x:175,y:290,w:110,h:90,act:async()=>{await bubble('«Conservas Arrieta · envases vacíos». Como las cajas que iban en el barco… y que tanto le interesaban a Laika.',4600)}},
  {id:'frascoV',tool:'linterna',x:720,y:280,w:40,h:46,act:async()=>{await bubble('Detrás de los tarros de la despensa hay un frasquito azul que no pinta nada entre las conservas. Vacío.',4400);
    nar('Un frasquito escondido detrás de los tarros.<br><br><i>Mira la etiqueta con la lupa.</i>')}},
  {id:'frasquito',tool:'lupa',x:720,y:280,w:40,h:46,when:()=>found('frascoV'),act:async()=>{await bubble('La etiqueta: «Dispensario del Puerto. Sr. Arrieta. Una cucharada si hay dolor. R. S.»',4600);
    await pista('frasquito','El frasquito de la despensa','Un frasquito vacío del dispensario, escondido detrás de los tarros: «Sr. Arrieta. Una cucharada si hay dolor. R. S.».')}},
 ],
 check:()=>{const f=d5(),p=f.preg||{};if(f.salida||!f.carta||!p.comia||!p.salia||!p.nota||!found('frasquito'))return;f.salida=1;save();
   nar('Un frasquito del dispensario escondido en la despensa. Y un doctor que traía medicinas «como si fueran perfume». Hora de hacerle una visita.');
   narBtn('Ir al dispensario',async()=>{narPaso('Aitor me acompaña hasta el puerto y se queda en la taberna de enfrente, «por si acaso». El dispensario huele a éter desde la calle.');await sleep(5000);goScene(2)})},
 enter:async()=>{const f=d5();
   if(f.salida){nar('Benigna me da la espalda. Ya me ha dicho todo lo que piensa decirme.');narBtn('Ir al dispensario',()=>goScene(2));return}
   if(!f.cocina){f.cocina=1;save();nar('La puerta de servicio, a las once en punto. Aitor se queda fuera, vigilando la calle. Dentro huele a caldo y a leña.<br><br><i>Benigna está junto al fogón.</i>')}
   else nar('La cocina del palacete. Benigna barre sin mirarme.')}},

// ===== El dispensario del doctor =====
{svg:SVG.dispensario,dark:.03,tools:['mano','linterna','lupa'],cartel:'ALTAMAR<br>EL DISPENSARIO DEL PUERTO',
 ekiSpots:[
  {who:'Dr. Salazar',x:430,y:360,when:()=>!d5().solo||d5().vuelta,act:async()=>{await bubble('Eki da dos pasos hacia el doctor, olfatea el aire… y se vuelve. Aquí todo huele a éter.',4200);
    ekiLog('Dr. Salazar','NO se acerca. Huele a éter (es médico).')}},
 ],
 spots:[
  {id:'salazar',tool:'mano',x:430,y:360,r:95,once:false,when:()=>!d5().solo||d5().vuelta,act:async()=>{const f=d5();
    if(f.vuelta){await talk('Dr. Salazar','¿Algo más, querida? Si es la tos, pásese el jueves.');endTalk();return}
    await talk('Dr. Salazar','¡Mi querida detective! Pase, pase. ¿Viene a que le mire esa tos, o a hacerme preguntas?');
    await talk('Candela','Preguntas. En el despacho de Don Julián encontré una nota: «Esta noche se acaba todo. Que Dios me perdone».');
    await talk('Dr. Salazar','(Se quita las gafas y las limpia despacio.) No me sorprende. Julián estaba hundido, Candela. La fábrica, el hijo, las deudas… Un hombre puede cargar con mucho. Hasta que no puede.');
    await choose(null,null,['«Benigna dice que usted le traía medicinas.»','«¿Lo atendía usted a menudo?»']);
    await talk('Dr. Salazar','Tónicos, para el estómago y para los nervios. Lo demás es secreto médico, querida. Ni muerto se lo cuento a nadie.');
    persona('Dr. Salazar','«Julián estaba hundido.» Le daba tónicos para el estómago y los nervios; lo demás, «secreto médico».');
    if(ANIM2){allSel('.chaval',e=>e.setAttribute('opacity','1'));anima('.chaval',[{transform:'translateX(110px)'},{transform:'none'}],{duration:350,easing:'ease-out'})}
    await bubble('Un chaval asoma por la puerta: «¡Doctor! ¡En la conservera, a uno del piquete le han abierto la cabeza!».',4400);
    if(ANIM2)anima('.chaval',[{transform:'none'},{transform:'translateX(110px)'}],{duration:300,easing:'ease-in'});
    await talk('Dr. Salazar','(Coge el maletín.) El deber llama. Cinco minutos. No toque nada, que aquí hay frascos que tumban a un caballo.');endTalk();
    if(ANIM2)await anima('.docG',[{transform:'translate(0,0)'},{transform:'translate(-95px,-6px)'},{transform:'translate(-190px,0)'},{transform:'translate(-285px,-6px)',opacity:1},{transform:'translate(-380px,0)',opacity:0}],{duration:1700,easing:'linear'});
    f.solo=1;save();AU.sfx('clic');swapSvg(SVG.dispensarioV);
    nar('Me he quedado sola en el dispensario. Cinco minutos.<br><br><i>El armario de cristal, el perchero… Mira bien.</i>')}},
  {id:'armarioVer',tool:'mano',x:125,y:250,r:90,once:false,act:async()=>{const f=d5();
    if(!f.solo){await bubble('Un armario de cristal lleno de frascos. Con el doctor delante, mejor no tocar nada.',3800);return}
    if(f.vuelta){await bubble('El doctor ha vuelto. El armario, mejor ni mirarlo.',3400);return}goScene(3)}},
  {id:'impermeable',tool:'lupa',x:700,y:240,w:110,h:230,act:async()=>{await bubble('Un impermeable de mar, de hule. Todavía chorrea. Y en los pliegues hay costras blancas de sal… Esto no es de la lluvia: es agua de mar.',5000);
    await pista('impermeable','El impermeable del doctor','En el perchero del dispensario, un impermeable de mar empapado, con costras de sal. No es lluvia: es agua de mar.')}},
  {id:'diploma',tool:'lupa',x:405,y:83,w:90,h:66,act:async()=>{await bubble('«Licenciado en Medicina. Ramón Salazar Ortiz. Valladolid, 1901.» Veintiséis años de médico. Y de puerto.',4200)}},
 ],
 check:()=>{const f=d5();if(f.vuelta||!f.solo||!hasP('fichaMedica')||!found('impermeable'))return;run(vuelta5)},
 enter:async()=>{const f=d5();
   if(f.vuelta){nar('El doctor ordena su maletín y tararea algo. Ya tengo lo que venía a buscar.');narBtn('Volver a casa',()=>{narSigue=true;goScene(4)});return}
   if(f.solo){swapSvg(SVG.dispensarioV);nar(hasP('fichaMedica')?'El doctor está a punto de volver.':'Sola en el dispensario. El armario de cristal, el perchero…');return}
   nar('Azulejo blanco, frascos de colores y olor a éter. El sitio más limpio y más seguro de todo Altamar.<br><br><i>El doctor Salazar está detrás del mostrador.</i>')}},

// ===== El armario de los frascos =====
{svg:SVG.armario,pre:()=>armarioPinta(1),dark:0,tools:['mano','linterna','lupa'],
 spots:[
  ...[0,1,2,3,4,5].map(i=>({id:'fr'+i,tool:'mano',x:FR_X(i),y:290,r:44,once:false,when:()=>!d5().cajon,act:()=>frasco(i)})),
  {id:'tabla',tool:'lupa',x:740,y:200,w:104,h:176,act:async()=>{await bubble('Una hoja del recetario: «Pesas de botica». 1 escrúpulo (℈) = 24 granos · 1 dracma (ʒ) = 72 granos · 1 onza (℥) = 576 granos.',5000);
    await pista('tablaBotica','Pesas de botica','gr. = 1 grano. ℈ = 1 escrúpulo = 24 granos. ʒ = 1 dracma = 72 granos. ℥ = 1 onza = 576 granos. ½ = media, 1/10 = una décima.')}},
  {id:'fichaMedica',tool:'mano',x:370,y:432,r:70,when:()=>d5().cajon,act:async()=>{
    await docShow('<div style="text-align:left;font-size:15px;line-height:1.7"><b style="color:#8a2a20">Ficha clínica · Dispensario del Puerto</b><br>Paciente: <b>Arrieta, Julián</b>. 58 años.<br>Diagnóstico: tumor de estómago, muy avanzado.<br>Pronóstico: <u>pocos meses</u>. El paciente lo sabe.<br>Tratamiento: calmantes, según dolor.<br><i>No informar a la familia, por deseo expreso del paciente.</i><br><span style="float:right">R. S.</span></div>');
    await pista('fichaMedica','La ficha médica de Don Julián','Escondida en un cajón secreto del dispensario: Don Julián tenía un tumor de estómago y le quedaban pocos meses. Él lo sabía; su familia, no.');
    persona('Don Julián Arrieta','Estaba muy enfermo: le quedaban pocos meses de vida. Su familia no lo sabía.');
    nar('Don Julián se moría. Y lo sabía. ¿Por eso escribió «que Dios me perdone»?');narBtn('Cerrar el armario',()=>goScene(2))}},
 ],
 enter:async()=>{const f=d5();if(f.sel!=null){f.sel=null;save()}armarioPinta(1);
   if(hasP('fichaMedica')){nar('Los frascos, en su sitio. El cajón, vacío… salvo por mi conciencia.');narBtn('Cerrar el armario',()=>goScene(2));return}
   if(f.cajon){nar('Dentro del cajón hay un papel doblado.');return}
   nar('Seis frascos con las dosis en medidas antiguas de botica, cada una de su padre y de su madre. Y una tarjeta del doctor: «Cada cosa en su sitio: de más a menos, empezando por la derecha».<br><br><i>Toca un frasco y luego otro para cambiarlos de sitio.</i>');
   narBtn('Cerrar el armario',()=>goScene(2))}},

// ===== Esa noche =====
{svg:SVG.noche,dark:.35,tools:['mano','linterna','lupa'],sleep:1,laikaHome:120,ekiHome:215,cartel:'ALTAMAR<br>ESA NOCHE',
 enter:async()=>{nar(`Aitor se ha ido de ronda. Laika y Eki duermen junto al fogón.<br><br>Pistas de hoy: ${S.pistas.filter(p=>p.day===5).length}.<br>Don Julián estaba enfermo. Le quedaban meses.`);
   await sleep(5000);narAdd('Un hombre enfermo y arruinado, que escribe «que Dios me perdone»… Todo encaja con un suicidio. Demasiado bien.<br><br>Y en el despacho hay una caja fuerte que nadie ha abierto. Mañana, de vuelta al palacete.');
   narBtn('Cerrar el día',()=>{endDay();SC=null;drawCal();show('cal');bubCal('Día 5 resuelto. Mañana, la caja fuerte del palacete.')})}},
];
