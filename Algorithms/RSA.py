def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def extend_gcd(a, b):
    if b == 0:
        x = 1
        y = 0
        return x, y
    else:
        x1, y1 = extend_gcd(b, a % b)
        x = y1
        y = x1 - int(a / b) * y1
        return x, y


def fast_mul(a, b, n):
    res = 1
    while b != 0:
        if b % 2 == 0:
            b = b / 2
            a = (a * a) % n
        elif b % 2 != 0:
            b = b - 1
            res = (res * a) % n
    return res


def generate_key(p, q):
    n = p * q
    fn = (p - 1) * (q - 1)
    e = 65537  # Number 4 of Fermat
    x, y = extend_gcd(e, fn)
    if x < 0:
        x = x + fn
    d = x
    return (n, e), (n, d)


def encrypt(m, public_key):
    n = public_key[0]
    e = public_key[1]
    return fast_mul(m, e, n)


def decrypt(c, private_key):
    n = private_key[0]
    d = private_key[1]
    return fast_mul(c, d, n)


p = 761
q = 1019
publicKey, privateKey = generate_key(p, q)
message = 1234
print("Unencrypted text:% s" % message)
encrypted_message = encrypt(message, publicKey)
print("Encrypted text:% s" % encrypted_message)
unencrypted_message = decrypt(encrypted_message, privateKey)
print("Unencrypted text after unencrypted:% s" % unencrypted_message)
