comand = input()
stack = []
while comand != "exit":
    if comand[:4] == "push":
        i = 6
        argument = comand[5]
        if i != len(comand):
            while comand[i].isdigit():
                argument += comand[i]
                i+=1
                if i == len(comand):
                    break

        stack.append(int(argument))
        print("ok")

    if comand == "pop":
        print(stack[-1])
        stack.pop(-1)

    if comand == "back":
        print(stack[-1])

    if comand == "size":
        print(len(stack))

    if comand == "clear":
        print("ok")
        stack = []

    comand = input()

print("bye")

