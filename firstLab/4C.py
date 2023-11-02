s = input()
try:
    result = eval(s)
    if type(result) == int:
        print(result)
    else:
        print("WRONG")
except BaseException:
    print("WRONG")
