## LEVEL 2 - QUESTION 2

Question Name: _N3UR41_

- **Question Statement**: Their beacon of hope, now on the brink of destruction, his n3ur4l m47r1x destabilized and vulnerable. The transformation into a harbinger of doom is imminent. Restoring the cognitive pathways and **recalibrating** his n3ur4l c0r3 is the only way. Amidst the shattered memories, a faint but familiar name echoes: ...Orion Pax...

- **Key**: `actf{m3m0l13s_b3f0f3_fr4gm3ents_c0ll1d3_in_pr1m3}`

## Metadata
- **Tags**: `Forensics`
- **Author**: [Arnav](https://github.com/ArnDev7), [Atharva](https://github.com/atharva786738)
- **File**: `raqvan.zip`

## Solution Approach
- The file is named **"raqvan"**, which is **ROT13** for "endian".
- On execution, the program outputs:


        S*y$t3m... f4111ng... Pr0c3ss disrupt3d.
        Fr@gm3nt: Input <L1ttl3m1nd v3rs10n>.
        F!xx3d m1nd -- EnT3r l1ttl3m1nd!

-Enter the little endian of the word **"Orion Pax"** (`786150206E6F69724F`)
- **If the answer is correct**, the program continues; otherwise, it **terminates and displays:**.
    ```c
        Pr1mU5: UncH@in3D... C0rRupted... D3l3t3d...
        R3b00t f@1l3d...
        Y0u h@v3 f@iled!

- After the correct little endian input, the program outputs:
    ```c
        l1ttl3m1nd cal1br@t3d.
        C0rrupt! Bigm1nd r3qu1r3d!
        ```
-Enter the big endian of the word **"Orion Pax"** (`4F72696F6E20506178`)

-If the big endian answer is incorrect, the program **terminates**; if correct, it reveals the **flag**.


        Bigm1nd c4l1br@t3d. f0rM4771nG M3m0R|\!....
        Flag: m3m0l13s_b3f0f3_fr4gm3ents_c0ll1d3_in_pr1m3
