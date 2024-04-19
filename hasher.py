# Hashing password using passlib

def hash(password):
    from passlib.hash import sha256_crypt
    # hash the password using sha256_crypt with 5000 rounds and a random salt
    hashed = sha256_crypt.using(rounds=5000).hash(password)

    # verify the hashed password against the plain password
    if (sha256_crypt.verify(password, hashed)):
        return hashed
def verify(password, hash):
    from passlib.hash import sha256_crypt
    # verify the hashed password against the plain password
    if (sha256_crypt.verify(password, hash)):
        return True
    else:
        return False
if __name__ == "__main__":
    print(hash("password"))
    print(verify("password", "$5$qG4UNBb2uM1NWhFE$/Nr0T8MSV.Wpg/ftCPTETI3GiL2kdL2IBvc5FB0a002"))