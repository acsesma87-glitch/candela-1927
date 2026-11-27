// ---------- Día 4 ----------
const d4=()=>D(4).flags;
function catch4(){const f=d4();if(f.pillada||!found('bloc')||!f.secreter||!found('poliza'))return;run(pillada)}
async function pillada(){const f=d4();f.pillada=1;save();await sleep(600);swapSvg(SVG.despachoL);await shake();
  await talk('Doña Leonor','¿Qué hace usted aquí?');
  const ops=['«Buscaba el baño, perdone.»','«Su marido no se suicidó, Doña Leonor.»'];if(S.pistas.find(p=>p.id==='floristeria'))ops.push('«Usted dijo que no salió esa noche. Mintió.»');
  const c=await choose(null,null,ops);
  if(c===0)await talk('Doña Leonor','¿En el despacho de mi marido? ¿Detrás de su escritorio? No me tome por tonta.');
  if(c===1)await talk('Doña Leonor','(Se pone pálida un instante. Solo un instante.) Mi marido era un cobarde. Y los cobardes se tiran desde las rocas.');
  if(c===2){await talk('Doña Leonor','(Mira el secreter abierto. Le tiembla la mano, apenas.) Lo que yo haga de noche es asunto mío y de Dios. De nadie más.');persona('Doña Leonor','Al enseñarle que salió esa noche, no lo niega: «es asunto mío y de Dios».')}
  await talk('Doña Leonor','¡Benigna! Acompañe a la señorita a la puerta. Y que el sereno se vaya con ella.');endTalk();
  nar('Fuera. Bajo la lluvia, con Aitor, en la puerta del palacete. Pero no me voy con las manos vacías.');narBtn('Volver a casa',()=>goScene(5))}
DAYS[4]=[
// ===== Periódico =====
{svg:SVG.periodico4,dark:0,tools:['mano','linterna','lupa'],cartel:'DOMINGO<br>4 DE DICIEMBRE DE 1927',
 spots:[
  {id:'p4vela',tool:'lupa',x:240,y:332,w:250,h:72,act:async()=>{await bubble('«Unos por respeto, otros por curiosidad, y algunos para asegurarse.» Hoy todo Altamar entra en el palacete. Yo también.',4800)}},
  {id:'p4test',tool:'lupa',x:539,y:328,w:280,h:72,act:async()=>{persona('Don Julián Arrieta','Se rumorea que cambió el testamento días antes de morir.');await bubble('Un testamento cambiado días antes de morir… Y el heredero, otra vez en el Casino.',4400)}},
  {id:'p4joya',tool:'lupa',x:243,y:410,w:240,h:34,act:async()=>{await bubble('«Joyería Zubeldia: compramos oro y alhajas. Discreción.» En este barrio todo el mundo necesita discreción.',4400)}},
  {id:'p4flor',tool:'lupa',x:243,y:455,w:240,h:30,act:async()=>{await bubble('«Floristería Las Dalias. Servicio nocturno.» ¿Quién compra flores de noche?',4000)}},
  {id:'p4breve',tool:'lupa',x:539,y:432,w:280,h:44,act:async()=>{await bubble('«Del brazo del sereno.» Doña Puri, me cae usted mejor cada día.',3800)}},
  {id:'p4marea',tool:'lupa',x:539,y:467,w:200,h:10,act:async()=>{await bubble('«Pleamar a las 3:30.»',3000)}},
 ],
 enter:async()=>{nar('Domingo. Aitor se ha puesto la chaqueta buena. «A un velatorio de los Arrieta no se va de sereno», dice.<br><br><i>Léelo bien: la letra pequeña también cuenta.</i>');
   narBtn('Ir al palacete',async()=>{nar('El palacete de los Arrieta, en lo alto. Medio barrio hace cola para dar el pésame. Unos por respeto, otros por curiosidad.');await sleep(5000);goScene(1)})}},

// ===== El salón (velatorio) =====
{svg:SVG.salon,dark:.25,tools:['mano','linterna','lupa'],cartel:'ALTAMAR<br>EL PALACETE',
 spots:[
  {id:'leonor',tool:'mano',x:420,y:340,r:95,once:false,act:async()=>{const f=d4();
    if(!f.leonor1){await talk('Doña Leonor','(Sin mirarte.) El sereno tiene la desvergüenza de presentarse aquí. Y con compañía.');
      await talk('Candela','Mis condolencias, Doña Leonor. ¿Puedo preguntarle dónde estuvo la noche del 30?');
      await talk('Doña Leonor','En mi casa. Dormida. No salí en toda la noche. Y ahora, si me disculpa, tengo un marido que enterrar.');endTalk();
      f.leonor1=1;save();persona('Doña Leonor','Dice que la noche del 30 no salió de casa: «estuve dormida».');return}
    await talk('Doña Leonor','No tengo nada más que decirle, señorita.');endTalk()}},
  {id:'inigo',tool:'mano',x:680,y:340,r:95,once:false,act:async()=>{const f=d4();
    if(!f.inigo1){await talk('Íñigo Arrieta','Así que usted es la famosa argentina. Mi padre habría odiado que alguien tan guapa husmeara en sus cosas.');
      await talk('Candela','Dicen que discutieron en el Casino la noche que murió.');
      await talk('Íñigo Arrieta','(Sonríe y da una calada.) Discutimos, sí. ¿Quién no discutía con él? Luego me fui a casa a medianoche. Pregúntele a quien quiera.');endTalk();
      f.inigo1=1;save();persona('Íñigo Arrieta','Encantador y fumador. Reconoce que discutió con su padre en el Casino; dice que volvió a casa a medianoche.');return}
    await talk('Íñigo Arrieta','¿Otra vez por aquí? Empiezo a pensar que le caigo bien.');endTalk()}},
  {id:'baston',tool:'lupa',x:650,y:420,w:30,h:90,act:async()=>{await bubble('Íñigo lleva un bastón con puño dorado. Muy elegante. Y nuevo: el de los retratos es otro.',4200)}},
  {id:'clara',tool:'mano',x:120,y:345,r:85,once:false,act:async()=>{const f=d4();
    if(!f.clara1){await talk('Clara Arrieta','¿Usted es la que hace preguntas? Haga muchas. En esta casa todos mienten.');
      await talk('Candela','¿Usted también?');await talk('Clara Arrieta','(Se ríe sin ganas.) Yo la que más. Pero no de eso.');endTalk();
      f.clara1=1;save();persona('Clara Arrieta','La hija. Lista y rebelde: «En esta casa todos mienten. Yo la que más».');return}
    await talk('Clara Arrieta','Siga preguntando, señorita.');endTalk()}},
  {id:'tinta',tool:'lupa',x:148,y:392,w:40,h:30,act:async()=>{await bubble('Las manos de Clara: tiene los dedos manchados de tinta azul. Como si hubiera estado escribiendo… o imprimiendo.',4600);
    await pista('tintaClara','Tinta en las manos de Clara','Clara Arrieta tiene los dedos manchados de tinta azul.')}},
  {id:'benigna',tool:'mano',x:300,y:360,r:85,once:false,act:async()=>{const f=d4();
    if(!f.ben1){await talk('Benigna','(Te ofrece la bandeja. Te mira fijamente y baja la voz.) Usted es la de… (se calla).');
      await talk('Candela','Traigo una carta de su hermana Maite. Me la dio en el barco, para usted.');
      await talk('Benigna','Aquí no, señorita. Mañana, por la puerta de servicio. A las once.');endTalk();
      f.ben1=1;save();persona('Benigna','El ama de llaves. Me mira raro. Quiere verme mañana a las once por la puerta de servicio.');return}
    await talk('Benigna','Mañana, señorita. Por la puerta de servicio.');endTalk()}},
  {id:'aitorS',tool:'mano',x:560,y:330,r:90,once:false,act:async()=>{const f=d4();
    if(f.distr){await talk('Aitor','Ahora, Candela. Que no te vean.');endTalk();return}
    if(!f.leonor1){await talk('Aitor','(En voz baja.) No le quites ojo a la viuda. Ni ella a nosotros.');endTalk();return}
    const c=await choose('Candela','(Le hablo a Aitor al oído.)',['«Necesito entrar en el despacho. ¿Me cubres?»','Nada, luego te cuento.']);
    if(c===1){endTalk();return}
    await talk('Aitor','(Traga saliva.) …Déjamelo a mí.');endTalk();await sleep(500);AU.sfx('cristales');swapSvg(SVG.salonCa);await shake();
    await bubble('¡CRASH! Aitor «tropieza» con Benigna y una bandeja de copas acaba en la alfombra. Todo el salón se vuelve a mirar.',4000);
    f.distr=1;save();nar('Ahora. La puerta del despacho, a la izquierda.')}},
  {id:'puertaDesp',tool:'mano',x:210,y:230,r:60,once:false,act:async()=>{const f=d4();
    if(!f.distr){await bubble('Doña Leonor no le quita ojo a la puerta del despacho. Necesito que alguien la distraiga.',4200);return}goScene(2)}},
 ],
 enter:async()=>{const f=d4();if(f.pillada){nar('Ya me han echado. Mejor no tentar a la suerte.');narBtn('Volver a casa',()=>goScene(5));return}
   if(f.distr)swapSvg(SVG.salonC);
   if(!f.salon){f.salon=1;save();nar('Velas, terciopelo y retratos de antepasados con cara de pocos amigos. Toda la familia Arrieta junta. Y ninguno llora.')}
   else nar(f.distr?'El salón sigue revuelto por lo de la bandeja. La puerta del despacho está a la izquierda.':'El salón huele a cera y a flores. Doña Leonor vigila.')}},

// ===== El despacho =====
{svg:SVG.despacho,dark:.55,tools:['mano','linterna','lupa'],
 spots:[
  {id:'blocVer',tool:'mano',x:295,y:310,r:45,once:false,act:async()=>{goScene(3)}},
  {id:'poliza',tool:'lupa',x:432,y:311,w:70,h:22,act:async()=>{await bubble('Una póliza de La Previsora: el seguro de vida de Don Julián, subido el 2 de noviembre a 200.000 pesetas. Beneficiaria: Leonor Arrieta.',5000);
    await pista('poliza','El seguro de vida','Subido el 2 de noviembre a 200.000 pesetas. Beneficiaria: Doña Leonor.')}},
  {id:'retrato',tool:'mano',x:390,y:135,r:70,once:false,act:async()=>{const f=d4();if(!f.caja){f.caja=1;save();persona('Don Julián Arrieta','Tenía una caja fuerte detrás de su retrato, en el despacho.')}
    await bubble('Detrás del retrato de Don Julián hay una caja fuerte, con una rueda de números. Cerrada. Sin la combinación, ni lo intento.',4600)}},
  {id:'secreterVer',tool:'mano',x:640,y:196,r:80,once:false,act:async()=>{goScene(4)}},
 ],
 enter:async()=>{const f=d4();
   if(f.pillada){swapSvg(SVG.despachoL);nar('Doña Leonor me ha pillado. Toca irse.');narBtn('Volver a casa',()=>goScene(5));return}
   nar(f.desp?'El despacho de Don Julián, a oscuras. Rápido.':'El despacho de Don Julián. Huele a tabaco frío. Tengo poco tiempo.<br><br><i>El escritorio, el retrato, el secreter…</i>');f.desp=1;save()},
 check:catch4},

// ===== El bloc y el lápiz =====
{svg:SVG.escritorio,dark:0,tools:['mano','linterna','lupa'],
 spots:[
  {id:'bloc',tool:'pencil',el:'lapiz',x:610,y:285,r:90,tip:[646,338],area:[230,130,260,290],need:.5,act:async()=>{
    await bubble('Con el grafito aparecen las letras que se marcaron en la hoja de abajo: «Esta noche se acaba todo. Que Dios me perdone. J.»',5000);
    await pista('bloc','El bloc de Don Julián','Calcado con lápiz: «Esta noche se acaba todo. Que Dios me perdone. J.». Parece una despedida.');
    nar('«Que Dios me perdone.» ¿Una nota de suicidio? ¿Y si el médico tenía razón?');narBtn('Volver al despacho',()=>goScene(2))}},
 ],
 enter:async()=>{if(found('bloc')){rubSet(1);nar('«Esta noche se acaba todo. Que Dios me perdone. J.»')}
   else nar('Un bloc en blanco. Pero la hoja de encima la arrancaron… y al escribir se marca la de abajo.<br><br><i>Coge el lápiz con el dedo y pásalo por encima del bloc.</i>');
   narBtn('Volver al despacho',()=>goScene(2))}},

// ===== El secreter =====
{svg:SVG.secreter,dark:0,tools:['mano','linterna','lupa'],
 spots:[
  {id:'botines',tool:'lupa',x:300,y:360,w:180,h:60,when:()=>d4().secreter,act:async()=>{await bubble('Unos botines de señora con el bajo manchado de barro claro, de tierra. No es arena de playa.',4400)}},
  {id:'floristeria',tool:'lupa',x:525,y:250,w:150,h:100,when:()=>d4().secreter,act:async()=>{await bubble('«Floristería Las Dalias. 30 de noviembre. Entrega: 23:00. Un ramo blanco.»',4200);
    await pista('floristeria','Leonor salió esa noche','Escondido en su secreter: un recibo de Las Dalias, 30 de noviembre, entrega a las 23:00, un ramo blanco. Y botines con barro. Dijo que no salió de casa.');
    persona('Doña Leonor','Mintió: la noche del 30 salió (ramo blanco a las 23:00, botines con barro).');
    nar('Doña Leonor dijo que no salió de casa. Mintió.');narBtn('Volver al despacho',()=>goScene(2))}},
 ],
 enter:async()=>{const f=d4();
   if(f.secreter){swapSvg(SVG.secreterA);nar('El secreter de Doña Leonor, abierto.');narBtn('Volver al despacho',()=>goScene(2));return}
   nar('El secreter de Doña Leonor está cerrado con llave. Una cerradura pequeña… se puede forzar con una horquilla.<br><br><i>Mueve el dedo para colocar la horquilla. Mantén «Girar». Si tiembla, estás cerca; si fuerzas, se resbala y hay que volver a empezar.</i>');
   narBtn('Volver al despacho',()=>goScene(2));
   if(!f.sweet){f.sweet=40+Math.round(Math.random()*100);save()}
   pickOpen({sweet:f.sweet,tol:7,breakMs:1100,onOpen:async()=>{f.secreter=1;save();swapSvg(SVG.secreterA);await bubble('¡Clic! El secreter se abre.',2400);
     nar('Dentro: unos botines y un papel.<br><br><i>Míralos con la lupa.</i>');narBtn('Volver al despacho',()=>goScene(2))}})}},

// ===== Esa noche =====
{svg:SVG.noche,dark:.35,tools:['mano','linterna','lupa'],sleep:1,laikaHome:120,ekiHome:215,cartel:'ALTAMAR<br>ESA NOCHE',
 enter:async()=>{nar(`Aitor se seca el pelo junto al fogón. Laika y Eki duermen.<br><br>Pistas de hoy: ${S.pistas.filter(p=>p.day===4).length}.<br>Doña Leonor mintió. Y Don Julián escribió algo que parece una despedida.`);
   await sleep(5000);narAdd('¿Y si de verdad se tiró? Mañana, a las once, la puerta de servicio. Benigna tiene algo que contarme… y yo tengo una carta para ella.');
   narBtn('Cerrar el día',()=>{endDay();SC=null;drawCal();show('cal');bubCal('Día 4 resuelto. Mañana, la cocina del palacete.')})}},
];
FACES['Íñigo Arrieta']=FACE_INIGO;FACES['Clara Arrieta']=FACE_CLARA;FACES['Benigna']=FACE_BENIGNA;
