import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static int factorial(int a) {
        if(a == 0)
            return 1;
        return a * factorial(a-1);
    }

    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt(), k = scanner.nextInt();
        
        System.out.println(factorial(n) / (factorial(k) * factorial(n-k)));
    }
}

