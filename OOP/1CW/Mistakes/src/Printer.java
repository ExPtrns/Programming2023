class Expr {
    public static String expr(char a) throws Exception {
// Введите свое решение ниже
        String line = String.valueOf(a);
        if (line.equals(" ")) {
            throw new Exception("Пустая строка введена.");
        } else {
            return ("Ваш ввод - " + a);
        }
    }
}
// Не удаляйте этот класс - он нужен для вывода результатов на экран и проверки

public class Printer {
    public static void main(String[] args) {
        char a;

        if (args.length == 0) {
            a = ' '; // Значение по умолчанию, если аргументы не были предоставлены
        } else {
            a = args[0].charAt(0); // Преобразуйте первый аргумент командной строки в символ
        }

        try {
            String result = Expr.expr(a);
            System.out.println("Result: " + result);
        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}