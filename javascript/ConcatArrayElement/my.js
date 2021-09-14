function allNumsToString(obj){
 var arr = [];
     for(let key in obj) {
         arr = arr.concat(obj[key]);
     }
 return arr.sort((a,b) => a-b ).join(';');   
}