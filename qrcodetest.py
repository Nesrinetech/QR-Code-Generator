import pyqrcode
from PIL import Image
link = input("enter the link to generated into qr code : ")
qr_code = pyqrcode.create(link)
qr_code.png("QRCode.png", scale=5)
Image.open("QRCode.png").show()




import pyqrcode
from PIL import Image
link = input("enter a link to generate a QR code : ")
qr_code = pyqrcode.create(link)
qr_code.png("QRCode.png", scale=5)
Image.open("QRCode.png").show()