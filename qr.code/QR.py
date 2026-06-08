import qrcode

data = input (" Enter Text Or Link : ")

img = qrcode.make(data)

img.save("QR_Code.png") 

img.show()

print (" QR Code Generated Successfully ")
