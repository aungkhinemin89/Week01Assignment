def multiply(func):
    print("multiply decorator is called.")
    def wrapper(arg1):
        print("wrap function is called.")
        func(arg1*2)
    return wrapper
    
@multiply
def getResult(var):
    print("getResult function is called.")
    print(var)
    
print(getResult(8))
