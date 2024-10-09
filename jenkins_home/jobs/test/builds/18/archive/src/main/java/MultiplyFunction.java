/**
 * This class represents a simple multiplication function.
 * It takes two numbers as input, multiplies them, and displays the result.
 */
public class MultiplyFunction {

    // Define the variables to store the input numbers and the product
    private int num1;
    private int num2;
    private long product; // Use long to accommodate larger products

    // Define the output message
    private static final String OUTPUT_MESSAGE = "The product is: ";

    /**
     * Constructor to initialize the variables
     */
    public MultiplyFunction() {
        this.num1 = 0;
        this.num2 = 0;
        this.product = 0;
    }

    /**
     * Method to get the first number from the user
     */
    public void getFirstNumber() {
        // Use a Scanner to get the input from the user
        try (java.util.Scanner scanner = new java.util.Scanner(System.in)) {
            System.out.print("Enter the first number: ");
            this.num1 = scanner.nextInt();
        }
    }

    /**
     * Method to get the second number from the user
     */
    public void getSecondNumber() {
        // Use a Scanner to get the input from the user
        try (java.util.Scanner scanner = new java.util.Scanner(System.in)) {
            System.out.print("Enter the second number: ");
            this.num2 = scanner.nextInt();
        }
    }

    /**
     * Method to multiply the two numbers
     */
    public void multiplyNumbers() {
        // Multiply the two numbers and store the result in the product variable
        this.product = (long) this.num1 * this.num2;
    }

    /**
     * Method to display the result
     */
    public void displayResult() {
        // Display the output message and the product
        System.out.println(OUTPUT_MESSAGE + this.product);
    }

    /**
     * Main method to test the class
     * @param args Command-line arguments (not used)
     */
    public static void main(String[] args) {
        // Create an instance of the MultiplyFunction class
        MultiplyFunction multiplyFunction = new MultiplyFunction();

        // Get the first number from the user
        multiplyFunction.getFirstNumber();

        // Get the second number from the user
        multiplyFunction.getSecondNumber();

        // Multiply the two numbers
        multiplyFunction.multiplyNumbers();

        // Display the result
        multiplyFunction.displayResult();
    }

    // Public methods for unit testing
    public int getNum1() {
        return this.num1;
    }

    public int getNum2() {
        return this.num2;
    }

    public long getProduct() {
        return this.product;
    }

    public void setNum1(int num1) {
        this.num1 = num1;
    }

    public void setNum2(int num2) {
        this.num2 = num2;
    }

    public void setProduct(long product) {
        this.product = product;
    }
}