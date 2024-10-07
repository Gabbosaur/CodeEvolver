       IDENTIFICATION DIVISION.
       PROGRAM-ID. MultiplyFunction.

       ENVIRONMENT DIVISION.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  NUM1            PIC 9(5) VALUE 0.
       01  NUM2            PIC 9(5) VALUE 0.
       01  PRODUCT         PIC 9(10) VALUE 0.  *> Adjusted to accommodate larger products
       01  WS-OUTPUT-MESSAGE PIC X(30) VALUE 'The product is: '.

       PROCEDURE DIVISION.
       MAIN-PARAGRAPH.

           DISPLAY 'Enter the first number: '.
           ACCEPT NUM1.

           DISPLAY 'Enter the second number: '.
           ACCEPT NUM2.

           PERFORM MULTIPLY-NUMBERS.

           DISPLAY WS-OUTPUT-MESSAGE PRODUCT.

           STOP RUN.

       MULTIPLY-NUMBERS.
           MULTIPLY NUM1 BY NUM2 GIVING PRODUCT.

       END PROGRAM MultiplyFunction.
