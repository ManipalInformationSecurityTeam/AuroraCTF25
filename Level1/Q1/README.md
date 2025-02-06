## LEVEL 1 - QUESTION 1

Question Name: `n3w_w0rld++n3w_w0rld`

- **Question Statement**: Crash landing, you see that the world that surrounds you is completely flat. It seems to be like a giant disc that is floating through the cosmos of space. There is no edgeline, and the sight is just fascinating, for the world seems to have no day and night cycles. You turn around, and you see an eerily similar figure. It seems that you might have caught a neo-Caeser at the nick of time. Beside him, you see a robot version, with the nameplate Brutus. Seeing the knife that is being held back by Brutus, you try and stop the assisination attempt from taking place. Peeking into him, you are given a file to corrupt the robot. Try to decipher it, which you can use to save Caeser.
- **Key**: `actf{e7_7u_bru73_t73_s1nk1Ngd0m}`

## Metadata
- **Tags**: `Cryptography`
- **Author**: [Roonil03](https://github.com/Roonil03)
- **File**: `brutus.txt`

## Solution Approach
1. Download and open the provided binary text file containing a long string of binary data
2. Decode the binary data to ASCII, revealing an obfuscated C program with character assignments
3. Apply a Caesar cipher rotation of 7 positions to decrypt the obfuscated variable and function names
4. Add proper C headers and print statement to compile and run the program
5. Execute the modified C code to reveal the hidden flag
