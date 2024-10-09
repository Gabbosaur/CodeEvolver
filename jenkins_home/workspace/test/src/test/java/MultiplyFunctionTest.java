import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class MultiplyFunctionTest {

    @Test
    public void testMultiplyNumbers_PositiveNumbers() {
        MultiplyFunction multiplyFunction = new MultiplyFunction();
        long product = multiplyFunction.multiplyNumbers(5, 3);
        assertEquals(15, product);
    }

    @Test
    public void testMultiplyNumbers_NegativeNumbers() {
        MultiplyFunction multiplyFunction = new MultiplyFunction();
        long product = multiplyFunction.multiplyNumbers(-5, -3);
        assertEquals(15, product);
    }

    @Test
    public void testMultiplyNumbers_MixedNumbers() {
        MultiplyFunction multiplyFunction = new MultiplyFunction();
        long product = multiplyFunction.multiplyNumbers(-5, 3);
        assertEquals(-15, product);
    }

    @Test
    public void testMultiplyNumbers_Zero() {
        MultiplyFunction multiplyFunction = new MultiplyFunction();
        long product = multiplyFunction.multiplyNumbers(0, 3);
        assertEquals(0, product);
    }

    @Test
    public void testSettersAndGetters() {
        MultiplyFunction multiplyFunction = new MultiplyFunction();
        multiplyFunction.setNum1(5);
        multiplyFunction.setNum2(3);
        multiplyFunction.multiplyNumbers(multiplyFunction.getNum1(), multiplyFunction.getNum2());
        assertEquals(15, multiplyFunction.getProduct());
    }
}