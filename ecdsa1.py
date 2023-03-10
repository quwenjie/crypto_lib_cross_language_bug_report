import ecdsa
import hashlib

sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
pk = sk.get_verifying_key()
key = pk.to_string("compressed")
sig = sk.sign(key, hashfunc=hashlib.sha256)
pk.verify(sig, key, hashlib.sha256)

assert len(key)==33, "pubkey "+str(len(key))
assert len(sig)==64, "sig "+str(len(sig))

with open("key.bin", "wb") as f:
    f.write(key)
with open("test.bin", "wb") as f:
    f.write(sig)
