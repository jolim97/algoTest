import java.util.Scanner;

class Main{
    static Integer TIMES = 0;
    public static int recursion(String s, int l, int r){
        TIMES += 1;
        if(l >= r) return 1;
        else if(s.charAt(l) != s.charAt(r)) return 0;
        else return recursion(s, l+1, r-1);
    }
    public static int isPalindrome(String s){
        return recursion(s, 0, s.length()-1);
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        Integer T = sc.nextInt();
        sc.nextLine();
        for(int i=0;i<T;i++){
            String str = sc.nextLine();
            TIMES = 0;
            System.out.println(isPalindrome(str)+" "+TIMES);
        }
    }
}

