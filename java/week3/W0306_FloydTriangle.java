import java.util.Scanner;

public class W0306_FloydTriangle {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the height of the Floyd Triangle: ");
        int row = scanner.nextInt();
        int num = 1;
        for(int i = 0; i < row; i++){
            for(int j = 0; j <= i; j++){
                System.out.print("\t" + num++);
            }
            System.out.println("");
        }
        scanner.close();
    }
}
