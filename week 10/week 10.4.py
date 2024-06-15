
arr = list(map(int, input().strip().split()))
frequency = {}
for num in arr:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
for num in sorted(frequency):
    print(num, frequency[num])
