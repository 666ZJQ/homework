# 第二题
def isPrime(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")  # 抛出类型错误异常

    if n <= 1:
        return False  # 0、1 不是质数

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False  # 若 n 能被 i 整除，则 n 不是质数

    return True  # 若 n 不能被 2~(n-1) 中任何一个数整除，则 n 是质数
