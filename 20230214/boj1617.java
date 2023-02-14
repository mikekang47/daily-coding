
import java.util.*;
import java.io.*;

public class boj1617 {
    public static int[] A, temp;
    public static long result = 0;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        A = new int[N+1];
        temp = new int[N+1];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 1; i <= N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }
        mergeSort(1, N);
        System.out.println(result);
    }

    private static void mergeSort(int start, int end) {
        if(start == end) return;
        int mid = start + (end - start) / 2;
        mergeSort(start, mid);
        mergeSort(mid+1, end);
        for(int i = start; i <= end; i++) {
            temp[i] = A[i];
        }
        int k = start;
        int index1 = start;
        int index2 = mid + 1;
        while(index1 <= mid && index2 <= end) {
            if(temp[index1] > temp[index2]) {
                A[k] = temp[index2];
                result += index2 - k;
                k += 1;
                index2++;
            } else {
                A[k] = temp[index1];
                k++;
                index1++;
            }
        }
        while(index1 <= mid) {
            A[k] = temp[index1];
            k++;
            index1++;
        }
        while(index2 <= end) {
            A[k] = temp[index2];
            k++;
            index2++;
        }
    }

}
