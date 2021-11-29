import pyqrcode

text = input("Enter your text/url to generate QR code :")

url = pyqrcode.create(text)

url.svg("myqr.svg", scale=8)
url.png("myqr.png", scale=6)
