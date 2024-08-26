package model;

import java.time.LocalDate;

public class AnimalCreator {
    private Animals newAnimal;
    private int iD;

    public boolean addAnimal(Nursery nursery, AnimalType type, String name, LocalDate birthDate) {
        try (Counter counter = new Counter()) {
                iD = counter.getAnimalID();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
        switch (type) {
            case Cat:
                newAnimal = new Cats(iD, name, birthDate);
                break;
            case Dog:
                newAnimal = new Dogs(iD, name, birthDate);
                break;
            case Hamster:
                newAnimal = new Hamsters(iD, name, birthDate);
                break;
        }
        nursery.addAnimaltoNursery(newAnimal);
        return true;
    }
}
