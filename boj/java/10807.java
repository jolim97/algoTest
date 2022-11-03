import java.util.Scanner;

class Main{
    public static void main(String[] arg){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] arr = new int[N];
        for(int i=0; i<N; i++){
            arr[i] = sc.nextInt();
        }
        int v = sc.nextInt();
        int ans = 0;
        for(int a : arr){
            if(v == a){
                ans += 1;
            }
        }
        System.out.println(ans);
    }
}
