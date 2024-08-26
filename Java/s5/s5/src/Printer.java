import java.util.Arrays;

class HeapSort {
    public static void buildTree(int[] tree, int sortLength) {
        // Введите свое решение ниже
        for (int i = sortLength / 2 - 1; i >= 0; i--) {
            int l = i * 2 + 1;
            int r = i * 2 + 2;
            if (l < sortLength && tree[l] > tree[i]) {
                int temp = tree[i];
                tree[i] = tree[l];
                tree[l] = temp;
            }
            if (r < sortLength && tree[r] > tree[i]) {
                int temp = tree[i];
                tree[i] = tree[r];
                tree[r] = temp;
            }

        }
    }

    public static void heapSort(int[] sortArray, int sortLength) {
// Введите свое решение ниже
        buildTree(sortArray, sortLength);
        for (int i = 0; i < sortLength; i++) {
            int temp = sortArray[sortLength - 1 - i];
            sortArray[sortLength - 1 - i] = sortArray[0];
            sortArray[0] = temp;
            buildTree(sortArray, sortLength - i - 1);
        }
    }
}

// Не удаляйте и не меняйте метод Main!
public class Printer {
    public static void main(String[] args) {
        int[] initArray;

        if (args.length == 0) {
            initArray = new int[]{17, 32, 1, 4, 25, 17, 0, 3, 10, 7, 64, 1};
        } else {
            initArray = Arrays.stream(args[0].split(" ")).mapToInt(Integer::parseInt).toArray();
        }

        System.out.println("Initial array:");
        System.out.println(Arrays.toString(initArray));
        HeapSort.heapSort(initArray, initArray.length);
        System.out.println("Sorted array:");
        System.out.println(Arrays.toString(initArray));
    }
}