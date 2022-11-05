import java.util.Scanner;
import java.util.Arrays;
import java.util.Collections;

class Main{
	public static void main(String[] arg){
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int k = sc.nextInt();
		int[] xs = new int[N];
		for(int i=0; i<N; i++) {
			xs[i] = sc.nextInt();
		}
		Arrays.sort(xs,Collections.reverseOrder());
		System.out.println(xs[k-1]);
	}
}

