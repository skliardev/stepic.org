function checkUser(name){
 let access = (name == 'admin')?'��� ������� � ����������':
              (name == 'director')?'������ ������':
              (name == '')?'������� �����':'-';

 return access;   
}