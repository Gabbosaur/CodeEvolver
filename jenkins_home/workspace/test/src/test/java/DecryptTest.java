import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class DecryptTest {

    @Test
    public void testDecryptSingleLetter() {
        String inputText = "a";
        String expectedOutput = "a";
        assertEquals(expectedOutput, Decrypt.decrypt(inputText));
    }

    @Test
    public void testDecryptMultipleLetters() {
        String inputText = "abc";
        String expectedOutput = "bcd";
        assertEquals(expectedOutput, Decrypt.decrypt(inputText));
    }

    @Test
    public void testDecryptMixedCase() {
        String inputText = "AbC";
        String expectedOutput = "Bcd";
        assertEquals(expectedOutput, Decrypt.decrypt(inputText));
    }

    @Test
    public void testDecryptNonAlphabeticCharacters() {
        String inputText = "abc123";
        String expectedOutput = "bcd123";
        assertEquals(expectedOutput, Decrypt.decrypt(inputText));
    }

    @Test
    public void testDecryptEmptyString() {
        String inputText = "";
        String expectedOutput = "";
        assertEquals(expectedOutput, Decrypt.decrypt(inputText));
    }

    @Test
    public void testDecryptNullInput() {
        String inputText = null;
        try {
            Decrypt.decrypt(inputText);
            assert false;
        } catch (NullPointerException e) {
            assert true;
        }
    }
}