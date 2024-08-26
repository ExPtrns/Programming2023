package view;

import view.ComandsMenu.*;

import java.util.ArrayList;
import java.util.List;

public class MainMenu {
    private List<Menu> commandsMenu;

    public MainMenu(ConsoleUI consoleUI) {
        commandsMenu = new ArrayList<>();
        commandsMenu.add(new AddAnimal(consoleUI));
        commandsMenu.add(new GetNurseryList(consoleUI));
        commandsMenu.add(new GetAnimalFullInfo(consoleUI));
        commandsMenu.add(new AddAnimalSkill(consoleUI));
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

    public int size(){
        return commandsMenu.size();
    }
}