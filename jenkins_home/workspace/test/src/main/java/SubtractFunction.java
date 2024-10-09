/**
 * This class represents a simple subtraction function.
 * It takes two numbers as input, subtracts the second number from the first,
 * and displays the result.
 */
public class SubtractFunction {

    private int num1;
    private int num2;
    private int difference;

    /**
     * Constructor to initialize the SubtractFunction object.
     */
    public SubtractFunction() {
        this.num1 = 0;
        this.num2 = 0;
        this.difference = 0;
    }

    /**
     * Method to get the first number from the user.
     * @return the first number
     */
    public int getFirstNumber() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the first number: ");
        return scanner.nextInt();
    }

    /**
     * Method to get the second number from the user.
     * @return the second number
     */
    public int getSecondNumber() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the second number: ");
        return scanner.nextInt();
    }

    /**
     * Method to subtract the second number from the first.
     * @param num1 the first number
     * @param num2 the second number
     * @return the difference
     */
    public int subtractNumbers(int num1, int num2) {
        return num1 - num2;
    }

    /**
     * Method to display the result.
     * @param difference the difference between the two numbers
     */
    public void displayResult(int difference) {
        System.out.println("The difference is: " + difference);
    }

    /**
     * Main method to execute the subtraction function.
     * @param args command-line arguments (not used)
     */
    public static void main(String[] args) {
        SubtractFunction subtractFunction = new SubtractFunction();
        int num1 = subtractFunction.getFirstNumber();
        int num2 = subtractFunction.getSecondNumber();
        int difference = subtractFunction.subtractNumbers(num1, num2);
        subtractFunction.displayResult(difference);
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

    public int getDifference() {
        return difference;
    }

    public void setDifference(int difference) {
        this.difference = difference;
    }
}