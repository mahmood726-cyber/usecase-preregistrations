import {createRequire} from 'module'; const require=createRequire(import.meta.url);
require('./pb_engine_extract.js'); const P=require('./plus-engine.js');
const yi=[-0.45,-0.30,-0.62,-0.10,-0.85,-0.20,-0.05,-0.70,0.10,-0.95,-0.35,-1.20];
const sei=[0.05,0.08,0.12,0.15,0.20,0.25,0.30,0.35,0.40,0.45,0.52,0.60];
const rows=yi.map((t,i)=>({te:t,se:sei[i]}));
const e=globalThis.__almPubBiasEngine.eggerGeneric(rows);
const pet=P.pet(rows), pe=P.peese(rows), c=P.conditional(pet,pe);
console.log(JSON.stringify({egger_t:e.statistic,egger_p:e.p,pet:pet.values,peese:pe.values,cond:c.values}));
