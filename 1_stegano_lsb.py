from stegano import lsb
secret = lsb.hide("img/1.png", "secret message")
secret.save("img/1_secret.png")

result = lsb.reveal("img/1_secret.png")
print(result)
