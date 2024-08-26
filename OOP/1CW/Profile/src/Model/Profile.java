package Model;

import java.io.*;
import java.util.ArrayList;


public class Profile {
    public String addProfile(ArrayList<Object> list) {
        String path = list.get(0).toString() + ".txt";
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(path, true))) {
            for (Object value : list) {
                writer.write("<" + value + ">");
            }
            writer.write("\n");
            return "Данные записаны.";
        } catch (IOException e) {
            return e.toString();
        }
    }

    public String getFiles(String path) {
        File dir = new File(path);
        File[] files = dir.listFiles();
        StringBuilder sb = new StringBuilder();
        assert files != null;
        try {
            for (File file : files) {
                if (file.isFile() && file.getName().contains("txt")) {
                    sb.append(file.getName());
                    sb.append("\n");
                }
            }
        }catch (NullPointerException e){
            return "Укажите корректный путь к файлу в формате например - D:/Profile";
        }
        if (sb.length() > 0) {
            return sb.toString();
        } else return "Нет файлов в формате .txt.";
    }

    public String readFile(String path, String file) {

        try (BufferedReader reader = new BufferedReader(new FileReader(path + "/" + file));) {
            while (true) {
                StringBuilder sb = new StringBuilder();
                String line;
                while ((line = reader.readLine()) != null)
                    sb.append(line + "\n");
                return sb.toString();
            }
        } catch (Exception e) {
            return "Не удается найти указанный файл!\n";
        }
    }
}