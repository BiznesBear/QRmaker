import qrcode

x = input("QR>>> ")

img = qrcode.make(x)
c = input("QR name: ")
img.save(c + ".png")
