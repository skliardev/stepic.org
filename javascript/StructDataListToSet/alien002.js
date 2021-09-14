function modifyMap(map){
    let resStr = '';
    for (let entry of map) {
        let set = new Set();
        if (Array.isArray(entry[1])) {
            for (let el of entry[1]) {set.add(el);}
            map.set(entry[0],set);
        } else {map.delete(entry[0]);}
    }
    for (let entry of map) {
        resStr += entry[0] + ":";
        for (let el of entry[1]) {resStr += el;}
        resStr += ";";
    }
    console.log(resStr);
}