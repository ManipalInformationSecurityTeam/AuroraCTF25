## LEVEL 2 - QUESTION 5

Question Name: _F0R717UD3_

- **Question Statement**: Question Statement: The Matrix, now within reach, is veiled by a maze of cryptic enigmas and riddles.With their vast knowledge, the ancient primes carefully concealed the relic itself, draping it in intricate layers of mystery designed to mislead. To claim it, you must navigate this web of deception, unraveling each hidden layer with skill and insight. Only those with unmatched intellect and determination can pierce through the concealments and seize the Matrix's power, restoring Optimus Prime to his true form. Will you be the one to unlock its elusive secret?
- **Key**: `actf{m4rk_0f_134d3r_4n_3p170m3_0f_w15d0m}`

## Metadata
- **Tags**: `Forensics`
- **Author**: [Atharva](https://github.com/atharva786738)
- **File**: Limited by size. Kindly refer to solution for approach.

## Solution Approach
**WARNING** : the question file is above 450MB in size

   - Step 1: Check file type using the command `file m47r1x`. This will show that the file is a mp4 video file, append the correct extension.

   - Step 2: Unzip the video file using `unzip m47r1x.mp4`, or use binwalk
    this give the hidden zip files (14 in number)
       unzip them also using unzip command

   - Step 3: Fix permissions issues (if any)
        if facing any issue like "user has no permission" or "permission denied" use chmod a+r, a+w and a+x commands

   - Step 4: Search for metadata
        the ``Keywords`` section in the meta data of the extracted pdf files has been appended

   - Step 5: Identify the format of the encoded base64 strings
         identify the format of the appended base64 string (starts which ivBOR means base64 to png) and decode them by using any linux command or online tool

   - Step 6: the decoded base64 strings are basically qrcodes
        scan them to get 14 different flags (one from each)
            - Step 7: the flags are
        ```bash
            alpha_trion:        1actf{f0r_1_w1th1n_u5_15_4_c0d3_0f_l3g4cy}m
            alchemist_prime:    2actf{tru7h_15_my_l0d3st0n3}4
            amalgamous_prime:   3actf{ch4ng3_15_l1f3}r
            liege_maximo:       4actf{d1v1d3_4nd_c0nqu3r_15_my_w4y}k
            megatronus_prime:   5actf{p0w3r_15_4_d0ubl3-3dg3d_sw0rd}_
            micronus_prime:     6actf{sm4ll_d33ds_c4n_ch4ng3_futur3}0
            nexus_prime:        7actf{un1ty_15_4_str3ngth}f
            onyx_prime:         8actf{n4tur3_15_4_gr34t_t34ch3r}_
            prima_prime:        9actf{l1ght_15_my_guid3}1
            quintus_prime:      10actf{cr34t10n_15_4_b1ss1ng}3
            solus_prime:        11actf{1nf1n1t3_craft3d_4rt}4
            vector_prime:       12actf{t1m3_fl0ws_l1k3_4_r1v3r}d
            zeta_prime:         13actf{1_4m_th3_f1rst_w13ld3r}3
            optimus_prime:      14actf{t1ll_4ll_4r3_0n3}r

        ```

   - Step 8: the start of every flag has a number which corresponds to the order of the letter at the end of each flag (outside the {} brackets)

        ```bash
        1->m
        2->4
        3->r
        4->k
        5->_
        6->0
        7->f
        8->_
        9->1
        10->3
        11->4
        12->d
        13->3
        14->r
        combined-> m4rk_0f_134d3r

    this is the first part of the original flag which will be the answer

   - Step 8: going through the original file given, whcih is a video file, when you start from **14:25 timestamp**, you will find a **small qrcode** on a sheet of paper for half a second. that is our ***second part of the flag***
     it says ```4n_3p170m3_0f_w15d0m}```

   - Step 9: on combining both you get the complete flag
       - actf{m4rk_0f_134d3r_4n_3p170m3_0f_w15d0m}
