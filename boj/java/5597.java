import java.util.Arrays;
import java.util.Scanner;

class Main{
    public static void main(String[] arg){
        Scanner sc = new Scanner(System.in);
        Integer[] students = new Integer[31];
        Arrays.fill(students,0);
        students[0] = 1;
        for(Integer i=0; i<28; i++){
            int std = sc.nextInt();
            students[std] = 1;
        }
        for(Integer i=1; i<31; i++){
            if(students[i] == 0){
                System.out.println(i);
            }
        }
    }
}
