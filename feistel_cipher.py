def feistel_cipher(plaintext, key):
    left, right = plaintext[:4], plaintext[4:]

    for _ in range(4):
        e = feistel_function(right, key)
        new_right = xor(left, e)
        left, right = right, new_right
    
    return right + left

def feistel_function(data, key):
  new_data = [0, 0, 0 ,0]

  for i in range(len(key)):
    new_data[key[i]] = data[i]

  print(data, "->", new_data)
  return bytes(new_data)  

def xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))


# key = [3, 2, 0, 1]
# text = bytes("abcdefgh", 'UTF-8')
# print("Mensagem inicial:", text)

# encoded = feistel_cipher(text, key)
# print("Mensagem criptografada:", encoded)

# decoded = feistel_cipher(encoded, key)
# print("Mensagem decriptografada:", decoded)