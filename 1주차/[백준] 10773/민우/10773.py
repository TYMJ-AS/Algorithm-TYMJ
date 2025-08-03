K = int(input())
sum = 0
numbuffer = []
for i in range(K):
    number = int(input())
    if number != 0:
        sum += number
        numbuffer.append(number)
    else:
        sum -= numbuffer.pop()

print(sum)