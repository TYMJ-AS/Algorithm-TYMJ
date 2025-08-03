import sys
input = sys.stdin.readline
a = int(input())

stack = []
for i in range(a):
    b = input()
    if int(b) == 0:
        if len(stack) > 0:
            stack.pop()
    else:
        stack.append(int(b))
if len(stack) == '0':
    print(0)
else:
    print(sum(stack))