function modifyObj(person){
 delete person.info;
 person.age = 25;
 person.work.level = "middle";
 return person;   
}