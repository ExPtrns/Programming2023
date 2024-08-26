import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class Task3 {
    public static void main(String[] args) {
        String patch = "C:\\Users\\Кирилл\\Desktop\\rabota\\gb\\Ex\\sem2\\seminar25.12.2023\\src\\names.txt";
        List<String[]> strings = readInFile(patch);
        modificationArray(strings);
        writeInFile(patch, strings);
    }

    public static List<String[]> readInFile(String patch) {
        List<String[]> names = new ArrayList<>();
        try {
            BufferedReader br = new BufferedReader(new FileReader(patch));
            String line = "";
            while ((line = br.readLine()) != null) {
                names.add(line.split("="));
            }
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
        return names;
    }

    public static void modificationArray(List<String[]> names) {
        for (String[] arrayString : names) {
            if (!arrayString[1].equals("?") && !checkInteger(arrayString[1])) {
                throw new IllegalArgumentException("Элемент не ? и не число");
            }
            if (arrayString[1].equals("?"))
                arrayString[1] = String.valueOf(arrayString[0].length());
        }
    }

    public static boolean checkInteger(String string) {
        try {
            Integer.parseInt(string);
            return true;
        } catch (NumberFormatException e) {
            return false;
        }
    }

    public static void writeInFile(String patch, List<String[]> arrays) {
        try {
            BufferedWriter bw = new BufferedWriter(new FileWriter(patch));
            for (String[] strings : arrays) {
                bw.write(strings[0] + "=" + strings[1] + "\n");
            }
            bw.close();
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
    }
}