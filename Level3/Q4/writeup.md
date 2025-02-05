## Level 3 - Question 4

Question Name: `L0cked_t0il3t`

- **Question Statement**: Through a stroke of audacious cunning, you gain the aid of a once-revered veteran of the Legion: the enigmatic G-Toilet. With their begrudging assistance, you uncover the location of the Legion's current monarch, a figure draped in infamy—the inheritor of the accursed title of The Skibidi Toilet.

Navigating a web of deception, you finally arrive at the coordinates provided by G-Toilet. However, instead of an imposing throne or a fortress, you find yourself standing before the male washroom??? A surreal, almost insulting sight given the gravity of your quest. The door is locked, and its encryption is maddeningly intricate. You've encountered nothing like it before—ever-shifting keys, endless iterations, and a requirement to enter a pair of passwords a thousand times. Seems a bit... Bizzare??

"Erm what da sigma?" you mutter, teetering on the edge of exasperation. "What kind of sigma-level rizzler thought this was a good idea?"

- **Key**: `actf{th3_sk1b1d1_l0rd_a5k5_4_f4num_t4x}`

## Metadata
- **Tags**: `Binary Exploitation`, `Cryptography`
- **Author**: [Ayan](https://github.com/nayanko)
- **File**: (Binary interaction over network with a chal3.c or chal3-fixed.c binary)

## Solution Approach
- Challenge requires entering 1000 correct plaintext-ciphertext pairs
- Initial key pair is "skibidi = rizzler"
- Key increments by 1 after each correct answer
- Key array alternates between "skibidi" (on even numbers) and "alpha" (on multiples of 100)
- Any incorrect answer resets progress to beginning
- Need to write script to automate responses for 1000 successful iterations

## NOTE
- While the question was originally released with chal3.c, chal3-fixed.c was the intended question, as it performs input validation.
