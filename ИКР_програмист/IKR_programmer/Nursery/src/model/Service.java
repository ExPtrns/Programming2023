package model;

import java.time.LocalDate;

public class Service {
    private AnimalCreator animalCreator;
    private Nursery nursery;

    public Service() {
        animalCreator = new AnimalCreator();
        nursery = new Nursery();
    }

    public String addAnimal(AnimalType type, String name, LocalDate birthDate) {
        if (animalCreator.addAnimal(nursery, type, name, birthDate))
            return "Animal " + name + " add successful.";
        return name + " WASN'T add to Nursery. Check information and try again.";
    }

    public void getAnimalFullInfo(int iD) {
        nursery.getAnimalFullInfo(iD);
    }

    public void getNurseryList() {
        nursery.getAnimalsList();
    }

    public String addAnimalSkill(int iD, String skill) {
        if (nursery.addSkilltoAnimal(iD, skill)) {
            return skill + " add successful!";
        }
        return "Skill not add";
    }
}
