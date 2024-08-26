package model;

import java.time.LocalDate;
import java.util.List;

public class Hamsters extends Pets {
    public Hamsters(int iD, String name, LocalDate birthDate) {
        super(iD, name, birthDate);
    }

    public Hamsters(int iD, String name, LocalDate birthDate, List<String> skills) {
        super(iD, name, birthDate, skills);
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("ID - " + getID() + ". ");
        sb.append("Name - " + getName() + "\n");
        sb.append("Class - Pet\n");
        sb.append("Type - Hamster\n");
        sb.append("Birth Date - " + getBirthDate() + "\n");
        if (getSkills().isEmpty()) {
            sb.append("Have no skills\n");
        } else
            sb.append("Skills and commands:\n");
        for (int i = 0; i < getSkills().size(); i++) {
            sb.append(getSkills().get(i));
            if(i!=getSkills().size()-1){
                sb.append(", ");
            }

        }
        return sb.toString();
    }
}

