## LEVEL 1 - QUESTION 4

Question Name: `ED1TH_HON3_D3N`

- **Question Statement**: After saving the ship, you are given new coordinates by one of the survivors, stating that one of their treasury coffers is present there. While it is of no use to you, you decide to visit the area, with the optimistic spirit that there may be something that can lead you to get somewhere else?
- **Key**: `actf{run_7o_4re4_51}`

## Metadata
- **Tags**: `Cryptography`, `Forensics`
- **Author**: Asmita Guha
- **File**: `ZIP.zip`

## Solution Approach
- Download the Papyrus scroll pdf
- The scroll has information about Egyptian Gods, notice the heading of the file (the question name)
- The heading is an anagram of "The Hidden One"
- The Hidden One is another name for Amun, the God. Go to the section dedicated to Amun
- There is a picture of Amun in the section
- A QR code is hidden/camouflaged in the picture
- Scan the QR code to get a message in hieroglyphics
- Put it in an online decoder to get the message "The mummy has awakened!" + flag
