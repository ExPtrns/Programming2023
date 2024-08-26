
public class Main {
    public static void main(String[] args) {
        //Реализуйте структуру телефонной книги с помощью HashMap.
        //Программа также должна учитывать, что в во входной структуре будут повторяющиеся имена с разными телефонами,
        // их необходимо считать, как одного человека с разными телефонами. Вывод должен быть отсортирован по убыванию
        // числа телефонов.
        PhoneBook phoneBook = new PhoneBook();
        phoneBook.add("Denis",8834511);
        phoneBook.add("Maksim",98834521);
        phoneBook.add("Andrey",98834531);
        phoneBook.add("Valentina",98834541);
        phoneBook.add("Denis",91234512);
        phoneBook.add("Denis",91234513);
        phoneBook.add("Valentina",98834542);
        phoneBook.add("Valentina",98834543);
        phoneBook.add("Valentina",98834544);
        phoneBook.add("Andrey",98834532);
        phoneBook.add("Denis",91234514);
        System.out.println(PhoneBook.getPhoneBook());
        phoneBook.printPhoneBook();
    }
}