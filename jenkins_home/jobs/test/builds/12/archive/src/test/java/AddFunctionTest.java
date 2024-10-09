import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class AddFunctionTest {

    @Test
    public void testConstructor() {
        // Create an instance of the AddFunction class
        AddFunction addFunction = new AddFunction();

        // Verify that the constructor initializes the variables correctly
        assertEquals(0, addFunction.getNum1());
        assertEquals(0, addFunction.getNum2());
        assertEquals(0, addFunction.getSum());
    }

    @Test
    public void testAddNumbers() {
        // Create an instance of the AddFunction class
        AddFunction addFunction = new AddFunction();

        // Set the input numbers
        addFunction.setNum1(5);
        addFunction.setNum2(3);

        // Calculate the sum
        addFunction.addNumbers();

        // Verify that the sum is calculated correctly
        assertEquals(8, addFunction.getSum());
    }

    @Test
    public void testAddNumbersNegativeNumbers() {
        // Create an instance of the AddFunction class
        AddFunction addFunction = new AddFunction();

        // Set the input numbers
        addFunction.setNum1(-5);
        addFunction.setNum2(-3);

        // Calculate the sum
        addFunction.addNumbers();

        // Verify that the sum is calculated correctly
        assertEquals(-8, addFunction.getSum());
    }

    @Test
    public void testAddNumbersZero() {
        // Create an instance of the AddFunction class
        AddFunction addFunction = new AddFunction();

        // Set the input numbers
        addFunction.setNum1(0);
        addFunction.setNum2(0);

        // Calculate the sum
        addFunction.addNumbers();

        // Verify that the sum is calculated correctly
        assertEquals(0, addFunction.getSum());
    }

    @Test
    public void testSettersAndGetters() {
        // Create an instance of the AddFunction class
        AddFunction addFunction = new AddFunction();

        // Set the input numbers
        addFunction.setNum1(10);
        addFunction.setNum2(20);
        addFunction.setSum(30);

        // Verify that the setters and getters work correctly
        assertEquals(10, addFunction.getNum1());
        assertEquals(20, addFunction.getNum2());
        assertEquals(30, addFunction.getSum());
    }
}