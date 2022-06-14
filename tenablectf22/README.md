# Macro Economics

We take the [VBA script](https://github.com/OmskHackers/writeups/blob/main/tenablectf22/script.vba) out of Exlel. The script takes the phrases from secret.txt in C://docs and makes GET requests to the web server with hex strings from these phrases and gets the key for XOR encryption.

![image info](https://github.com/OmskHackers/writeups/raw/main/tenablectf22/Screenshot%20from%202022-06-15%2003-53-07.png)

Xor function

![image info](https://github.com/OmskHackers/writeups/raw/main/tenablectf22/cipher.png)
From traffic dump we understand where key and ciphertext are located.
![image info](https://github.com/OmskHackers/writeups/raw/main/tenablectf22/dump.png)


We write a simple [script](https://github.com/OmskHackers/writeups/blob/main/tenablectf22/macro_economics_xor.py) to decrypt the data transmitted.

> flag{d0nt_3nable_macr0s}

