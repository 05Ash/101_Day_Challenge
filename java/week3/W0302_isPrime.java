import java.util.Scanner;

public class W0302_isPrime{

    public static boolean isPrime(int num){
        for(int i = 2; i * i <= num; i ++){
            if (num % i == 0){
                System.out.print("\t" + i + "\n");
                return false;
            }
        }
        return true;
    }

    public static void main(String[] argv){
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the number: ");
        int num = scanner.nextInt();
        boolean check = isPrime(num);
        if (check)
            System.out.println("The entered number is prime.");
        else
            System.out.println("The entered number is not prime.");
        scanner.close();
    }
}
