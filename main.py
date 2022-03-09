#QR code (encode-decode)

# module
import qrcode
from PIL import Image
from pyzbar.pyzbar import decode

# Function: QR code encoder
def QREncoder(text, path="qrcode/myqrcode.png", color='black'):
    qr = qrcode.QRCode(version=1, box_size=15, border=2)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color=color, back_color='white')
    img.save(path)

# encode youtube
QREncoder('www.youtube.com')



# Function: QR code decoder
def QRDecoder(path):
    img = Image.open(path)
    text = decode(img)
    print(text[0].data.decode("utf-8"))

# decode qrcode
QRDecoder("qrcode/myqrcode.png")