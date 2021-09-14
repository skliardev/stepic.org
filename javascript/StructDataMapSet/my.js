function swap(map, key){
    let res = new Map();
    if(!map.has(key)) return false;
    for (let lst of map) {
        if(lst[0] === key) res.set(lst[1], lst[0]);
        else res.set(lst[0], lst[1]);
    }
    return res;
}

let mm = new Map([['user',  'Tom'], ['confirm', 'isConfirmed']]);
let a = swap(mm, "confirm"); //{"user":"Tom","confirm":"isConfirmed"}
console.log(a);