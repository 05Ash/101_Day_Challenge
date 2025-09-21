import java.util.Scanner;

public class W0305_FiboSum{
    public static void main(String[] argv){
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the number of fibonacci numbers to generate: ");
        int n = scanner.nextInt();
        int f0 = 0, f1 = 1, sum = 1, fn;
        System.out.println("Fibonacci Series: ");
        System.out.print("\t" + f0);
        System.out.print("\t" + f1);

        for(int i = 2; i < n; i++){
            fn = f0 + f1;
            sum += fn;
            System.out.print("\t" + fn);
            f0 = f1;
            f1 = fn;
        }

        System.out.println("\nThe sum of n fibonacci numbers is: " + sum);

        scanner.close();
    }
}
