// ---------- Día 3 ----------
DAYS[3]=[
// ===== Periódico =====
{svg:SVG.periodico3,dark:0,tools:['mano','linterna','lupa'],cartel:'SÁBADO<br>3 DE DICIEMBRE DE 1927',
 spots:[
  {id:'p3mateo',tool:'lupa',x:240,y:332,w:250,h:72,act:async()=>{persona('Mateo «el Rubio»','En la asamblea dijo: «Arrieta tuvo lo que se merecía».');await bubble('«Arrieta tuvo lo que se merecía.» Y luego, «que nadie haga tonterías». ¿Tonterías como cuáles, Mateo?',4600)}},
  {id:'p3viuda',tool:'lupa',x:539,y:328,w:280,h:72,act:async()=>{persona('Doña Leonor','Se queda al mando de la conservera hasta que se lea el testamento.');await bubble('La viuda al mando de la conservera. Y el testamento, sin fecha para leerse. Qué prisa no tiene nadie.',4600)}},
  {id:'p3casino',tool:'lupa',x:243,y:410,w:240,h:34,act:async()=>{await bubble('«Casino de Altamar. Esta noche, ruleta y orquesta.» Como la ficha que tenía Don Julián en la mano.',4200)}},
  {id:'p3disp',tool:'lupa',x:243,y:455,w:240,h:30,act:async()=>{await bubble('El doctor Salazar, vacunando gratis los martes. Ese hombre está en todas partes.',4000)}},
  {id:'p3breve',tool:'lupa',x:539,y:432,w:280,h:44,act:async()=>{await bubble('¡Doña Puri se ha comprado otra libreta para apuntar lo que hago! Y el tabernero de El Ancla «ya me guarda sitio». Habrá que ir.',4800)}},
  {id:'p3marea',tool:'lupa',x:539,y:467,w:200,h:10,act:async()=>{await bubble('«Pleamar a las 2:50.» Cada noche, un poco más tarde.',3600)}},
 ],
 enter:async()=>{nar('Sábado. Llueve sobre Altamar. Aitor ha traído churros y el periódico, por este orden.<br><br><i>Léelo bien: la letra pequeña también cuenta.</i>');
   narBtn('Ir a El Ancla',async()=>{nar('Si Mateo no estuvo en El Ancla hasta el cierre, el tabernero lo sabrá. En Altamar, los taberneros lo saben todo.');await sleep(5000);goScene(1)})}},

// ===== Taberna El Ancla =====
{svg:SVG.taberna,dark:.3,cartel:'ALTAMAR<br>TABERNA EL ANCLA',
 ekiSpots:[
  {who:'Paco',x:400,y:240,act:async()=>{await bubble('Eki se pone de pie contra la barra. Paco le da un trozo de chorizo «porque es sábado».',4000);ekiLog('Paco, el tabernero','le cae genial (y le da chorizo).')}},
  {who:'Un marinero',x:110,y:360,act:async()=>{await bubble('Eki va a saludar al marinero de la barra. Él le hace un nudo con una cuerdita para que juegue.',4000);ekiLog('Los marineros de El Ancla','saluda a todos.')}},
 ],
 spots:[
  {id:'paco',tool:'mano',x:400,y:230,r:60,once:false,act:async()=>{const f=D(3).flags;
    if(!f.paco1){await talk('Paco','¡La argentina! Ya le dije a Doña Puri que vendría. Siéntese, siéntese. ¿Sidra?');
      await talk('Candela','Vengo a preguntar por Mateo. Dice que la noche del 30 estuvo aquí hasta el cierre.');
      await talk('Paco','(Sonríe y se seca las manos en el mandil.) En El Ancla nada es gratis, señorita. Ni la sidra ni lo que se oye.');
      await talk('Paco','Vuelva cuando tenga algo que me interese.');endTalk();
      f.paco1=1;save();persona('Paco, el tabernero','Lo sabe todo del puerto, pero nada es gratis.');
      if(!f.diana)nar('Paco no suelta prenda gratis. Habrá que encontrar algo por mí misma. Miremos bien la taberna.');return}
    if(!f.diana){await talk('Paco','¿Otra sidra? Lo otro, ya le dije: tráigame algo que me interese.');endTalk();return}
    if(!f.paco2){await talk('Candela','(Le pongo el papel encima de la barra.) ¿Y esto, Paco? Estaba escondido detrás de su diana.');
      await talk('Paco','(Mira el papel. Mira a los marineros. Baja la voz.) …Vaya. Tiene usted buen ojo, argentina.');
      await talk('Paco','Mateo estuvo aquí, sí… pero se fue a medianoche, no al cierre. Dijo que tenía «un asunto». Y no volvió.');
      await talk('Paco','Y ese papelito no es el primero. Mateo usa mi diana de buzón desde hace meses.');
      await talk('Candela','¿Buzón de quién?');await talk('Paco','Eso ya es mucho preguntar para una sola sidra.');endTalk();
      f.paco2=1;save();await pista('paco','Lo que dice Paco','Mateo se fue de El Ancla a medianoche, no al cierre, por «un asunto». Usa la diana como buzón para recibir notas.');
      persona('Mateo «el Rubio»','Se fue de El Ancla a medianoche por «un asunto». Recibe notas escondidas detrás de la diana.');
      fin3();return}
    await talk('Paco','¿Otra sidra, señorita? Para la información hay que esperar a otro día.');endTalk()}},
  {id:'dianaVer',tool:'mano',x:650,y:150,r:50,once:false,act:async()=>{goScene(2)}},
  {id:'dianaLupa',tool:'lupa',x:650,y:150,w:90,h:90,act:async()=>{await bubble('La diana está torcida y el clavo, gastado. Como si alguien la moviera a menudo…',4000)}},
  {id:'fiados',tool:'lupa',x:385,y:132,w:110,h:60,act:async()=>{await bubble('La pizarra de fiados: «Mateo… 2 sidras (30-XI)». Solo dos sidras. Para alguien que se quedó hasta el cierre, poca sed.',4800)}},
  {id:'sangre',tool:'linterna',x:50,y:462,w:80,h:40,act:async()=>{await bubble('Bajo la escalera, a oscuras: una silla rota y gotas de sangre seca en el suelo.',4000);
    await talk('Paco','(Desde la barra.) Una pelea, el otro día. Gente de fuera. Nada que le importe.');endTalk();
    await pista('sangreAncla','Sangre en El Ancla','Bajo la escalera de El Ancla: una silla rota y gotas de sangre seca. Paco dice que fue una pelea «de gente de fuera».')}},
  {id:'trastienda',tool:'mano',x:755,y:210,r:40,once:false,act:async()=>{await bubble('«PRIVADO». La puerta de la trastienda está cerrada con llave. Paco la mira de reojo cuando me acerco.',4400)}},
  {id:'marinero',tool:'mano',x:110,y:360,r:50,once:false,act:async()=>{const t=['Dicen que la viuda no derramó ni una lágrima en el faro. Ni una.','Al sereno lo van a echar, ya verá. Los Arrieta no perdonan.','Don Julián estaba enfermo, ¿sabe? Lo decían en la conservera. Algo malo.'];
    const f=D(3).flags;f.chisme=((f.chisme||0)+1);save();await talk('Un marinero',t[(f.chisme-1)%3]);endTalk();if(f.chisme===3)persona('Don Julián Arrieta','Según un marinero de El Ancla, «estaba enfermo, algo malo».')}},
 ],
 laika:()=>{const f=D(3).flags;if(!f.tortilla){f.tortilla=1;save();return{x:300,t:'Laika ha encontrado medio pintxo de tortilla en el suelo. Paco hace como que no ha visto nada.'}}return null},
 enter:async()=>{const f=D(3).flags;
   if(f.paco2){fin3();return}
   if(!f.taberna){f.taberna=1;save();nar('Humo, sidra y voces. Marineros en la barra y, detrás, un hombre enorme con bigote: Paco, el tabernero.')}
   else nar(f.diana?'Tengo el papel de la diana. A ver qué me cuenta ahora Paco.':'Paco limpia vasos y me mira de reojo.')}},

// ===== La diana =====
{svg:SVG.diana,dark:0,tools:['mano','linterna','lupa'],
 spots:[
  {id:'apartar',tool:'drag',el:'diana',x:400,y:250,r:160,dist:170,hint:'Está colgada de un clavo. Arrástrala con el dedo hacia un lado.',act:async()=>{await bubble('Detrás de la diana hay un hueco en la pared. Y dentro, un papel doblado.',4000);
    nar('Un papel doblado, escondido detrás de la diana.<br><br><i>Tócalo con la mano.</i>');narBtn('Volver a la barra',()=>goScene(1))}},
  {id:'papel',tool:'mano',x:400,y:245,r:45,once:false,when:()=>found('apartar'),act:async()=>{goScene(3)}},
 ],
 enter:async()=>{if(found('apartar')){nar('El hueco de la pared, con el papel doblado.<br><br><i>Tócalo con la mano.</i>');}
   else nar('Una diana vieja, colgada de un clavo y un poco torcida.');
   narBtn('Volver a la barra',()=>goScene(1))}},

// ===== La nota de «C.» =====
{svg:SVG.notaC,dark:0,tools:['mano','linterna','lupa'],
 spots:[
  {id:'imprenta',tool:'lupa',x:330,y:366,w:90,h:12,act:async()=>{await bubble('Abajo, en letra diminuta: «Papelería · Imprenta Ugalde». El papel es de una imprenta.',4200);
    await pista('notaC','La nota de «C.»','Escondida tras la diana: «A las doce, donde siempre. Trae los papeles. — C.». Papel de la Imprenta Ugalde.');D(3).flags.diana=1;save();
    nar('«C.» Como la «C» de la ficha del Casino que tenía Don Julián en la mano… ¿o es otra cosa? Paco tendrá algo que decir de lo que pasa detrás de su diana.');narBtn('Volver a la barra',()=>goScene(1))}},
 ],
 enter:async()=>{nar('Letra de mujer, con tinta azul. «A las doce, donde siempre. Trae los papeles. — C.»<br><br><i>Mírala bien.</i>');
   if(found('imprenta'))narBtn('Volver a la barra',()=>goScene(1))}},

// ===== Esa noche =====
{svg:SVG.noche,dark:.35,tools:['mano','linterna','lupa'],sleep:1,laikaHome:120,ekiHome:215,cartel:'ALTAMAR<br>ESA NOCHE',
 enter:async()=>{nar(`Llueve sobre los tejados del puerto. Laika y Eki, junto al fogón.<br><br>Pistas de hoy: ${S.pistas.filter(p=>p.day===3).length}.<br>Mateo se fue a medianoche a ver a alguien. A «C.».`);
   await sleep(5000);narAdd('¿Quién es C.? ¿Qué papeles? Y en el despacho de Don Julián debe de haber respuestas…<br><br>Mañana, al palacete de los Arrieta.');
   narBtn('Cerrar el día',()=>{endDay();SC=null;drawCal();show('cal');bubCal('Día 3 resuelto. Mañana, al palacete de los Arrieta.')})}},
];
function fin3(){nar('Mateo se fue a medianoche a ver a alguien. A «C.». Ya tengo bastante por hoy.');narBtn('Volver a casa',()=>goScene(4))}
FACES['Paco']=FACE_PACO;FACES['Un marinero']=FACE_EST;
