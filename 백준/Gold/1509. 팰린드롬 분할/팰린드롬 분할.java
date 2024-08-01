import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String a = scanner.nextLine();
        ArrayList<Character> aArray = new ArrayList<>();
        for (char c : a.toCharArray()) {
            aArray.add(c);
        }

        ArrayList<ArrayList<Boolean>> isPalindromic = new ArrayList<>();
        for (int i = 0; i < a.length(); i++) {
            ArrayList<Boolean> innerList = new ArrayList<>();
            for (int j = 0; j < a.length(); j++) {
                innerList.add(false);
            }
            isPalindromic.add(innerList);
        }

        for (int x = 0; x < a.length(); x++) {
            for (int y = 0; y < a.length() - x; y++) {
                int j = y + x;
                if (y + 1 > j - 1) {
                    isPalindromic.get(y).set(j, aArray.get(y).equals(aArray.get(j)));
                    continue;
                }
                isPalindromic.get(y).set(j, aArray.get(y).equals(aArray.get(j)) && isPalindromic.get(y + 1).get(j - 1));
            }
        }

        ArrayList<Integer> minimalPartitionCount = new ArrayList<>();
        for (int i = 0; i < a.length(); i++) {
            minimalPartitionCount.add(0);
        }
        minimalPartitionCount.set(0, 1);

        for (int i = 1; i < a.length(); i++) {
            ArrayList<Integer> subCounts = new ArrayList<>();
            subCounts.add(minimalPartitionCount.get(i - 1) + 1);
            for (int j = 0; j < i; j++) {
                if (isPalindromic.get(j).get(i)) {
                    if (j >= 1) {
                        subCounts.add(minimalPartitionCount.get(j - 1) + 1);
                    } else {
                        subCounts.add(1);
                    }
                }
            }
            minimalPartitionCount.set(i, subCounts.stream().min(Integer::compare).orElse(Integer.MAX_VALUE));
        }
        
        System.out.println(minimalPartitionCount.get(minimalPartitionCount.size() - 1));
        scanner.close();
    }
}
