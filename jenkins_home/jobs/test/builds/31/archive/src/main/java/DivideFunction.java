/**
 * This class represents a division function that takes two numbers as input and returns their quotient.
 */
public class DivideFunction {

    private double num1;
    private double num2;
    private double quotient;
    private static final String OUTPUT_MESSAGE = "The quotient is: ";
    private static final String DIVISION_BY_ZERO_MESSAGE = "Division by zero error!";

    /**
     * Constructor to initialize the object with default values.
     */
    public DivideFunction() {
        this.num1 = 0;
        this.num2 = 0;
        this.quotient = 0;
    }

    /**
     * Method to get the first number from the user.
     * @return the first number
     */
    public double getFirstNumber() {
        // For simplicity, we'll use a hardcoded value here.
        // In a real-world application, you'd use a Scanner or other input method.
        return 10.0;
    }

    /**
     * Method to get the second number from the user.
     * @return the second number
     */
    public double getSecondNumber() {
        // For simplicity, we'll use a hardcoded value here.
        // In a real-world application, you'd use a Scanner or other input method.
        return 2.0;
    }

    /**
     * Method to perform the division operation.
     * @param num1 the dividend
     * @param num2 the divisor
     * @return the quotient
     * @throws ArithmeticException if the divisor is zero
     */
    public double divideNumbers(double num1, double num2) {
        if (num2 == 0) {
            throw new ArithmeticException(DIVISION_BY_ZERO_MESSAGE);
        }
        return num1 / num2;
    }

    /**
     * Method to display the result of the division operation.
     * @param quotient the quotient
     */
    public void displayResult(double quotient) {
        System.out.println(OUTPUT_MESSAGE + quotient);
    }

    /**
     * Main method to execute the division function.
     */
    public void execute() {
        num1 = getFirstNumber();
        num2 = getSecondNumber();

        try {
            quotient = divideNumbers(num1, num2);
            displayResult(quotient);
        } catch (ArithmeticException e) {
            System.out.println(e.getMessage());
        }
    }

    public static void main(String[] args) {
        DivideFunction divideFunction = new DivideFunction();
        divideFunction.execute();
    }
}