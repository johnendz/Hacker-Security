def call_numbers():
    for number in range(0,10):
        print(number)

def call_numbers_with_limit(limit):
    for number in range(limit):
        print(number)

'''
def calculator(x, y):
    print(x-y)
calculator(y=10, x=5)

def calculator(x=10, y=5):
    print(x-y)
calculator()
'''
def calculator(x=10, y=5):
    return(x-y)

result = calculator(5)

print("Result is:", result)