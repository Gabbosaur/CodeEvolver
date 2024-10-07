*> Brayden Cowell - 0844864
*> Monday, Mar. 7th, 2016
*> Trimethius Cipher.
*> Encrypt "Function"
*> Compilation Instructions in Reflection Doc!

identification division.
program-id. encrypt.

data division.
	working-storage section.
	*> Loop iterators
	01 i pic 9999 value 1.
	01 j pic 99 value 1.

	*> Positions
	01 pos pic 99 value 0.
	01 num pic 99 value 1.

	01 temp-char pic x.

	linkage section.
	01 input-text pic x(2000).

	01 alphabet-record.
                03 row occurs 26 times.
                        05 alpha pic x occurs 26 times.

procedure division using input-text, alphabet-record.

*> Use the characters position in the input-string to find what it encodes to in the cipher-table.
encode.
	move 1 to num.
	*> Go through each row of shifted letters.
	if pos is not equal to 26 then
		move function mod(pos,26) to pos
	end-if.

	*> Find the position of the letter to replace it with.
	evaluate temp-char
		when "a" move 1 to num
		when "b" move 2 to num
		when "c" move 3 to num
		when "d" move 4 to num
		when "e" move 5 to num
		when "f" move 6 to num
		when "g" move 7 to num
		when "h" move 8 to num
		when "i" move 9 to num
		when "j" move 10 to num
		when "k" move 11 to num
		when "l" move 12 to num
		when "m" move 13 to num
		when "n" move 14 to num
		when "o" move 15 to num
		when "p" move 16 to num
		when "q" move 17 to num
		when "r" move 18 to num
		when "s" move 19 to num
		when "t" move 20 to num
		when "u" move 21 to num
		when "v" move 22 to num
		when "w" move 23 to num
		when "x" move 24 to num
		when "y" move 25 to num
		when "z" move 26 to num
	end-evaluate.
	
	move alpha(pos,num) to temp-char.
	
	add 1 to pos.

*> Read each character one at a time calling encode for the string.
translate.
	move 1 to i.
	
	perform until i > 2000
		if input-text(i:1) is alphabetic then
			move input-text(i:1) to temp-char
			perform encode
			move temp-char to input-text(i:1)
		end-if
		add 1 to i
	end-perform.

exit program.