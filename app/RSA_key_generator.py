"""
RSA_key_generator.py
====================================
The file includes methods for generate public key and private key.
"""

import random

max_NumLen = 100000000000000
"""
:param max_NumLen: [int] length keys
"""

def gcd(a, b):
    """
    The method of finding the greatest common divisor of two numbers based on the remainder of the division.
    
    :param num: [int] number for checking
    :return: [int] a
    """

    while b != 0:
        a, b = b, a % b
    return a
    
def egcd(a, b):
    """
    The method of finding the greatest common divisor of two numbers based on the Euclidean algorithm.
    
    :param num: [int] number for checking
    :return: [int] a
    """
    
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def is_prime(num):
    """
    The method for checking if a number is prime.
    
    :param num: [int] number for checking
    :return: boolean
    """
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

def RandomPrim():
    """
    The method for generate random prime number.

    :return: [int] ranPrime
    """
    while(1):
        ranPrime = random.randint(0,max_NumLen)
        if is_prime(ranPrime):
            return ranPrime

def generate_keys_RSA():
    """
    The method for generate keys.

    :return: [list] public_key, [list] private_key
    """
    p = RandomPrim()
    q = RandomPrim()
    
    n = p*q
    phi = (p-1) * (q-1) 

    e = random.randint(1, phi)
    g = gcd(e,phi)
    while g != 1:
        e = random.randint(1, phi)
        g = gcd(e, phi)
    d = egcd(e, phi)[1]
    
    d = d % phi
    if(d < 0):
        d += phi
    public_key = (hex(e),hex(n))
    private_key = (hex(d),hex(n))
    
    return (public_key, private_key)