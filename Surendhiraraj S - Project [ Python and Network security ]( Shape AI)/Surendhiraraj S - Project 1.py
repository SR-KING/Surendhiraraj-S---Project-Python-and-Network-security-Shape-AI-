import hashlib

print("Convert the given string into MD5 Hash \n ")

userInput = str(input("Enter your string for change into hashes:"))

Output = hashlib.md5(userInput.encode())

print("\n #-----------------------------------------------------------------#")

print("\n The hash values of your string: " + Output.hexdigest())

print("\n #-----------------------------------------------------------------#")
