import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class AddFunctionTest {

    @Test
    public void testAddNumbers() {
        // Arrange
        AddFunction addFunction = new AddFunction();
        addFunction.setNum1(5);
        addFunction.setNum2(7);

        // Act
        addFunction.addNumbers();

        // Assert
        assertEquals(12, addFunction.getSum());
    }

    @Test
    public void testAddNumbersWithNegativeNumbers() {
        // Arrange
        AddFunction addFunction = new AddFunction();
        addFunction.setNum1(-5);
        addFunction.setNum2(7);

        // Act
        addFunction.addNumbers();

        // Assert
        assertEquals(2, addFunction.getSum());
    }

    @Test
    public void testAddNumbersWithZero() {
        // Arrange
        AddFunction addFunction = new AddFunction();
        addFunction.setNum1(0);
        addFunction.setNum2(7);

        // Act
        addFunction.addNumbers();

        // Assert
        assertEquals(7, addFunction.getSum());
    }

    @Test
    public void testAddNumbersWithSameNumbers() {
        // Arrange
        AddFunction addFunction = new AddFunction();
        addFunction.setNum1(5);
        addFunction.setNum2(5);

        // Act
        addFunction.addNumbers();

        // Assert
        assertEquals(10, addFunction.getSum());
    }

    @Test
    public void testAddNumbersWithDefaultValues() {
        // Arrange
        AddFunction addFunction = new AddFunction();

        // Act
        addFunction.addNumbers();

        // Assert
        assertEquals(0, addFunction.getSum());
    }
}