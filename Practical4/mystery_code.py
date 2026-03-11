# What does this piece of code do?
# Answer: It calculates and prints the sum of 11 randomly generated integers, each between 1 and 10.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil 
# 💡 Note: ceil is imported here, but it is never actually used in the code below!

total_rand = 0  # 记录随机数总和的变量，初始值为 0
progress = 0    # 循环计数器，初始值为 0

while progress <= 10:  # 当 progress 小于或等于 10 时持续循环（会运行 11 次：0到10）
    progress += 1      # 每次循环将计数器加 1
    n = randint(1, 10) # 随机抽取一个 1 到 10 之间的整数赋值给 n
    total_rand += n    # 将抽到的随机数 n 加到总和 total_rand 中

print(total_rand)      # 循环结束后，打印最终的总和