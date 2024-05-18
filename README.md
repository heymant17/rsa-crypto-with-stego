# RSA-cryptography-with-steganography

This project is a simple chat app that uses RSA to encrypt the message and LSB steganography to hide encrypted message in the image, encryption and steganography both are done in client side, for key sharing this project simply appends key along with encrypted message before hididng it in the image, and on the receiver side the key and encrypted message is extracted seperately to decrypt the message

NOTE: Donot use RSA to encrypt long messages, it is slow
