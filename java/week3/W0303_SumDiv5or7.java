public class W0303_SumDiv5or7{
    public static void main(String[] argv){
        int sum = 0;
        for (int i = 1000; i <= 2000; i++){
            if ((i % 5) == 0 || (i % 7) == 0)
                sum += i;
        }
        System.out.println("The sum of numbers divisible by either 5 or 7 is " + sum + ".");
    }
}
