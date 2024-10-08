       IDENTIFICATION DIVISION.
       PROGRAM-ID. DivideFunction.

       ENVIRONMENT DIVISION.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  NUM1            PIC 9(5) VALUE 0.
       01  NUM2            PIC 9(5) VALUE 0.
       01  QUOTIENT        PIC 9(5)V99 VALUE 0.  *> Adjusted for decimal precision
       01  WS-OUTPUT-MESSAGE PIC X(30) VALUE 'The quotient is: '.
       01  WS-DIVISION-BY-ZERO PIC X(30) VALUE 'Division by zero error!'.

       PROCEDURE DIVISION.
       MAIN-PARAGRAPH.

           DISPLAY 'Enter the first number: '.
           ACCEPT NUM1.

           DISPLAY 'Enter the second number: '.
           ACCEPT NUM2.

           IF NUM2 = 0 THEN
               DISPLAY WS-DIVISION-BY-ZERO
           ELSE
               PERFORM DIVIDE-NUMBERS
               DISPLAY WS-OUTPUT-MESSAGE QUOTIENT
           END-IF.

           STOP RUN.

       DIVIDE-NUMBERS.
           DIVIDE NUM1 BY NUM2 GIVING QUOTIENT.

       END PROGRAM DivideFunction.
