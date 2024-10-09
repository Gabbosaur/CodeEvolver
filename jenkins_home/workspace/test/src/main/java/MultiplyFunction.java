/**
 * This class represents a simple multiplication function.
 * It takes two numbers as input, multiplies them, and displays the result.
 */
public class MultiplyFunction {

    // Define the maximum length for the input numbers
    private static final int MAX_INPUT_LENGTH = 5;

    // Define the maximum length for the product
    private static final int MAX_PRODUCT_LENGTH = 10;

    // Define the output message
    private static final String OUTPUT_MESSAGE = "The product is: ";

    // Define the input numbers
    private int num1;
    private int num2;

    // Define the product
    private long product;

    /**
     * Constructor to initialize the input numbers and product.
     */
    public MultiplyFunction() {
        this.num1 = 0;
        this.num2 = 0;
        this.product = 0;
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
     * Method to multiply the two numbers.
     * @param num1 the first number
     * @param num2 the second number
     * @return the product
     */
    public long multiplyNumbers(int num1, int num2) {
        return (long) num1 * num2;
    }

    /**
     * Method to display the result.
     * @param product the product
     */
    public void displayResult(long product) {
        System.out.println(OUTPUT_MESSAGE + product);
    }

    /**
     * Main method to execute the program.
     * @param args command-line arguments (not used)
     */
    public static void main(String[] args) {
        MultiplyFunction multiplyFunction = new MultiplyFunction();
        int num1 = multiplyFunction.getFirstNumber();
        int num2 = multiplyFunction.getSecondNumber();
        long product = multiplyFunction.multiplyNumbers(num1, num2);
        multiplyFunction.displayResult(product);
    }

    // Public methods for unit testing
    public void setNum1(int num1) {
        this.num1 = num1;
    }

    public void setNum2(int num2) {
        this.num2 = num2;
    }

    public long getProduct() {
        return product;
    }
}

class InputUtil {
    public static int getInput(String prompt) {
        java.util.Scanner scanner = new java.util.Scanner(System.in);
        System.out.print(prompt);
        return scanner.nextInt();
    }
}