import java.util.*;
public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt(); sc.nextLine();
        for (int i = 0; i < t; i++) {
            int cnt = 0;
            String str = sc.nextLine();
            while (true) {
                int[] arrSave = new int[4];
                for (int j = 0; j < str.length(); j++) {
                    arrSave[j] = Character.getNumericValue(str.charAt(j));
                }
                Arrays.sort(arrSave);
                String maxSave = ""; String minSave = "";
                int j2 = arrSave.length-1;
                for (int j = 0; j < arrSave.length; j++,j2--) {
                    minSave += arrSave[j];
                    maxSave += arrSave[j2];
                }
                int result = Integer.parseInt(maxSave) - Integer.parseInt(minSave);
                if (str.equals(result+""))
                    break;
                cnt++;
                str = result+"";
            }
            System.out.println(cnt);            
        }
    }
}
