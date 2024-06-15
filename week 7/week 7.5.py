def find_repeated_number(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return -1  # This should never be reached given the problem constraints

# Accept input from the user
nums = list(map(int, input().split()))
result = find_repeated_number(nums)
print(result)
