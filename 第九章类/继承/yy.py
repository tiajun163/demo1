# 100以内所有的奇数 —— 列表解析式
a = [i for i in range(100) if i & 1]

# 100以内3的倍数 —— 集合解析式
b = {i for i in range(100) if i % 3 == 0}

import random
import string

# 生成100个name和对应的id —— 字典解析式
name_id = {"".join([random.choice(string.ascii_letters) for i in range(4)]):random.randint(1000, 9999) for j in range(100)}

print(name_id)
print(a)
print(b)