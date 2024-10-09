/**
 * This class represents a simple addition function.
 * It takes two numbers as input, adds them together, and displays the result.
 */
public class AddFunction {

    // Define the output message
    private static final String OUTPUT_MESSAGE = "The sum is: ";

    /**
     * Method to get the first number from the user
     * @return the first number
     */
    public int getFirstNumber() {
        return getNumberFromUser("Enter the first number: ");
    }

    /**
     * Method to get the second number from the user
     * @return the second number
     */
    public int getSecondNumber() {
        return getNumberFromUser("Enter the second number: ");
    }

    /**
     * Method to get a number from the user
     * @param prompt the prompt to display to the user
     * @return the number entered by the user
     */
    private int getNumberFromUser(String prompt) {
        try (java.util.Scanner scanner = new java.util.Scanner(System.in)) {
            System.out.print(prompt);
            return scanner.nextInt();
        }
    }

    /**
     * Method to add two numbers together
     * @param num1 the first number
     * @param num2 the second number
     * @return the sum of the two numbers
     */
    public int addNumbers(int num1, int num2) {
        return num1 + num2;
    }

    /**
     * Method to display the result
     * @param sum the sum to be displayed
     */
    public void displayResult(int sum) {
        System.out.println(OUTPUT_MESSAGE + sum);
    }

    /**
     * Main method to execute the program
     * @param args command-line arguments (not used)
     */
    public static void main(String[] args) {
        AddFunction addFunction = new AddFunction();
        int num1 = addFunction.getFirstNumber();
        int num2 = addFunction.getSecondNumber();
        int sum = addFunction.addNumbers(num1, num2);
        addFunction.displayResult(sum);
    }
}