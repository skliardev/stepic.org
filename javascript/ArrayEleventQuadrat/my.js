function modify(arr){
let result = [];
 arr.filter((el)=> el%2!=0 ).reduce((accum, el)=>{
     result.push(accum*el);
     return accum*el;
 },1);
 return result;   
}