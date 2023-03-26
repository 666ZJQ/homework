# 周氏加密
import random

def caesar_cipher(plaintext):
    key = random.randint(1, 25)   # 随机生成第一个密钥
    ciphertext = ''
    for i, char in enumerate(plaintext):
        if char.isalpha():
            # 对每个字母进行加密
            shifted = (ord(char) - ord('a') + key) % 26 + ord('a')
            ciphertext += chr(shifted)
        else:
            ciphertext += char
    # 将第一个密钥附加在密文末尾
    ciphertext += '|' + str(key)
    return ciphertext

plaintext = input("请输入明文：")
ciphertext = caesar_cipher(plaintext)
print("加密后的密文为：", ciphertext)
