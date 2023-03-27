def has_duplicates(lst):
    # 复制原列表，避免改变原来的值
    new_lst = lst.copy()
    return len(new_lst) != len(set(new_lst))

# 测试函数是否正确
lst1 = [1, 2, 3, 4, 5]
lst2 = [1, 2, 3, 4, 4, 5]
lst3 = ['a', 'b', 'c', 'd', 'd', 'e']

print(has_duplicates(lst1)) # False
print(has_duplicates(lst2)) # True
print(has_duplicates(lst3)) # True
