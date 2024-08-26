package model;

import java.util.ArrayList;
import java.util.List;

public class Nursery {
    private List<Animals> animalsList;

    public Nursery() {
        animalsList = new ArrayList<>();
    }

    public void addAnimaltoNursery(Animals animal) {
        animalsList.add(animal);
    }

    public void getAnimalsList() {
        StringBuilder sb = new StringBuilder();
        for (Animals animal : animalsList) {
            sb.append(animal.getID());
            sb.append(". ");
            sb.append(animal.getName());
            sb.append(" - ");
            sb.append(animal.getClass().getSimpleName());
            sb.append(".\n");
        }
        if (sb.length() > 0) {
            System.out.println(sb);
        } else
            System.out.println("Питомник пуст.");
    }

    private Animals getAnimalByID(int iD) {
        Animals nededAnimal = null;
        for (Animals animal : animalsList) {
            if (animal.getID() == iD) {
                nededAnimal = animal;
            }
        }
        return nededAnimal;
    }

    public void getAnimalFullInfo(int iD) {
        Animals animal = getAnimalByID(iD);
        if (animal == null) {
            System.out.println("Animal with ID " + iD + " not found.");
        } else {
            System.out.println(animal);
        }
    }

    public boolean addSkilltoAnimal(int iD, String skill) {
        Animals animal = getAnimalByID(iD);
        if (animal == null) {
            System.out.println("Animal with ID " + iD + " not found.");
            return false;
        } else {
            return animal.addSkill(skill);
        }

    }
}
