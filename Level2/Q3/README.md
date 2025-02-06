## LEVEL 2 - QUESTION 3

Question Name: _FR4GM3NT5_

- **Question Statement**:  Within Optimus's shattered memories, fleeting glimpses of a glorious past emerge. Iacon, The Hall of Records, and the legacy of the original ***PRIMES***, those who led before him, hold the key to mending his fractured mind. Each Prime’s story, etched in the fabric of time, is a puzzle piece waiting to be rediscovered. You must rekindle Optimus's memory, unlocking ancient wisdom, to thwart the malevolent force and restore him to his true self.
- **Key**: `actf{L3g3nd_0f_0pt1mu5}`

## Metadata
- **Tags**: `Reverse Engineering`
- **Author**:  [Arnav](https://github.com/ArnDev7), [Atharva](https://github.com/atharva786738)
- **File**: `t3m3n05.zip`

## Solution Approach
- Solving Approach: The `encoded` array holds the flag in an encoded format. The `flag` array provides a clue by containing 13 elements. The 13th element is **13**, the number of PRIMES(Story clue) were 13, and this is the key to decoding the flag. Solvers must figure out that the values in the `encoded` array need to be **XOR'd with 13** in order to decode the flag.

    1. **Convert JAR to Java:**
    - First, convert the `t3m3n05.jar` file to a `.java` file. You can use online tools like [JD-GUI](http://jd.benow.ca/) or any suitable decompiler to extract the Java code from the JAR file.

    2. **Open the Java File:**
    - Open the extracted `.java` file in a text editor.
    - Look at the **13th line**, which contains a **hint** in the form of a **commented-out code**. This will guide you toward solving the challenge.

    3. **Understand the Arrays:**
    - In the code, you will see two arrays: `encoded` and `flag`.
    - The `encoded` array holds the encoded flag.
    - The `flag` array contains **13 elements**. The last element (13th) is **13**, which serves as the XOR key.

    4. **Decoding the Flag:**
    - To decode the flag, you need to XOR each element in the `encoded` array with the number `13`. This operation will decode the flag.

    5. **Use an Online XOR Decoder:**
    - You can use online XOR decoders to perform this operation.
    - Alternatively, you can use the following **Python script** to decode the flag.

### Python Code to Decode the Flag:
```python
    # Python code to XOR the encoded array with 13 to decode the flag

    encoded = [your_encoded_values_here]  # Replace with the actual encoded values
    key = 13
    decoded_flag = ''.join([chr(byte ^ key) for byte in encoded])

    print("Decoded Flag:", decoded_flag)
