from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import base64

# Given RSA public key
public_key_pem = """
-----BEGIN RSA PUBLIC KEY-----
MIGJAoGBAL4GJr/gTUCWUz8jHJ/KSR0VQXVxFzPgI0eOj/cKeoIBj2IlcJyL9JtU
6ulPbn+Xc7jyr0hblrFYOU3iukQtmZsgHWl9rMgmL9FG4/tSYSIIZcQ3hP/FMjwe
QDKCLPNdC0BM/BgsEMoP7Id3xYnLgWWSy5iJt3O4GLFMRH21DNGZAgMBAAE=
-----END RSA PUBLIC KEY-----
"""

# Given ciphertext
ciphertext_base64 = "boSqEOQtvMt/3CmXSR9NqReZmwXGya2BbeBOGh+vImyZKZcM2zgadeOfVRgcwMr04ggNX8FE6dD0P2FmP7+fePD0FIzn325XbMpopTzFp7mS05gPD0IBKhTcJhDbSuFFR4c1gbajnm4N1hqZhRwL+4apkBx+dBjIO37d+pxLfnI="

# Decode the base64 ciphertext
ciphertext = base64.b64decode(ciphertext_base64)

# Load RSA public key
public_key = serialization.load_pem_public_key(public_key_pem.encode(), backend=default_backend())

# Decrypt the ciphertext
plaintext = public_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Print the decrypted plaintext
print("Decrypted plaintext:")
print(plaintext.decode())
