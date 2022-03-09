import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while(true) {
            String num = scanner.next();
            if(num.equals("0"))
                break;
            StringBuffer sb = new StringBuffer(num);
            if(sb.reverse().toString().equals(num))
                System.out.println("yes");
            else
                System.out.println("no");
        }

    }
}
