def print_primes():
    primes = []
    for num in range(2, 201):
        for i in range(2, num):
            if num % i == 0:
                break  # 如果能被整除，就不是素数，跳出循环
        else:
            primes.append(num)  # 如果 for 循环正常结束，则 num 是素数，将其添加到 primes 列表中

    print(" ".join(str(p) for p in primes))  # 将 primes 列表中的素数用空格连接起来打印输出
