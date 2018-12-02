with open('input.txt') as f:
    total, min = 0, 0
    for line in f:
        num = int(line.strip())
        if num >= min: 
            total += num
            min = num

print(total)