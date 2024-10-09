/**
 * This class represents the AddFunction program, which takes two numbers as input and displays their sum.
 */
public class AddFunction {

    // Define the variables to store the input numbers and their sum
    private int num1;
    private int num2;
    private int sum;

    // Define the output message
    private static final String OUTPUT_MESSAGE = "The sum is: ";

    /**
     * Constructor to initialize the variables
     */
    public AddFunction() {
        this.num1 = 0;
        this.num2 = 0;
        this.sum = 0;
    }

    /**
     * Method to get the first number from the user
     */
    public void getFirstNumber() {
        System.out.print("Enter the first number: ");
        // Use a Scanner to get the user input
        try (java.util.Scanner scanner = new java.util.Scanner(System.in)) {
            this.num1 = scanner.nextInt();
        }
    }

    /**
     * Method to get the second number from the user
     */
    public void getSecondNumber() {
        System.out.print("Enter the second number: ");
        // Use a Scanner to get the user input
        try (java.util.Scanner scanner = new java.util.Scanner(System.in)) {
            this.num2 = scanner.nextInt();
        }
    }

    /**
     * Method to calculate the sum of the two numbers
     */
    public void addNumbers() {
        this.sum = this.num1 + this.num2;
    }

    /**
     * Method to display the sum
     */
    public void displaySum() {
        System.out.println(OUTPUT_MESSAGE + this.sum);
    }

    /**
     * Main method to execute the program
     * @param args Command-line arguments (not used)
     */
    public static void main(String[] args) {
        AddFunction addFunction = new AddFunction();
        addFunction.getFirstNumber();
        addFunction.getSecondNumber();
        addFunction.addNumbers();
        addFunction.displaySum();
    }

    // Public methods for unit testing
    public int getSum() {
        return this.sum;
    }

    public void setNum1(int num1) {
        this.num1 = num1;
    }

    public void setNum2(int num2) {
        this.num2 = num2;
    }
}