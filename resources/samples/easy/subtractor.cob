       IDENTIFICATION DIVISION.
       PROGRAM-ID. SubtractFunction.

       ENVIRONMENT DIVISION.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  NUM1            PIC 9(5) VALUE 0.
       01  NUM2            PIC 9(5) VALUE 0.
       01  DIFFERENCE      PIC 9(5) VALUE 0.
       01  WS-OUTPUT-MESSAGE PIC X(30) VALUE 'The difference is: '.

       PROCEDURE DIVISION.
       MAIN-PARAGRAPH.

           DISPLAY 'Enter the first number: '.
           ACCEPT NUM1.

           DISPLAY 'Enter the second number: '.
           ACCEPT NUM2.

           PERFORM SUBTRACT-NUMBERS.

           DISPLAY WS-OUTPUT-MESSAGE DIFFERENCE.

           STOP RUN.

       SUBTRACT-NUMBERS.
           SUBTRACT NUM2 FROM NUM1 GIVING DIFFERENCE.

       END PROGRAM SubtractFunction.
