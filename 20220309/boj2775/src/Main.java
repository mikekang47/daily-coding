import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        while(t-- > 0)
            System.out.println(find(scanner.nextInt(), scanner.nextInt()));

    }

    private static int find(int k, int n) {
        if(k == 0)
            return n;
        if(n == 0)
            return 0;
        return find(k,n-1) + find(k-1,n);
    }
}
