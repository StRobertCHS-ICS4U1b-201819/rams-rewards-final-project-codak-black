from pyzbar.pyzbar import decode
from PIL import Image
qr = decode(Image.open("CSQRCODE.png"))
print(qr)