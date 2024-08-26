package view.ComandsMenu;

import view.ConsoleUI;

public class AddAnimal extends Menu {

    public AddAnimal(ConsoleUI consoleUI) {
        super("Завести новое животное", consoleUI);
    }

    public void action() {
        getConsoleUI().addAnimal();
    }
}