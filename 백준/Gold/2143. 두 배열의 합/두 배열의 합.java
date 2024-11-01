import java.io.*;
import java.util.*;


public class Main {

    static int T;
    static ArrayList<Integer> A;
    static ArrayList<Integer> B;


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        T = Integer.parseInt(br.readLine());

        int An = Integer.parseInt(br.readLine());
        A = new ArrayList<>();
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < An; i++) {
            A.add(Integer.parseInt(st.nextToken()));
        }
        int Bn = Integer.parseInt(br.readLine());
        B = new ArrayList<>();
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < Bn; i++) {
            B.add(Integer.parseInt(st.nextToken()));
        }

        HashMap<Integer, Long> Amap = new HashMap<>();

        for (int i = 0; i < An; i++) {
            int key = 0;
            for (int j = i; j < An; j++) {
                key += A.get(j);
                //System.err.println(key + " " + i + " " + j);
                if (Amap.containsKey(key)) {
                    Amap.put(key, Amap.get(key) + 1);
                } else {
                    Amap.put(key, 1L);
                }
            }
        }


        long answer = 0;
        for (int i = 0; i < Bn; i++) {
            int key = 0;
            for (int j = i; j < Bn; j++) {
                key += B.get(j);
                //System.err.println((T - key) + " " + key + " " + i + " " + j);
                if (Amap.containsKey(T - key)) {
                    answer += Amap.get(T - key);
                }
            }
        }
        System.out.println(answer);
    }
}