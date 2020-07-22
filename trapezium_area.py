def addition(x,y):
    return x+y
def multiplication(x,y):
    return x*y
def divided_by_2(x):
    return x/2


print(addition(10,5))
print(multiplication(10,5))
print(divided_by_2(50))

'''
#if called in other file, it doesn't work
if __name__ =='__main__':
    print(addition(10,5))
    print(multiplication(10,5))
    print(divided_by_2(50))
'''
