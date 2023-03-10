import secp256k1
privkey = secp256k1.PrivateKey()
pubkey=privkey.pubkey
key=pubkey.serialize()
signature=privkey.ecdsa_sign(key)
ecds=secp256k1.ECDSA()
sig=ecds.ecdsa_serialize_compact(signature)

assert len(key)==33, "pubkey "+str(len(key))
assert len(sig)==64, "sig "+str(len(sig))

with open("key.bin", "wb") as f:
    f.write(key)
with open("test.bin", "wb") as f:
    f.write(sig)