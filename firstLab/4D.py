histogram = [int(i) for i in input().split()]
n = histogram[0]
histogram.pop(0)
print(histogram)
stack = list()
maxim = 0
index = 0
while index < len(histogram):
    if (not stack) or (histogram[stack[-1]] <= histogram[index]):
        stack.append(index)
        index += 1
    else:
        top = stack.pop()
        if stack:
            area = histogram[top] * (index - stack[-1] - 1)
        else:
            area = index
        maxim = max(maxim, area)
while stack:
    top = stack.pop()
    if stack:
        area = histogram[top] * (index - stack[-1] - 1)
    else:
        area = index
    maxim = max(maxim, area)

print(maxim)

