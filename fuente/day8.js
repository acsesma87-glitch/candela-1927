// ---------- Día 8 ----------
const d8=()=>D(8).flags;
// --- la carta rota: 8 trozos; se arrastran al marco y se giran con dos toques ---
const TROZO_INI=[[10,10,1],[600,10,2],[240,290,3],[90,22,0],[700,120,1],[520,335,2],[10,104,3],[430,296,1],[690,30,3],[140,330,2],[620,200,0],[100,112,2],[330,330,1],[40,300,3],[610,110,2],[20,196,0],[706,214,2],[620,300,1],[240,400,3]],TW=72,TH=66,TX=220,TY=50,NTZ=15;
const TROZO_ID=JSON.stringify(TROZO_INI);
function trozos(){const f=d8();if(!f.tz||f.tzId!==TROZO_ID){f.tz=TROZO_INI.map(p=>({x:p[0],y:p[1],r:p[2],ok:0}));f.tzId=TROZO_ID;f.orden8=TROZO_INI.map((_,i)=>i);save()}return f.tz}
function trozosPinta(sel,dx,dy){const t=trozos();t.forEach((p,i)=>{let x=p.x,y=p.y;if(i===sel){x+=dx;y+=dy}
  allSel(`.trozo[data-i="${i}"]`,e=>{e.style.transition=i===sel?'none':'';e.style.transform=`translate(${x}px,${y}px) rotate(${p.r*90}deg)`;e.style.transformOrigin='36px 33px'})});
  // el último que se tocó, encima
  [base,lit,lens].forEach(c=>{const g=c.querySelector('.trozo')&&c.querySelector('.trozo').parentNode;if(!g)return;d8().orden8.forEach(i=>{const e=g.querySelector(`.trozo[data-i="${i}"]`);if(e)g.appendChild(e)})})}
let tzA=null,tzTap={i:-1,t:0};
document.addEventListener('pointerdown',e=>{if(!SC||SC.svg!==SVG.carta||busy||d8().carta)return;const[x,y]=rel(e),t=trozos(),o=d8().orden8;
  for(let k=o.length-1;k>=0;k--){const i=o[k],p=t[i];if(p.ok)continue;if(Math.abs(x-(p.x+36))<38&&Math.abs(y-(p.y+33))<36){tzA={i,x0:x,y0:y,dx:0,dy:0};o.splice(k,1);o.push(i);trozosPinta(i,0,0);return}}},true);
document.addEventListener('pointermove',e=>{if(!tzA)return;const[x,y]=rel(e);tzA.dx=x-tzA.x0;tzA.dy=y-tzA.y0;trozosPinta(tzA.i,tzA.dx,tzA.dy)},true);
document.addEventListener('pointerup',()=>{if(!tzA)return;const a=tzA;tzA=null;const t=trozos(),p=t[a.i],now=performance.now();
  if(Math.hypot(a.dx,a.dy)<8){if(tzTap.i===a.i&&now-tzTap.t<400){p.r=(p.r+1)%4;AU.sfx('papel');tzTap.i=-1}else tzTap={i:a.i,t:now}}
  else{p.x=Math.max(0,Math.min(728,p.x+a.dx));p.y=Math.max(0,Math.min(434,p.y+a.dy));tzTap.i=-1}
  const gx=TX+(a.i%5)*TW,gy=TY+Math.floor(a.i/5)*TH;
  if(a.i<NTZ&&p.r===0&&Math.abs(p.x-gx)<20&&Math.abs(p.y-gy)<20){p.x=gx;p.y=gy;p.ok=1;AU.sfx('clic')}
  save();trozosPinta();if(t.slice(0,NTZ).every(q=>q.ok)&&!d8().carta)run(cartaEntera)},true);
async function cartaEntera(){const f=d8();f.carta=1;save();$('#acts').innerHTML='';await sleep(500);
  await docShow('<div style="text-align:left;font-size:16px;line-height:1.8;font-style:italic;color:#1e2a4a">Lola:<br>Esta noche se acaba todo. Ya no puedo seguir con esta mentira. Te espero en el faro a la una, para despedirme como Dios manda. Lo de la niña está arreglado: pase lo que pase, no os faltará de nada.<br><span style="float:right">J. · 30 de noviembre</span></div>');
  await pista('cartaLola','La carta rota de Lola','Don Julián a Lola, el 30 de noviembre: «Esta noche se acaba todo… Te espero en el faro a la una, para despedirme como Dios manda. Lo de la niña está arreglado».');
  await bubble('«Esta noche se acaba todo»… ¡La misma frase del bloc del despacho! No era una nota de suicidio: era el borrador de esta carta.',5200);
  await pista('noSuicidio','No era una nota de suicidio','La frase del bloc («Esta noche se acaba todo. Que Dios me perdone») era el borrador de la carta a Lola. Don Julián pensaba despedirse de ella, no matarse.');
  persona('Lola','Julián la citó en el faro a la una de la madrugada del 30 de noviembre «para despedirse». Ella dice que esa noche ni lo vio.');
  nar('Don Julián no pensaba matarse. Pensaba despedirse de Lola… en el faro, a la una.');narBtn('Enseñarle la carta a Lola',()=>goScene(2))}
function trozosReinicia(){const f=d8();f.tzId=null;save();trozos();trozosPinta()}

DAYS[8]=[
// ===== Periódico =====
{svg:SVG.periodico8,dark:0,tools:['mano','linterna','lupa'],cartel:'JUEVES<br>8 DE DICIEMBRE DE 1927',
 spots:[
  {id:'p8royal',tool:'lupa',x:243,y:410,w:240,h:34,act:async()=>{await bubble('«LOLA canta para usted. Entrada discreta.» Lola. «L.»',3800)}},
  {id:'p8sastre',tool:'lupa',x:243,y:455,w:240,h:30,act:async()=>{await bubble('«Lutos en veinticuatro horas.» En Altamar, el luto es buen negocio esta semana.',4000)}},
  {id:'p8breve',tool:'lupa',x:539,y:432,w:280,h:44,act:async()=>{persona('Comisario Ibarra','Según los «Ecos del barrio», un comisario frecuenta la calle del Farol «por razones de servicio».');
    await bubble('¿Un comisario que frecuenta la calle del Farol? «Por razones de servicio». Ya.',4200)}},
  {id:'p8marea',tool:'lupa',x:539,y:467,w:200,h:10,act:async()=>{await bubble('«Luna menguante. Pleamar a las 6:10.»',3000)}},
 ],
 enter:async()=>{persona('Don Fermín Olaso','El capitán del puerto. Presiona para que el caso se cierre «de una vez» como un accidente.');
   nar('Jueves, día de la Inmaculada. Aitor ha dormido de un tirón por primera vez en una semana. Le despierto con el periódico y una pregunta: ¿me llevas esta noche a la calle del Farol?<br><br><i>Léelo bien: la letra pequeña también cuenta.</i>');
   narBtn('Ir a la calle del Farol',async()=>{narPaso('Al caer la noche, Aitor me lleva por callejones que no salen en ningún mapa. «Tú no te separes de mí», dice, muy serio.');await sleep(5000);goScene(1)})}},

// ===== La calle del Farol =====
{svg:SVG.calleFarol,dark:.06,tools:['mano','linterna','lupa'],cartel:'ALTAMAR<br>LA CALLE DEL FAROL',
 laika:()=>d8().colonia?null:(d8().colonia=1,save(),{x:430,t:'Laika olfatea un charco junto al portal y estornuda tres veces seguidas. Colonia barata, de la de litro.'}),
 spots:[
  {id:'portero',tool:'mano',x:270,y:330,r:80,once:false,act:async()=>{const f=d8();
    if(f.dentro){await talk('El portero','Por la de atrás, he dicho. La de los artistas.');endTalk();return}
    await talk('El portero','(Se cruza de brazos.) Señora, esto no es sitio para una dama decente.');
    for(;;){const c=await choose('Candela','(¿Cómo entro?)',['«Vengo a ver a Lola.»','«Soy de la policía.»','Dejar que hable Aitor.']);
      if(c===0){await talk('El portero','Todos vienen a ver a Lola, señora. Pagando.');continue}
      if(c===1){await talk('El portero','(Se ríe.) Y yo, el obispo. La policía aquí entra por la puerta de atrás… y sin decir que es policía.');continue}
      break}
    await talk('Aitor','Txato. Que viene conmigo.');
    await talk('El portero','(Le mira, suspira.) Por ti, sereno, que me sacaste del calabozo aquel invierno. Por la puerta de atrás, la de los artistas. Y no armen jaleo.');endTalk();
    f.dentro=1;save();nar('La puerta de los artistas da a un pasillo estrecho que huele a polvos de arroz y a tabaco. Al fondo, una puerta con una estrella pintada: «Lola».');
    narBtn('Ir al camerino de Lola',()=>goScene(2))}},
  {id:'senoritas',tool:'mano',x:495,y:360,r:60,once:false,act:async()=>{await talk('Una señorita','(Echa el humo despacio.) ¿Buscas trabajo, guapa? Con ese acento, aquí arrasarías… (Mira a Aitor y se ríe.) Ah, que vienes con el sereno. Pues nada.');endTalk()}},
  {id:'aitor8',tool:'mano',x:80,y:340,r:60,once:false,act:async()=>{await talk('Aitor','Aquí los serenos no vemos nada. Es lo que se espera de nosotros.');endTalk()}},
 ],
 enter:async()=>{const f=d8();if(f.dentro){nar('La puerta de los artistas.');narBtn('Ir al camerino de Lola',()=>goScene(2));return}
   nar('La calle del Farol. Farolas rojas, un piano desafinado y señoritas fumando en los portales. En la puerta del Café Royal, un portero como un armario.')}},

// ===== El camerino de Lola =====
{svg:SVG.camerino,dark:.1,tools:['mano','linterna','lupa'],
 ekiSpots:[
  {who:'Lola',x:340,y:330,act:async()=>{await bubble('Eki se acerca a Lola, olfatea sus zapatos de tacón y le apoya la cabeza en la rodilla. Lola, sorprendida, le rasca detrás de las orejas.',4600);ekiLog('Lola','le cae bien: se deja rascar detrás de las orejas.')}},
 ],
 spots:[
  {id:'lola',tool:'mano',x:190,y:330,r:75,once:false,act:async()=>{const f=d8();
    if(!f.lola1){await talk('Lola','(Sin dejar de empolvarse frente al espejo.) ¿Y tú quién eres? ¿La nueva? No, tú no eres de aquí. Ese acento…');
      await talk('Candela','Vengo por Don Julián Arrieta.');
      await talk('Lola','(Se le para la mano un segundo.) ¿Julián? Hace semanas que no venía. Esa noche ni lo vi.');
      await talk('Lola','Aquí todas somos «artistas», señorita. Unas cantamos mejor que otras. Y ahora, si me disculpa, salgo en diez minutos.');endTalk();
      f.lola1=1;save();persona('Lola','Dice que Julián «hace semanas que no venía» y que esa noche ni lo vio.');return}
    if(f.confesion){await talk('Lola','Ya le he dicho todo. Váyase.');endTalk();return}
    await talk('Lola','Diez minutos, he dicho.');endTalk()}},
  {id:'foto',tool:'lupa',x:455,y:80,w:50,h:60,act:async()=>{await bubble('Metida en el marco del espejo, una foto: Don Julián, sonriendo como nunca le he visto, con una niña pequeña en brazos.',4800);
    await pista('foto8','La foto del espejo','En el camerino de Lola, una foto de Don Julián con una niña pequeña en brazos.')}},
  {id:'dibujo',tool:'mano',x:132,y:108,r:60,once:false,act:async()=>{
    await docShow('<div style="font-size:18px;line-height:1.6;color:#3050a0;font-family:\'Comic Sans MS\',cursive">Para mamá y papá<br><span style="font-size:14px">Julia · 8 años</span></div>');
    if(hasP('dibujo8'))return;await pista('dibujo8','El dibujo de la niña','Un dibujo infantil en la pared del camerino: «Para mamá y papá — Julia, 8 años». La niña del testamento.')}},
  {id:'papelera',tool:'linterna',x:472,y:420,w:90,h:70,act:async()=>{await bubble('Debajo del tocador hay una papelera… y dentro, una carta hecha pedazos.',3600)}},
  {id:'trozosVer',tool:'mano',x:472,y:420,r:55,once:false,when:()=>found('papelera'),act:async()=>{if(d8().carta){await bubble('Ya he recompuesto la carta.',2400);return}goScene(3)}},
 ],
 check:()=>{const f=d8();if(f.confesion||!f.carta||!found('foto')||!hasP('dibujo8'))return;run(confiesa8)},
 enter:async()=>{const f=d8();if(f.salida){nar('Fuera de aquí.');narBtn('Volver a casa',()=>{narSigue=true;goScene(4)});return}
   nar(f.lola1?'Lola se pinta los labios frente al espejo. Me vigila por el reflejo.':'El camerino de Lola: espejo con bombillas, vestidos de lentejuelas, olor a polvos de arroz. Ella, sentada frente al espejo, ni se vuelve.')}},

// ===== La carta rota =====
{svg:SVG.carta,dark:0,tools:['mano','linterna','lupa'],
 enter:async()=>{const f=d8();if(f.carta){goScene(2);return}trozosPinta();
   nar('Los trozos de la carta, mezclados con los de otro papel, sobre el tocador.<br><br><i>Arrastra cada trozo a su sitio dentro del marco. Toca dos veces un trozo para girarlo.</i>');
   narBtn('Dejarlo para luego',()=>goScene(2));const b=document.createElement('button');b.className='go';b.textContent='Revolver los trozos otra vez';b.onclick=trozosReinicia;$('#acts').appendChild(b)}},

// ===== En casa: atar cabos con Aitor =====
{svg:SVG.cocinaMesa,dark:.05,laikaHome:560,ekiHome:150,cartel:'ALTAMAR<br>CASA DEL SERENO',
 enter:async()=>{const f=d8();
   if(!f.cabos){nar('Aitor enciende la estufa y pone dos tazas de caldo en la mesa. Laika y Eki se arriman al calor.');await sleep(1200);
     await talk('Aitor','(Sopla el caldo.) A ver, detective. La nota del bloc, la de «que Dios me perdone»… ¿qué era, entonces?');
     for(;;){const c=await choose(null,null,['Una nota de suicidio','El borrador de su carta a Lola','Una confesión de algo que había hecho']);
       if(c===1){await talk('Aitor','El borrador de la carta. «Esta noche se acaba todo»: lo suyo con Lola, no su vida.');break}
       await talk('Aitor',c===0?'¿Suicidio? Si iba al faro a despedirse y a dejarle a la niña bien atada…':'Confesión… no. Fíjate en la carta rota: es la misma frase.');
       await talk('Aitor','Piénsalo otra vez.')}
     await talk('Aitor','Ahora lo gordo. Si todo Altamar cree que se tiró… ¿quién sale ganando?');
     for(;;){const c=await choose(null,null,['Lola','Quien lo hubiera matado','Don Julián']);
       if(c===1){await talk('Aitor','Eso es. Un suicidio no se investiga. Un asesinato, sí.');break}
       await talk('Aitor',c===0?'¿Lola? Lola pierde: se queda sin él y sin despedida.':'¿Don Julián? Ese ya no gana nada, mujer.');
       await talk('Aitor','Otra vez.')}
     await talk('Candela','Y Lola sabe algo más, Aitor. Lo llevaba en la cara.');
     await talk('Aitor','En la calle del Farol aprenden a callar antes que a cantar. Ya hablará. Dale tiempo.');endTalk();
     f.cabos=1;save();await pista('cabos8','Atando cabos con Aitor','La nota del bloc era el borrador de la carta a Lola, no una nota de suicidio. Si parecía un suicidio, el que salía ganando era quien lo hubiera matado.')}
   nar('El caldo se enfría en las tazas. Fuera, empieza a llover.');narBtn('Irse a dormir',()=>goScene(5))}},

// ===== Esa noche =====
{svg:SVG.noche,dark:.35,tools:['mano','linterna','lupa'],sleep:1,laikaHome:120,ekiHome:215,cartel:'ALTAMAR<br>ESA NOCHE',
 enter:async()=>{nar(`Aitor ha salido de ronda. Laika y Eki duermen junto al fogón.<br><br>Pistas de hoy: ${S.pistas.filter(p=>p.day===8).length}.<br>«Esta noche se acaba todo» no era una despedida del mundo. Era una despedida para Lola.`);
   await sleep(5000);narAdd('Don Julián iba al faro a la una a despedirse de Lola y de su hija. No pensaba matarse.<br><br>Entonces… ¿quién quería que pareciera un suicidio?');
   narBtn('Cerrar el día',()=>{endDay();SC=null;drawCal();show('cal');bubCal('Día 8 resuelto. El suicidio ya no se sostiene.')})}},
];
async function confiesa8(){const f=d8();f.confesion=1;save();
  await talk('Candela','(Le dejo la carta recompuesta sobre el tocador.) «Te espero en el faro a la una.» Usted sí lo vio esa noche, Lola. O lo esperó.');
  await talk('Lola','(Mira la carta mucho rato. Se le corre el rímel.) Sí. Le esperaba en el faro. Iba a despedirse de mí, de nosotras… y no vino.');
  await talk('Lola','Me cansé de esperar y me volví. Eso es todo. Eso es todo, ¿me oye?');
  await talk('Candela','(Lo repite dos veces. Como quien se lo quiere creer.)');
  await talk('Madame Odette','(Abriendo la puerta de golpe.) ¡Lola, a escena! Y usted, señorita, fuera de mi casa. Aquí no se viene a hacer llorar a mis artistas.');endTalk();
  persona('Lola','Confiesa que esperó a Julián en el faro a la una y que «no vino». Insiste demasiado en que se volvió y «eso es todo».');
  f.salida=1;save();
  nar('Volvemos por los callejones sin decir nada. Detrás, el piano del Café Royal empieza una canción triste.');narBtn('Volver a casa',()=>{narSigue=true;goScene(4)})}
FACES['Lola']=FACE_LOLA;FACES['El portero']=FACE_PORTERO;
