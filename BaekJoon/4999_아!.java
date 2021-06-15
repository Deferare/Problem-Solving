import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String patient = sc.nextLine();
        String doctor = sc.nextLine();
        int check = 0;
        if (patient.length() >= doctor.length()) {
            if (patient.equals(doctor)) System.out.println("go");
            else {
                for (int i = 0; i < patient.length()-doctor.length()+1; i++) {
                    String save = "";
                    for (int j = i; j < i+doctor.length(); j++) {
                        save += patient.charAt(j);
                    }
                    if (save.equals(doctor)) {
                        System.out.println("go");
                        check = 1;
                        break;
                    }
                }
            }
        }
        else {
            System.out.println("no");
        }
    }
}
