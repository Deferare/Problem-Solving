import java.io.*;
import java.util.Scanner;
public class Main {
	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));        
		int a,x;
        a = sc.nextInt();
        x = sc.nextInt();
		int[] arr = new int[a];			
		for (int i = 0; i < a; i++) {
			arr[i] = sc.nextInt();	
			if (arr[i] < x)
				bw.write(arr[i]+" ");
		}					
		bw.flush();
	}
}
