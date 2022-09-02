import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while(scanner.hasNextInt()) {
            int inputNumber = scanner.nextInt();
            int cnt = 1, ret = 1;
            while (true) {
                if (cnt % inputNumber == 0) {
                    System.out.println(ret);
                    break;
                } else {
                    cnt = (cnt * 10) + 1;
                    cnt %= inputNumber;
                    ret++;
                }
            }
        }

    }
}
