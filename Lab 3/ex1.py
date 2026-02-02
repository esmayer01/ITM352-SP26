from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

encoded_text = cipher_suite.encrypt(b"This is a really secret message.")
print(f"Encoded text: {encoded_text}")

# Use cryptography library to encode and decode a message
decoded_text = cipher_suite.decrypt(encoded_text)
print(f"Decoded text: {decoded_text.decode('utf-8')}")

from cryptography.fernet import Fernet

# Generate an encryption key and create a Fernet object
key = Fernet.generate_key()
cipher = Fernet(key)

# Get user input
user_message = input("Enter a message to encrypt: ")

# Encode the string into bytes
encoded_message = user_message.encode("utf-8")

# Encrypt the message
encrypted_message = cipher.encrypt(encoded_message)
print(f"Encrypted message: {encrypted_message}")

# Decrypt the message
decrypted_message = cipher.decrypt(encrypted_message)

# Decode bytes back into a string
decoded_message = decrypted_message.decode("utf-8")
print(f"Decrypted message: {decoded_message}")
