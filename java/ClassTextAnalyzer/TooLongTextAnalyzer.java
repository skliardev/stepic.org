package com.vk.brainstorm;

public class TooLongTextAnalyzer implements TextAnalyzer {
    private int maxLength;

    public TooLongTextAnalyzer(int commentMaxLength) {
        this.maxLength = commentMaxLength;
    }

    @Override
    public Label processText(String text) {
        if(text.length() > maxLength) return Label.TOO_LONG;
        return Label.OK;
    }
}
