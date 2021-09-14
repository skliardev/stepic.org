package com.vk.brainstorm;

public class Main {

    public static final int pointX = 7;
    public static final int pointY = -3;

    public static void main(String[] args) {
        Robot rob = new Robot(-5,10, Direction.UP);
        moveRobot(rob, pointX, pointY);
        if(rob.getX() == pointX && rob.getY() == pointY)
            System.out.println("You win!");
    }

    public static void moveRobot(Robot robot, int toX, int toY) {
        if(robot.getX() > toX) {
            //Повернуть в направление Left
            switch(robot.getDirection()) {
                case LEFT: break;
                case RIGHT: robot.turnRight(); robot.turnRight(); break;
                case UP: robot.turnLeft(); break;
                case DOWN: robot.turnRight(); break;
            }
        }
        else {
            //Повернуть в направление Right
            switch(robot.getDirection()) {
                case RIGHT: break;
                case LEFT: robot.turnLeft(); robot.turnLeft(); break;
                case UP: robot.turnRight(); break;
                case DOWN: robot.turnLeft(); break;
            }
        }

        while (robot.getX() != toX) {
            robot.stepForward();
        }

        if(robot.getY() > toY) {
            //Повернуть в направление Down
            switch(robot.getDirection()) {
                case DOWN: break;
                case UP: robot.turnRight(); robot.turnRight(); break;
                case RIGHT: robot.turnRight(); break;
                case LEFT: robot.turnLeft(); break;
            }
        }
        else {
            //Повернуть в направление Up
            switch(robot.getDirection()) {
                case DOWN: robot.turnRight(); robot.turnRight(); break;
                case UP: break;
                case RIGHT: robot.turnLeft(); break;
                case LEFT: robot.turnRight(); break;
            }
        }

        while (robot.getY() != toY) {
            robot.stepForward();
        }
    }
}

//    Интересная задача ! Для поиска оптимального числа поворот вокруг себя, то есть для выбора направления "шагания" робота использовал:
//        1. векторное произведение векторов (только по двумерным компонентам x, y)  - для определения направления поворота в нужную сторону:
//        "==0" поворот не требуется просто шагаем в направлении нужной оси;
//        ">0" делаем поворот налево;
//        "<0" делаем поворот направо;
//        2. скалярное произведение векторов  - для определения числа поворотов в нужную сторону:
//        ">=0" требуется один поворот;
//        "<0" требуются 2 поворота;
//        А для простоты вычислений систему координат лучше перенести в Робота (его центр тяжести, в данном случае его первоначальное положение) . Тогда  ВЕЛИЧИНЫ КОСВЕННО, ХАРАКТЕРИЗУЮЩИЕ УГОЛ между "единичным" направлением вектор робота и радиус-вектором конечного положения в новой системе координат, легко рассчитываются через скалярное и векторное произведение данных векторов как попарное умножение (соответствующих в одном случае координат, либо не соответствующих в другом) с последующим сложением/вычитанием координат векторов.
//        Таким образом выходит, что повороты либо не нужны в самом примитивном случае, либо их максимальное число равно двум.
//
//public static void moveRobot(Robot robot, int toX, int toY) {
//
//        // перенос в систему координат, где центр - текущее положение робота:
//        int X, Y, i = 0, j = 0, angle, turn, num_step;
//
//        X = toX - robot.getX();
//        Y = toY - robot.getY();
//
//        Direction d = robot.getDirection();
//
//        // Определение направления взгляда робота:
//        switch (d) {
//        case UP:
//        i = 0; j = 1;
//        break;
//
//        case DOWN:
//        i = 0; j = -1;
//        break;
//
//        case RIGHT:
//        i = 1; j = 0;
//        break;
//
//        case LEFT:
//        i = -1; j = 0;
//        break;
//        }
//
//        turn  = i * Y - j * X;
//        angle = i * X + j * Y;
//
//        if (angle > 0) {
//
//        num_step = (d == Direction.UP || d == Direction.DOWN)? Math.abs(Y):Math.abs(X);
//        for(int k = 0; k < num_step; ++k) {
//        robot.stepForward();
//        }
//
//        if (turn > 0) {
//        robot.turnLeft();
//        } else {
//        robot.turnRight();
//        }
//
//        d = robot.getDirection();
//        num_step = (d == Direction.UP || d == Direction.DOWN)? Math.abs(Y):Math.abs(X);
//        for(int k = 0; k < num_step; ++k) {
//        robot.stepForward();
//        }
//
//        } else if (angle < 0) {
//
//        for(int k = 0; k < 2; ++k) {
//        if (turn > 0) {
//        robot.turnLeft();
//        } else {
//        robot.turnRight();
//        }
//        d = robot.getDirection();
//        num_step = (d == Direction.UP || d == Direction.DOWN)? Math.abs(Y):Math.abs(X);
//        for(int l = 0; l < num_step; ++l) {
//        robot.stepForward();
//        }
//        }
//        } else if (angle == 0) {
//        if (turn > 0) {
//        robot.turnLeft();
//        } else {
//        robot.turnRight();
//        }
//        d = robot.getDirection();
//        num_step = (d == Direction.UP || d == Direction.DOWN)? Math.abs(Y):Math.abs(X);
//        for(int k = 0; k < num_step; ++k) {
//        robot.stepForward();
//        }
//        }
//
//        }
