package Model;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;
import java.util.ArrayList;

public class Parser {
    private String lastName = "unknown";
    private String firstName = "unknown";
    private String patronymic = "unknown";
    private char sex = 'E';
    private long phoneNumber = -1;
    DateTimeFormatter df = DateTimeFormatter.ofPattern("dd.MM.yyyy");
    private LocalDate birthDate = LocalDate.of(1900, 01, 01);
    private LocalDate pattern = LocalDate.of(1900, 01, 01);
    ArrayList<Object> list;

    public String Formatter(String s) {
        list = new ArrayList<>(6);
        String message = "true";
        String[] elements = s.split(",");
        for (String element : elements) {
            element = element.trim();
            FormatToLong(element);
            FormatToDate(element);
            FormatToChar(element);
            String[] fIO = element.split(" ");
            if (fIO.length == 3) {
                lastName = fIO[0];
                firstName = fIO[1];
                patronymic = fIO[2];
            }
        }
        if (lastName.equals("unknown") || lastName.matches(".*\\d.*") || firstName.matches(".*\\d.*")
                || patronymic.matches(".*\\d.*")) {
            return "Формат имени введен неверно, пример - 'Иванов Иван Иванович'.";
        } else {
            list.add(lastName);
            list.add(firstName);
            list.add(patronymic);
        }
        if (birthDate.isEqual(pattern)) {
            return "Формат даты введен неверно, пример - '01.01.1970'.";
        } else {
            list.add(birthDate);
        }
        if (phoneNumber != -1) {
            list.add(phoneNumber);
        } else {
            return "Формат номера телефона введен неверно, пример - '89991234567'.";
        }
        if (sex == 'м' || sex == 'ж') {
            list.add(sex);
        } else {
            return "Пол человека введен неверно, пример - 'м' - мужской, 'ж' - женский.";
        }

//        System.out.println(lastName + " " + firstName + " " + patronymic + " "
//                + sex + " " + PrintDate(birthDate) + " " + phoneNumber);
        return message;
    }

    private boolean FormatToLong(String element) {
        try {
            phoneNumber = Math.abs(Long.parseLong(element));
            return true;
        } catch (NumberFormatException e) {
            return false;
        }
    }

    private boolean FormatToChar(String element) {
        if (element.length() == 1) {
            sex = element.toCharArray()[0];
            return true;
        } else {
            return false;
        }
    }

    private boolean FormatToDate(String element) {
        try {
            birthDate = LocalDate.parse(element, df);
            return true;
        } catch (DateTimeParseException e) {
            return false;
        }
    }

    public String CheckStringLength(String profile) {
        String[] elements = profile.split(",");
        for (String element : elements) {
            element = element.trim();
        }
        if (elements.length != 4)
            return "Количество введенных данных  " + elements.length + ". Должно быть 4. Данные не записаны!";
        else
            return "true";
    }

    public String PrintDate(LocalDate date) {//можно удалить
        try {
            return df.format(date);
        } catch (Exception e) {
            return df.format(birthDate);
        }
    }
    public ArrayList GetList(){
        return list;
    }
}

