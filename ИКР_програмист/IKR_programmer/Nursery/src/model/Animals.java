package model;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

public abstract class Animals {
    private int iD;
    private String name;
    private LocalDate birthDate;
    private List<String> skills;

    public Animals(int iD, String name, LocalDate birthDate) {
        this.iD = iD;
        this.name = name;
        this.birthDate = birthDate;
        skills = new ArrayList<>();
    }

    public Animals(int iD, String name, LocalDate birthDate, List<String> skills) {
        this.iD = iD;
        this.name = name;
        this.birthDate = birthDate;
        this.skills = skills;
    }

    public int getID() {
        return iD;
    }

    public String getName() {
        return name;
    }

    public LocalDate getBirthDate() {
        return birthDate;
    }

    public List<String> getSkills() {
        return skills;
    }

    public boolean addSkill(String skill) {
        this.skills.add(skill);
        return true;
    }
}
