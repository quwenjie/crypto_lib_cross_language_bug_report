import cryptography
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes

sk = ec.generate_private_key(ec.SECP256K1())
pk = sk.public_key()  
key = pk.public_bytes(
        encoding=serialization.Encoding.X962,
        format=serialization.PublicFormat.CompressedPoint,
    )

signature = sk.sign(key, ec.ECDSA(hashes.SHA256()))
pk.verify(signature,key,ec.ECDSA(hashes.SHA256()))

r,s=cryptography.hazmat.primitives.asymmetric.utils.decode_dss_signature(signature)
sig=int.to_bytes(r,32,'big')+int.to_bytes(s,32,'big')

assert len(key)==33, "pubkey "+str(len(key))
assert len(sig)==64, "sig "+str(len(sig))
with open("key.bin", "wb") as f:
    f.write(key)
with open("test.bin", "wb") as f:
    f.write(sig)