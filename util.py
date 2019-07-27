import qrcode
import random
from Crypto.Cipher import AES

def showQR(data, version=10):
    code = qrcode.QRCode(
        version=version,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    code.add_data(data)
    print(data)
    code.make(fit=True)

    img = code.make_image(fill_color="black", back_color="white")
    img.show()

AES_IV = [70, 69, 68, 67, 66, 65, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48]
def encrypt(src, desc, key):
    cryptor = AES.new(key, AES.MODE_CBC, bytes(AES_IV))
    with open(src, 'rb') as fin:
        with open(desc, 'wb') as fout:
            data = fin.read()
            data += bytes([0] * (16 - len(data)%16 if len(data) % 16 != 0 else 0))
            fout.write(cryptor.encrypt(data))


def decrypt(src, desc, key):
    cryptor = AES.new(key, AES.MODE_CBC, bytes(AES_IV))
    with open(src, 'rb') as fin:
        with open(desc, 'wb') as fout:
            data = fin.read()
            fout.write(cryptor.decrypt(data))
