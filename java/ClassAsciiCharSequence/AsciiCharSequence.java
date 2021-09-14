package com.vk.brainstorm;

import java.util.Arrays;

public class AsciiCharSequence implements CharSequence {
    private byte[] sequence;
    private int length;

    public AsciiCharSequence(byte[] sequence) {
        length = sequence.length;
        this.sequence = Arrays.copyOfRange(sequence, 0, sequence.length);

    }

    @Override
    public int length() {
        return length;
    }

    @Override
    public char charAt(int index) {
        return (char) this.sequence[index];
    }

    @Override
    public CharSequence subSequence(int start, int end) {
        return new AsciiCharSequence(Arrays.copyOfRange(sequence, start, end));
    }

    @Override
    public String toString() {
        return new String(sequence);
    }
}
