package view.ComandsMenu;

import view.ConsoleUI;

public class GetAnimalFullInfo extends Menu {

    public GetAnimalFullInfo(ConsoleUI consoleUI) {
        super("Полная информация о животном", consoleUI);
    }

    public void action() {
        getConsoleUI().getAnimalFullInfo();
    }

}