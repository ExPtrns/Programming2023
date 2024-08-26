package presenter;

import model.AnimalType;
import model.Service;
import view.View;

import java.time.LocalDate;

public class Presenter {
    private View view;
    private Service service;

    public Presenter(View view) {
        this.view = view;
        service = new Service();
    }

    public void getNurseryList() {
        service.getNurseryList();
    }

    public void addAnimal(AnimalType type, String name, LocalDate birthDate) {
        view.printAnswer(service.addAnimal(type, name, birthDate));
    }

    public void getAnimalFullInfo(int iD) {
        service.getAnimalFullInfo(iD);
    }

    public void addAnimalSkill(int iD, String skill) {
        view.printAnswer(service.addAnimalSkill(iD, skill));

    }
}