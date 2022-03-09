import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt(), m = scanner.nextInt();
        int sum = 0;
        int[] arr = new int[10000001];
        int result = 0;
        for(int i = 0;i < n; i++) {
            arr[i] = scanner.nextInt();
        }

        for(int i = 0; i < n-2; i++) {
            for(int j = i+1; j < n-1; j++) {
                for(int k = j+1; k < n; k++) {
                    sum = arr[i] + arr[j] + arr[k];
                    if(sum <= m)
                        result = Math.max(result, sum);
                }
            }
        }
        System.out.println(result);
    }
}
