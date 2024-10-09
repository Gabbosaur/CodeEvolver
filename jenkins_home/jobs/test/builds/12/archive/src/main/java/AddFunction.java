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
     * Method to calculate the sum of the two numbers
     */
    public void addNumbers() {
        // Calculate the sum
        this.sum = this.num1 + this.num2;
    }

    /**
     * Method to display the sum
     */
    public void displaySum() {
        // Display the output message and the sum
        System.out.println(OUTPUT_MESSAGE + this.sum);
    }

    /**
     * Main method to execute the program
     * @param args Command-line arguments (not used)
     */
    public static void main(String[] args) {
        // Create an instance of the AddFunction class
        AddFunction addFunction = new AddFunction();

        // Get the first number from the user
        addFunction.getFirstNumber();

        // Get the second number from the user
        addFunction.getSecondNumber();

        // Calculate the sum
        addFunction.addNumbers();

        // Display the sum
        addFunction.displaySum();
    }

    // Public methods for unit testing
    public int getNum1() {
        return this.num1;
    }

    public int getNum2() {
        return this.num2;
    }

    public int getSum() {
        return this.sum;
    }

    public void setNum1(int num1) {
        this.num1 = num1;
    }

    public void setNum2(int num2) {
        this.num2 = num2;
    }

    public void setSum(int sum) {
        this.sum = sum;
    }
}