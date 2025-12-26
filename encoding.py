import base64

# my_txt = "Hello, World!"

# my_bytes = my_txt.encode('ascii')
# encoded = base64.b64encode(my_bytes)
# encoded_str = encoded.decode('ascii')
# decode_str = base64.b64decode(encoded_str)

# print(my_txt)
# print(my_bytes)
# print(encoded)
# print(encoded_str)
# print(decode_str)

with open('image.png',"rb") as f:
    data = f.read()

encoded_data = base64.b64encode(data)

decoded_data = base64.b64decode(encoded_data)
# print(decoded_data)

with open('image2.png', "wb") as f:
    f.write(decoded_data)