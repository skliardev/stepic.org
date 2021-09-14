package com.vk.brainstorm;

import java.util.function.DoubleUnaryOperator;

public class Main {

    public static void main(String[] args) {
	// write your code here

        System.out.println("Finish result: " + integrate(x -> 1, 0, 10) + '\n'); //10.0
        System.out.println("Finish result: " + integrate(x -> x + 2, 0, 10) + '\n'); //70.0
        System.out.println("Finish result: " + integrate( x -> Math.sin(x) / x , 1, 5) + '\n'); //0.603848
    }

    public static double integrate(DoubleUnaryOperator f, double a, double b) {
        final double accuracy = 1e-7;
        final int maxSteps = (int) ((b - a) / accuracy);
        double summary = 0;
        boolean secondCycle = false;
        double result = 0;

        for(int nSteps = 1; nSteps <= maxSteps; nSteps *= 10) {
            /*
             h - ширина шага, при кол-ве итераций nStep
             nStep начинается с 1 и заканчивая maxSteps
             это означает что с каждым разом фу-ия будет дробиться на nStep прямоугольников
             */
            double h = (b - a) / nSteps;
            summary = 0;

            //System.out.println("Current Step = " + h);

            //Calculation block
            for (int j = 0; j < nSteps ; ++j) {
                summary += f.applyAsDouble(a + j*h );
            }
            summary *= (double) h;

            if(!secondCycle) { result = summary; secondCycle = true; }
            else if((int)(summary/accuracy) == (int)(result/accuracy)) { break; }
            else { result = summary; }

            //System.out.println("Current Result = " + summary);
        }

        return result;
    }
}
