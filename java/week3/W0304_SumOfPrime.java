public class W0304_SumOfPrime{

    public static boolean isPrime(int num){
        for(int i = 2; i * i <= num; i ++)
            if (num % i == 0){
                return false;
            }
        return true;
    }
    public static void main(String[] args) {
        int sum = 0;

        for(int i = 2; i <= 1000; i++){
            if(isPrime(i)){
                sum += i;
            }
        }

        System.out.println("The sum of prime numbers between 0 and 1000 is " + sum + ".");
    }
}
