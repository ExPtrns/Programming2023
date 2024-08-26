package model;

import java.time.LocalDate;
import java.util.List;

public abstract class Pets extends Animals {

    public Pets(int iD, String name, LocalDate birthDate) {
        super(iD, name, birthDate);
    }
    public Pets(int iD, String name, LocalDate birthDate, List<String> skills) {
        super(iD, name, birthDate,skills);
    }
}
