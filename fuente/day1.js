// ---------- Día 1 ----------
DAYS[1]=[
// ===== Escena 0 · Portada del periódico =====
{svg:SVG.periodico,dark:0,tools:['mano','linterna','lupa'],cartel:'JUEVES<br>1 DE DICIEMBRE DE 1927',
 spots:[
  {id:'breve',tool:'lupa',x:539,y:420,w:280,h:62,act:async()=>{await bubble('«El sereno de Altamar espera hoy la visita de una señorita argentina…» Mirá vos. Y Doña Puri preguntando si soy formal. Ya le contaré yo.',5200)}},
  {id:'jarabe',tool:'lupa',x:243,y:408,w:240,h:36,act:async()=>{await bubble('«Jarabe del Dr. Salazar: para la tos, los nervios y el insomnio.» Un médico que se anuncia como un tónico milagroso. Qué cosa.',4600)}},
  {id:'mozo',tool:'lupa',x:243,y:454,w:240,h:34,act:async()=>{await bubble('«Se busca mozo para la conservera. Abstenerse huelguistas.» Ni disimulan.',3600)}},
  {id:'huelga',tool:'lupa',x:243,y:338,w:250,h:72,act:async()=>{persona('Mateo «el Rubio»','Capataz del muelle y cabeza de la huelga: «Sin seguridad en la conservera, no hay descarga».');await bubble('Mateo «el Rubio», capataz del muelle. «Sin seguridad en la conservera, no hay descarga.» Un hombre con motivos para odiar a Arrieta.',4800)}},
  {id:'conservera',tool:'lupa',x:539,y:332,w:280,h:72,act:async()=>{persona('Íñigo Arrieta','El hijo de Don Julián. El periódico dice que anoche estaba en el Casino «de excelente humor», con la empresa de su padre en la ruina.');await bubble('La conservera no paga desde octubre… y el hijo, Íñigo, anoche en el Casino «de excelente humor». Con la empresa del padre en la ruina. Mirá vos.',5200)}},
  {id:'marea',tool:'lupa',x:539,y:467,w:200,h:10,act:async()=>{await bubble('«Pleamar a la 1:30.» No sé por qué, pero lo apunto en la cabeza.',3600)}},
 ],
 enter:async()=>{nar('En el asiento del Topo, alguien ha dejado el periódico de hoy. Lo hojeo mientras el tren entra en Donostia.<br><br><i>La letra pequeña se lee con la lupa.</i>');
   narBtn('Pasar la página',next)}},

// ===== Escena 1 · La estación del Topo =====
{svg:SVG.topo,dark:.28,laikaHome:395,laikaStand:1,cartel:'DONOSTIA<br>ESTACIÓN DEL TOPO',
 spots:[
  {id:'aitor',tool:'mano',x:690,y:250,r:80,glow:()=>!D(1).flags.saludo,act:async()=>{
    const f=D(1).flags;
    if(f.saludo){await talk('Aitor','Vamos, que en casa hay café. Y alguien que se muere por conocerte.');endTalk();return}
    const c=await choose('Candela','Gorra, farol, chuzo… y cara de no haber dormido. Es él. ¿Cómo lo saludo?',['«¿Aitor?»','Darle la mano, muy formal','Abrazarlo sin pensar']);
    if(c===0)await talk('Aitor','El mismo. Bueno… el sereno de Altamar, para servirte.');
    if(c===1)await talk('Aitor','(Te estrecha la mano muy serio… y luego se ríe.) Qué formales somos los dos.');
    if(c===2)await talk('Aitor','(Se queda rígido un segundo, con el farol en una mano y el chuzo en la otra. Luego te abraza.) …Hola.');
    await talk('Aitor','Tú debes de ser Candela. Escribes mejor de lo que yo hablo.');
    await talk('Aitor','Vivo en Altamar, el barrio del puerto. Para el resto de Donostia somos «los de abajo». Ya verás: tiene su encanto… y sus cosas raras.');
    endTalk();f.saludo=true;save();
    persona('Aitor','El sereno de Altamar. Me esperaba en el andén del Topo, con el farol todavía encendido.');
    persona('Aitor','Dice que Altamar «tiene su encanto… y sus cosas raras».');
    nar('Aitor me coge la maleta antes de que pueda decir nada. Laika lo huele de arriba abajo y decide que aprueba.');
    narBtn('Ir a casa',async()=>{narPaso('Bajamos hacia el puerto. Las calles se estrechan, huele a sardina y a carbón, y la gente saluda a Aitor por su nombre…');await sleep(5000);next()})}},
  {id:'chapa',tool:'lupa',x:690,y:130,act:async()=>{await bubble('En la chapa de la gorra: «SERENO · 7». El siete. Me gusta.',3800)}},
  {id:'letrero',tool:'lupa',x:575,y:142,act:async()=>{await bubble('«TOPO · Frontera – San Sebastián». Un tren que va por la calle como un tranvía. En La Plata no me lo creerían.',4400)}},
 ],
 laika:()=>D(1).flags.ladra?null:(D(1).flags.ladra=1,save(),{x:180,t:'Laika le ladra al Topo. El Topo pita. Laika se lo piensa mejor.'}),
 enter:async()=>{nar('Un tren que va por la calle como un tranvía. Laika lo mira con desconfianza. Yo busco entre la gente a alguien a quien solo conozco por su letra…<br><br><i>Toca a la gente con la mano para hablar.</i>');
   if(D(1).flags.saludo)narBtn('Ir a casa',next)}},

// ===== Escena 2 · La casa de Aitor y Eki =====
{svg:SVG.cocina,dark:.22,laikaHome:560,cartel:'ALTAMAR<br>CASA DEL SERENO',ekiHome:150,
 ekiSpots:[
  {who:'Aitor',x:380,y:260,act:async()=>{const f=D(1).flags;
    if(!f.ekiTut){await bubble('Eki va a saludar a Aitor, pero cambia de idea a medio camino…',3000);await ekiToCandela();return}
    await bubble('Eki le pone la cabeza en la rodilla a Aitor. Él le rasca detrás de las orejas sin dejar de mirarte.',3600);ekiLog('Aitor','le cae bien, de toda la vida.')}},
  {who:'Candela',x:628,y:330,act:async()=>{const f=D(1).flags;if(!f.ekiTut){await ekiToCandela();return}
    await bubble('Eki te da la pata otra vez. Y otra. Y otra.',2800)}},
 ],
 spots:[
  {id:'ronda',tool:'lupa',x:400,y:329,w:70,h:18,act:async()=>{
    await docShow('<div style="text-align:left;font-size:16px;line-height:1.7"><b style="color:#8a2a20">Cuaderno de ronda · noche del 30 de noviembre</b><br>23:40 — Cierra El Ancla. Mateo «el Rubio» sale de los últimos.<br>0:30 — Cierro la verja del faro. Todo en orden.<br><u>1:10 — Motor de barca hacia el faro, sin luces.</u><br>3:00 — La señora Puri no encuentra la llave. Otra vez.<br>5:50 — Niebla cerrada. Fin de ronda.</div>');
    await pista('ronda','Cuaderno de ronda de Aitor','«1:10, motor de barca hacia el faro, sin luces». Y a las 0:30 cerró la verja del faro.');
    nar('Una barca sin luces hacia el faro a la una y diez de la noche. ¿Quién sale a pescar a esas horas, y a oscuras?')}},
  {id:'tablon',tool:'lupa',x:300,y:128,w:160,h:110,act:async()=>{await bubble('Son mis cartas. Todas. La primera tiene una mancha de café.',3000);
    await talk('Aitor','(Se pone colorado.) La he leído tantas veces que se ha gastado.');endTalk()}},
  {id:'moneda',tool:'lupa',x:498,y:331,act:async()=>{D(1).flags.moneda=1;save();
    await bubble('Una moneda dorada. Con la lupa se lee: «PortAventura». Una ficha de feria rarísima: no conozco ningún sitio con ese nombre.',4600);
    await talk('Aitor','Es mi moneda de la suerte. (Y no suelta prenda.)');endTalk();
    persona('Aitor','Tiene una moneda de la suerte que pone «PortAventura». No quiere contar de dónde la sacó.')}},
  {id:'galletas',tool:'linterna',x:759,y:270,act:async()=>{await bubble('En lo más alto de la despensa, escondida: una lata roja de GALLETAS. Eki la mira con una devoción casi religiosa.',4400)}},
  {id:'aitorHabla',tool:'mano',x:380,y:262,r:70,once:false,act:async()=>{
    const asked=D(1).flags.q||(D(1).flags.q={});
    while(true){const o=[];
      if(!asked.raras)o.push(['raras','¿Qué cosas raras pasan en el puerto?']);
      if(!asked.noche)o.push(['noche','¿Siempre trabajas de noche?']);
      if(!asked.preg)o.push(['preg','¿Qué era eso que querías preguntarme en persona?']);
      o.push(['fin','Nada, tomate el café.']);
      const c=await choose('Candela','(Aitor sopla el café. Te mira por encima de la taza.)',o.map(x=>x[1]));const k=o[c][0];
      if(k==='fin')break;asked[k]=1;save();
      if(k==='raras'){await talk('Aitor','Barcas que salen de noche sin luces. Y una con un farol verde que no es de ningún pescador que yo conozca.');persona('Aitor','Ve barcas que salen de noche sin luces, y una con un farol verde.')}
      if(k==='noche')await talk('Aitor','De noche Altamar es otro barrio. Más honrado, a veces. Otras, mucho menos.');
      if(k==='preg')await talk('Aitor','(Se pone rojo hasta las orejas.) A… su debido tiempo.');}
    endTalk()}},
 ],
 laika:()=>D(1).flags.silla?null:(D(1).flags.silla=1,save(),{x:330,t:'Laika se ha subido a la silla de Aitor. Aitor se sienta en el suelo sin rechistar.'}),
 check:()=>{const f=D(1).flags;if(f.knock||!f.ekiTut||!found('ronda'))return;f.knock=1;save();run(knock)},
 enter:async()=>{const f=D(1).flags;
   if(!f.ekiTut){unlockTool('eki');nar('Eki levanta las orejas. Me mira. Yo la miro…<br><br><i>Pulsa el botón de Eki y toca a una persona.</i>')}
   else if(f.knock){if(ANIM2)allSel('.txoP',e=>e.setAttribute('opacity','1'));nar('Txomin espera en la puerta, sin aliento.');narBtn('Salir corriendo',next)}
   else nar('La cocina huele a café y a leña. Aitor tiene su cuaderno de ronda abierto encima de la mesa.')}},

// ===== Escena 3 · El portal =====
{svg:SVG.portal,dark:.8,
 spots:[
  {id:'papel',tool:'linterna',x:505,y:460,act:async()=>{await bubble('Algo blanco asoma por debajo del felpudo. La esquina de un papel.',3000);nar('Hay un papel debajo del felpudo.<br><br><i>Tócalo con la mano para cogerlo.</i>')}},
  {id:'coger',tool:'mano',x:505,y:462,r:55,when:()=>found('papel'),once:false,act:async()=>{next()}},
  {id:'felpudo',tool:'mano',x:455,y:468,r:60,when:()=>!found('papel'),once:false,act:async()=>{await bubble('Está demasiado oscuro para ver qué he pisado.',2200)}},
 ],
 laika:()=>({x:430,t:'Laika olfatea el felpudo y estornuda.'}),
 enter:async()=>{nar('Aitor ya va por la escalera. Yo me paro. Juraría que he pisado algo…<br><br><i>Está muy oscuro. Usa la linterna.</i>');setTool('linterna',1);
   if(found('papel'))nar('Hay un papel debajo del felpudo.<br><br><i>Tócalo con la mano para cogerlo.</i>')}},

// ===== Escena 3b · La nota =====
{svg:SVG.nota,dark:0,tools:['mano','linterna','lupa'],
 spots:[
  {id:'eta',tool:'lupa',x:600,y:92,w:60,h:50,act:async()=>{
    await bubble('Papel caro, de carta. Y la esquina recortada con tijeras: en el borde queda media palabra impresa, «…ETA».',4400);
    await pista('nota','La nota del portal','«NO FUE UN SUICIDIO. QUE LO MIRE LA ARGENTINA.» Papel de carta bueno, con el membrete recortado: queda «…ETA».');
    objeto({id:'nota',i:'✉️',t:'Nota anónima',d:'«NO FUE UN SUICIDIO. QUE LO MIRE LA ARGENTINA.» Membrete recortado: «…ETA».'});
    nar('Alguien ha recortado el membrete. Alguien de una casa con papel bueno…');narBtn('Al faro',alFaro)}},
 ],
 enter:async()=>{const f=D(1).flags;
   nar('Mayúsculas a lápiz. Escritas despacio, para que no se reconozca la letra.');
   if(!f.notaAitor){await sleep(900);
     await talk('Aitor','(Sube de dos en dos al oírte.) ¿Qué es eso? …¿Suicidio? Si el chaval acaba de decir que lo han encontrado. ¿Cómo sabe nadie lo que va a decir la policía?');
     await talk('Candela','(Me guardo la nota en la gabardina.) Eso mismo me pregunto yo.');endTalk();f.notaAitor=1;save();
     objeto({id:'nota',i:'✉️',t:'Nota anónima',d:'«NO FUE UN SUICIDIO. QUE LO MIRE LA ARGENTINA.»'})}
   nar('Mayúsculas a lápiz. Escritas despacio, para que no se reconozca la letra.<br><br><i>Mírala bien antes de irte.</i>');
   if(found('eta'))narBtn('Al faro',alFaro)}},

// ===== Escena 4 · El faro =====
{svg:SVG.faro,dark:.45,cartel:'ALTAMAR<br>EL FARO',
 ekiSpots:[
  {who:'El guardia',x:190,y:300,act:async()=>{await bubble('Eki va corriendo a saludar al guardia. Él, muy serio, le rasca detrás de las orejas.',3400);ekiLog('El guardia civil','saludo y rascada de orejas.')}},
  {who:'El comisario',x:532,y:300,act:async()=>{await bubble('Eki va derecha al comisario y le olisquea los bolsillos del gabán. Parece que le ha caído bien.',3600);ekiLog('Comisario Ibarra','le cae bien (sobre todo sus bolsillos).')}},
  {who:'El doctor',x:450,y:350,act:async()=>{await bubble('Eki se para a dos pasos del doctor. No se acerca. Vuelve y te da la pata para que la toques.',3800);
    await bubble('Al pasar a su lado notas olor a hospital, a éter. Normal: es médico.',3200);ekiLog('Dr. Salazar','NO se acerca. Huele a éter (es médico).')}},
  {who:'Doña Leonor',x:598,y:375,r:100,when:()=>D(1).flags.leonor,act:async()=>{await bubble('Eki tampoco se acerca a Doña Leonor. Se sienta y te mira para que le hagas caso.',3600);
    await bubble('El abrigo de luto huele muchísimo a naftalina.',2800);ekiLog('Doña Leonor','NO se acerca. Huele a naftalina.')}},
 ],
 spots:[
  {id:'algas',tool:'drag',el:'algas',x:222,y:420,r:50,dist:60,hint:'Hay algas tapando la mano. Arrástralas con el dedo hacia un lado.',act:async()=>{await bubble('Debajo de las algas, la mano del muerto. Tiene algo rojo entre los dedos.',3200);nar('La mano aprieta algo rojo, pequeño.<br><br><i>Míralo con la lupa.</i>')}},
  {id:'ficha',tool:'lupa',x:222,y:416,w:30,h:20,when:()=>found('algas'),act:async()=>{await bubble('Una ficha del Casino. Donde estaba su hijo Íñigo anoche, «de excelente humor», según el periódico.',4000);
    await pista('ficha','La ficha del Casino','Una ficha roja del Casino de Altamar, con una «C», apretada en la mano del muerto. Íñigo, el hijo, estuvo anoche en el Casino.');faroCheck()}},
  {id:'bajos',tool:'lupa',x:444,y:398,w:70,h:18,act:async()=>{await bubble('Los bajos del pantalón del doctor: empapados de agua de mar, con arena y un hilo de alga.',3600);
    await talk('Dr. Salazar','(Se da cuenta de que lo mira.) Las rocas, querida. Para atender a un muerto hay que mojarse los pies.');endTalk();
    await pista('bajos','El pantalón del doctor','Los bajos, mojados de mar, con arena y un hilo de alga. Dice que se mojó al bajar a las rocas.');faroCheck()}},
  {id:'huellas',tool:'linterna',x:90,y:452,w:150,h:50,act:async()=>{await bubble('En las rocas todavía a oscuras: pisadas de bota grande, de suela claveteada, que salen del agua y van hacia el cuerpo. Botas de trabajo, como las de los estibadores.',4800);
    await pista('huellas','Huellas en las rocas','Pisadas de bota claveteada, como las de los estibadores, que salen del agua y van hacia el cuerpo. El puerto está en huelga contra Arrieta…');faroCheck()}},
  {id:'verja',tool:'lupa',x:636,y:306,w:40,h:34,act:async()=>{await bubble('El candado de la verja está abierto. No forzado. Quien lo abrió tenía la llave.',3600);
    await bubble('Miro a Aitor. Aitor mira al suelo.',2600);
    await pista('verja','La verja del faro','El candado está abierto, no forzado. Quien lo abrió tenía la llave. Y la llave la tiene Aitor.');faroCheck()}},
  {id:'doctor',tool:'mano',x:448,y:340,r:72,once:false,act:async()=>{const f=D(1).flags;
    if(!f.informe){await talk('Dr. Salazar','¡Vaya! Usted debe de ser la famosa argentina. Doctor Ramón Salazar, para servirla. Mi querida colega aficionada…');
      await talk('Dr. Salazar','(Saca un papel del maletín y lo lee en voz alta.) «Suicidio. Muerte por la caída, hacia las tres de la madrugada.» Pobre Julián. Estaba hundido.');
      await talk('Dr. Salazar','Si necesita cualquier cosa, el dispensario del puerto está siempre abierto. Para usted, también.');endTalk();
      f.informe=1;save();persona('Dr. Salazar','Médico del dispensario del puerto. Muy amable conmigo: me llama «mi querida colega aficionada».');
      await pista('informe','El informe del doctor','«Suicidio. Muerte por la caída, hacia las tres de la madrugada.» Firmado: Dr. R. Salazar.');faroCheck()}
    else{await talk('Dr. Salazar','No se canse, querida. A veces las cosas son exactamente lo que parecen.');endTalk()}}},
  {id:'comisario',tool:'mano',x:532,y:300,r:95,once:false,act:async()=>{await talk('Comisario Ibarra','Estaba arruinado. Se tiró. Caso cerrado antes del almuerzo.');endTalk();persona('Comisario Ibarra','Quiere cerrar el caso como suicidio «antes del almuerzo».')}},
  {id:'guardia',tool:'mano',x:190,y:290,r:90,once:false,act:async()=>{await talk('El guardia','(Apenas habla.) Lo encontraron los pescadores. A las seis y cuarenta.');
    if(!found('algas'))await talk('El guardia','Uno juraba que el muerto aprieta algo en la mano. Pero con tanta alga encima, nadie ha querido tocarle.');
    endTalk();persona('El guardia civil','Los pescadores encontraron el cuerpo a las 6:40. Uno dice que el muerto aprieta algo en la mano.')}},
  {id:'aitorF',tool:'mano',x:715,y:320,r:85,once:false,act:async()=>{await talk('Aitor','La cerré a las doce y media, Candela. Te lo juro. Está en mi cuaderno.');endTalk()}},
  {id:'leonor',tool:'mano',x:598,y:375,r:100,once:false,when:()=>D(1).flags.leonor,act:async()=>{const n=faroN();
    if(!(found('ficha')&&D(1).flags.informe&&n>=4)){nar('Todavía no tengo suficiente para enfrentarme a esa mujer.<br><br><i>Busca más pistas en el faro.</i>');return}
    next()}},
 ],
 laika:()=>{const f=D(1).flags;if(f.ampolla)return{x:120,t:'Laika persigue a un cangrejo. Gana el cangrejo.'};
   return{x:330,act:async()=>{f.ampolla=1;save();await bubble('<b>¡Guau! ¡Guau!</b> Laika ha encontrado algo entre las rocas: una ampolla de cristal rota. Huele dulzón. ¿Una medicina? ¿Algo que tomaba Don Julián?',4600);
     await pista('ampolla','La ampolla rota','Entre las rocas, una ampolla de cristal rota con olor dulzón. ¿Una medicina de Don Julián? Solo la ha encontrado Laika.');faroCheck()}}},
 enter:async()=>{const f=D(1).flags;
   if(f.leonor)swapSvg(SVG.faroL);
   if(!f.llegada){await talk('Comisario Ibarra','¿Y esta señorita?');await talk('Aitor','Viene conmigo. Es… de confianza.');await talk('Comisario Ibarra','Que no toque nada.');endTalk();
     f.llegada=1;save();persona('Comisario Ibarra','Bigote, gabán y prisa. «Que no toque nada.»');nar('Voy a tocarlo todo.<br><br><i>Habla con la gente: el guardia ha llegado el primero.</i>')}
   else nar(f.leonor?'Doña Leonor espera junto al coche, de luto, sin una lágrima.':'Niebla, olas y un muerto bajo una sábana. Voy a tocarlo todo.')}},

// ===== Escena 5 · El trato =====
{svg:SVG.trato,dark:0,tools:['mano','linterna','lupa'],
 enter:async()=>{const f=D(1).flags;nar('');
   await talk('Doña Leonor','(Mira el cuerpo sin una lágrima. Luego se vuelve hacia Aitor, delante de todos.) ¿Y dónde estaba el sereno esa noche?');
   await talk('Doña Leonor','La verja del faro estaba abierta. Si no ha sido un suicidio, ese hombre dejó pasar a alguien… o algo peor. Mi familia se encargará de que no vuelva a llevar ese farol.');
   await shake();await talk('Aitor','(Blanco como la sábana.) La cerré a las doce y media. Lo juro.');
   await talk('Candela','(El comisario mira a Aitor de reojo y apunta algo en su libreta.)');
   const c=await choose('Candela','Tengo que decir algo. ¿Qué le digo al comisario?',['«Esto no es un suicidio.»','Enseñarle una pista de la libreta','«Comisario, usted conoce a Aitor desde hace años, ¿verdad?»']);
   if(c===0)await talk('Comisario Ibarra','¿Y usted quién es, señorita? Llegó esta mañana en el Topo y ya sabe más que el médico.');
   if(c===1){const ps=S.pistas.filter(p=>p.day===1);const k=await choose('Candela','¿Qué pista le enseño?',ps.map(p=>p.t));
     await talk('Candela',`(Le enseño: «${ps[k].t}».)`);await talk('Comisario Ibarra','Muy bonito. Eso no prueba nada.')}
   if(c!==2)await talk('Candela','(Respiro hondo. Por ahí no. Pruebo de otra manera.) Comisario… usted conoce a Aitor desde hace años, ¿verdad?');
   await talk('Comisario Ibarra','(Gruñe.) Veinte años con ese farol. Es el único sereno que me trae los recados sin abrirlos.');
   await talk('Candela','¿Y de verdad lo ve capaz de algo así? ¿De dejar pasar a un asesino por una verja?');
   await talk('Comisario Ibarra','(Mira a Aitor un buen rato. Luego a Doña Leonor, que no le quita ojo.) Lo que yo vea da igual, señorita. Los Arrieta mandan en medio puerto.');
   await talk('Candela','Entonces no le pido que abra nada. Ciérrelo como suicidio en sus papeles, si quiere. Pero no acuse a Aitor ni deje que lo echen hasta Nochebuena.');
   await talk('Candela','Si para entonces no le traigo al culpable, haga lo que tenga que hacer.');
   await talk('Comisario Ibarra','(Se rasca el bigote.) Sin escándalos. Sin molestar a la familia. Y lo que encuentre, me lo trae a mí primero, ¿entendido?');
   await talk('Comisario Ibarra','Hasta Nochebuena, argentina. Ni un día más.');
   await talk('Aitor','(En voz baja, sin mirarte.) …Gracias.');endTalk();
   persona('Comisario Ibarra','Conoce a Aitor desde hace veinte años. Me da hasta Nochebuena, sin escándalos y contándole a él lo que encuentre.');
   S.trato=true;save();$('#dayLbl').innerHTML=`Día 1 · 1 dic<b id="cdLbl">${countdown(1)}</b>`;
   persona('Doña Leonor','La viuda. De luto, sin una lágrima. Acusa a Aitor delante de todos y amenaza con que lo echen.');
   nar('Hasta Nochebuena. Veintitrés días para encontrar al culpable… y para que Aitor no cargue con esto.');narBtn('Volver a casa',()=>{narSigue=true;next()})}},

// ===== Escena 6 · Esa noche =====
{svg:SVG.noche,dark:.35,tools:['mano','linterna','lupa'],sleep:1,laikaHome:120,ekiHome:215,cartel:'ALTAMAR<br>ESA NOCHE',
 enter:async()=>{const ids=['informe','ficha','bajos','huellas','verja','ampolla'],falta=ids.filter(i=>!S.pistas.find(p=>p.id===i)).length;
   nar(`La cocina a oscuras, solo con las brasas. Laika y Eki duermen enroscadas juntas junto al fogón.<br><br>Pistas de hoy: ${S.pistas.filter(p=>p.day===1).length}.`+(falta?`<br><i>Algo por descubrir en el faro…</i>`:''));
   await sleep(5000);luzVerde();await bubble('Por la ventana, un punto de luz verde cruza la bahía despacio… y se apaga.',4200);
   narAdd('Lo he visto antes. En boca de un piloto, sobre Vigo…<br><br>Mañana, al muelle.');
   narBtn('Cerrar el día',()=>{endDay();SC=null;drawCal();show('cal');bubCal('Día 1 resuelto. Mañana, al muelle.')})}},
];
FACES['Aitor']=FACE_AITOR;FACES['Candela']=FACE_CANDELA;FACES['Txomin']=FACE_TXOMIN;FACES['Comisario Ibarra']=FACE_IBARRA;FACES['Dr. Salazar']=FACE_SALAZAR;FACES['El guardia']=FACE_GUARDIA;FACES['Doña Leonor']=FACE_LEONOR;
async function ekiToCandela(){const f=D(1).flags;
  await bubble('Eki se te tira encima, te lame las manos y te da la pata.',3000);
  await bubble('Eki ha decidido que ahora vive contigo.',2600);
  await bubble('Eki se va a olerle el culo a Laika. Laika se deja. Ya son amigas.',3200);
  f.ekiTut=1;save();ekiLog('Candela','le cae bien. Muy bien.');
  nar('Eki ya me ha adoptado. Ahora, a ver qué tiene Aitor encima de la mesa…<br><br><i>Hay cosas que solo se ven con la lupa o con la linterna.</i>')}
const faroN=()=>['informe','ficha','bajos','huellas','verja','ampolla'].filter(i=>S.pistas.find(p=>p.id===i)).length;
async function faroCheck(){const f=D(1).flags;if(f.leonor||faroN()<3)return;f.leonor=1;save();await sleep(500);await shake();
  swapSvg(SVG.faroL);llegaLeonor();nar('Un motor. Un coche negro se para junto al camino del faro. Baja una mujer de luto, con velo y abrigo de pieles: Doña Leonor, la viuda.<br><br><i>Cuando tengas suficiente, habla con ella.</i>')}
function llegaLeonor(){anima('.cocheL',[{transform:'translateX(160px)'},{transform:'none'}],{duration:1800,easing:'cubic-bezier(.2,.7,.3,1)'});
  anima('.farosL',[{opacity:0},{opacity:1,offset:.3},{opacity:1}],{duration:2600});
  if(ANIM2)anima('.leoF',[{transform:'translateX(130px)',opacity:0},{transform:'translateX(130px)',opacity:0,offset:.45},{transform:'translateX(90px)',opacity:1,offset:.55},{transform:'none',opacity:1}],{duration:3400,easing:'ease-out'})}
function luzVerde(){const t0=performance.now(),D=7000;const f=t=>{const p=Math.min(1,(t-t0)/D);
  document.querySelectorAll('.verde').forEach(c=>{c.setAttribute('cx',572+118*p);c.setAttribute('opacity',p<.15?p/.15:p>.8?(1-p)/.2:1)});if(p<1)requestAnimationFrame(f)};requestAnimationFrame(f)}
async function alFaro(){narPaso('Corremos por el muelle. La niebla se traga las farolas una a una. Al fondo, la luz del faro gira, como si nada.');await sleep(5000);next()}
async function knock(){await sleep(600);AU.sfx('toc');await shake();await sleep(250);await shake();
  if(ANIM2){allSel('.txoP',e=>e.setAttribute('opacity','1'));await anima('.txoP',[{transform:'translateX(140px)'},{transform:'none'}],{duration:450,easing:'ease-out'})}
  nar('Tres golpes en la puerta. Fuertes.');await sleep(900);
  await talk('Txomin','¡Aitor! ¡Aitor! ¡En las rocas del faro! ¡Don Julián Arrieta!');
  await talk('Aitor','¿Arrieta? ¿El de la conservera?');
  await talk('Candela','(Cojo la gabardina antes que él.)');endTalk();
  persona('Txomin','Un crío del puerto, con boina y bufanda. Vino corriendo a avisar a Aitor del muerto del faro.');
  nar('Don Julián Arrieta. El del periódico. El de las cajas de Doña Maite…');narBtn('Salir corriendo',next)}
