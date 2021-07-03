import hashlib

message = str(input("Enter string for change into the hash:"))

md_5 = hashlib.md5(message.encode()).hexdigest()

sha_256 = hashlib.sha256(message.encode()).hexdigest()

sha_512 = hashlib.sha512(message.encode()).hexdigest()


print("\n The MD5 hash of given string : " + md_5)

print("\n #-------------------------------------------------------------------------#")

print("\n The SHA256 hash of given string : " + sha_256)

print("\n #-------------------------------------------------------------------------#")

print("\n The SHA512 hash of given string : " + sha_512)
