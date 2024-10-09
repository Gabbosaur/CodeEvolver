import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class SubtractFunctionTest {

    @Test
    public void testSubtractNumbers_PositiveNumbers() {
        SubtractFunction subtractFunction = new SubtractFunction();
        subtractFunction.setNum1(10);
        subtractFunction.setNum2(5);
        int result = subtractFunction.subtractNumbers(subtractFunction.getNum1(), subtractFunction.getNum2());
        assertEquals(5, result);
    }

    @Test
    public void testSubtractNumbers_NegativeNumbers() {
        SubtractFunction subtractFunction = new SubtractFunction();
        subtractFunction.setNum1(-10);
        subtractFunction.setNum2(-5);
        int result = subtractFunction.subtractNumbers(subtractFunction.getNum1(), subtractFunction.getNum2());
        assertEquals(-5, result);
    }

    @Test
    public void testSubtractNumbers_MixedNumbers() {
        SubtractFunction subtractFunction = new SubtractFunction();
        subtractFunction.setNum1(10);
        subtractFunction.setNum2(-5);
        int result = subtractFunction.subtractNumbers(subtractFunction.getNum1(), subtractFunction.getNum2());
        assertEquals(15, result);
    }

    @Test
    public void testDisplayResult() {
        SubtractFunction subtractFunction = new SubtractFunction();
        subtractFunction.setDifference(10);
        // Since displayResult method doesn't return anything, we can't assert its result directly.
        // However, we can verify that it doesn't throw any exception.
        subtractFunction.displayResult(subtractFunction.getDifference());
    }

    @Test
    public void testGettersAndSetters() {
        SubtractFunction subtractFunction = new SubtractFunction();
        subtractFunction.setNum1(10);
        subtractFunction.setNum2(5);
        subtractFunction.setDifference(5);
        assertEquals(10, subtractFunction.getNum1());
        assertEquals(5, subtractFunction.getNum2());
        assertEquals(5, subtractFunction.getDifference());
    }
}