package view.ComandsMenu;

import view.ConsoleUI;

public class AddAnimalSkill  extends Menu {

    public AddAnimalSkill(ConsoleUI consoleUI) {
        super("Обучить животное новым командам", consoleUI);
    }

    public void action() {
        getConsoleUI().addAnimalSkill();
    }
}
