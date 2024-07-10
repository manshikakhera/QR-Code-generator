import qrcode
from PIL import Image
qr = qrcode.QRCode(version = 1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size = 10 , border=4)
qr.add_data("https://www.carwale.com/used/rolls-royce-cars/#car=25&city=10&pc=10&sc=-1&so=-1&pn=1")
qr.make(fit=True)
img = qr.make_image(fill_color = "blue",back_color = "white")
img.save("rolls.png")
