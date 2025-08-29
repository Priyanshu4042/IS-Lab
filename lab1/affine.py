from pycipher import Affine

cipher = "XPALASXYFGFUKPXUSOGEUTKCDGEXANMGNVS"
a, b = 5, 6
plain = Affine(a,b).decipher(cipher)
print("Decrypted:", plain)
