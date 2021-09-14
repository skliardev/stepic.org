function checkUser(name){
 let access = (name == 'admin')?'Без доступа к статистике':
              (name == 'director')?'Полный доступ':
              (name == '')?'Введите логин':'-';

 return access;   
}