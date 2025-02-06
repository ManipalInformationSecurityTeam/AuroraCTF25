## LEVEL 2 - QUESTION R3B1R7H

**Question Name**: R3B1R7H

- **Question Statement**: The Matrix of Leadership, disintegrates into spectral dust right before you. Yet, its essence lingers, whispering the will of PRIMUS. "To reclaim it, worth must be demonstrated, a trial of unparalleled complexity unveiled."
A labyrinth of cryptic ingenuity emerges, demanding acuity and perseverance to traverse its veiled intricacies. Each cipher unraveled edges closer to a rekindled destiny. Only through triumph over this shall the Matrix's brilliance be forged anew, igniting the spark of ReSurgAnce.

- **Key**: `actf{Pr1m3_Rul35_1n_M1nd_4nd_3ff0rt99}`

## Metadata
- **Tags**: `Cryptography`
- **Author**: [Arnav Tiwari](https://github.com/ArnDev7)
- **File**: `ciphertron.zip`

## Solution Approach
1. **Extract the Public Key and Ciphertext**
   - Public exponent `e` (`PRIME_DIRECTIVE`) = `0x10001`
   - Locate modulus (`n`) and ciphertext (`c`) in provided text file
   - Note: Two letters (`d7`) from ciphertext are hidden within file

2. **Format Hexadecimal Values**
   - Add `0x` prefix to `n` and `c` values
   - Prepare values for RSA decryption

3. **RSA Decryption**
   - Use RSA decryption tool/script with `n`, `e`, `c` values
   - Implement private key calculator for custom values

4. **Retrieve Flag**
   Example Python implementation:
   ```python
   from Crypto.Util.number import long_to_bytes

   n = int("<value_of_n>", 16)  # Replace with hex n value
   e = 0x10001  # Public exponent
   c = int("<value_of_c>", 16)  # Replace with hex c value

   # If private key d is known:
   d = <value_of_private_key>

   # Decrypt ciphertext
   plaintext = long_to_bytes(pow(c, d, n))
   print("Decrypted Flag:", plaintext.decode())
   ```

5. **Flag Verification**
   - Decrypted output format: `actf{Pr1m3_Rul35_1n_M1nd_4nd_3ff0rt99}`
