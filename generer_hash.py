import hashlib

password = "veronique"
sha3hash = hashlib.sha3_512(password.encode('utf-8')).hexdigest()

print(f"Le hash SHA-3-256 pour le mot de passe '{password}' est : {sha3hash}")