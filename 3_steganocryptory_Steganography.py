from steganocryptopy.steganography import Steganography

Steganography.generate_key("")
secret = Steganography.encrypt("key.key", "img/3.png", "secret_message.txt")
secret.save("img/3_secret.png")

result = Steganography.decrypt("key.key", "img/3_secret.png")
print(result)
