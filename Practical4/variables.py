# part 1: population change
a = 5.08  # scotland pop 2004
b = 5.33  # scotland pop 2014
c = 5.55  # scotland pop 2024

d = b - a  # change 2004 to 2014
e = c - b  # change 2014 to 2024

# compare d and e
print(d, e)
# d > e so population growth is slowing down

# part 2: booleans
X = True
Y = False
W = X or Y  # True or False = True

print(f"X = {X}, Y = {Y}, W = X or Y = {W}")

# truth table:
# X      Y      | W
# True   True   | True
# True   False  | True
# False  True   | True
# False  False  | False
