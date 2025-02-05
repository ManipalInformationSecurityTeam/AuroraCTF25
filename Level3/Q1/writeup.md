## LEVEL 3 - QUESTION 1

Question Name: `L4ngu4g3_b4rri3r`

- **Question Statement**: The traveler discovers that an old friend is stranded in Cultus, a world besieged by the Legion of Astral Toilets. Finding this friend is of the utmost importance—a task shrouded in peril and urgency.

As you enter the chaotic airspace of Cultus, a sudden alert jolts your console. A message arrives—but it is not from the Legion. Something else, lurking in the void, has reached you first. The message is encrypted, its code a swirling anomaly of characters that defy logical patterns. It seems to mock your attempts at decryption with its bizarre complexity. What could it mean?

https://youtu.be/eECbTe9-tBU

- **Key**: `actf{4_tru3_s1gma_never_5top5_m0gg1ng}`

## Metadata
- **Tags**: `OSINT`, `Cryptography`
- **Author**: [TheVariable](https://github.com/variablethe)
- **File**: None (Web Challenge)

## Solution Approach
1. Watch provided YouTube video with "sigma boi" music background
2. Follow link in video description to original song
3. Use hadzy.com to find TheVariable's comment pointing to their Threads account
4. Locate ciphertext file on Threads profile
5. Use Vigenere cipher with romanized "sigma boi" lyrics as key
6. Starting with the complete lyrics from top to bottom as the key, the decryption is not successful. We need to selectively remove portions:

   - First remove "[Intro: Betsy & Maria Yankovskaya]", which reveals some text
   - Remove "[Chorus: Betsy, Maria Yankovskaya, Both]" and "[Verse: Betsy & Maria Yankovskaya]"

   At this point, you should see:

   ![Screenshot 2025-02-04 231420](https://github.com/user-attachments/assets/022ad999-8d80-4adc-bc24-03115aecb020)

   - Attempting to remove "(Betsy, Betsy, Betsy, Betsy)" re-encrypts text, indicating it's part of the key
   - Similarly, removing "(Iu)(Aga)(Davay)" re-encrypts text, so keep these
   - The first 2 lines of repeating text are also required, as removing them encrypts text again
   - Remove remaining redundant lines one by one
   - Finally remove "[Chorus: Betsy & Maria Yankovskaya, Maria Yankovskaya, Betsy]"

7. Use the resulting refined lyrics as the decryption key
