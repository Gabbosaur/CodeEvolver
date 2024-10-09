import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

public class DivideFunctionTest {

    @Test
    public void testGetFirstNumber() {
        DivideFunction divideFunction = new DivideFunction();
        double result = divideFunction.getFirstNumber();
        assertEquals(10.0, result);
    }

    @Test
    public void testGetSecondNumber() {
        DivideFunction divideFunction = new DivideFunction();
        double result = divideFunction.getSecondNumber();
        assertEquals(2.0, result);
    }

    @Test
    public void testDivideNumbers() {
        DivideFunction divideFunction = new DivideFunction();
        double result = divideFunction.divideNumbers(10.0, 2.0);
        assertEquals(5.0, result);
    }

    @Test
    public void testDivideNumbersByZero() {
        DivideFunction divideFunction = new DivideFunction();
        ArithmeticException exception = assertThrows(ArithmeticException.class, () -> divideFunction.divideNumbers(10.0, 0.0));
        assertEquals("Division by zero error!", exception.getMessage());
    }

    @Test
    public void testDisplayResult() {
        // Since displayResult method is void and prints to console, we can't directly test its output.
        // However, we can test that it doesn't throw any exceptions.
        DivideFunction divideFunction = new DivideFunction();
        divideFunction.displayResult(5.0);
    }
}