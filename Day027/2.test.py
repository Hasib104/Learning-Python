
"""#Unlimited arguments"""
# def add(*args):
#     print(args[1]) #unlimited positional arguments
#     total = 0
#     for n in args:
#         total += n
#     return total
# print(add(1,2,3,6,4,5,8))

"""#Unlimited keyword arguments"""
def calculate(n, **kwargs):
    # print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(n=2, add= 3, multiply= 5) #add & multiply are in **kwargs