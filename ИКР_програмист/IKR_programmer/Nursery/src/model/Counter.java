package model;

import java.time.LocalDate;

public class Counter implements AutoCloseable {
    private static int animalID = 0;


    public int getAnimalID(){
        return ++animalID;
    }

    @Override
    public void close() {

    }
}
