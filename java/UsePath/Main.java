package com.company;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class Main {

    public static void main(String[] args) {
        String str = "koawemf egknfm diam aa";
        System.out.println(str.contains("rer"));

        Path path = Paths.get("google.com");
        try {
            InputStream nn = Files.newInputStream(path);
        } catch (IOException e) {
            e.printStackTrace();
        }

        try {
            InputStream nif = new FileInputStream(path.toFile());
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        // write your code here
    }
}
