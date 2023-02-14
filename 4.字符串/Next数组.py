
def get_next(needle):
    # 初始化next数组

    next_ = [0] * len(needle)
    next_[0] = 0
    # 初始化指针：i前缀末尾；j:后缀末尾
    # i表示i左侧字符都是公共后缀
    j = 0
    for i in range(1, len(needle)):
        # 如果匹配
        if needle[i] == needle[j]:
            j += 1

        # 如果不匹配，j往回找可能匹配的更短的位置，最多会往回找两次，两次循环则j=0
        else:
            while j > 0 and needle[i] != needle[j]:
                j = next_[j - 1]
            # 跳出循环，要么循环一次，找到可匹配的前后缀，则长度为j + 1
            # 要么没找到，则j=0
            if j > 0:
                j += 1
        next_[i] = j
    return next_
needle = 'aabaa'
result = get_next(needle)