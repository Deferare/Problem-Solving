import java.util.*;
public class Main {
   public static void main(String[] args){
      Scanner sc = new Scanner(System.in);   
      String s = sc.nextLine();
      String alpa = "abcdefghijklmnopqrstuvwxyz";
      int[] arr = new int[26];
      for (int i = 0; i < arr.length; i++) {
    	  arr[i] = -1;
      }
      for (int i = 0; i < s.length(); i++) {
         for (int j = 0; j < alpa.length(); j++) {            
            if (s.charAt(i) == alpa.charAt(j)) {  
            	if (arr[j] == -1)
            		arr[j] = i;
            }            
         }          
      } 
      for (int i = 0; i < arr.length; i++) {
    	  System.out.print(arr[i]+" ");
      }
   }   
}
