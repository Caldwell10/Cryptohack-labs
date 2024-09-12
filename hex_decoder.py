import base64

#given the hex string
hex_string="72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

#decoding the hex string into bytes then into a readable string
flag_bytes=bytes.fromhex(hex_string)

#encoding the bytes into base64 for readability
flag_base64=base64.b64encode(flag_bytes)

#decode the base64 into a readable string
flag=flag_base64.decode('ascii')

#display resulting flag
print(flag)