package Presenter;

import Model.Service;
import View.View;

public class Presenter {
    private View view;
    private Service service;

    public Presenter(View view) {
        this.view = view;
        service = new Service(this);
    }

    public void addElement(String s) {
        service.CheckString(s);
    }

    public void getElementsList(String path) {

        view.printAnswer(service.GetFiles(path));
    }

    public void returnAnswer(String message) {
        view.printAnswer(message);
    }

    public void read(String path, String file) {
        service.readFile(path, file);
    }
}
