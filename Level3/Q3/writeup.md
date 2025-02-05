## Level 3 - Question 3

Question Name: `gr1m4c3_sh4k3`

- **Question Statement**: The Legion makes its stance clear: Leave Cultus to their dominion or face annihilation. Their decree is final. Land, and you die. A surge of defiance courses through your veins. You decide to infiltrate Cultus despite the warning, but the planet's terrain is an unrelenting labyrinth of instability. Jagged cliffs and fissures erupt beneath your feet, and the relentless pursuit by Astral Toilet Special Forces tests your endurance to its limits. Desperation mounts as you search for refuge—a place to regroup, someone to trust. Clinging to hope, you replay the message from The Variable, only to find that its contents have shifted, twisting into something altogether unexpected.
- **Key**: `actf{c4nt_f0rg3t_th3_v3t3r4n_to1l3t5}`

## Metadata
- **Tags**: `Forensics`, `Cryptography`
- **Author**: [Ayan](https://github.com/nayanko)
- **Files**: `ZIP.zip`

## Solution Approach
- Player receives two images: an XOR'd image of Andrew Tate and a QR code
- QR code contains a link to the original Andrew Tate image
- Use steghide with passphrase "Top G" to extract hidden data from the Andrew Tate image
- Reverse the XOR operation to reveal a second QR code
- New QR code leads to a Reddit post containing a website link
- Website contains approximately 30 images and 10 videos
- Locate the G-Toilet version 3.0 image (character from Skibidi lore)
- Download and use steghide with no passphrase to extract the flag
- Note: The version number (3.0) references the three years since Andrew Tate's "Top G" association
