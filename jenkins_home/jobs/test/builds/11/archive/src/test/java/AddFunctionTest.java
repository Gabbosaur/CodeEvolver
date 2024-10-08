import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class AddFunctionTest {

    private AddFunction addFunction;

    @BeforeEach
    public void setup() {
        addFunction = new AddFunction();
    }

    @Test
    public void testConstructor() {
        assertEquals(0, addFunction.getNum1());
        assertEquals(0, addFunction.getNum2());
        assertEquals(0, addFunction.getSum());
    }

    @Test
    public void testCalculateSum() {
        addFunction.setNum1(10);
        addFunction.setNum2(20);
        addFunction.calculateSum();
        assertEquals(30, addFunction.getSum());
    }

    @Test
    public void testCalculateSumWithNegativeNumbers() {
        addFunction.setNum1(-10);
        addFunction.setNum2(-20);
        addFunction.calculateSum();
        assertEquals(-30, addFunction.getSum());
    }

    @Test
    public void testCalculateSumWithZero() {
        addFunction.setNum1(0);
        addFunction.setNum2(0);
        addFunction.calculateSum();
        assertEquals(0, addFunction.getSum());
    }

    @Test
    public void testSettersAndGetters() {
        addFunction.setNum1(10);
        addFunction.setNum2(20);
        addFunction.setSum(30);
        assertEquals(10, addFunction.getNum1());
        assertEquals(20, addFunction.getNum2());
        assertEquals(30, addFunction.getSum());
    }
}