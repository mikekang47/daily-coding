import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int start = 666;
        int n = scanner.nextInt();
        while(true) {
            if(Integer.toString(start).contains("666")) {
                n -= 1;
            }
            if(n == 0) {
                break;
            }
            start += 1;
        }
        System.out.println(start);
    }
}
