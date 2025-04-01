
import os
from os.path import join, dirname

import binascii, bcrypt
from hashlib import md5
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


# if not os.environ.get('password'):
key = md5("password".encode('utf-8')).hexdigest()
# else: key = os.environ.get('password')

cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)

def encrypt(pl_text):
    # return pl_text

    return \
    binascii.hexlify(
        cipher.encrypt(
            pad(
                str(
                    str(int(type(pl_text) is str)) + \
                    str(pl_text)
                    ).encode('utf-8'), 
                AES.block_size
                )
            )
        ).decode('utf-8')

def decrypt(cp_text):
    # return cp_text
    
    pl_text = \
    unpad(
        cipher.decrypt(
            binascii.unhexlify(cp_text.encode('utf-8'))
            ),
        AES.block_size
        ).decode('utf-8')
    return int(pl_text[1:]) if (int(pl_text[0])==0) else pl_text[1:]


def fast_hash(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def check(password, hpassword):
    if bcrypt.checkpw(password.encode(), hpassword): 
        return True
    return False

if __name__ == "__main__":
    print(type(decrypt("1f1c83d8fdc8f22ce0b5a40cad34b23a")))