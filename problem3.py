def showEmployee(name,selary=9000):
    print(f"Name: {name} salary: {selary}")
fun_str = input()
fun = compile(fun_str, '', 'exec')
exec(fun)