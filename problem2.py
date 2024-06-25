def calculation(x,y):
    add=x+y
    sub=x-y
    return [add,sub]

a=int(input())
b=int(input())
res = calculation(a, b)
print("{},{}".format(res[0], res[1]))