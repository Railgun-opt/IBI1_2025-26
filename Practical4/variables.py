a = 5.08
b = 5.33
c = 5.55
d = b - a
e = c - b
print (e-d > 0)
# False, because e-d is equal to 0.22-0.25 which is -0.03, and -0.03 is not greater than 0.

# 1. 打印表头
print(f"{'A':<5} | {'B':<5} | {'A and B':<7} | {'A or B':<6} | {'not A':<5}")
print("-" * 40)

# 2. 定义布尔值（习惯上先排 True，后排 False，反之亦可）
values = [True, False]

# 3. 遍历所有的组合并计算逻辑值
for A in values:
    for B in values:
        # 使用 Python 原生的 and, or, not
        res_and = A and B
        res_or  = A or B
        res_not = not A
        
        # 4. 打印每一行，使用格式化对齐
        print(f"{str(A):<5} | {str(B):<5} | {str(res_and):<7} | {str(res_or):<6} | {str(res_not):<5}")