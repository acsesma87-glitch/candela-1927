// ---------- Día 9: el Casino ----------
const d9=()=>D(9).flags;
async function casino9fin(){const f=d9();f.cuenta=1;save();await sleep(400);
  await talk('Aitor','(Me coge del brazo, en voz baja.) Te he visto mirar ese espejo como si te fuera la vida. ¿Qué ponía en el libro?');
  for(;;){const c=await choose('Candela','(¿Cuánto debía Íñigo en total?)',['4.000 pesetas','6.000 pesetas','10.000 pesetas','12.500 pesetas']);
    if(c===3){await talk('Candela','Doce mil quinientas pesetas, Aitor. En un solo mes. Y la última deuda, del 29: el día antes de que muriera su padre.');break}
    await talk('Candela','(No… espera. Había tres apuntes. Tengo que volver a mirarlo.)');
    const v=await choose(null,null,['Volver a mirar el espejo','Pensarlo otra vez']);if(v===0){endTalk();f.cuenta=0;save();goScene(2);return}}
  await talk('Aitor','(Silba bajito.) Con eso se compra un barco. Y debajo, ¿qué?');
  await talk('Candela','Una nota de Don Julián: «Paga mi hijo. Es la última vez». Iba a dejar de pagarle.');endTalk();
  await pista('deudas9','El registro de deudas del Casino','Íñigo debía 12.500 pesetas en noviembre (4.000, 2.500 y 6.000, la última el día 29). Don Julián pagó y dejó escrito: «Paga mi hijo. Es la última vez».');
  persona('Íñigo Arrieta','Debía 12.500 pesetas al Casino en noviembre. Su padre le advirtió: «Es la última vez».');
  casino9salida()}
function casino9salida(){const f=d9();if(!f.cuenta||!f.crupier)return;
  nar('Íñigo mintió en la hora y debía una fortuna. Aitor me dice que Paco, el de El Ancla, sabe algo de esa noche.');narBtn('Ir a El Ancla',async()=>{narPaso('Cruzamos el puerto bajo la lluvia. En El Ancla huele a sidra, a serrín mojado y a tabaco negro.');await sleep(5000);goScene(3)})}

DAYS[9]=[
// ===== Periódico =====
{svg:SVG.periodico9,dark:0,tools:['mano','linterna','lupa'],cartel:'VIERNES<br>9 DE DICIEMBRE DE 1927',
 spots:[
  {id:'p9casino',tool:'lupa',x:243,y:410,w:240,h:34,act:async()=>{await bubble('«Se admiten señoras acompañadas.» Pues voy acompañada.',3400)}},
  {id:'p9cuadras',tool:'lupa',x:243,y:455,w:240,h:30,act:async()=>{await bubble('«Caballerizas Iriondo. Coches de alquiler. Mozo de confianza.» Lo apunto.',3800)}},
  {id:'p9coche',tool:'lupa',x:539,y:330,w:280,h:70,act:async()=>{await bubble('Un coche bajando sin faros hacia el puerto, pasada la una. En Altamar solo hay dos: el del médico y el de los Arrieta.',5000)}},
  {id:'p9breve',tool:'lupa',x:539,y:432,w:280,h:44,act:async()=>{await bubble('Doña Puri ha tenido que sentarse. Pobre mujer, qué semana lleva.',3600)}},
 ],
 enter:async()=>{nar('Viernes. Llueve desde el amanecer. Aitor lee el periódico por encima de mi hombro y resopla: «El Casino, lleno. Esta gente no tiene luto ni para un muerto».<br><br><i>Íñigo dijo que volvió a casa a medianoche. Hoy toca comprobarlo.</i>');
   narBtn('Ir al Casino',async()=>{narPaso('Por la noche, Aitor se pone la chaqueta buena, la de los entierros. «Al Casino no se entra con el capote de sereno», dice. A mí me presta un broche de su madre.');await sleep(5000);goScene(1)})}},

// ===== El Casino =====
{svg:SVG.casino,dark:.06,tools:['mano','linterna','lupa'],cartel:'ALTAMAR<br>EL CASINO',
 spots:[
  {id:'crupier9',tool:'mano',x:600,y:330,r:55,once:false,act:async()=>{const f=d9();
    if(f.crupier){await talk('El crupier','Hagan juego, señores. (Ni me mira.)');endTalk();return}
    await talk('El crupier','(Sin levantar la vista de la ruleta.) Hagan juego… ¿La señora juega o mira?');
    const c=await choose('Candela','(Necesito saber a qué hora se fue Íñigo.)',['«Miro. Y pregunto por Íñigo Arrieta.»','Poner una ficha en el rojo y preguntar después.']);
    if(c===0){await talk('El crupier','En el Casino no se pregunta por los clientes, señora. Se juega.');
      await talk('Candela','(Dejo una ficha en el rojo.)')}
    else await talk('Candela','(Dejo una ficha en el rojo. La bola gira…)');
    AU.sfx('tic');await sleep(900);
    await talk('El crupier','Negro, el diecisiete. (Recoge la ficha con el rastrillo y, por fin, me mira.) El joven Arrieta, ¿eh? Esa noche discutió con su padre a gritos, ahí mismo, junto a la caja. A las once y media, más o menos.');
    await talk('El crupier','Se fue a la una en punto. Lo sé porque cerramos la ruleta a esa hora y me dejó una ficha de propina. Se marchó en el coche de la familia.');
    await talk('Candela','¿A la una? Él dice que volvió a casa a medianoche.');
    await talk('El crupier','(Se encoge de hombros.) Pues dirá misa. Hagan juego, señores.');endTalk();
    f.crupier=1;save();persona('Íñigo Arrieta','El crupier: se fue del Casino a la una en punto, en el coche de la familia. No a medianoche, como dijo.');
    await pista('hora9','Íñigo mintió en la hora','El crupier del Casino: Íñigo discutió con su padre a las 23:30 y se fue a la una en punto, en el coche de la familia. Él dijo que volvió a casa a medianoche.');
    casino9salida()}},
  {id:'caja9',tool:'mano',x:415,y:170,r:60,once:false,act:async()=>{const f=d9();
    if(!f.caja){f.caja=1;save();await talk('El cajero','(Tras la rejilla.) ¿Desea fichas, señorita?');
      await talk('Candela','Quisiera ver las cuentas de Íñigo Arrieta.');
      await talk('El cajero','(Aparta el libro de la ventanilla, sin cerrarlo.) Los libros del Casino no se enseñan, señorita. Ni a la policía, si viene sin papeles.');endTalk();
      nar('El cajero deja el libro de deudas abierto sobre el mostrador, de espaldas a mí. Detrás de la rejilla. Imposible acercarse.');return}
    await bubble('El cajero me vigila. El libro sigue abierto sobre el mostrador, de espaldas a mí.',3600)}},
  {id:'espejoVer',tool:'lupa',x:686,y:196,w:80,h:50,act:async()=>{await bubble('En el espejo se refleja el mostrador de la caja… y el libro abierto. Al revés, pero se ve.',4200);goScene(2)}},
  {id:'jugadores9',tool:'mano',x:170,y:340,r:80,once:false,act:async()=>{await talk('Un jugador','(Sin soltar los naipes.) ¿El hijo de Arrieta? Ese juega como si el dinero se lo regalaran. Y se lo regalaban, hasta hace nada.');endTalk()}},
  {id:'jugador9b',tool:'mano',x:480,y:360,r:45,once:false,act:async()=>{await talk('Un jugador','Al rojo, siempre al rojo. Algún día saldrá. (No ha salido en toda la noche.)');endTalk()}},
  {id:'aitor9',tool:'mano',x:405,y:390,r:45,once:false,act:async()=>{await talk('Aitor','(Tirándose del cuello de la chaqueta.) Me pica. Esto de ir de señorito no es lo mío.');endTalk()}},
 ],
 enter:async()=>{const f=d9();if(f.cuenta&&f.crupier){casino9salida();return}
   if(f.espejo&&!f.cuenta){await casino9fin();return}
   nar('El Casino de Altamar: humo de puro, lámparas verdes y el ruido de la bola en la ruleta. Al fondo, la ventanilla de la caja. En las paredes, espejos dorados por todas partes.<br><br><i>Íñigo estuvo aquí la noche del 30.</i>')}},

// ===== El espejo =====
{svg:SVG.espejo,dark:0,tools:['mano','linterna','lupa'],
 spots:[
  {id:'deudasLeer',tool:'lupa',x:400,y:250,w:380,h:300,act:async()=>{d9().espejo=1;save();await bubble('Todo al revés… tendré que leerlo como en un espejo.',3200)}},
 ],
 enter:async()=>{d9().espejo=1;save();nar('El espejo dorado, frente a la caja. En el reflejo, el libro de deudas abierto sobre el mostrador. Las letras, del revés.');
   narBtn('Dejar de mirar',()=>goScene(1))}},

// ===== El Ancla: Paco vende un dato =====
{svg:SVG.taberna,dark:.08,tools:['mano','linterna','lupa'],cartel:'ALTAMAR<br>TABERNA EL ANCLA',
 spots:[
  {id:'paco9',tool:'mano',x:560,y:240,r:60,once:false,act:async()=>{const f=d9();
    if(f.paco){await talk('Paco','Lo dicho: yo no he dicho nada.');endTalk();return}
    await talk('Paco','(Secando un vaso.) Vaya, la argentina y el sereno. ¿Una sidra, o vienen a por otra cosa?');
    await talk('Candela','El hijo de Arrieta. La noche del 30. ¿Estuvo aquí?');
    await talk('Paco','En este puerto nada es gratis, señorita. Ni la sidra ni lo que se oye.');
    for(;;){const c=await choose('Candela','(¿Qué le ofrezco?)',['Pagarle unas pesetas','Que lo arregle Aitor','Insistir']);
      if(c===0){await talk('Paco','(Mira la moneda y se ríe.) Con eso no me pago ni el serrín.');continue}
      if(c===2){await talk('Paco','Insistir tampoco se cobra, señorita. Pero no sirve.');continue}
      break}
    await talk('Aitor','Paco. La noche de la sidrería de Tolosa, cuando cerraste a las cuatro y yo no vi nada… ¿te acuerdas?');
    await talk('Paco','(Deja el vaso.) …Me acuerdo. Está bien, sereno.');
    await talk('Paco','El señorito Arrieta vino a las diez y media, ya bebido. Se encaró con unos marineros de un pesquero de Bermeo por una partida de mus. Acabaron a golpes ahí, bajo la escalera.');
    await talk('Paco','Le abrieron la ceja y él le partió una silla a uno en la espalda. La sangre que vio usted el otro día, señorita… es suya. O de ellos. Se fue a las once, sangrando, hacia el Casino.');
    await talk('Paco','Y yo no he dicho nada.');endTalk();
    f.paco=1;save();persona('Paco, el tabernero','Le debe un favor a Aitor (la noche de la sidrería de Tolosa).');
    persona('Íñigo Arrieta','Se pegó con unos marineros de Bermeo en El Ancla a las 22:30; se fue sangrando hacia el Casino.');
    await pista('pelea9','La pelea de Íñigo en El Ancla','Paco: Íñigo llegó bebido a las 22:30 y se pegó con unos marineros de Bermeo bajo la escalera. La sangre bajo la escalera era de esa pelea. Se fue a las once, sangrando, hacia el Casino.');
    nar('Así que la sangre de El Ancla era de Íñigo. Y de ahí, al Casino, a discutir con su padre.');narBtn('Volver a casa',()=>{narSigue=true;goScene(4)})}},
  {id:'escalera9',tool:'mano',x:60,y:420,r:60,once:false,act:async()=>{await bubble('La silla rota sigue bajo la escalera. Nadie se ha molestado en recogerla.',3600)}},
 ],
 enter:async()=>{const f=d9();if(f.paco){nar('Paco ya ha hablado.');narBtn('Volver a casa',()=>{narSigue=true;goScene(4)});return}
   nar('Paco limpia la barra con el mismo trapo de siempre. Nos ve entrar y no cambia la cara.')}},

// ===== En casa: atar cabos con Aitor =====
{svg:SVG.cocinaMesa,dark:.05,laikaHome:560,ekiHome:150,cartel:'ALTAMAR<br>CASA DEL SERENO',
 enter:async()=>{const f=d9();
   if(!f.cabos){nar('Aitor se quita la chaqueta buena como quien se quita un castigo. Pone dos tazas de caldo y se sienta. Laika y Eki, junto a la estufa.');await sleep(1200);
     await talk('Aitor','A ver, detective. Íñigo dijo que volvió a casa a medianoche. ¿Qué hacía a esa hora, de verdad?');
     for(;;){const c=await choose(null,null,['Estaba en su cama','Seguía en el Casino','Estaba en El Ancla']);
       if(c===1){await talk('Aitor','En el Casino. Hasta la una en punto, según el crupier. Y luego, en coche.');break}
       await talk('Aitor',c===0?'¿En su cama? Eso es lo que dice él. ¿Y el crupier?':'En El Ancla estuvo antes, de diez y media a once. Luego se fue.');
       await talk('Aitor','Piénsalo otra vez.')}
     await talk('Aitor','¿Y por qué iba a mentir en la hora?');
     for(;;){const c=await choose(null,null,['Para tapar la pelea de El Ancla','Para tapar lo que hizo después de la una','Porque estaba borracho y no se acuerda']);
       if(c===1){await talk('Aitor','Eso. La pelea fue antes, eso no lo esconde. Lo que esconde es lo que hizo después de la una… con el coche.');break}
       await talk('Aitor',c===0?'La pelea fue a las diez y media. Mintiendo en la medianoche no la tapa.':'Borracho estaba. Pero de la hora se acuerda muy bien: la dice siempre igual.');
       await talk('Aitor','Otra vez.')}
     await talk('Candela','Debía doce mil quinientas pesetas, su padre le iba a dejar sin nada y esa noche discutieron a gritos. Y a la una cogió el coche.');
     await talk('Aitor','(Mira la taza un rato.) No me gusta decirlo, Candela. Pero si yo fuera Ibarra, ya le habría puesto las esposas.');endTalk();
     f.cabos=1;save();await pista('cabos9','Atando cabos con Aitor','Íñigo mintió en la hora: no volvió a medianoche, se fue del Casino a la una en coche. Debía 12.500 pesetas, su padre lo iba a desheredar y discutieron esa noche. La sangre de El Ancla era de su pelea.')}
   nar('Fuera llueve sobre el puerto. Aitor se queda mirando por la ventana, muy callado.');narBtn('Irse a dormir',()=>goScene(5))}},

// ===== Esa noche =====
{svg:SVG.noche,dark:.35,tools:['mano','linterna','lupa'],sleep:1,laikaHome:120,ekiHome:215,cartel:'ALTAMAR<br>ESA NOCHE',
 enter:async()=>{nar(`Aitor ha salido de ronda. Laika y Eki duermen junto al fogón.<br><br>Pistas de hoy: ${S.pistas.filter(p=>p.day===9).length}.<br>Íñigo debía una fortuna, mintió en la hora y a la una cogió el coche de la familia.`);
   await sleep(5000);narAdd('Todo señala a Íñigo. Demasiado bien, quizá.<br><br>Mañana, las caballerizas: si el coche salió esa noche, alguien tuvo que sacarlo.');
   narBtn('Cerrar el día',()=>{endDay();SC=null;drawCal();show('cal');bubCal('Día 9 resuelto. Mañana, las caballerizas.')})}},
];
FACES['El crupier']=FACE_CRUPIER;FACES['El cajero']=FACE_CRUPIER;FACES['Un jugador']=FACE_JUGADOR;
