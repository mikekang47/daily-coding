import java.util.Scanner;

public class main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        for(int i = 0; i < t; i++) {
            int h = scanner.nextInt(), w = scanner.nextInt(), n = scanner.nextInt();
            int floor, line;
            if(n%h == 0) {
                floor = h;
                line = n / h;
            } else {
                floor = n % h;
                line = n/h + 1;
            }
            System.out.println(floor*100+line);
        }

    }
}
