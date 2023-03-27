def count_chars(string):
    nums = 0  # 数字计数器
    letters = 0  # 字母计数器
    spaces = 0  # 空格计数器
    others = 0  # 其他字符计数器

    for char in string:
        if char.isdigit():
            nums += 1
        elif char.isalpha():
            letters += 1
        elif char.isspace():
            spaces += 1
        else:
            others += 1

    return (nums, letters, spaces, others)
