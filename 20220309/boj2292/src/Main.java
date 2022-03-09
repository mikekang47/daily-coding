import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        int start = 1;
        int path = 0;
        while(true) {
            if(start >= a) {
                System.out.println(path+1);
                break;
            }
            path++;
            start += path*6;
        }

    }
}
