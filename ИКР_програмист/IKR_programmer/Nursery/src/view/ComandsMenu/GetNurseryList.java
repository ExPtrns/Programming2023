package view.ComandsMenu;

import view.ConsoleUI;

public class GetNurseryList extends Menu {

    public GetNurseryList(ConsoleUI consoleUI) {
        super("Список животных в питомнике", consoleUI);
    }

    public void action() {
        getConsoleUI().getNurseryList();
    }

}