with open("input.txt","r") as f:
    data = f.read().split("\n")

def readSno(data): 
    stack = []
    for i in range(len(data)):
        for ch in data[i]:
            if ch == " ":
                stack.append(31)
            elif ch == ":":
                stack = [sum(stack)]
            elif ch == "|":
                stack.append(3)
            elif ch == "'":
                A,B = stack.pop(),stack.pop()
                stack += [A+B]
            elif ch == ".":
                A,B = stack.pop(),stack.pop()
                stack += [A-B, B-A]
            elif ch == "_":
                A, B = stack.pop(),stack.pop()
                stack += [A*B,A]
            elif ch == "/":
                stack.pop()
            elif ch == "i":
                stack += [stack[-1]]
            elif ch == "\\":
                stack[-1] += 1
            elif ch =="*":
                A,B = stack.pop(),stack.pop()
                stack += [A//B]
            elif ch == "]":
                poppedElem = stack.pop()
                if poppedElem%2 == 0:
                    stack += poppedElem
            elif ch == "~":
                stack = stack[:-3] + [max(stack[-3:])]
    return stack
print(readSno(data))
