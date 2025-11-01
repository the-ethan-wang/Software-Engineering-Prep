name = input("What is your name? ")
print("Welcome,", name)

def add(a: int, b: int) -> int:
    return a + b

try:
    a = input("Input a number: ")
    b = input("Input another number: ")
    sum = add(int(a), int(b))
    print("Those two numbers add up to", sum)
except:
    print("You probably didn't input an integer. well why. like why.")
    
root_four = 2.0
print(type(root_four))
print(1/10 + 2/10)