def countDistinctPairs(t, k):
    pair_set = set()
    distinct_pairs = set()
    for num in t:
        complement = k - num
        if complement in pair_set:
            distinct_pairs.add((min(num, complement), max(num, complement)))
        pair_set.add(num)
    return len(distinct_pairs)

# Accept input from the user
t = tuple(map(int, input().split(',')))
k = int(input())

# Calculate the count of distinct pairs
result = countDistinctPairs(t, k)

# Print the result
print(result)
