import pyqrcode

q = pyqrcode.create('RAMs')
q.png('RAMs_Rewards.png', scale=7)
print('QR Code generated...')
