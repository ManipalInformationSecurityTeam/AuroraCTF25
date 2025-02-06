## LEVEL 1 - QUESTION 3

## Question Name: `7H3_MY7H_4ND_7H3_V35531`

- **Question Statement**: Saving Atlantis, you can see that there are always things that need to be saved. You resurface and look at the space shard you have present on the ship. You have no idea what the shards do, but all you can think of is the stabilising power that it holds. As you try to learn to navigate the ship, you read the clue that you gained while saving the sinking city. Nearing the coordinates present, all you can hear are some signals and slowly realize that it is a distress signal. Doing your best, it is your task to save the ship. Wrap the flag in actf{}.
- **Key**: `actf{7h3tr3a5ureaw4i7syou}`

## Metadata
- **Tags**: `Audio`, `Cryptography`
- **Author**: Asmita Guha
- **File**: `ZIP.zip`

## Solution Approach
- Trim the audio file after timestamp 00:01:05 to isolate the morse code section
- Use a morse code detector tool to decode the beeping signals
- Use the decoded output as input for a Vigenère cipher decoder
- Use the key "atlantis" (hint provided in the attached image) to decrypt
- Apply the decrypted result to get the flag
