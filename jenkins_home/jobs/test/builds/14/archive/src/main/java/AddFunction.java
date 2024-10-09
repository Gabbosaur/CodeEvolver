/**
 * This class represents a simple addition function.
 * It takes two numbers as input, adds them together, and displays the result.
 */
public class AddFunction {

    // Private variables to store the numbers and the result
    private int num1;
    private int num2;
    private int sum;

    // Constructor to initialize the variables
    public AddFunction() {
        this.num1 = 0;
        this.num2 = 0;
        this.sum = 0;
    }

    /**
     * Method to get the first number from the user
     */
    public void getFirstNumber() {
        // Using Java's built-in Scanner class to get user input
        try (java.util.Scanner scanner = new java.util.Scanner(System.in)) {
            System.out.print("Enter the first number: ");
            this.num1 = scanner.nextInt();
        }
    }

    /**
     * Method to get the second number from the user
     */
    public void getSecondNumber() {
        // Using Java's built-in Scanner class to get user input
        try (java.util.Scanner scanner = new java.util.Scanner(System.in)) {
            System.out.print("Enter the second number: ");
            this.num2 = scanner.nextInt();
        }
    }

    /**
     * Method to add the two numbers together
     */
    public void addNumbers() {
        // Simple addition operation
        this.sum = this.num1 + this.num2;
    }

    /**
     * Method to display the result
     */
    public void displayResult() {
        // Using string concatenation to display the result
        System.out.println("The sum is: " + this.sum);
    }

    /**
     * Main method to execute the program
     * @param args Command-line arguments (not used in this program)
     */
    public static void main(String[] args) {
        // Creating an instance of the AddFunction class
        AddFunction addFunction = new AddFunction();

        // Getting the numbers from the user
        addFunction.getFirstNumber();
        addFunction.getSecondNumber();

        // Adding the numbers together
        addFunction.addNumbers();

        // Displaying the result
        addFunction.displayResult();
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