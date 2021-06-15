import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int testCase = sc.nextInt(); //가게 수
        int[] storage = new int[testCase];
        for (int i = 0; i < testCase; i++) {
        	int candyNum = sc.nextInt();
        	int boxNum = sc.nextInt();
        	int[] boxSize = new int[boxNum];
        	for (int j = 0; j < boxNum; j++) {        		
        		boxSize[j] = sc.nextInt() * sc.nextInt();
        	}
        	Arrays.sort(boxSize); //박스 오름차순 
        	int check = 0; 
        	int j = 0; int k = boxSize.length-1;
        	while(true) {        		
        		candyNum -= boxSize[k];
        		check++;
        		if (candyNum <= 0) break;	
        		k--;
        	}
        	storage[i] = check;
        }
        for (int r = 0; r < storage.length; r++) {
    		System.out.println(storage[r]);
    	}
	}
}
