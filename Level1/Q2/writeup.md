# LEVEL 1 - QUESTION 2

## Question Name: `Atl4ntis_0f_S4ndS`

- **Question Statement**: After getting your thanks from Caeser for getting saved, he directs you to the location from where this robot might have emerged. He gives you a clue and departs from the place, leaving the corpse of the robot. Reading the clue, you realize that Brutus was wanting to save Atlantis of the Sands, present in the Arabian Peninsula. This Lost City of Ubar thrived along the Incense route, but was now being swallowed into the sand. You feel that you should go and investigate it. Therefore, you head towards the location to try and fix the sinking problem that is present at Atlantis.
- **Key**: `aCTF{r4153d_fr0m_54nd5_n0w_r4153_th3_t1t4n1c}`

## Metadata
- **Tags**: `Forensics`, `Cryptography`
- **Author**: Anoushka Ghosh
- **File**: `ZIP.zip`, which contains `q2img.png`

## Solution Approach
- The challenge provides a barcode image that needs to be scanned
- Scanning the barcode reveals a URL that leads to another image
- Examine the EXIF data of the second image
- The camera model field contains a base64 encoded string
- Decode the base64 string to obtain the flag
