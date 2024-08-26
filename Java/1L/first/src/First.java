import java.time.LocalTime;
import java.util.Arrays;
import java.util.Scanner;

public class First {
    public static void main(String[] args) {
        task2();
    }

    static void task0() {
        System.out.println("Как тебя зовут?");
        Scanner scanner = new Scanner(System.in);
        String name = scanner.nextLine();

        LocalTime time = LocalTime.now();
        Integer hour = time.getHour();

        if (hour >= 5 && hour < 12)
            System.out.println("Доброе утро" + name);
        else if (hour < 18) System.out.println("Добрый день " + name);
        else if (hour < 23) System.out.println("Добрый вечер " + name);
        else System.out.println("Доброй ночи " + name);
    }
    static void task1(){

        int[] array = {1, 1, 0, 1, 0, 0, 1, 1, 1};
        int count = 0;
        int maxOnes = 0;
        for (int i = 0; i < array.length; i++) {
            if(array[i] == 1) count++;
            if (array[i] == 0 || i == array.length - 1){
                if(count > maxOnes) maxOnes = count;
                count = 0;
            }
        }
        System.out.println(maxOnes);
    }
    static void task2(){
        int[] nums = {2,2,3,3,1,4,2,6,8,4,4};
        int val = 3;
        int[] temp = new int[nums.length];
        Arrays.fill(temp, val);
        for (int i = 0, j = 0 ; i < nums.length; i++ ) {
            if(nums[i] != val){
                temp[j++] = nums[i];
            }
        }
        System.out.println(Arrays.toString(temp));

    }
    static void task4(int a, int b){
//        <aside>
//📔 **Текст задачи:**
//
//        Реализовать функцию возведения числа а в степень b. a, b из Z. Сводя количество выполняемых действий к минимуму.
//
//        Пример 1: а = 3, b = 2, ответ: 9
//
//        Пример 2: а = 2, b = -2, ответ: 0.25
//
//        Пример 3: а = 3, b = 0, ответ: 1
//
//                </aside>
        double result = 1;
        for (int i = 0; i < Math.abs(b); i++) {
            result = result * a;
        }

        result = (b > 0 ? result : 1/result );
        System.out.println(result);
    }
}
