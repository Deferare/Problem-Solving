import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
    	int num = 0;
    	int i = 1;
    	int place = 0;
    	while (i <= 9) {
    		int newNum = sc.nextInt();
    		if (newNum > num) {
    			num = newNum;
    			place = i;
    		}
                		i++;
        }
    	System.out.println(num);
    	System.out.print(place);
	}
}
