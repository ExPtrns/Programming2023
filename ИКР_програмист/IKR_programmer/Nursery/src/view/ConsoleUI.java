package view;

import model.AnimalType;
import presenter.Presenter;

import java.time.LocalDate;
import java.util.Scanner;

public class ConsoleUI implements View {
    private Scanner scanner;
    private Presenter presenter;
    boolean fl;
    AnimalType type;
    private MainMenu menu;

    public ConsoleUI() {
        scanner = new Scanner(System.in);
        presenter = new Presenter(this);
        menu = new MainMenu(this);
    }

    public void exit() {
        System.out.println("До свидания");
        fl = false;
    }

    @Override
    public void start() {
        fl = true;
        System.out.println("Реестр домашних животных");
        while (fl) {
            System.out.println("\nГлавное меню:");
            System.out.println(menu.menuElements());
            String choice = scanner.nextLine();
            try {
                int correctChoice = Integer.parseInt(choice);
                System.out.println(correctChoice);
                menu.action(correctChoice);
            } catch (NumberFormatException e) {
                System.out.println("Такой операции не существует.");
                ;
            } catch (IndexOutOfBoundsException e) {
                System.out.println("Такой операции нет в списке.");
            }
        }

    }

    @Override
    public void printAnswer(String answer) {
        System.out.println(answer);
    }

    public void addAnimalSkill() {
        getNurseryList();
        String skill;
        try {
            System.out.println("Укажите ID питомца для обучения: ");
            int iD = Integer.parseInt(scanner.nextLine());
            System.out.println("Какую комманду научился выполнять питомец? ");
            skill = scanner.nextLine();
            presenter.addAnimalSkill(iD, skill);
        } catch (NumberFormatException e) {
            System.out.println("Ошибка! ID должен быть числом.");
        }
    }

    public void addAnimal() {
        AnimalType animalType;
        String name;
        LocalDate birthDate;
        try {
            System.out.println("Выберите тип животного из списка:");
            int counter = 0;
            for (AnimalType type : AnimalType.values()) {
                System.out.print(++counter + ". ");
                System.out.println(type.name());
            }
            String choice = scanner.nextLine().toLowerCase();
            System.out.println(choice);

            if ("1коткошкаcat".contains(choice))
                animalType = AnimalType.Cat;
            else if ("2собакапесdog".contains(choice))
                animalType = AnimalType.Dog;
            else if ("3хомякhamster".contains(choice))
                animalType = AnimalType.Hamster;
            else {
                throw new Exception();
            }
            System.out.println("Введите имя животного");
            name = scanner.nextLine();
            System.out.println("Введите дату рождения: ");
            System.out.println("День: ");
            int day = Integer.parseInt(scanner.nextLine());
            System.out.println("Месяц: ");
            int month = Integer.parseInt(scanner.nextLine());
            System.out.println("Год: ");
            int year = Integer.parseInt(scanner.nextLine());
            birthDate = LocalDate.of(year, month, day);
            System.out.println("Проверьте данные:");
            System.out.println(animalType+ " - " + name + " дата рождения - " + birthDate);
            System.out.println("Если все верно, введите - 1");
            String answer = scanner.nextLine();
            if (answer.equals("1"))
                presenter.addAnimal(animalType, name, birthDate);
            else
                throw new Exception();
        } catch (NumberFormatException e) {
            System.out.println("Ошибка! Дата должна быть числом.");
        } catch (Exception e) {
            System.out.println("Ошибка! Проверьте данные и повторите ввод.");
        }
    }

    public void getAnimalFullInfo() {
        getNurseryList();
        try {
            System.out.println("Укажите ID питомца: ");
            int iD = Integer.parseInt(scanner.nextLine());
            presenter.getAnimalFullInfo(iD);
        } catch (NumberFormatException e) {
            System.out.println("Ошибка! ID должен быть числом.");
        }
    }

    public void getNurseryList() {
        presenter.getNurseryList();
    }
}
