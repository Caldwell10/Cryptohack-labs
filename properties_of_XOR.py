from binascii import unhexlify
from pwn import xor

# Given values in hexadecimal
key1 = unhexlify("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
key2_xor_key1 = unhexlify("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
key2_xor_key3 = unhexlify("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
flag_xor_keys = unhexlify("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")

# Calculate KEY2 by XORing key1 with (key2 ^ key1)
key2 = xor(key1, key2_xor_key1)

# Calculate KEY3 by XORing key2 with (key2 ^ key3)
key3 = xor(key2, key2_xor_key3)

# Now XOR FLAG ^ KEY1 ^ KEY3 ^ KEY2 with the keys to isolate FLAG
flag = xor(flag_xor_keys, key1, key2, key3)

# Print the flag
print(flag.decode('utf-8'))
