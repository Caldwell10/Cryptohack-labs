from Crypto.Util.number import long_to_bytes

#define the integer
large_integer=11515195063862318899931685488813747395775516287289682636499965282714637259206269

#convert integer into bytes
message_bytes=long_to_bytes(large_integer)

#decode the bytes into a readable file
message_bytes=message_bytes.decode('utf-8')

#display message
print(message_bytes)
