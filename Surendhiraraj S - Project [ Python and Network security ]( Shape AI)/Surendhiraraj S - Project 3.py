import hashlib

dk=hashlib.pbkdf2_hmac('sha256',b'Marshmello',b'salt',5)

print("\n  The final output hash of given is: " + dk.hex())

