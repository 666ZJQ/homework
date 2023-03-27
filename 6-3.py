import random

# 定义包含字母和数字的列表
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

def generate_password(length=8):
    # 从chars中随机选择length个字符
    password = ''.join(random.choices(chars, k=length))
    return password

# 生成10个8位随机密码
for i in range(10):
    password = generate_password(8)
    print(password)
