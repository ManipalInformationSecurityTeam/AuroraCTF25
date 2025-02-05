## LEVEL 2 - QUESTION 1

Question Name: _5C0UT_

- **Question Statement**: Your broken ship catches a distorted signal emerging through the static. A voice fragmented and fraught with urgency. Bumblebee, bruised and struggling, transmits a cryptic message. "C0rup7I0n'5 gr1p s7r3ng7h3n5...". The transmission holds a secret, a riddle cloaked in desperation.

- **Key**: `actf{0nly_h3_c4n_s4v3_us}`

## Metadata
- **Tags**: `Reverse Engineering`, `Forensics`
- **Author**: [Atharva](https://github.com/atharva786738)
- **File**: `-... ..- -- -... .-.. . -... . .zip`

## Solution Approach
- search for "spectogram analyzer" (prefereably [academo](https://academo.org/demos/spectrum-analyzer/) or [dcode](https://www.dcode.fr/spectral-analysis))
- upload the audio file to the website
- uncheck the "logarithmic scale" option if turned on
- the freq range should be 0-20kHz on the website
- the audio waves form the hidden text and reveal the flag
