def feistel_cipher(block, key):
    left, right = block[:4], block[4:]

    for _ in range(4):
        e = feistel_function(right, key)
        new_right = xor(left, e)
        left, right = right, new_right
    
    return right + left

def feistel_function(data, key):
  new_data = [0, 0, 0 ,0]

  for i in range(len(key)):
    new_data[key[i]] = data[i]

  return bytes(new_data)  

def xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))


# key = [3, 2, 0, 1]
# text = bytes("abcdefh", 'UTF-8')

# encoded = feistel_cipher(text, key)
# print(encoded)
# print(feistel_cipher(encoded, key))


# 3210
# efgh