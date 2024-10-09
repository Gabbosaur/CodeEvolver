import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class MultiplyFunctionTest {

    private MultiplyFunction multiplyFunction;

    @BeforeEach
    public void setup() {
        multiplyFunction = new MultiplyFunction();
    }

    @Test
    public void testConstructor() {
        assertEquals(0, multiplyFunction.getNum1());
        assertEquals(0, multiplyFunction.getNum2());
        assertEquals(0, multiplyFunction.getProduct());
    }

    @Test
    public void testSetAndGetNum1() {
        multiplyFunction.setNum1(10);
        assertEquals(10, multiplyFunction.getNum1());
    }

    @Test
    public void testSetAndGetNum2() {
        multiplyFunction.setNum2(20);
        assertEquals(20, multiplyFunction.getNum2());
    }

    @Test
    public void testMultiplyNumbers() {
        multiplyFunction.setNum1(10);
        multiplyFunction.setNum2(20);
        multiplyFunction.multiplyNumbers();
        assertEquals(200, multiplyFunction.getProduct());
    }

    @Test
    public void testMultiplyNumbersWithNegativeNumbers() {
        multiplyFunction.setNum1(-10);
        multiplyFunction.setNum2(20);
        multiplyFunction.multiplyNumbers();
        assertEquals(-200, multiplyFunction.getProduct());
    }
}