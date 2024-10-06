import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;

public class Main {

    private static final String ALPHABET = "abcdefghijklmnopqrstuvwxyz";
    private static final int MAX_SIZE = 2000;
    private static final int MAX_ROWS = 26;
    private static final int MAX_COLS = 26;

    public static void main(String[] args) {
        String[] alphabetRecord = new String[MAX_ROWS];
        for (int i = 0; i < MAX_ROWS; i++) {
            alphabetRecord[i] = ALPHABET;
        }

        // Create the Trimethius Cipher table of each shifted alphabet
        for (int i = 1; i <= MAX_ROWS; i++) {
            String tempStr = alphabetRecord[i - 1];
            for (int j = 0; j < MAX_COLS; j++) {
                tempStr = tempStr.substring(1) + tempStr.charAt(0);
            }
            alphabetRecord[i - 1] = tempStr;
        }

        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter an input filename:");
        String filename = scanner.nextLine();

        try (BufferedReader reader = new BufferedReader(new FileReader(filename))) {
            StringBuilder inStr = new StringBuilder();
            String line;
            while ((line = reader.readLine()) != null) {
                inStr.append(line).append("\n");
            }

            // Change any Upper-case letters to lower-case
            inStr = new StringBuilder(inStr.toString().toLowerCase());

            // Trim the spaces inbetween words
            String[] words = inStr.toString().split("\\s+");
            StringBuilder vwork = new StringBuilder();
            for (String word : words) {
                vwork.append(word).append(" ");
            }
            inStr = new StringBuilder(vwork.toString().trim());

            System.out.println("Text: " + inStr.toString());

            while (true) {
                System.out.println("Would you like to encipher or decipher? Enter e or d (q to quit).");
                String choice = scanner.nextLine();
                if (choice.equalsIgnoreCase("q")) {
                    break;
                }

                if (choice.equalsIgnoreCase("e")) {
                    String encrypted = encrypt(inStr.toString(), alphabetRecord);
                    System.out.println("Encrypted: " + encrypted);
                } else if (choice.equalsIgnoreCase("d")) {
                    String decrypted = decrypt(inStr.toString(), alphabetRecord);
                    System.out.println("Decrypted: " + decrypted);
                }
            }
        } catch (IOException e) {
            System.out.println("Cannot read file! Error: " + e.getMessage());
            System.out.println("Exiting.");
        }
    }

    private static String encrypt(String inStr, String[] alphabetRecord) {
        StringBuilder encrypted = new StringBuilder();
        for (char c : inStr.toCharArray()) {
            if (c >= 'a' && c <= 'z') {
                int index = c - 'a';
                encrypted.append(alphabetRecord[index].charAt(index));
            } else {
                encrypted.append(c);
            }
        }
        return encrypted.toString();
    }

    private static String decrypt(String inStr, String[] alphabetRecord) {
        StringBuilder decrypted = new StringBuilder();
        for (char c : inStr.toCharArray()) {
            if (c >= 'a' && c <= 'z') {
                int index = c - 'a';
                decrypted.append(alphabetRecord[index].charAt(0));
            } else {
                decrypted.append(c);
            }
        }
        return decrypted.toString();
    }
}