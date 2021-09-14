package com.vk.brainstorm;

import java.math.BigInteger;
import java.util.function.DoubleUnaryOperator;

public class Main3 {

    public static void main(String[] args) {
        // write your code here

        System.out.println("Finish result: " + integrate(x -> 1, 0, 10) + '\n'); //10.0
        System.out.println("Finish result: " + integrate(x -> x + 2, 0, 10) + '\n'); //70.0
        System.out.println("Finish result: " + integrate( x -> Math.sin(x) / x , 1, 5) + '\n'); //0.603848
    }

    public static double integrate(DoubleUnaryOperator f, double a, double b) {
        // масштаб
        BigInteger scale = BigInteger.valueOf(10);
        // шаг - величина обратная масштабу
        double step = 1 / scale.doubleValue();
        // площадь фигуры
        double area = 0.0;
        // площадь фигуры, посчитанная в прошлый раз
        double area_prev;
        // интегрируем в цикле
        for (double x = a; x < b; x = x + step) {
            // интегрируем по оси Y
            area += f.applyAsDouble(x);
        }
        // домножаем на шаг цикла
        area *= step;
        // пересчитываем в цикле площадь, пока не добьёмся точности
        do {
            // увеличиваем масштаб в 10 раз
            scale = scale.multiply(BigInteger.valueOf(10));
            // пересчитываем шаг
            step = 1 / scale.doubleValue();
            // запоминаем предыдущее значение площади
            area_prev = area;
            // обнуляем площадь
            area = 0.0;
            // интегрируем в цикле
            for (double x = a; x < b; x = x + step) {
                // интегрируем по оси Y
                area += f.applyAsDouble(x);
            }
            // домножаем на шаг цикла
            area *= step;
            // проверяем изменение в пересчитанной площади с заданной точностью
        } while (Math.abs(area - area_prev) > 0.001);
        // возвращаем значение площади
        return area;
    }
}
