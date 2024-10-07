       IDENTIFICATION DIVISION.
       PROGRAM-ID. AddFunction.

       ENVIRONMENT DIVISION.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  NUM1            PIC 9(5) VALUE 0.
       01  NUM2            PIC 9(5) VALUE 0.
       01  SUM             PIC 9(5) VALUE 0.
       01  WS-OUTPUT-MESSAGE PIC X(30) VALUE 'The sum is: '.

       PROCEDURE DIVISION.
       MAIN-PARAGRAPH.

           DISPLAY 'Enter the first number: '.
           ACCEPT NUM1.

           DISPLAY 'Enter the second number: '.
           ACCEPT NUM2.

           PERFORM ADD-NUMBERS.

           DISPLAY WS-OUTPUT-MESSAGE SUM.

           STOP RUN.

       ADD-NUMBERS.
           ADD NUM1 TO NUM2 GIVING SUM.

       END PROGRAM AddFunction.
