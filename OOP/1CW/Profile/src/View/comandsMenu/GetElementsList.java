package View.comandsMenu;

import View.ConsoleUI;

public class GetElementsList extends Menu{
    public GetElementsList(ConsoleUI consoleUI) {
        super("Получить список добавленных записей", consoleUI);
    }

    public void action() {
        getConsoleUI().getElementsList();
    }
}
