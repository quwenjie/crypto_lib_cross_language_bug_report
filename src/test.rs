use secp256k1::PublicKey;
use secp256k1::Secp256k1;
use sha2::Sha256;
use sha2::Digest;
use secp256k1::ecdsa::Signature;

use std::fs::File;
use std::io::Read;
fn main() {
    //&[u8]
    let inputfile="key.bin";
	let mut _inputfile = File::open(inputfile).unwrap();;
	let mut buffer:[u8;33]=[0;33];
	let len = _inputfile.read(&mut buffer).unwrap();
    

    let inputfile2="test.bin";
	let mut _inputfile2 = File::open(inputfile2).unwrap();;
	let mut buffer2:[u8;64]=[0;64];
	let len2 = _inputfile2.read(&mut buffer2).unwrap();

    let user_consent_signature = Signature::from_compact(&buffer2).unwrap();
    let user_public_key: PublicKey = PublicKey::from_slice(&buffer).unwrap();
    let verify_consent_signature =
        secp256k1::Message::from_slice(&Sha256::digest(&buffer)).unwrap();
    let secp = Secp256k1::new();
    secp.verify_ecdsa(
        &verify_consent_signature,
        &user_consent_signature,
        &user_public_key,
    ).unwrap(); //{
    //    Ok(_) => Ok(user_consent.clone().public_key),
    //    Err(e) => e
    //}
    
}
