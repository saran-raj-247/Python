def count_frequency(arr):
    freq_dict = {}
    for num in arr:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    
    for key, value in freq_dict.items():
        print(f"{key} occurs {value} times")
n = int(input())
arr = [int(input()) for _ in range(n)]
count_frequency(arr)
