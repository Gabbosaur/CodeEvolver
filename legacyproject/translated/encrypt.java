public class TrimethiusCipher {

    public static void main(String[] args) {
        String inputText = "Function";
        char[][] alphabetRecord = new char[26][26];

        // Initialize alphabet record
        for (int i = 0; i < 26; i++) {
            for (int j = 0; j < 26; j++) {
                alphabetRecord[i][j] = (char) ('a' + j);
            }
        }

        // Encrypt the input text
        String encryptedText = encrypt(inputText, alphabetRecord);

        System.out.println("Encrypted text: " + encryptedText);
    }

    public static String encrypt(String inputText, char[][] alphabetRecord) {
        StringBuilder encryptedText = new StringBuilder();
        int pos = 0;
        int num = 1;

        for (char c : inputText.toCharArray()) {
            if (Character.isLetter(c)) {
                // Find the position of the letter to replace it with
                int charPos = c - 'a';
                pos = (pos + charPos) % 26;
                num = (num + pos) % 26;

                // Find the new character
                char newChar = alphabetRecord[pos][num - 1];

                encryptedText.append(newChar);
            } else {
                encryptedText.append(c);
            }
        }

        return encryptedText.toString();
    }
}