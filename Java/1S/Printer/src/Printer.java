import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.List;

class Equation {
    public static String getSolution(String str) {
        // Введите свое решение ниже
        String result = "Result: {цельное выражение}";


        return result;

    }
}


// Не удаляйте этот класс - он нужен для вывода результатов на экран и проверки
public class Printer{
    public static void main(String[] args) {
        String file = "";

        if (args.length == 0) {
            file = "input.txt";
        }
        else{
            file = args[0];
        }

        Equation eq = new Equation();
        String result = eq.getSolution(file);
        System.out.println(result);
    }
}