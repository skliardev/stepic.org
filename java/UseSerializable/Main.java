package com.company;

import java.io.*;
import java.util.Objects;

class Animal implements Serializable {
    private final String name;

    public Animal(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    @Override
    public boolean equals(Object obj) {
        if (obj instanceof Animal) {
            return Objects.equals(name, ((Animal) obj).name);
        }
        return false;
    }
}

public class Main {

    public static void main(String[] args) throws IOException {
	// write your code here
        Animal[] animalM1 = { new Animal("Cat"), new Animal("Dog"), new Animal("Elephant"),
                new Animal("Cock"), new Animal("Bull"), new Animal("Ant"),
                new Animal("Tentecles"), new Animal("Worm")};
        ByteArrayOutputStream bai = new ByteArrayOutputStream();
        ObjectOutputStream oos = new ObjectOutputStream(bai);
        oos.writeInt(animalM1.length);
        for (int i = 0; i < animalM1.length; i++) {
            oos.writeObject(animalM1[i]); //normal
            //if(i == animalM1.length - 1) oos.writeDouble(0.0); // Fail last data -> java.io.OptionalDataException
            //else oos.writeObject(animalM1[i]); //normal

            //oos.writeDouble(0.0); //Fail data -> java.io.OptionalDataException
            //oos.writeObject(null); //Fail data -> java.lang.NullPointerException
        }
        oos.flush();
        oos.close();
        Animal[] animalM2 = deserializeAnimalArray(bai.toByteArray());
        for (Animal animal : animalM2)
            System.out.println(animal.getName());
    }

    public static Animal[] deserializeAnimalArray(byte[] data) {
        // your implementation here
        // Получилли массив данных
        Animal[] animals = null;
        try (ObjectInputStream inObjectStream = new ObjectInputStream(new ByteArrayInputStream(data))) {

            int countAnimals = inObjectStream.readInt();
            animals = new Animal[countAnimals];

            for (int i = 0; i < countAnimals; ++ i) {
                animals[i] = (Animal) inObjectStream.readObject();
            }
        } catch (IOException | ClassNotFoundException e) { // java.lang.ClassCastException откуда?
            //System.out.println("Fail");                   // ClassCastException | ClassNotFoundException | IOException | NullPointerException e
            //e.printStackTrace();
            throw new IllegalArgumentException();
        }
        return animals;
    }

}
