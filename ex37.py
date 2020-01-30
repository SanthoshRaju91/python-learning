# execute a string as python code.
exec('print("hello")')

# lamdba functions in python, like arrow functions
def s(y): return y * y

print(s(3))

# in also used for testing a value in some context like an array
print(1 in [10, 100, 1000])

# is equality test
print(1 is 1 == True)

# defining an empty block, useful for empty else block condition
condition = False

if condition:
    print("Condition is True")
else:
    pass

# Try catch blocks in python
try:
    raise ValueError("No")
except ValueError as e:
    print(f"Error {e}")
