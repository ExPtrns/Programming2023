package View.comandsMenu;

import View.ConsoleUI;

public class AddProfile extends Menu{

    public AddProfile(ConsoleUI consoleUI) {
        super("Добавить профиль", consoleUI);
    }
    @Override
    public void action() {
        getConsoleUI().addElement();
    }
}
