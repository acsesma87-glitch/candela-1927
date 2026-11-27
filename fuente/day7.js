// ---------- Día 7 ----------
const d7=()=>D(7).flags;
// --- el puzle de las cajas: se deslizan por su raíl; la carretilla roja tiene que llegar a la máquina ---
const CAJA_INI=[[2,0,2,0],[4,4,2,0],[5,1,2,0],[0,5,2,1],[1,0,3,0],[1,3,2,1],[0,2,2,0],[4,0,2,1],[4,2,2,0],[2,2,2,1],[2,5,2,1],[3,0,2,0]],CW=66,CX=200,CY=52,COLS=6,FILAS=6;
function cajasEst(){const f=d7();if(!f.cajas){f.cajas=CAJA_INI.map(p=>[p[0],p[1]]);save()}return f.cajas}
function cajasPinta(sel,dx,dy){const p=cajasEst();CAJA_INI.forEach((q,i)=>{let x=CX+p[i][1]*CW,y=CY+p[i][0]*CW;if(i===sel){x+=dx||0;y+=dy||0}
  allSel(`.caja[data-i="${i}"]`,e=>e.style.transform=`translate(${x}px,${y}px)`)})}
function ocupada(i,r,c){const p=cajasEst();return CAJA_INI.some((q,j)=>{if(j===i)return false;const[l,v]=[q[2],q[3]];for(let k=0;k<l;k++){if((v?p[j][0]+k:p[j][0])===r&&(v?p[j][1]:p[j][1]+k)===c)return true}return false})}
function rango(i){const p=cajasEst(),[l,v]=[CAJA_INI[i][2],CAJA_INI[i][3]];let lo=0,hi=0;
  for(let s=1;;s++){const r=v?p[i][0]-s:p[i][0],c=v?p[i][1]:p[i][1]-s;if(r<0||c<0||ocupada(i,r,c))break;lo=-s}
  for(let s=1;;s++){const r=v?p[i][0]+l-1+s:p[i][0],c=v?p[i][1]:p[i][1]+l-1+s;if(r>=FILAS||c>=COLS||ocupada(i,r,c))break;hi=s}return[lo,hi]}
let arr=null;
document.addEventListener('pointerdown',e=>{if(!SC||SC.svg!==SVG.cajas||busy||d7().carretilla)return;const[x,y]=rel(e),c=Math.floor((x-CX)/CW),r=Math.floor((y-CY)/CW);
  if(c<0||r<0||c>=COLS||r>=FILAS)return;const p=cajasEst();
  const i=CAJA_INI.findIndex((q,j)=>{for(let k=0;k<q[2];k++){if((q[3]?p[j][0]+k:p[j][0])===r&&(q[3]?p[j][1]:p[j][1]+k)===c)return true}return false});
  if(i<0)return;arr={i,x0:x,y0:y,rg:rango(i),d:0}},true);
document.addEventListener('pointermove',e=>{if(!arr)return;const[x,y]=rel(e),v=CAJA_INI[arr.i][3];let d=(v?y-arr.y0:x-arr.x0)/CW;
  d=Math.max(arr.rg[0],Math.min(arr.rg[1],d));arr.d=d;cajasPinta(arr.i,v?0:d*CW,v?d*CW:0)},true);
document.addEventListener('pointerup',()=>{if(!arr)return;const a=arr;arr=null;const n=Math.round(a.d),p=cajasEst(),v=CAJA_INI[a.i][3];
  if(n){if(v)p[a.i][0]+=n;else p[a.i][1]+=n;d7().movs=(d7().movs||0)+1;save();AU.sfx('arrastre')}cajasPinta();
  if(p[0][1]===COLS-2&&!d7().carretilla)run(carretillaFuera)},true);
async function carretillaFuera(){const f=d7();f.carretilla=1;save();$('#acts').innerHTML='';
  await anima('.caja[data-i="0"]',[{transform:`translate(${CX+4*CW}px,${CY+2*CW}px)`},{transform:`translate(${CX+5*CW+30}px,${CY+2*CW}px)`}],{duration:700,easing:'ease-in'});
  await bubble('La carretilla rueda hasta la máquina. Paso libre.',3000);goScene(3)}
function cajasReinicia(){const f=d7();f.cajas=null;f.movs=0;save();cajasPinta()}

DAYS[7]=[
// ===== Periódico =====
{svg:SVG.periodico7,dark:0,tools:['mano','linterna','lupa'],cartel:'MIÉRCOLES<br>7 DE DICIEMBRE DE 1927',
 spots:[
  {id:'p7royal',tool:'lupa',x:243,y:410,w:240,h:34,act:async()=>{await bubble('«Café Royal, calle del Farol. Esta noche, LOLA y sus "artistas". Reservados discretos.» Ya me imagino qué clase de artistas.',4800)}},
  {id:'p7ultra',tool:'lupa',x:243,y:455,w:240,h:30,act:async()=>{await bubble('«Ultramarinos Zabaleta. Se fía a las conserveras.» En este puerto, quien no fía no vende.',4000)}},
  {id:'p7breve',tool:'lupa',x:539,y:432,w:280,h:44,act:async()=>{await bubble('Doña Puri me ha visto de noche cerca del palacete. Esta mujer tiene ojos en la nuca.',4200)}},
  {id:'p7marea',tool:'lupa',x:539,y:467,w:200,h:10,act:async()=>{await bubble('«Viento sur. Pleamar a las 5:30.»',3000)}},
 ],
 enter:async()=>{persona('Mateo «el Rubio»','Dice que no se cargará ni una caja «hasta que arreglen la máquina» del accidente.');
   nar('Miércoles. Aitor ha dormido tres horas y aun así se empeña en venir conmigo. «A la conservera no vas sola», dice.<br><br><i>Léelo bien: la letra pequeña también cuenta.</i>');
   narBtn('Ir a la conservera',async()=>{narPaso('La conservera Arrieta huele a sardina, a aceite y a vapor. Dentro, una fila de mujeres con pañuelo llena latas sin levantar la vista.');await sleep(5000);goScene(1)})}},

// ===== La conservera =====
{svg:SVG.conservera,dark:.1,tools:['mano','linterna','lupa'],cartel:'ALTAMAR<br>LA CONSERVERA ARRIETA',
 ekiSpots:[
  {who:'Una obrera',x:210,y:360,act:async()=>{await bubble('Eki se planta delante de una obrera y pone su mejor cara. La mujer mira a los lados y le da una sardina por debajo de la mesa.',4600);ekiLog('Las obreras de la conservera','le dan sardinas a escondidas.')}},
  {who:'Doña Remedios',x:640,y:360,act:async()=>{await bubble('Eki va hacia Doña Remedios… «¡Ese chucho, fuera de mi fábrica!». Eki da media vuelta sin discutir.',4400);ekiLog('Doña Remedios','no la deja acercarse: «¡fuera de mi fábrica!».')}},
 ],
 spots:[
  {id:'remedios',tool:'mano',x:640,y:360,r:90,once:false,act:async()=>{const f=d7();
    if(!f.permiso){await talk('Doña Remedios','(Sin dejar de mirar la fila de obreras.) Aitor. Tú siempre de noche, y ahora de día. ¿Y la señorita?');
      await talk('Aitor','Viene conmigo, Remedios. Solo quiere mirar.');
      await talk('Doña Remedios','Cinco minutos. Y que nadie toque la máquina del fondo: ya se llevó a un chaval por delante, no quiero otro.');endTalk();
      f.permiso=1;save();persona('Doña Remedios','La encargada de la conservera. Seca y desconfiada, pero conoce a Aitor de toda la vida.');return}
    await talk('Doña Remedios','Cinco minutos he dicho.');endTalk()}},
  {id:'obrera',tool:'mano',x:330,y:360,r:70,once:false,act:async()=>{const f=d7();
    if(f.lola){await talk('La obrera charlatana','(Bajito.) Yo no le he dicho nada, ¿eh?');endTalk();return}
    await talk('Candela','¿Conocía usted a Don Julián?');
    await talk('La obrera charlatana','¿Don Julián? Los jueves se iba a la calle del Farol, a oír cantar a la Lola…');
    await talk('La obrera charlatana','(Las demás se ríen por lo bajo.) Bueno… a «oír cantar».');
    await talk('Candela','(Lola. «L.»)');
    await talk('La obrera charlatana','Y de la máquina mejor ni hablar. Al chaval de los Goñi se lo llevó en octubre. Dieciséis años tenía.');endTalk();
    f.lola=1;save();await pista('lola','Lola, la «artista»','Una obrera: Don Julián iba los jueves a la calle del Farol «a oír cantar» a la Lola. ¿Es «L.», la del testamento?');
    persona('Lola','La «artista» de la calle del Farol. Don Julián iba los jueves «a oírla cantar».')}},
  {id:'obreras',tool:'mano',x:210,y:360,r:60,once:false,act:async()=>{await talk('Una obrera','(Sin levantar la vista de las latas.) Ni me mire, señorita, que me descuentan.');endTalk()}},
  {id:'obrera3',tool:'mano',x:470,y:360,r:60,once:false,act:async()=>{await talk('Una obrera','Hemos vuelto porque hay que comer. Pero la máquina, que la arreglen primero.');endTalk()}},
  {id:'aitor7',tool:'mano',x:90,y:340,r:60,once:false,act:async()=>{await talk('Aitor','Remedios es buena gente. Seca como un bacalao, pero buena gente.');endTalk()}},
 ],
 check:()=>{const f=d7();if(f.nave||!f.permiso||!f.lola)return;f.nave=1;save();
   nar('La máquina del accidente está al fondo, en la nave. Pero no se ve: delante hay una montaña de cajas que nadie carga.');narBtn('A la nave',()=>goScene(2))},
 enter:async()=>{const f=d7();if(f.nave){nar('La nave está al fondo.');narBtn('A la nave',()=>goScene(2));return}
   nar(f.permiso?'Las obreras llenan latas sin parar. Doña Remedios no me quita ojo.':'Doña Remedios, la encargada, vigila la fila de obreras como un guardia civil.')}},

// ===== La nave: las cajas =====
{svg:SVG.cajas,dark:.1,tools:['mano','linterna','lupa'],
 enter:async()=>{const f=d7();if(f.carretilla){goScene(3);return}cajasPinta();
   nar('Las cajas de latas tapan el paso a la máquina. Cada una solo se puede empujar por su raíl: unas a lo largo, otras a lo ancho.<br><br><i>Arrastra las cajas con el dedo hasta que la carretilla roja pueda llegar a la máquina.</i>');
   narBtn('Volver con las obreras',()=>goScene(1));const b=document.createElement('button');b.className='go';b.textContent='Colocar las cajas como estaban';b.onclick=cajasReinicia;$('#acts').appendChild(b)}},

// ===== La máquina =====
{svg:SVG.maquina,dark:.35,tools:['mano','linterna','lupa'],
 spots:[
  {id:'reja',tool:'lupa',x:330,y:200,w:270,h:270,act:async()=>{await bubble('Los agujeros de la reja de protección: limpios, sin óxido y sin roscas rotas. La reja no se cayó: alguien la desatornilló con cuidado.',5000);
    await pista('reja','La reja de la máquina','A la máquina del accidente le quitaron la reja de protección a propósito: los tornillos se sacaron, no se rompieron.')}},
  {id:'ordenL',tool:'linterna',x:485,y:450,w:90,h:56,act:async()=>{await bubble('Debajo de la máquina, entre la grasa, hay un papel arrugado.',3200)}},
  {id:'orden',tool:'mano',x:485,y:450,r:50,once:false,when:()=>found('ordenL'),act:async()=>{
    await docShow('<div style="text-align:left;font-size:15px;line-height:1.7"><b style="color:#8a2a20">CONSERVAS ARRIETA · Orden a la encargada</b><br>Quítese la reja de la máquina n.º 3. Estorba y retrasa: con ella no sacamos las latas que pide el barco.<br><span style="float:right">J. A. · 2 de octubre de 1927</span></div>');
    if(hasP('orden'))return;
    await pista('orden','La orden de Don Julián','Él mismo mandó quitar la reja de la máquina «para sacar más latas», el 2 de octubre. Semanas después, la máquina mató a un chaval de dieciséis años.');
    persona('Don Julián Arrieta','Mandó quitar la reja de protección de la máquina para producir más. La máquina mató a un chaval en octubre.');
    persona('Mateo «el Rubio»','Tenía motivos de sobra contra Don Julián: la máquina sin reja mató al chaval de los Goñi.')}},
 ],
 check:()=>{const f=d7();if(f.maq||!found('reja')||!hasP('orden'))return;f.maq=1;save();
   nar('Don Julián mandó quitar la reja. Y el chaval de los Goñi lo pagó. Ahora entiendo a Mateo.');
   narBtn('Volver a la entrada',async()=>{narPaso('Al volver, la puerta de la oficina de Doña Remedios está abierta: ella ha salido al muelle a discutir con un camionero.');await sleep(5000);goScene(4)})},
 enter:async()=>{const f=d7();if(f.maq){nar('La máquina, parada. Ya lo he visto todo.');narBtn('Volver a la entrada',()=>goScene(4));return}
   nar('La máquina del accidente, parada. Huele a grasa y a hierro. Abajo, todo está a oscuras.')}},

// ===== La oficina de la encargada =====
{svg:SVG.oficina,dark:.3,tools:['mano','linterna','lupa'],
 laika:()=>d7().venenoL?null:(d7().venenoL=1,save(),{x:160,t:'Laika olfatea el estante de los frascos y se aparta estornudando. Ni ella quiere saber nada de eso.'}),
 spots:[
  {id:'registro',tool:'lupa',x:250,y:286,w:150,h:44,act:async()=>{await bubble('«Registro de venenos. 14-XI · 2 frascos · Remedios (ratas del almacén). 28-XI · 1 frasco · C. Arrieta.»',5000);
    await pista('matarratas','El registro del matarratas','El 28 de noviembre, dos días antes de la muerte de Don Julián, alguien firmó por un frasco de matarratas: «C. Arrieta».');
    persona('Clara Arrieta','El 28 de noviembre firmó por un frasco de matarratas en la conservera.')}},
  {id:'envios',tool:'lupa',x:470,y:285,w:130,h:44,act:async()=>{await bubble('El libro de envíos: fechas y número de cajas… pero en vez de los destinos, unos símbolos raros. Lo copio tal cual en la libreta.',4800);
    await pista('envios','El libro de envíos, en clave','12-XI ✶◆✶ 40 cajas · 19-XI ◆◆✶ 38 · 26-XI ✶✶◆ 44 · 30-XI ◆✶◆ (sin cajas). ¿Qué significan los símbolos?')}},
  {id:'frascosV',tool:'lupa',x:160,y:62,w:200,h:50,act:async()=>{await bubble('«VENENO. Matarratas.» Con una cucharada se tumba a un perro. O a un hombre.',4000)}},
 ],
 check:()=>{const f=d7();if(f.pillada||!found('registro')||!found('envios'))return;run(fuera7)},
 enter:async()=>{const f=d7();if(f.pillada){nar('Ya estamos fuera.');narBtn('Volver a casa',()=>{narSigue=true;goScene(5)});return}
   nar('La oficina de Doña Remedios. Un estante de frascos, una mesa con libros y una lámpara encendida. Rápido.')}},

// ===== Esa noche =====
{svg:SVG.noche,dark:.35,tools:['mano','linterna','lupa'],sleep:1,laikaHome:120,ekiHome:215,cartel:'ALTAMAR<br>ESA NOCHE',
 enter:async()=>{nar(`Aitor ha salido de ronda. Laika y Eki duermen junto al fogón.<br><br>Pistas de hoy: ${S.pistas.filter(p=>p.day===7).length}.<br>«L.»… ¿Lola, la «artista» de la calle del Farol?`);
   await sleep(5000);narAdd('Don Julián mandó quitar la reja que habría salvado a un chaval. Y Clara firmó por un frasco de matarratas dos días antes de que muriera su padre.<br><br>Mañana, la calle del Farol.');
   narBtn('Cerrar el día',()=>{endDay();SC=null;drawCal();show('cal');bubCal('Día 7 resuelto. Mañana, la calle del Farol.')})}},
];
async function fuera7(){const f=d7();f.pillada=1;save();await sleep(400);AU.sfx('toc');await shake();
  await talk('Doña Remedios','(Desde la puerta.) ¿Qué hace usted en mi oficina?');
  await talk('Candela','Buscaba a alguien que me explicara lo de la máquina, Doña Remedios.');
  await talk('Doña Remedios','(Mira el libro abierto y luego a Aitor.) Fuera. Los dos. Y tú, Aitor, que te conozco desde que llevabas pantalón corto: no me vuelvas a traer problemas.');endTalk();
  await talk('Aitor','(Ya en la calle.) La calle del Farol… Allí las farolas son rojas, y los serenos aprendemos pronto a mirar para otro lado.');
  await talk('Candela','Pues mañana no vamos a mirar para otro lado.');endTalk();
  nar('Volvemos a casa por el muelle. Las cajas de latas siguen allí, sin que nadie las cargue.');
  narBtn('Volver a casa',()=>{narSigue=true;goScene(5)})}
FACES['Doña Remedios']=FACE_REMEDIOS;FACES['La obrera charlatana']=FACE_OBRERA;FACES['Una obrera']=FACE_OBRERA;
