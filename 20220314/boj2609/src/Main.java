import java.math.BigInteger;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        BigInteger a = scanner.nextBigInteger(), b = scanner.nextBigInteger();
        System.out.println(a.gcd(b).intValue());
        System.out.println((a.intValue() * b.intValue()) / a.gcd(b).intValue());
    }
}
