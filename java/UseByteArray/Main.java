package com.company;

import java.io.*;

public class Main {
    public static void main(String[] args) {
        //Test
        byte[] arr = {65, 66, 13, 13, 13, 10, 10, 13, 67, 13, 13};
        ByteArrayInputStream inputStream = new ByteArrayInputStream(arr);
        System.setIn(inputStream);
        //Proga
        int prev = 0, next = 0;
        try {
            if ((prev = System.in.read()) >= 0){
                while ((next = System.in.read()) >= 0){
                    if(prev == 13 && next == 10) {
                        prev = next;
                        continue;
                    }
                    System.out.write(prev);
                    prev = next;
                }
                System.out.write(prev);
            }
            System.out.flush();
        } catch (IOException e){
            e.printStackTrace();
        }
    }
}
