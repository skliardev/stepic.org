package com.vk.brainstorm;

import java.util.function.DoubleUnaryOperator;

public class Main2 {

    public static void main(String[] args) {
        // write your code here

        System.out.println("Finish result: " + integrate(x -> 1, 0, 10) + '\n'); //10.0
        System.out.println("Finish result: " + integrate(x -> x + 2, 0, 10) + '\n'); //70.0
        System.out.println("Finish result: " + integrate( x -> Math.sin(x) / x , 1, 5) + '\n'); //0.603848
    }

    public static double integrate(DoubleUnaryOperator f, double a, double b) {
        final double accuracy = 1e-6;
        final int maxSteps = (int) ((b - a) / accuracy);
        double h = (b - a) / maxSteps;
        double summary = 0;


        for (int j = 0; j < maxSteps ; ++j) {
            summary += f.applyAsDouble(a + j*h );
        }
        summary *= (double) h;

        return summary;
    }
}
