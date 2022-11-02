import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] chess = new String[6];
        chess[0] = String.valueOf(1 - sc.nextInt());
        chess[1] = String.valueOf(1 - sc.nextInt());
        chess[2] = String.valueOf(2 - sc.nextInt());
        chess[3] = String.valueOf(2 - sc.nextInt());
        chess[4] = String.valueOf(2 - sc.nextInt());
        chess[5] = String.valueOf(8 - sc.nextInt());
        System.out.println(String.join(" ",chess));
    }
}
