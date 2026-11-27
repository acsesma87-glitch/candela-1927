// ---------- Día 2 ----------
function setText(sel,t){[base,lit,lens].forEach(c=>c.querySelectorAll(sel).forEach(e=>e.textContent=t))}
const GUARDIA_OK=['Mateo','Koldo','Bixente','Patxi'],NOMBRES=['Mateo','Koldo','Bixente','Patxi','Andoni'];
function pizarraPinta(){const a=D(2).flags.turnos||[];for(let i=0;i<4;i++)setText(`.slot[data-i="${i}"]`,a[i]||'')}
DAYS[2]=[
// ===== Periódico =====
{svg:SVG.periodico2,dark:0,tools:['mano','linterna','lupa'],cartel:'VIERNES<br>2 DE DICIEMBRE DE 1927',
 spots:[
  {id:'p2breve',tool:'lupa',x:539,y:432,w:280,h:44,act:async()=>{await bubble('«Formal, lo que se dice formal, no es.» Doña Puri, te voy a conocer. Y los estibadores, en asamblea a mediodía en el muelle…',4600)}},
  {id:'p2funeraria',tool:'lupa',x:243,y:410,w:240,h:34,act:async()=>{await bubble('Pompas fúnebres Olazabal, «discreción absoluta». En Altamar hasta los entierros guardan secretos.',4000)}},
  {id:'p2ancla',tool:'lupa',x:243,y:455,w:240,h:30,act:async()=>{await bubble('Sidrería El Ancla: «se fía a los huelguistas». Ahí debe de saberse todo lo que pasa en el puerto.',4000)}},
  {id:'p2marea',tool:'lupa',x:539,y:467,w:200,h:10,act:async()=>{await bubble('«Pleamar a las 2:10.» Cada día cambia un poco. Lo apunto, por si acaso.',3600)}},
 ],
 enter:async()=>{persona('Doña Leonor','Dicen que el seguro de vida de Don Julián se subió hace apenas un mes.');nar('Aitor deja el periódico encima de la mesa sin decir nada. Ya sale en portada.<br><br><i>Léelo bien: la letra pequeña también cuenta.</i>');narBtn('Ir al muelle',async()=>{narPaso('Los estibadores se juntan en el muelle a mediodía. Si alguien sabe qué pasa en el puerto de noche, son ellos.');await sleep(5000);next()})}},

// ===== El muelle =====
{svg:SVG.muelle,dark:.22,cartel:'ALTAMAR<br>EL MUELLE',
 ekiSpots:[
  {who:'Los estibadores',x:175,y:330,act:async()=>{await bubble('Eki va de estibador en estibador recogiendo caricias. Uno le da un trozo de pan duro.',3600);ekiLog('Los estibadores','saluda a todos, uno por uno.')}},
  {who:'Mateo',x:592,y:330,act:async()=>{await bubble('Eki se tira panza arriba a los pies de Mateo. El Rubio, muy serio, se agacha a rascarle la tripa.',3800);ekiLog('Mateo «el Rubio»','le encanta. Panza arriba y todo.')}},
 ],
 spots:[
  {id:'mateo',tool:'mano',x:592,y:330,r:60,once:false,act:async()=>{const f=D(2).flags;
    if(!f.mateo1){await talk('Mateo «el Rubio»','¿La argentina del faro? Ya me han hablado de usted. Si viene a preguntar si amenacé a Arrieta: sí. Delante de todo el puerto.');
      await talk('Mateo «el Rubio»','Murió un chaval de diecisiete años en su máquina de la conservera. Y ese hombre ni vino al entierro.');
      await talk('Candela','¿Y dónde estuvo la noche del 30?');
      await talk('Mateo «el Rubio»','En El Ancla, hasta el cierre. Pregúntele a Paco, el tabernero.');endTalk();f.mateo1=1;save();
      persona('Mateo «el Rubio»','Capataz del muelle. Amenazó a Julián en público tras la muerte de un chaval de 17 años en la conservera.');
      persona('Mateo «el Rubio»','Dice que la noche del 30 estuvo en El Ancla hasta el cierre.');
      nar('Mateo lo dice muy seguro. Demasiado seguro.<br><br><i>Mira por el muelle: la caseta, las barcas, la gente.</i>');return}
    if(f.mateoConf){await talk('Mateo «el Rubio»','Ya le he dicho lo que tenía que decirle, señorita.');endTalk();return}
    await talk('Mateo «el Rubio»','(Se cruza de brazos.) ¿Otra vez usted? ¿Qué quiere ahora?');
    const c=await choose(null,null,['¿Seguro que estuvo en El Ancla toda la noche?','Enseñarle una prueba de la libreta','Nada, gracias.']);
    if(c===0){await talk('Mateo «el Rubio»','¿Me está llamando mentiroso delante de mis hombres?');endTalk();return}
    if(c===2){endTalk();return}
    const ps=S.pistas.filter(p=>p.day<=2);const k=await choose('Candela','¿Qué prueba le enseño?',ps.map(p=>p.t));const pid=ps[k].id;
    if(pid==='guardia'||pid==='nota0'){
      await talk('Candela','Según la pizarra de la caseta, usted tenía la guardia de amarras de once a una. Y alguien apuntó que la dejó a medianoche.');
      await talk('Mateo «el Rubio»','(Baja la voz.) …Dejé la guardia a medianoche, sí. Con esa niebla nadie iba a sacar una barca. Eso pensaba.');
      await talk('Candela','¿Y adónde fue?');
      await talk('Mateo «el Rubio»','A un sitio que no es asunto suyo. Y desde luego no al faro.');endTalk();
      f.mateoConf=1;save();await pista('mateoMiente','Mateo mintió','No estuvo en El Ancla hasta el cierre: dejó la guardia de amarras a medianoche y no quiere decir adónde fue.');
      persona('Mateo «el Rubio»','Mintió: dejó la guardia a medianoche y se niega a decir adónde fue.');
      nar('Mateo mintió. Y esconde algo. Lo que no sé es si es un crimen… o otra cosa.');narBtn('Volver a casa',()=>{narSigue=true;goScene(3)})}
    else if(pid==='botas'){await talk('Mateo «el Rubio»','¿Botas claveteadas? Mire a su alrededor, señorita. Todo el puerto lleva las mismas.');endTalk()}
    else{await talk('Mateo «el Rubio»','No sé qué tiene que ver eso conmigo. No tengo nada más que decirle.');endTalk()}}},
  {id:'botas',tool:'lupa',x:592,y:468,w:64,h:16,act:async()=>{await bubble('Las botas de Mateo: suela gruesa, claveteada. Como las huellas de las rocas del faro.',3800);
    await bubble('…Y como las de todos los estibadores del muelle, eso también.',3000);
    await pista('botas','Las botas de Mateo','Suela claveteada, como las huellas del faro. Aunque todo el puerto lleva botas así.')}},
  {id:'gaviota',tool:'lupa',x:350,y:276,w:100,h:24,act:async()=>{await bubble('«GAVIOTA». Una barca de recreo, blanca, demasiado bonita para este muelle. Le falta el farol: solo queda el gancho.',4600)}},
  {id:'cajas',tool:'lupa',x:76,y:362,w:70,h:60,act:async()=>{await bubble('Cajas de CONSERVAS ARRIETA. Como las del barco de Doña Maite. Y estas tampoco parecen vacías.',4200)}},
  {id:'estibadores',tool:'mano',x:175,y:320,r:70,once:false,act:async()=>{await talk('Un estibador','Aquí no ha trabajado nadie en tres semanas, señorita. Bueno… salvo la guardia de amarras. Alguien tiene que vigilar las barcas.');endTalk()}},
  {id:'pizarraVer',tool:'mano',x:700,y:257,r:50,once:false,act:async()=>{goScene(2)}},
 ],
 laika:()=>{const f=D(2).flags;if(!f.sardina){f.sardina=1;save();return{x:76,t:'Laika ha robado una sardina de una caja. El pescadero no la ha visto. Tú sí.'}}return null},
 enter:async()=>{const f=D(2).flags;
   if(f.mateoConf){nar('Mateo mintió. Y esconde algo.');narBtn('Volver a casa',()=>{narSigue=true;goScene(3)});return}
   if(!f.muelle){f.muelle=1;save();nar('Grúas paradas, barcos sin descargar y un montón de hombres con los brazos cruzados. En el centro, un rubio con los tirantes caídos: Mateo, el capataz.')}
   else nar('El muelle sigue en silencio. La pizarra de la caseta sigue ahí.')}},

// ===== La pizarra de turnos =====
{svg:SVG.pizarra,dark:0,tools:['mano','linterna','lupa'],
 spots:[
  ...[160,222,284,346].map((y,i)=>({id:'slot'+i,tool:'mano',x:520,y:y,r:40,once:false,act:async()=>{const f=D(2).flags;if(f.turnosOk)return;
    const k=await choose('Candela',`¿Quién hacía la guardia de ${['23:00 a 1:00','1:00 a 3:00','3:00 a 5:00','5:00 a 7:00'][i]}?`,NOMBRES);endTalk();
    (f.turnos=f.turnos||[])[i]=NOMBRES[k];save();pizarraPinta();polvo(520,y);
    if(f.turnos.filter(Boolean).length===4){
      if(GUARDIA_OK.every((n,j)=>f.turnos[j]===n)){f.turnosOk=1;save();await bubble('Ahora sí: Mateo, Koldo, Bixente y Patxi. La guardia de once a una era de Mateo, justo al lado de las barcas.',4600);
        await pista('guardia','La guardia de amarras','La noche del 30, Mateo tenía la guardia de las barcas de 23:00 a 1:00. Alguien borró su nombre de la pizarra.');
        nar('Mateo vigilaba las barcas la noche del crimen. Y su nombre está borrado.<br><br><i>¿Habrá algo más en la pizarra?</i>');narBtn('Volver al muelle',()=>goScene(1))}
      else{await bubble('Algo no cuadra. Mira bien los restos de tiza con la lupa.',3000);f.turnos=[];save();pizarraPinta()}}}})),
  {id:'nota0',tool:'lupa',x:640,y:412,w:80,h:14,act:async()=>{await bubble('En la esquina, a tiza y torcido: «Mateo deja la guardia 0:00».',3600);
    await pista('nota0','Nota en la pizarra','Alguien escribió en la esquina: «Mateo deja la guardia 0:00».')}},
 ],
 enter:async()=>{pizarraPinta();nar('La pizarra de la guardia de amarras. Alguien ha borrado los nombres con la manga, pero la tiza deja rastro.<br><br><i>Toca cada hueco con la mano para escribir un nombre. La lupa ayuda.</i>');
   narBtn('Volver al muelle',()=>goScene(1))}},

// ===== Esa noche =====
{svg:SVG.noche,dark:.35,tools:['mano','linterna','lupa'],sleep:1,laikaHome:120,ekiHome:215,cartel:'ALTAMAR<br>ESA NOCHE',
 enter:async()=>{nar(`Aitor ronca en el sillón. Laika y Eki, junto al fogón.<br><br>Pistas de hoy: ${S.pistas.filter(p=>p.day===2).length}.<br>Mateo mintió… pero, ¿mintió por miedo, o por algo peor?`);
   await sleep(5000);narAdd('Paco, el de El Ancla, dice Mateo que lo vio hasta el cierre. Habrá que preguntarle.<br><br>Mañana, a la taberna El Ancla.');
   narBtn('Cerrar el día',()=>{endDay();SC=null;drawCal();show('cal');bubCal('Día 2 resuelto. Mañana, a la taberna El Ancla.')})}},
];
FACES['Mateo «el Rubio»']=FACE_MATEO;FACES['Un estibador']=FACE_EST;
