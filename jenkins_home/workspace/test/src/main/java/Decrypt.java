public class Decrypt {

    private static final String ALPHABET = "abcdefghijklmnopqrstuvwxyz";
    private static final int MAX_INPUT_LENGTH = 2000;

    /**
     * Decrypts the input text by shifting each letter one position forward in the alphabet.
     * 
     * @param inputText the text to be decrypted
     * @return the decrypted text
     */
    public static String decrypt(String inputText) {
        if (inputText == null || inputText.isEmpty()) {
            return inputText;
        }

        char[] inputTextArray = inputText.toLowerCase().toCharArray();
        char[] alphabet = ALPHABET.toCharArray();

        for (int i = 0; i < inputTextArray.length; i++) {
            if (Character.isLetter(inputTextArray[i])) {
                int pos = ALPHABET.indexOf(inputTextArray[i]);
                if (pos != -1) {
                    int num = (pos + 1) % 26;
                    inputTextArray[i] = alphabet[num];
                }
            }
        }

        return new String(inputTextArray);
    }

    public static void main(String[] args) {
        String inputText = "Function";
        System.out.println("Input Text: " + inputText);
        System.out.println("Decrypted Text: " + decrypt(inputText));
    }
}