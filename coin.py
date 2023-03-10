from cryptography.hazmat.primitives.asymmetric.utils import decode_dss_signature
import coincurve

sk=coincurve.PrivateKey()
pk=sk.public_key
key=pk.format()
signature = sk.sign(key)
pk.verify(signature, key)
r,s=decode_dss_signature(signature)
sig=int.to_bytes(r,32,'big')+int.to_bytes(s,32,'big')

assert len(key)==33, "pubkey "+str(len(key))
assert len(sig)==64, "sig "+str(len(sig))
with open("key.bin", "wb") as f:
    f.write(key)
with open("test.bin", "wb") as f:
    f.write(sig)