## LEVEL 1 - QUESTION 1

Question Name: _New World, New World!_

- **Question Statement**: Crash landing, you see that the world that surrounds you is completely flat. It seems to be like a giant disc that is floating through the cosmos of space. There is no edgeline, and the sight is just fascinating, for the world seems to have no day and night cycles. You turn around, and you see an eerily similar figure. It seems that you might have caught a neo-Caeser at the nick of time. Beside him, you see a robot version, with the nameplate Brutus. Seeing the knife that is being held back by Brutus, you try and stop the assisination attempt from taking place. Peeking into him, you are given a file to corrupt the robot. Try to decipher it, which you can use to save Caeser.
- **Key**: `actf{e7_7u_bru73_t73_s1nk1Ngd0m}`

## Metadata
- Author: [Roonil03](https://github.com/Roonil03)
- File: `ZIP.zip` (contains `brutus.txt`)

## Solution
- The encoded text file has data encoded in a binary format.
- Decode the binary text to ASCII characters.
- The encoded text file is ina  Caesar Cipher, which can be decoded by applying 7 rotations.
- The given output is a `C` script, which has to be modified to ave a header for printing and then print the flag.
- This, then, gives the user the flag.
