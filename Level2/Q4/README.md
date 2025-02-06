## LEVEL 2 - QUESTION 4

Question Name: _G1A5535_

- **Question Statement**: The legacy unveils a powerful relic—the Matrix of Leadership, a symbol of authority and wisdom. Its location, once concealed, was accidentally revealed by Megatron, etched into the eyes of Archibald Witwicky, an Arctic explorer. You must infiltrate the system, manipulate the right pathways, and extract the coordinates to the Matrix before the Decepticons destroy it.
- **Key**: `actf{02_26_15.7_n_125_03_06.2_3}`

## Metadata
- **Tags**: `Web Exploitation`
- **Author**: [Arnav Tiwari](https://github.com/ArnDev7)
- **File**: Web instance of `./Flask/` folder

## Solution Approach
- Open the webpage, locate the "Buy it now" button, and click it 30 times
- Enter revealed bidder name and bid amount (30500) into form fields
- Access browser dev tools, modify `is_admin` cookie to `true`
- Navigate to `/admin` endpoint to reveal flag
