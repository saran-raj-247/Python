def findRepeatedDnaSequences(s):
    seen = set()
    repeated = set()
    for i in range(len(s) - 9):
        sequence = s[i:i+10]
        if sequence in seen:
            repeated.add(sequence)
        else:
            seen.add(sequence)
    return sorted(list(repeated))

# Accept input from the user
s = input()
# Find repeated DNA sequences
result = findRepeatedDnaSequences(s)

# Print the result
for sequence in result:
    print(sequence)
