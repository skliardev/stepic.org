package com.vk.brainstorm.tests;
import com.vk.brainstorm.KeywordAnalyzer;
import com.vk.brainstorm.SpamAnalyzer;

import java.util.Arrays;

public class TextStringClone {
    public static void main(String[] args) {
        String[] keywords = {"spam", "bad"};
        KeywordAnalyzer keyAn = new SpamAnalyzer(keywords);
        System.out.println("keywords = " + Arrays.toString(keywords));
        //System.out.println("keyAn = " + Arrays.toString(keyAn.getKeywords()));
        keywords[0] = "sex";
        System.out.println("keywords = " + Arrays.toString(keywords));
        //System.out.println("keyAn = " + Arrays.toString(keyAn.getKeywords())); //This text is old because I use the string.clone() method
    }
}
