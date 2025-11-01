# Python Cheatsheet (Beginner)

## Types
- `int`, `float`, `str`, `bool`, `list`, `dict`, `tuple`, `set`

## Common patterns
```python
# input
name = input("Name: ")

# if
if len(name) > 0:
    print("hi")

# loop
for i in range(5):
    print(i)

# function
def greet(n):
    return f"Hello, {n}!"

# while
player_alive = True
while player_alive:
    # Game code
