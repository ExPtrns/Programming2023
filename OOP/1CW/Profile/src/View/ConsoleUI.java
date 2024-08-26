package View;

import Presenter.Presenter;
import View.comandsMenu.MainMenu;

import java.util.Scanner;

public class ConsoleUI implements View {
    private Scanner scanner;
    private Presenter presenter;
    boolean fl;
    private MainMenu menu;

    public ConsoleUI() {
        scanner = new Scanner(System.in);
        presenter = new Presenter(this);
        menu = new MainMenu(this);
    }

    @Override
    public void printAnswer(String answer) {
        System.out.println(answer);
    }

    @Override
    public void start() {
        fl = true;
        System.out.println("Программа по созданию профиля пользователей");
        while (fl) {
            System.out.println(menu.menuElements());
            String choice = scanner.nextLine();
            try {
                int correctChoice = Integer.parseInt(choice);
                System.out.println(correctChoice);
                menu.action(correctChoice);
            }catch (NumberFormatException e) {
                System.out.println("Такой операции не существует.");;
            }catch (IndexOutOfBoundsException e){
                System.out.println("Доступно только 3 операции.");
            }
        }

    }

    public void addElement() {
        System.out.println("Введите строку с данными : ФИО, пол, дата рождения, телефон (вводятся через запятую, ФИО через пробел):");
        String profile = scanner.nextLine();
        //String profile = "Timo Den Nik, м, 22.10.2000, 89298882929";
        presenter.addElement(profile);
    }

    public void getElementsList() {
        System.out.println("Укажите путь к файлу профиля:");
        String path = scanner.nextLine();
//        String path = "D:/Education/OOP/1CW/Profile";
        System.out.println("По указанному пути найдено:");
        presenter.getElementsList(path);
        String file = scanner.nextLine();
        presenter.read(path, file);
    }

    public void exit() {
        System.out.println("До свидания");
        fl = false;
    }
}
