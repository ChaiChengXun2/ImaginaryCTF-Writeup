import base64

challenge = "AAAAABIFGFIOPBJWGw4VEjYFRBQ2FxwDNhRFCEg8VTlIPFU5SDxVOUg8VTlIPFU5SDxVGw=="
xor_key = "ictf"

xor_key = xor_key * (len(challenge) // len(xor_key)) + xor_key[:len(challenge) % len(xor_key)]
decoded_challenge = base64.b64decode(challenge)

flag = ""

for i in range(len(decoded_challenge)):
	flag += chr(decoded_challenge[i] ^ ord(xor_key[i]))

print(flag)