found_string = '62 68 7f 6d 70 61 7e 78 7f 54 64 65 6e 54 68 6a 6e 78 6a 79 54 64 6d 54 66 6a 65 72 54 7f 64 54 68 64 66 6e 54 42 54 63 64 7b 6e 76'

flag = ""

found_string = found_string.split(" ")

for char in found_string:
	char = bytearray.fromhex(char).decode()
	flag += chr(ord(char) ^ 11)

print(flag)