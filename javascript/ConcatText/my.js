function filterPersons(str){
    let arr = str.split(',');
    let cstr = '';
    for(let name of arr) {
        if(name == 'Sam') continue;
        cstr += name;
    }
    //console.log(name);
    return cstr;
}