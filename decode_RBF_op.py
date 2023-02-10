from btcpy.structs import script;


compiled = script.Script.compile('OP_DUP OP_HASH160 a33ce8cf2760e2f9ef384bcbbe9a5491759feb14 OP_EQUALVERIFY OP_CHECKSIG')
print(compiled)

hexdata='512012419b705d41f0e447b4058975a4138121549143f024a53e467f97c2b3b62c70'

byarr=bytearray.fromhex(hexdata)

print(byarr)


script1=script.Script(byarr)


print(script1.decompile())

