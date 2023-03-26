a = input("输入要解密的文本：")
b = eval(a[-1])
text = a[:-1]
print("解密为：")
for c in text:
    print(chr(ord(c)-b),end='')
