dolls = []

with open('input.txt') as f:
    for line in f:
        line = line.strip().split(',')
        color, length = line[0], int(line[1])
        dolls.append((color, length))

dolls.sort(key=lambda s: s[1])

arr = [1]*len(dolls)

for i in range(1, len(dolls)):
    for j in range(i):
        if dolls[i][1] > dolls[j][1] and dolls[i][0] != dolls[j][0]:
            if arr[j] + 1 > arr[i]:
                arr[i] = arr[j] + 1

print(max(arr))