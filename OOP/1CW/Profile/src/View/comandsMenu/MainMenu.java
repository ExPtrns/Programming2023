package View.comandsMenu;

import View.ConsoleUI;


import java.util.ArrayList;
import java.util.List;

public class MainMenu {
    private List<Menu> commandsMenu;

    public MainMenu(ConsoleUI consoleUI) {
        commandsMenu = new ArrayList<>();
        commandsMenu.add(new AddProfile(consoleUI));
        commandsMenu.add(new GetElementsList(consoleUI));
        commandsMenu.add(new Exit(consoleUI));
    }

    public String menuElements() {
        StringBuilder stringBuilder = new StringBuilder();
        for (int i = 0; i < commandsMenu.size(); i++) {
            stringBuilder.append(i + 1);
            stringBuilder.append(". ");
            stringBuilder.append(commandsMenu.get(i).getDescription());
            stringBuilder.append("\n");
        }
        return stringBuilder.toString();
    }

    public void action(int choice) {
        Menu menu = commandsMenu.get(choice - 1);
        menu.action();
    }
}
