import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a,b,c;
		int a1,a2,a3;
		int b1,b2,b3;
		a = sc.nextInt();	
		b = sc.nextInt();	
		a3 = a/100; //100의자리
		a2 = -1*((a3*10)-(a/10)); //10의자리
		a1 = a-((a/10)*10); //1의자리		
			
		b3 = b/100; //100의자리
		b2 = -1*((b3*10)-(b/10)); //10의자리
		b1 = b-((b/10)*10); //1의자리
		
		int n1 = a*b1;
		int n2 = a*b2;
		int n3 = a*b3;
		System.out.println(a*b1);	
		System.out.println(a*b2);
		System.out.println(a*b3);
		System.out.println(n1+n2*10+n3*100);
	}
}
