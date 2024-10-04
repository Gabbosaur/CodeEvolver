public class TrimethiusCipher {

    // Main method to run the program
    public static void main(String[] args) {
        String inputText = "Function"; // Example input text
        String encryptedText = encrypt(inputText);
        System.out.println("Encrypted Text: " + encryptedText);
    }

    public static String encrypt(String inputText) {
        char[] inputChars = inputText.toCharArray();
        int pos = 0; // Position for encoding
        StringBuilder result = new StringBuilder();

        // Loop through each character in the input text
        for (int i = 0; i < inputChars.length; i++) {
            char currentChar = inputChars[i];

            // Check if the character is alphabetic
            if (Character.isLetter(currentChar)) {
                char encodedChar = encode(currentChar, pos);
                result.append(encodedChar);
                pos++; // Increment position for next character
            } else {
                result.append(currentChar); // Keep non-alphabetic characters unchanged
            }
        }

        return result.toString();
    }

    private static char encode(char tempChar, int pos) {
        int num = 0;

        // Determine the numeric position of the letter
        if (Character.isLowerCase(tempChar)) {
            num = tempChar - 'a' + 1; // 'a' = 1, 'b' = 2, ..., 'z' = 26
        } else if (Character.isUpperCase(tempChar)) {
            num = tempChar - 'A' + 1; // 'A' = 1, 'B' = 2, ..., 'Z' = 26
        }

        // Calculate new position using modulus
        pos = (pos % 26);

        // Determine the new character based on the encoded position
        char newChar = (char) ('a' + (pos + num - 1) % 26); // Wrap around if exceeds 'z'

        return newChar;
    }
}