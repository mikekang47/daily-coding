import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int result = 0;
        for(int i = 1; i < n; i++) {
            int k = i;
            int sum = 0;
            while(k > 0) {
                sum += k % 10;
                k /= 10;
            }
            if(sum + i == n) {
                result = i;
                break;
            }
        }
        System.out.println(result);
    }

}
