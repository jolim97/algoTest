import java.util.Scanner;
import java.util.Arrays;

class Main{
    public static void main(String[] arg){
        Scanner sc = new Scanner(System.in);
        int[] scores = new int[5];
        for(int i=0; i<5; i++){
            scores[i] = sc.nextInt();
        }
        Arrays.sort(scores);
        System.out.println(Arrays.stream(scores).sum()/5);
        System.out.println(scores[2]);
    }
}
