function modifyMap(map){
    let res = '';
    for (let [k, v] of map) res += Array.isArray(v)? `${k}:${[...new Set(v)].join('')};`: '';
    console.log(res);
}