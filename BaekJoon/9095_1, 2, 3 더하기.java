import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt(); //테스트 케이스 입력
        for(int i = 0; i<t; i++) { //테스트 케이스 만큼 반복
        	int n = sc.nextInt(); //첫번쨰 숫자 입력
        	int[] arr = new int[n+1]; //입력된 숫자보다 +1 큰 배열을 생성
        	if(n==1) //n이 1이면 1 출력되고 끝남.
        		System.out.println(1);
        	else if(n==2) //n이 2이면 2 출력되고 끝남.
        		System.out.println(2);
        	else if(n==3) //n이 3이면 4 출력되고 끝남.
        		System.out.println(4);
        	
        	else {//만약 n이 1,2,3이 아니라면,
        		arr[1] = 1; //1,2,3 일때의 값을 해당 배열에 담아주고.
        		arr[2] = 2;
        		arr[3] = 4;
        		for(int j = 4; j<=n; j++) { //그 다음 배열에 값을 대입하는데, 입력받았던 n만큼 반복한다. <=인것이 함정.
                	arr[j] = arr[j-3] + arr[j-2] + arr[j-1]; //이전의 3번째까지의 값들을 더함.
            	}
            	System.out.println(arr[n]);	
        	}
        }
	}
}
