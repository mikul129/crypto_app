"""
RSA.py
====================================
The file includes methods for encoding and decoding messages.
"""

def encode_RSA(text,public_key):
    """
    Method for encode message.
  
    :param text: [str] original text for encode
    :param public_key: [list] public_key for encode message
    :return: encode_text
    """
    
    key,n = int(public_key[0],16),int(public_key[1],16)
    encode_text = [hex(pow(ord(char),key,n)) for char in text]
    return encode_text

def decode_RSA(encode_text, private_key):
    """
    Method for decode message.
  
    :param encode_text: [list] encode text for decode
    :param private_key: [list] private_key for decode message
    :return: decode_text
    """
    
    key,n = int(private_key[0],16),int(private_key[1],16)
    decode_text = [chr(pow(int(char,16),key,n)) for char in encode_text]
    return "".join(decode_text)