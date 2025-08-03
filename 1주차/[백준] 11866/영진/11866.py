a, b = map(int, input().split())

box = list(range(1, a + 1))
new_box = []
idx = 0

while box:
    idx = (idx + b - 1) % len(box) 
    new_box.append(box.pop(idx))

print("<" + ", ".join(map(str, new_box)) + ">")
