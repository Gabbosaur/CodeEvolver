*> Brayden Cowell - 0844864
*> Monday, Mar. 7th, 2016
*> Trimethius Cipher
*> Main "Function"
*> Compilation Instructions in Reflection Doc!

identification division.
program-id. cipher.

environment division.
input-output section.
file-control.
    select file-name 
    assign to dynamic user-input
    file status is in-file-status.

data division.
file section.
    fd file-name.
    01 in-str		pic x(2000).

working-storage section.
    *> File stuff.
    01 in-file-status		pic xx.
	77 lf					pic x(01) 	value x'0A'.
	77 cr					pic x(01) 	value x'0D'.
	77 crlf					pic x(02) 	value x'0D0A'.
    01 end-of-file-switch	pic xxx 	value 'no '.
		88 end-of-file					value 'yes'.
    88 infinity							value 'no'.
 
    *> Loop iterators
    01 i    pic 99  	value 2.
    01 j    pic 99  	value 1.
    
    *> Data-structure - 26 rows each with 26 letters
    01 alphabet-record. 
            03 row              	occurs 26 times.
            05 alpha    pic x   	occurs 26 times.
	
	*> String stuff
    01 temp-str     	pic x(26)   value spaces.
    01 user-input       pic x(20).
    01 str-size         pic 9999.
    
    *> Variables for removing spaces.
    01 vout     pic x(2000).
    01 vwork    pic x(2000).
    01 vtemp    pic x(2000).
    01 p1       pic 9999.
    01 p2       pic 9999.

    
procedure division.
*> Create the Trimethius Cipher table of each shifted alphabet.
init-table.
    *> Initialize the first row.
    move "abcdefghijklmnopqrstuvwxyz" to row(1).

    perform until i > 26
        move i to j
        subtract 1 from j
        move row(j) to temp-str

        *> Replacing each letter with the next.
        inspect temp-str
        converting "abcdefghijklmnopqrstuvwxyz" to "bcdefghijklmnopqrstuvwxyza"

        move temp-str to row(i)
        Add 1 to i
    end-perform.


*> Remove spaces for a string.
*> source: http://www.tek-tips.com/viewthread.cfm?qid=858815 - Frederico Fonseca
unstring1.
    move 1 to p1 p2.
           
    perform until p1 > 2000
        move spaces to vout vtemp
           
        perform until p1 > 2000
            unstring vwork delimited by all spaces
				*> Trim line-endings
				or lf or cr or crlf
				*> Trim punctuation
				or '.' or ',' or '!' or ':' or ';' or '-' or '?' 
                into vtemp
            pointer p1
            *> If vtemp not = spaces
            string vtemp delimited by spaces
                into vout
            pointer p2
            *> End-if
        end-perform
    end-perform.
    *> Vout now holds the string sans spaces.
    move vout to in-str.


*> Read in user-input, encrypt, decrypt, and display output.
translate.
    *> Ask the user for filename
    display "Enter an input filename:".
    accept user-input from console.

    display "Opening " user-input.
    *> Read the lines from file.
    open input file-name.
	
	if in-file-status not = '00'
		display "Cannot read file! Error: " in-file-status "!"
		display "Exiting."
		perform exit-program
	end-if.
	
	perform until end-of-file
		read file-name into in-str
			at end set end-of-file to true
		end-read
	end-perform.
    
    *> Change any Upper-case letters to lower-case.
    inspect in-str converting "ABCDEFGHIJKLMNOPQRSTUVWXYZ" to "abcdefghijklmnopqrstuvwxyz".
    
    *> Trim the spaces inbetween words.
    move in-str to vwork.
    perform unstring1.
    
    *> User-input is still 2000 chars long, so we need to cut the right-trailing spaces.
    unstring in-str delimited by all spaces
    into in-str
    count in str-size
    end-unstring.
    
	display " ".
    display "Text: " in-str(1:str-size).
    
    *> Now we can call encrypt/decrypt with the properly sized string.
	perform until infinity
		display "  "
		display "Would you like to encipher or decipher? Enter e or d (q to quit)."
		accept user-input from console
		
		if (user-input is equal to "q") then
			perform exit-program
		end-if
		
		*> Encrypt the string
		if (user-input is equal to "e") then
			call 'encrypt' using in-str(1:str-size), by content alphabet-record
			display "Encrypted " in-str(1:str-size)
		end-if
		
		*> Decrypt the string
		if (user-input is equal to "d") then
			call 'decrypt' using in-str(1:str-size), by content alphabet-record
			display "Decrypted " in-str(1:str-size)
		end-if
	end-perform.

exit-program.
	close file-name
	stop run.