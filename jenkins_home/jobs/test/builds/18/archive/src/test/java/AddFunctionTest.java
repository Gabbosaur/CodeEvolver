import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class AddFunctionTest {

    @Test
    public void testAddNumbers_PositiveNumbers() {
        // Arrange
        AddFunction addFunction = new AddFunction();
        addFunction.setNum1(10);
        addFunction.setNum2(20);

        // Act
        addFunction.addNumbers();

        // Assert
        assertEquals(30, addFunction.getSum());
    }

    @Test
    public void testAddNumbers_NegativeNumbers() {
        // Arrange
        AddFunction addFunction = new AddFunction();
        addFunction.setNum1(-10);
        addFunction.setNum2(-20);

        // Act
        addFunction.addNumbers();

        // Assert
        assertEquals(-30, addFunction.getSum());
    }

    @Test
    public void testAddNumbers_MixedNumbers() {
        // Arrange
        AddFunction addFunction = new AddFunction();
        addFunction.setNum1(10);
        addFunction.setNum2(-20);

        // Act
        addFunction.addNumbers();

        // Assert
        assertEquals(-10, addFunction.getSum());
    }

    @Test
    public void testAddNumbers_ZeroNumbers() {
        // Arrange
        AddFunction addFunction = new AddFunction();
        addFunction.setNum1(0);
        addFunction.setNum2(0);

        // Act
        addFunction.addNumbers();

        // Assert
        assertEquals(0, addFunction.getSum());
    }

    @Test
    public void testAddNumbers_DefaultConstructor() {
        // Arrange
        AddFunction addFunction = new AddFunction();

        // Act
        addFunction.addNumbers();

        // Assert
        assertEquals(0, addFunction.getSum());
    }
}