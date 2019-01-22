import qrtools

qr = qrtools.QR()
qr.decode("CSQRCODE.png")
print(qr.data)