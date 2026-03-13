a = 5.08
b = 5.33
c = 5.55
d = b - a
e = c - b
print (e-d > 0)
# False, because e-d is equal to 0.22-0.25 which is -0.03, and -0.03 is not greater than 0.

print(f"{'A':<5} | {'B':<5} | {'A and B':<7} | {'A or B':<6} | {'not A':<5}")
print("-" * 40)

values = [True, False]

for A in values:
    for B in values:
        res_and = A and B
        res_or  = A or B
        res_not = not A
        
        print(f"{str(A):<5} | {str(B):<5} | {str(res_and):<7} | {str(res_or):<6} | {str(res_not):<5}")