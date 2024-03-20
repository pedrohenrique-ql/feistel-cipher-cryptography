def feistel_cipher(block, key):
    left, right = block[:4], block[4:]
    for _ in range(4):
        e = feistel_function(right, key)
        new_right = xor(left, e)
        left, right = right, new_right
    
    return right + left

def feistel_function(data, key):
    substituted_data = substitution(data)
    return xor(substituted_data, key)

def substitution(data):
    substituted_data = b''
    for byte in data:
        shifted_byte = (byte + 1) % 256
        substituted_data += bytes([shifted_byte])
    return substituted_data

def xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))
