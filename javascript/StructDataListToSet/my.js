in_line = {"log14":[1,2,3,3,2,1],"log15":"none data","log16":["s","S"]};
let data = new Map(Object.entries(in_line));

function modifyMap(map){
    let resStr = '';
    for (let select of map) {
        if(select[1] === "none data") continue;
        let arr = '';
        for (let s of (new Set(select[1])))
            arr += s;
        resStr += select[0] + ':' + arr + ';';
    }
    console.log(resStr);
}

modifyMap(data);