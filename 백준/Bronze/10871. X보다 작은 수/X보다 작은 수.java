import java.io.IOException;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        StringBuilder input = new StringBuilder();
        StringBuilder output = new StringBuilder();
        int ch;

        while ((ch = System.in.read()) != -1) {
            input.append((char) ch);
        }

        StringTokenizer st = new StringTokenizer(input.toString());
        Integer n = Integer.parseInt(st.nextToken());
        Integer x = Integer.parseInt(st.nextToken());
        ArrayList<Integer> b = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            Integer e = Integer.parseInt(st.nextToken());
            if (e < x) {
                b.add(e);
            }
        }
        for (Integer integer : b) {
            output.append(Integer.toString(integer));
            output.append(" ");
        }
        System.out.println(output);
    }
}