public class Decrypt {
    public static void main(String[] args) {
        String inputText = "Function";
        String decryptedText = decrypt(inputText);
        System.out.println("Decrypted Text: " + decryptedText);
    }

    public static String decrypt(String inputText) {
        StringBuilder decryptedText = new StringBuilder();
        for (int i = 0; i < inputText.length(); i++) {
            char tempChar = inputText.toLowerCase().charAt(i);
            if (Character.isLetter(tempChar)) {
                int pos = tempChar - 'a';
                int row = pos / 26;
                int col = pos % 26;
                char[] alphabet = "abcdefghijklmnopqrstuvwxyz".toCharArray();
                decryptedText.append(alphabet[col]);
            } else {
                decryptedText.append(tempChar);
            }
        }
        return decryptedText.toString();
    }
}