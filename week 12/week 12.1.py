a=int(input())
nums=list(map(int,input().split()))
nums.sort()

k=int(input())
    
def count_pairs(nums, k):
    # Create a dictionary to store the frequency of each number
    frequency = {}
    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1
    
    # Count the pairs
    count = 0
    for num in nums:
        if k > 0:
            # For k > 0, check if the complement (num + k) exists
            count += frequency.get(num + k, 0)
        else:
            # For k = 0, count how many times each number appears more than once
            if frequency[num] > 1:
                count += 1
                # Set the frequency to 1 to avoid counting duplicates
                frequency[num] = 1
    
    return count

# Example usage:


# Example usage:
print(count_pairs(nums, k))
