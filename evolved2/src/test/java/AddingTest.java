import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class AddingTest {

    private Adding adding;

    public AddingTest() {
        this.adding = new Adding();
    }

    @Test
    public void testAddNumbers_PositiveNumbers() {
        adding.setNum1(10);
        adding.setNum2(20);
        int sum = adding.addNumbers(adding.getNum1(), adding.getNum2());
        assertEquals(30, sum);
    }

    @Test
    public void testAddNumbers_NegativeNumbers() {
        adding.setNum1(-10);
        adding.setNum2(-20);
        int sum = adding.addNumbers(adding.getNum1(), adding.getNum2());
        assertEquals(-30, sum);
    }

    @Test
    public void testAddNumbers_MixedNumbers() {
        adding.setNum1(10);
        adding.setNum2(-20);
        int sum = adding.addNumbers(adding.getNum1(), adding.getNum2());
        assertEquals(-10, sum);
    }

    @Test
    public void testAddNumbers_ZeroNumbers() {
        adding.setNum1(0);
        adding.setNum2(0);
        int sum = adding.addNumbers(adding.getNum1(), adding.getNum2());
        assertEquals(0, sum);
    }

    @Test
    public void testDisplaySum() {
        adding.setSum(10);
        try {
            adding.displaySum(adding.getSum());
        } catch (Exception e) {
            assert false;
        }
    }
}