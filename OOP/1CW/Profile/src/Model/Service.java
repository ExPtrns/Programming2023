package Model;

import Presenter.Presenter;

import java.util.ArrayList;

public class Service {
    private Parser parser;
    private Profile profile;
    private SaverLoader saverLoader;
    private Presenter presenter;
    ArrayList<Object> list;


    public Service(Presenter presenter) {
        parser = new Parser();
        profile = new Profile();
        saverLoader = new SaverLoader();
        this.presenter = presenter;
    }

    public void CheckString(String s) {
        String answer = parser.CheckStringLength(s);
        if (answer.contains("true")) {
            CheckFormat(s);
        } else {
            presenter.returnAnswer(answer);
        }

    }

    private void CheckFormat(String s) {
        String answer = parser.Formatter(s);
        if (answer.contains("true")) {
            list = parser.GetList();
            if (list.size() == 6) {
                presenter.returnAnswer(profile.addProfile(list));
            }
        } else {
            presenter.returnAnswer(answer + " Данные не записаны!\n");
        }
    }

    public String GetFiles(String path) {
        return profile.getFiles(path);

    }

    public void readFile(String path, String file) {
        presenter.returnAnswer(profile.readFile(path, file));
    }
}
