import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int h = sc.nextInt();
        int m = sc.nextInt();
        int time = sc.nextInt();

        int timeH = time/60;
        int timeM = time%60;

        int resultH = h + timeH;
        int resultM = m + timeM;

        if(resultM>=60){
            resultM -= 60;
            resultH += 1;
        }
        if(resultH>23){
            resultH -= 24;
        }
        System.out.println(resultH + " " + resultM);

    }
}
