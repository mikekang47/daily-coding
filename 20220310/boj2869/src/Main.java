import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String val = br.readLine();
        Double A = (double) Integer.parseInt(val.split(" ")[0]), B = (double) Integer.parseInt(val.split(" ")[1]), V = (double) Integer.parseInt(val.split(" ")[2]);
        System.out.println((int) Math.ceil((V - B) / (A - B)));
    }
}
