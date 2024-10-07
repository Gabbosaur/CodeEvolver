/**
 * This class represents the AddFunction program, which takes two numbers as input and returns their sum.
 */
public class Adding {

    private int num1;
    private int num2;
    private int sum;

    /**
     * Constructor to initialize the numbers and sum.
     */
    public Adding() {
        this.num1 = 0;
        this.num2 = 0;
        this.sum = 0;
    }

    /**
     * Method to get the first number from the user.
     * @return the first number
     */
    public int getFirstNumber() {
        return InputUtil.getInput("Enter the first number: ");
    }

    /**
     * Method to get the second number from the user.
     * @return the second number
     */
    public int getSecondNumber() {
        return InputUtil.getInput("Enter the second number: ");
    }

    /**
     * Method to add two numbers.
     * @param num1 the first number
     * @param num2 the second number
     * @return the sum of the two numbers
     */
    public int addNumbers(int num1, int num2) {
        return num1 + num2;
    }

    /**
     * Method to display the sum of two numbers.
     * @param sum the sum of the two numbers
     */
    public void displaySum(int sum) {
        System.out.println("The sum is: " + sum);
    }

    /**
     * Main method to execute the program.
     * @param args command-line arguments (not used)
     */
    public static void main(String[] args) {
        Adding adding = new Adding();
        int num1 = adding.getFirstNumber();
        int num2 = adding.getSecondNumber();
        int sum = adding.addNumbers(num1, num2);
        adding.displaySum(sum);
    }

    // Public methods for unit testing
    public int getNum1() {
        return num1;
    }

    public void setNum1(int num1) {
        this.num1 = num1;
    }

    public int getNum2() {
        return num2;
    }

    public void setNum2(int num2) {
        this.num2 = num2;
    }

    public int getSum() {
        return sum;
    }

    public void setSum(int sum) {
        this.sum = sum;
    }
}

class InputUtil {
    private static final java.util.Scanner scanner = new java.util.Scanner(System.in);

    public static int getInput(String prompt) {
        System.out.print(prompt);
        return scanner.nextInt();
    }
}