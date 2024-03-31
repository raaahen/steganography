from stegano import exifHeader

secret = exifHeader.hide("img/2.jpg", "img/2_secret.jpg",
                         "Жду тебя в 7, за 2 столиком. Возьми деньги под матрасом")

result = exifHeader.reveal("img/2_secret.jpg")
result = result.decode()
print(result)
