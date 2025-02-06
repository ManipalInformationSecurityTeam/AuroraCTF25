## LEVEL 3 - QUESTION 2

Question Name: `sh0ck3d`

- **Question Statement**: Before you can ponder further, another transmission crackles to life. This time, it's from an entity known as The Variable. Yet, as the message begins to relay its contents, interference from the Legion cuts through the signal like a jagged blade. Alarms blare, and from the depths of space emerges a gargantuan galactic warship. Its sheer size eclipses the horizon, its hull gleaming with ominous radiance. Strangely, you have not been obliterated upon detection. Your comms flare, and a distorted voice drenched in menace establishes contact—it is the Legion.
- **Key**: `r3st4rt3d`

## Metadata
- **Tags**: `Forensics`, `Cryptography`
- **Author**: [TheVariable](https://github.com/variablethe)
- **Files**: `ZIP.zip`

## Solution Approach
- Decode the provided WAV audio file using an SSTV decoder to reveal an image containing a cat with text "OIIAI"
- Analyze the hex dump of images.png to find the string "Ecabapa" at the end
- Use "OIIAI" as a key to decrypt "Ecabapa" using the Vigenère cipher, revealing "Skibidi"
- Use "Skibidi" as the password in stegosuite to extract the hidden flag from images.png
- The extracted flag is `r3st4rt3d`
