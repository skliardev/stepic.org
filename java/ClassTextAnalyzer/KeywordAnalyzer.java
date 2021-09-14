package com.vk.brainstorm;

public abstract class KeywordAnalyzer implements TextAnalyzer {

    protected abstract String[] getKeywords();
    protected abstract Label getLabel();

    @Override
    public Label processText(String text) {
        for (String keyValue : getKeywords()) {
            if( text.contains(keyValue) ) return getLabel();
        }
        return Label.OK;
    }
}
