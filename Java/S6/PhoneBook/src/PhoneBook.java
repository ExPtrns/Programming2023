import java.util.*;


class PhoneBook {
    private static HashMap<String, ArrayList<Integer>> phoneBook = new HashMap<>();

    public void add(String name, Integer phoneNum) {
        if (phoneBook.containsKey(name)) {
            ArrayList<Integer> list = phoneBook.get(name);
            list.add(phoneNum);
        } else {
            ArrayList<Integer> arr = new ArrayList<>();
            arr.add(0, phoneNum);
            phoneBook.putIfAbsent(name, arr);
        }
    }

    public ArrayList<Integer> find(String name) {
        if (phoneBook.containsKey(name)) {
            ArrayList<Integer> list = phoneBook.get(name);
            return list;
        } else {

            return new ArrayList<>();
        }
    }

    public static HashMap<String, ArrayList<Integer>> getPhoneBook() {

        return phoneBook;
    }

    public void printPhoneBook() {
        ArrayList<Integer> list = new ArrayList<>();
        LinkedHashMap<String, String> sortedMap = new LinkedHashMap<>();
        for (Map.Entry<String, ArrayList<Integer>> entry : phoneBook.entrySet()) {
            list.add(entry.getValue().size());
        }
        Collections.sort(list, Comparator.reverseOrder());
        for (Integer num : list) {
            for (Map.Entry<String, ArrayList<Integer>> entry : phoneBook.entrySet()) {
                if (entry.getValue().size() == num) {
                    sortedMap.put(entry.getKey(), entry.getValue().toString());
                }
            }
        }
        System.out.println(sortedMap);
    }

}

