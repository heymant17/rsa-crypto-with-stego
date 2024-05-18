
import random
bits = 512
def miller_rabin(n, k):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    r = 0
    s = n-1
    while s % 2 == 0:
        r = r+1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n-1)
        x = pow(a, s, n)
        if x == 1 or x == n-1:
            continue 
        else:
            return False
    return True


def random_odd_number(bits):
    n = random.randint(2 ** (bits-1), 2 ** bits - 1)
    if n % 2 == 0:
        n = n + 1
    return n


def probable_prime_number(bits):
    n = random_odd_number(bits)
    while miller_rabin(n, 40) == False:
        n = n + 2
    return n

def generate_publickey():
    for i in range(2):
        n = probable_prime_number(bits)
        if i == 0:
            p = n  
        else:
            q = n
    n = p*q
    phi = (p-1)*(q-1)
    e = random.randint(2, phi)
    while miller_rabin(e, 40) != True:
        e = e + 1
    return e,n,phi
     
#Extended Euclidean to calculate private key.
def generate_privatekey(phi,e): 
    ao = 1
    bo = 0
    do = phi
    a1 = 0
    b1 = 1
    d1 = e
    k1 = int(do/d1)
    while d1 != 1:
        a = ao - (a1*k1)
        b = bo - (b1*k1)
        d = do - (d1*k1)
        ao = a1
        a1 = a
        bo = b1
        b1 = b
        do = d1
        d1 = d
        k = int(do/d)
        k1 = k
   
    if b < 0:
        b = b + phi
       
    if b > phi:
        b = b % phi

    return b

def encrypt(message,e,n):
    encrypted_list = []
    for msg in message:
        integer_msg =ord(msg)
        encryption =pow(integer_msg,e,n)
        encrypted_list.append(encryption)
    return encrypted_list

def decrypt(en,d,n):
    en = [int(x) for x in en.split(',')]
    decrypted_message = ""
    for y in en:
        decryption = pow(int(y),d,n)
        decrypted_message += chr(decryption)
    return decrypted_message

