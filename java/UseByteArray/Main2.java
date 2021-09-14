package com.company;

import java.io.ByteArrayInputStream;
import java.io.IOException;

public class Main2 {
    public static void main(String[] args) {
        //Test
        byte[] arr = {65, 66, 13, 13, 13, 10, 10, 13, 67, 13, 13};
        ByteArrayInputStream inputStream = new ByteArrayInputStream(arr);
        System.setIn(inputStream);
        //Proga
        int next = -1, prev = 0;
        try {
            do {
                prev = next;
                next = System.in.read();
                if (prev == 13 & next == 10) {
                    continue;
                } else if (prev >= 0) {
                    //System.out.println(prev);
                    System.out.write(prev);
                    System.out.flush();
                }
            } while (next != -1);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
