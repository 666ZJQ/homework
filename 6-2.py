def char_frequency(text):
    # 统计每个字符出现的次数
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1

    # 按照字符出现次数从大到小排序
    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    # 输出结果
    for char, count in freq:
        print(char, ':', count)
