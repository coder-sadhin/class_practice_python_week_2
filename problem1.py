def func1(*args):
    if args:
        for arg in args:
            print(arg)
    else:
        print("No args")
sfun = input()
fun = compile(sfun, '', 'exec')
exec(fun)