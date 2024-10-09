import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class AddFunctionTest {

    @Test
    public void testAddNumbers_PositiveNumbers() {
        // Arrange
        AddFunction addFunction = new AddFunction();
        int num1 = 10;
        int num2 = 20;

        // Act
        int sum = addFunction.addNumbers(num1, num2);

        // Assert
        assertEquals(30, sum);
    }

    @Test
    public void testAddNumbers_NegativeNumbers() {
        // Arrange
        AddFunction addFunction = new AddFunction();
        int num1 = -10;
        int num2 = -20;

        // Act
        int sum = addFunction.addNumbers(num1, num2);

        // Assert
        assertEquals(-30, sum);
    }

    @Test
    public void testAddNumbers_MixedNumbers() {
        // Arrange
        AddFunction addFunction = new AddFunction();
        int num1 = 10;
        int num2 = -20;

        // Act
        int sum = addFunction.addNumbers(num1, num2);

        // Assert
        assertEquals(-10, sum);
    }

    @Test
    public void testAddNumbers_Zero() {
        // Arrange
        AddFunction addFunction = new AddFunction();
        int num1 = 0;
        int num2 = 0;

        // Act
        int sum = addFunction.addNumbers(num1, num2);

        // Assert
        assertEquals(0, sum);
    }

    @Test
    public void testDisplayResult() {
        // Arrange
        AddFunction addFunction = new AddFunction();
        int sum = 10;

        // Act and Assert
        // Since displayResult method is void and prints to console, we can't directly test its output.
        // However, we can test that it doesn't throw any exceptions.
        try {
            addFunction.displayResult(sum);
        } catch (Exception e) {
            assert false : "displayResult method threw an exception";
        }
    }
}